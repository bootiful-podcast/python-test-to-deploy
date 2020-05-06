# !/usr/bin/env python3

import os
import sys
import urllib.request

if __name__ == '__main__':
    url_for_bootstrap_sh = sys.argv[1]
    rmq_address = sys.argv[2]
    fragment = '_PODCAST_RMQ_ADDRESS_'
    contents = str(urllib.request.urlopen(url_for_bootstrap_sh).read())
    a, b = contents.split(fragment)
    lines = [a, rmq_address, b]
    print(''.join(lines))
