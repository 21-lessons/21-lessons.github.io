#! /usr/bin/python3
import gspread
import json
import os
import re

from oauth2client.service_account import ServiceAccountCredentials
from util import author_to_file_path, get_excerpt_from_page, get_valid_author_slug, title_to_file_path

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

articles = client.open("Bitcoin Resources").worksheet("Links")

NO_DATE = "1111-11-11"
NO_AUTHOR_LINKS = ""

for row in articles.get_all_values():
    if row[0] == 'Author':
        continue

    link_author = row[0]
    link_title = row[1].lstrip().rstrip()
    link_link = row[2].lstrip().rstrip()
    link_date = row[3] if row[3] != '' else NO_DATE
    link_lesson = row[4].lstrip().rstrip()

    md_file_path = title_to_file_path(link_title, 'links')
    if md_file_path == "":
        continue

    md_file = (
                f"---\n"
                f"layout: page\n"
                f"author: {link_author}\n"
                f"title: {link_title}\n"
                f"link: {link_link}\n"
                f"date: {link_date}\n"
                f"lesson: {link_lesson}\n"
                f"---\n")

    with open(md_file_path, 'w') as f:
        f.write(md_file)
