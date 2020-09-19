import pickle
import os.path

from googleapiclient.discovery import build
from google.oauth2 import service_account


def get_sheet(sheet_id, sheet_range):
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

    creds = service_account.Credentials.from_service_account_file(
        "credentials.json", scopes=SCOPES
    )
    service = build("sheets", "v4", credentials=creds)
    sheet = service.spreadsheets()

    result = sheet.values().get(spreadsheetId=sheet_id, range=sheet_range).execute()
    values = result.get("values", None)

    if values:
        return [dict(zip(values[0], r)) for r in values[1:]]
    return []


def x_to_bool(possible_bool):
    if isinstance(possible_bool, str):
        if possible_bool.lower() in ["y", "yes", "t", "true", "x"]:
            return True
    return False


def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial

    if partial_sum >= target:
        return

    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n['ev'])