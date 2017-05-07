#!/usr/bin/env python3

import json

def dict_raise_on_duplicates(ordered_pairs):
    """Reject duplicate keys."""
    d = {}
    for k, v in ordered_pairs:
        if k in d:
           raise ValueError("duplicate key: %r" % (k,))
        else:
           d[k] = v
    return d

try:
    with open('games.json') as json_data:
        data = json.load(json_data, object_pairs_hook=dict_raise_on_duplicates)
        print('loaded json items %s' % len(data))
except Exception as e:
    print('ERROR: invalid json: %s' % e)
    exit(1)

print('OK')
