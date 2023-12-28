# import zipfile
# from zipfile import *
# from zipfile import ZipFile

# w = for writing purpose
# with ZipFile('techamplifiers.zip', 'w') as z:     # w = it is for write purpose
#     z.write('shubham.txt')

# for extracting file and reading file purpose in zip
# with ZipFile('techamplifiers.zip', 'r') as z:     # r = it is for read purpose
#     # print(str(z.read('shubham.txt')))                # run adn it will open in default(binary) form
#     z.extractall("E:/myZip")

# for directory purpose in zip
# with ZipFile("techamplifiers.zip", 'w') as z:
# print('Directory')
# # z.printdir()
# z.write('Abstraction(Indian Flag) (24 Feb).py')
# z.write('rdj sketch.py')
# z.printdir()
# z.extractall("shubbhamzip")


# Date and Time in Python

import datetime
import time

# # print(datetime.datetime.utcnow())
# print(datetime.datetime.now())
# print(time.time())
# print(datetime.datetime.fromtimestamp(1678808196))
# print('Time Started')
# time.sleep(30)
# print('Time Ended')
# print(datetime.datetime.isocalendar())
# print(time.gmtime())

# strf time concept
# print(datetime.date.today().strftime("%d - %B - %Y"))
# %d== date in format of number
# %m == month in format of number
# %Y== year in number four digits
# %y == year in number two digits          # y = 2023 = 23
# %B == month in word format              # B = March

# another formats
# %B, %d, %Y
# print(datetime.date.today().strftime("%d %B, %Y"))
# print(type(datetime.date.today().strftime("%d %B, %Y")))
# # %m, %d, %y
# print(datetime.date.today().strftime("%m / %d / %y"))
# # %b, %d, %Y
# print(datetime.date.today().strftime("%b - %d - %Y"))

from datetime import datetime
import pytz

# To get standard UTC time
UTC = pytz.utc

# it will get time zone of the specified location
# a = pytz.timezone('')
IST = pytz.timezone('Asia/Kolkata')
# print(IST)


# print the date and time in standard format
print("IST in default Format : ",
      datetime.now(IST))

# print the date and time in specified format
# datetime_utc = datetime.now(UTC)
# print("Date & Time in UTC : ",
#       datetime_utc.strftime('%Y:%m:%d %H:%M:%S %Z %z'))       #%Z will tell UTC time and %z will tell timezone
#
# datetime_utc = datetime.now(IST)
# print("Date & Time in IST : ",
#       datetime_utc.strftime('%Y:%m:%d %H:%M:%S %Z %z'))

from datetime import date


def num0fDays(date1, date2):
      return (date2 - date1).days

# driver programs
# we can check birth date
date1 = date(2018, 12, 13)
date2 = date(2019, 2, 25)
print(num0fDays(date1, date2), "days")



