import json
import sys

def log_json(data):
    print(json.dumps(data), file=sys.stdout)
