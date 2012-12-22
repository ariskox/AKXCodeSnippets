#!/usr/bin/python
#
#  This small script can be used to duplicate .codesnippet files
# 
#  For every input file, a new .codesnippet file with a new UUID as 
#  IDECodeSnippetIdentifier and filename is created.
#
# Copyright 2012 Koxaras Aris
#
# Version 1.0
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os
import sys
import getopt
import uuid

def main():
    if len(sys.argv) <= 1:
        print "\nUsage: " + sys.argv[0] + " <filename> ...\n"
        print "Input: a list of .codesnippet files."
        print "For every input file, a new file with a random filename is created.\n"
        return

    for filename in sys.argv[1:]:
		if filename.endswith('codesnippet'):
		    from AppKit import NSDictionary
		    dict = NSDictionary.dictionaryWithContentsOfFile_(filename)
		    UUID = str(uuid.uuid1()).upper()
		    print 'Duplicating \"' + filename + '\" as \"' + UUID + '.codesnippet\"'
		    dict['IDECodeSnippetIdentifier'] = UUID
		    NSDictionary.dictionaryWithDictionary_(dict).writeToFile_atomically_(UUID + '.codesnippet', True)
		else:
		    print 'File \"' + filename + '\" is not a codesnippet file. Skipping...'

if __name__ == '__main__':
  sys.exit(main())
  