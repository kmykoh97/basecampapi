import csv
import pyjq

from .holidays_parser import holiday_parser

def csv_writer(path, res):
  with open(path, 'w') as file:
    mywriter = csv.writer(file)
    mywriter.writerows(res)

def parse_completed_to_csv(path, res, date_of_report):
  jq_parser = pyjq.all(f".[] | select(.created_at | startswith(\"{date_of_report}\")) | [.title,.created_at,.completion.created_at,.completed,.url]", res)
  holiday_parser(jq_parser)
  csv_writer(path, jq_parser)

def parse_incomplete_to_csv(path, res, date_of_report):
  jq_parser = pyjq.all(f".[] | select(.created_at | startswith(\"{date_of_report}\")) | [.title,.created_at,.blank,.blank,.url]", res)
  holiday_parser(jq_parser)
  csv_writer(path, jq_parser)
