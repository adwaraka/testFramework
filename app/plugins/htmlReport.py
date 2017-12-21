import os
import time
import datetime
import traceback

import nose
from nose.plugins import Plugin

class HtmlOutput(Plugin):
    '''Output test results on an html page.'''
    name = 'html-output'

    def __init__(self):
        super(HtmlOutput, self).__init__()
        self.html = [ '<html><head>',
                      '<title>Test Output</title>',
                      '</head><body><br><center>TEST CASE RESULTS</center>' ]
        self.html.append('<fieldset>')
    
    def addSuccess(self, test):
        self.html.append('<span>PASS</span>')
        
    def addError(self, test, err):
        err = self.formatErr(err)
        self.html.append('<span>ERROR</span>')
        self.html.append('<pre>%s</pre>' % err)
            
    def addFailure(self, test, err):
        test_case_name = str(test)
        err = self.formatErr(err)
        self.html.append('<span>FAIL</span>')
        self.html.append('<br><br><u>' + test_case_name +'</u><br><pre>%s</pre>' % err)

    def finalize(self, result):
        self.html.append('</fieldset>')
        self.html.append('<div>')
        self.html.append("Ran %d test%s" %
                         (result.testsRun, result.testsRun != 1 and "s" or ""))
        self.html.append('</div>')
        self.html.append('<div>')
        if not result.wasSuccessful():
            self.html.extend(['<span>FAILED ( ',
                              'Failures=%d ' % len(result.failures),
                              'Errors=%d' % len(result.errors),
                              ')</span>'])                             
        else:
            self.html.append('OK')
        self.html.append('</div></body></html>')
        try:
            curr_workdir = os.getcwd()
            t = datetime.datetime.now()
            directory = 'report_' + t.strftime('%Y%m%d%H%M%S')
            if not os.path.exists('Logs\\' +directory):
                os.makedirs('Logs\\'+directory)
            os.chdir('Logs\\'+directory)
            f=open('index.html', 'w')
            for l in self.html:
                f.write(l)
            f.close()
            print "Report prepared"
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        finally:
            os.chdir(curr_workdir)
            print "Done"
            
    def formatErr(self, err):
        exctype, value, tb = err
        return ''.join(traceback.format_exception(exctype, value, tb))
    
    def setOutputStream(self, stream):
        # grab for own use
        self.stream = stream        
        # return dummy stream
        class dummy:
            def write(self, *arg):
                pass
            def writeln(self, *arg):
                pass
            def flush(self, *arg):
                pass
        d = dummy()
        return d
    
    def startTest(self, test):
        dot_stream = '.............................................................................'
        self.html.extend([ '<div><span>',
                           test.shortDescription() or str(test),
                           '&nbsp;&nbsp;', str(dot_stream), '&nbsp;&nbsp;</span>' ])
        
    def stopTest(self, test):
        self.html.append('</div>')
