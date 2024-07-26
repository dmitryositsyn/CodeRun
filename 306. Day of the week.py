#  306. День недели

import sys
import datetime


d = {
	"January": 1,
	"February": 2,
	"March": 3,
	"April": 4,
	"May": 5,
	"June": 6,
	"July": 7,
	"August": 8,
	"September": 9,
	"October": 10,
	"November": 11,
	"December": 12
    }
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for line in sys.stdin:
    day, month, year = line.split()
    print(days[datetime.date(int(year), d[month], int(day)).weekday()])