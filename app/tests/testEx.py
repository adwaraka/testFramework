import sys
import nose
import time
import unittest
from nose import with_setup
from ..plugins.htmlReport import HtmlOutput

class MyTest(unittest.TestCase):
    def my_setup_function():
        pass

    def my_teardown_function():
        pass

    @with_setup(my_setup_function, my_teardown_function)
    def test_a_test(self):
        print "Executing test_a_test"
        time.sleep(5)
        assert False

    @with_setup(my_setup_function, my_teardown_function)
    def test_b_test(self):
        print "Executing test_b_test"
        time.sleep(10)
        assert True

    @with_setup(my_setup_function, my_teardown_function)
    def test_c_test(self):
        print "Executing test_c_test"
        time.sleep(5)
        assert False

    @with_setup(my_setup_function, my_teardown_function)
    def test_d_test(self):
        print "Executing test_d_test"
        time.sleep(2)
        assert True

    @with_setup(my_setup_function, my_teardown_function)
    def test_e_test(self):
        print "Executing test_e_test"
        assert True

    @with_setup(my_setup_function, my_teardown_function)
    def test_f_test(self):
        print "Executing test_f_test"
        time.sleep(5)
        assert True

    @with_setup(my_setup_function, my_teardown_function)
    def test_g_test(self):
        print "Executing test_g_test"
        time.sleep(5)
        assert True

if __name__ == '__main__':
    nose.main(addplugins=[HtmlOutput()])
