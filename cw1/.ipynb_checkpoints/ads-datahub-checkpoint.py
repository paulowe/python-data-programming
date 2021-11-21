#!/usr/bin/env python3

"""This sample shows how to retrieve all accounts associated with the user.
"""

from __future__ import print_function
import json
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/adsdatahub']
DISCOVERY_URL = 'https://adsdatahub.googleapis.com/$discovery/rest?version=v1'
creds = Credentials.from_service_account_file(
    'service-account.json').with_scopes(SCOPES)
developer_key = 'YOUR_DEVELOPER_KEY'  # Replace with your developer key.
service = build('AdsDataHub', 'v1', credentials=creds,
                developerKey=developer_key, discoveryServiceUrl=DISCOVERY_URL)

# Replace with your customer ID.
customer_name = input('Customer name (e.g. "customers/123"): ').strip()
queries = service.customers().analysisQueries().list(
    parent=customer_name).execute()
print(json.dumps(queries, sort_keys=True, indent=4))