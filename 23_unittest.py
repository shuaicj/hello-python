#!/usr/bin/env python3

# run by:
# python3 -m unittest 23_unittest

from unittest import TestCase

class TestSomething(TestCase):
    @classmethod
    def setUpClass(cls):
        print('in setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('in tearDownClass')

    def setUp(self):
        print('in setUp')

    def tearDown(self):
        print('in tearDown')

    def test_upper(self):
        print('in test_upper')
        self.assertEqual('AbC'.upper(), 'ABC')

    def test_lower(self):
        print('in test_lower')
        self.assertEqual('AbC'.lower(), 'abc')

