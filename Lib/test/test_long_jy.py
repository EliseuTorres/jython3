"""Misc long tests

Made for Jython.
"""
from test import support
import unittest

class MyLong(long):
    pass


class LongTestCase(unittest.TestCase):

    def _test_long_repr(self, type2test):
        val = type2test(42)
        self.assertEqual(str(val), '42')
        self.assertEqual(repr(val), '42L')

    def test_long_repr(self):
        self._test_long_repr(int)

    def test_long_subclass_repr(self):
        self._test_long_repr(MyLong)

    def test_subclass_bool(self):
        # http://bugs.jython.org/issue1828
        self.assertTrue(bool(MyLong(42)))

    def test_long_pow(self):
        self.assertEqual(pow(10, 10, None), 10000000000)
        self.assertEqual(int.__pow__(10, 10, None), 10000000000)
        self.assertEqual((10).__pow__(10, None), 10000000000)
        self.assertEqual((10).__pow__(10, None), 10000000000)


def test_main():
    support.run_unittest(LongTestCase)

if __name__ == '__main__':
    test_main()
