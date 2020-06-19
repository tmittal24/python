# display current date and time.
import datetime

now = datetime.datetime.now()
# print(now.strftime())
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%d-%m-%Y %H:%M:%S"))
