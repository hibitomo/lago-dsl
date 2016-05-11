#!/usr/bin/env python

# Copyright (C) 2014-2016 Nippon Telegraph and Telephone Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import getopt
import socket
from lagosh import DSLError
from lagosh import ds_client

def usage():
    print 'Usage' + sys.argv[0] + '[DSL command]'

if __name__ == "__main__":

    ds_client.port = 12345

    cmd = ''
    for word in sys.argv[1:]:
        cmd += word + ' '
    cmd += '\n'

    try:
        print ds_client().call(cmd)
    except socket.error:
        print 'Socket connection refused.  Lagopus is not running?'
    except DSLError as e:
        print e.value

