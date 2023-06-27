from datetime import datetime

calendar = input()
formated_calendar = datetime.strptime(calendar,"%m %d %Y")
day = formated_calendar.strftime("%A")
print(day.upper())
