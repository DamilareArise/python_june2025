import datetime as dt

my_dt = dt.datetime.now()
# print(my_dt.time())
# print(my_dt.date())
# print(my_dt.hour)
# print(my_dt.hour)
# print(my_dt.minute)
# print(my_dt.second)

my_dt = dt.datetime(2010, 8, 10, 10, 30, 0)
# print(my_dt)

print(my_dt.strftime("%d/%b/%y"))

"""
| Code | Meaning                        | Example      |
| ---- | ------------------------------ | ------------ |
| `%Y` | Year (4 digits)                | `2025`       |
| `%y` | Year (2 digits)                | `25`         |
| `%m` | Month (01 to 12)               | `05`         |
| `%B` | Full month name                | `May`        |
| `%b` | Abbreviated month name         | `May`        |
| `%d` | Day of the month (01 to 31)    | `10`         |
| `%H` | Hour (00 to 23)                | `14`         |
| `%I` | Hour (01 to 12)                | `02`         |
| `%p` | AM/PM                          | `PM`         |
| `%M` | Minute (00 to 59)              | `45`         |
| `%S` | Second (00 to 59)              | `09`         |
| `%f` | Microsecond (000000 to 999999) | `123456`     |
| `%z` | UTC offset                     | `+0200`      |
| `%Z` | Time zone name                 | `UTC`, `PST` |
| `%A` | Full weekday name              | `Saturday`   |
| `%a` | Abbreviated weekday name       | `Sat`        |
| `%j` | Day of the year (001 to 366)   | `130`        |
| `%W` | Week number                    |              |

"""