import json
import os

from dotenv import load_dotenv
from basecampapi import Basecamp, Todolists, Cards
from lib.csv_writer import parse_completed_to_csv, parse_incomplete_to_csv

load_dotenv() # to read .env

with open("credentials.json", "r") as jsonfile:
  data = json.load(jsonfile)

date_of_report = input("Select YYYY-MM (e.g. 2022-01) to generate report: ")

credentials = {
  "account_id": data["account_id"],
  "client_id": data["client_id"],
  "client_secret": data["client_secret"],
  "redirect_uri": data["redirect_uri"],
  "refresh_token": data["refresh_token"]
}

bc = Basecamp(credentials=credentials)

### Geckoterminal stats starts here

geckoterminal = Todolists(project_id=os.getenv('BC_PROJECT_ID'), todolists_id=os.getenv('BC_GECKOTERMINAL_TODOLIST_ID'))
geckoterminal_completed = geckoterminal.get_completed()
geckoterminal_incomplete = geckoterminal.get_incomplete()

parse_completed_to_csv('./data/geckoterminal_completed.csv', geckoterminal_completed, date_of_report)
parse_incomplete_to_csv('./data/geckoterminal_incomplete.csv', geckoterminal_incomplete, date_of_report)

### Geckoterminal stats ends here

### Non Geckoterminal stats starts here

non_geckoterminal = Cards(project_id=os.getenv('BC_PROJECT_ID'), completed_cards_id=os.getenv('BC_NON_GECKOTERMINAL_CARDS_ID_COMPLETED'), incomplete_cards_id=os.getenv('BC_NON_GECKOTERMINAL_CARDS_ID_INCOMPLETE'))
non_geckoterminal_completed = non_geckoterminal.get_completed()
non_geckoterminal_incomplete = non_geckoterminal.get_incomplete()

parse_completed_to_csv('./data/non_geckoterminal_completed.csv', non_geckoterminal_completed, date_of_report)
parse_incomplete_to_csv('./data/non_geckoterminal_incomplete.csv', non_geckoterminal_incomplete, date_of_report)

### Non Geckoterminal stats ends here
