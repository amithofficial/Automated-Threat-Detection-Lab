#!/usr/bin/env python3
import sys
import json
import urllib.request
import ssl

# 1. Read Arguments
try:
    alert_file = sys.argv[1]
    webhook_url = sys.argv[3]
except IndexError:
    sys.exit(1)

# 2. Read the Alert
with open(alert_file) as f:
    alert_json = json.load(f)

# 3. Prepare Request (Ignore SSL Warnings)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request(webhook_url)
req.add_header('Content-Type', 'application/json')

# 4. Send Data
jsondata = json.dumps(alert_json).encode('utf-8')
req.add_header('Content-Length', len(jsondata))

try:
    urllib.request.urlopen(req, jsondata, context=ctx)
except Exception as e:
    sys.exit(1)

sys.exit(0)
