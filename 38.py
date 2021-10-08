# 38. В 2018 г. 365 дней. Вывести индексы всех понедельников (первый
# понедельник 1 января). Вывести уже наименование дней недели праздников программиста и сисадмина!
import datetime

d = datetime.datetime.strptime("01/1/2018", "%m/%d/%Y")
while d.year == 2018:
    print(d.strftime("%j"))
    d += datetime.timedelta(days=7)

print("Sysadmin: Friday")
print("Prog:", (datetime.datetime.strptime("01/1/2018", "%m/%d/%Y") + datetime.timedelta(days=255)).strftime("%A"))