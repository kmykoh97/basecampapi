from datetime import datetime, timedelta
import holidays

def date_range(start, end):
  delta = end - start
  days = [start + timedelta(days=i) for i in range(delta.days + 1)]
  return days

def weekend(dates):
  if dates.weekday() >= 5:
    return True

  return False

def get_number_of_non_working_days(start, end):
  start_dt = datetime.strptime(start, "%Y-%m-%dT%H:%M:%S.%f%z")
  end_dt = datetime.strptime(end, "%Y-%m-%dT%H:%M:%S.%f%z")
  my_holidays = holidays.MY(subdiv='SGR')
  no_of_non_working_days = 0

  for date in date_range(start_dt, end_dt):
    if weekend(date) or my_holidays.get(date):
      no_of_non_working_days += 1
  
  return no_of_non_working_days

def holiday_parser(jq_response):
  for jq_response_list in jq_response:
    no_of_holiday = get_number_of_non_working_days(jq_response_list[1], jq_response_list[2])
    jq_response_list.append(str(no_of_holiday))
