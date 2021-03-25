#!/usr/bin/env python
# coding: utf-8

import sys
import pandas as pd
import requests
import json

url1 = 'https://dsci-551-zhixinxie-default-rtdb.firebaseio.com/hw1/chats.json'
url2 = 'https://dsci-551-zhixinxie-default-rtdb.firebaseio.com/hw1/roster.json'
input_file_name_1 = sys.argv[1]
input_file_name_2 = sys.argv[2]
chats = json.dumps(json.loads(open(input_file_name_1, 'r').read()))
roster = json.dumps(json.loads(open(input_file_name_2, 'r').read()))
response1 = requests.put(url1, chats)
response2 = requests.put(url2, roster)
    




