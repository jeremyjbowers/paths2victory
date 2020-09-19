import os

SHEET_ID = os.environ.get('SHEET_ID', None)
SHEET_RANGE = os.environ.get('SHEET_RANGE', None)

CANDIDATES = [
    {"name": "Joe Biden", "slug": "biden", "condition": ">"},
    {"name": "Donald Trump", "slug": "trump", "condition": "<"}
]