#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""`cssmin` - A Python port of the YUI CSS compressor."""

import unittest

import cssmin


class TestCssmin(unittest.TestCase):
    
    def test_remove_comments(self):
        css_before = """/*****
  Multi-line comment
  before a new class name
*****/
.classname {
    /* comment in declaration block */
    font-weight: normal;
}"""
        css_after = cssmin.remove_comments(css_before)
        expected = """
.classname {
    
    font-weight: normal;
}"""
        self.assertEqual(css_after, expected)

    def test_remove_unnecessary_whitespace(self):
        css_before = """
.classname {
    
    font-weight: normal;
}"""
        css_after = cssmin.remove_unnecessary_whitespace(css_before)
        expected = ".classname{font-weight:normal}"
        
if __name__ == '__main__':
    unittest.main()
