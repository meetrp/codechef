#
# Copyright 2013 Rp (www.meetrp.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#       http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import re
import sys

def is_debug():
    return False

def re_pattern(in_str):
    """ Add the wildcard characters between every alphabet in the string
    Useful in 'regular expression' search
    """
    pat = ''
    for c in in_str:
        pat += '.*' + c
    return pat

def can_marry(name1, name2):
    if len(name1) > len(name2):
        pattern = re_pattern(name2)
        string = name1
    else:
        pattern = re_pattern(name1)
        string = name2

    if is_debug(): print(string, pattern)

    # 'regular expression' search of _pattern_ (smaller in length name)
    # within the _string_ (bigger in length name)
    if re.search(pattern, string):
        return True

    return False

def main():
    blah = raw_input()
    if not len(blah):
        print "no input"
        sys.exit(2)

    try: count = int(blah)
    except:
        print "wrong input"
        sys.exit(2)

    # constraint #1: 1 <= T <= 100
    if (count < 1) or (count > 100):
        print "invalid input"
        sys.exit(1)

    for i in range(count):
        line = raw_input()
        if not len(line):
            print "insufficient input"
            continue

        words = line.split()
        if (len(words)) != 2:
            print "bad input: exactly 2 strings required"
            continue

        # constraint #2: 1 <= |word| <= 25000
        if ((len(words[0]) < 1) or (len(words[0]) > 25000)) or \
                ((len(words[1]) < 1) or (len(words[1]) > 25000)):
            print "bad input: too big a string"
            continue

        try:
            # constraint #3: All names consist of lowercase English letters only.
            if (not str(words[0]).islower()) or (not str(words[1]).islower()):
                print "bad input: lower case letters only"
                continue
        except:
            print "bad input: lower case ENGLISH letters only"
            continue

        print(can_marry(words[0], words[1]))


if __name__ == '__main__':
    """
    The solution for codechef challenge as detailed at
    http://ww2.codechef.com/MAY13/problems/NAME2
    """
    main()
