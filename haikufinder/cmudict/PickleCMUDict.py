#!/bin/env python

# Read the CMU pronounciation dictionary, count syllables (throwing away
# phoneme and stress information), and pickle the result.
#
#
# Copyright (c) 2009, Jonathan Feinberg <jdf@pobox.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#   3. The name of the author may not be used to endorse or promote products
#      derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

try:
    # HACK for Python 2
    import cPickle as pickle
except ImportError:
    import pickle
import re
import sys

from nltk.corpus import cmudict

if len(sys.argv) < 2:
    exit('destination file required')


syllables = {}
numeral = re.compile(r'\d')
for (word, phonemes) in cmudict.entries():
    word = word.upper()
    count = len([x for x in list(''.join(phonemes)) if x >= '0' and x <= '9'])
    if word in syllables:
        count = min(count, syllables[word])
    syllables[word] = count

with open(sys.argv[1], 'wb') as fp:
    # version 2 is the highest version that Python 2 supports
    # https://docs.python.org/3/library/pickle.html#data-stream-format
    pickle.dump(syllables, fp, 2)
