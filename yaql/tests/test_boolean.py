# Copyright (c) 2014 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import unittest
from yaql.tests import YaqlTest


class TestBooleans(YaqlTest):
    def test_and(self):
        self.assertEval(True, 'true and true')
        self.assertEval(False, 'true and false')
        self.assertEval(False, 'false and true')
        self.assertEval(False, 'false and false')

    def test_or(self):
        self.assertEval(True, 'true or true')
        self.assertEval(True, 'true or false')
        self.assertEval(True, 'false or true')
        self.assertEval(False, 'false or false')

    def test_not(self):
        self.assertEval(True, 'not false')
        self.assertEval(False, 'not true')
        self.assertEval(True, 'not (not true)')

    def test_excl(self):
        self.assertEval(True, '!false')
        self.assertEval(False, '!true')
        self.assertEval(True, '!(!true)')

    def test_bool_precedence(self):
        self.assertEval(True, 'true and not false')
        self.assertEval(True, 'not true or not false')

    @unittest.skip(
        "Custom precedence for 'or' and 'and' operators is not defined")
    def test_incorrect_boolean_precedence(self):
        self.assertEval(True, "true or (true and false)")  # works
        self.assertEval(True, "true or true and false")  # breaks

    def test_boolean_conversion(self):
        self.assertNotEquals(bool, type(self.eval('abcd')))
        self.assertEquals(bool, type(self.eval('bool(abcd)')))


if __name__ == '__main__':
    unittest.main()
