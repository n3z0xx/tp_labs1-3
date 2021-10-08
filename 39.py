# 39. Для 2018 г. ввести число, проверить что входит в число дней года
# и вывести (по мин-му): в каком это месяце и (по макс-му)какой это
# день недели.
import datetime

print((datetime.datetime.strptime("01/1/2018", "%m/%d/%Y") + datetime.timedelta(days=int(input()))).strftime("%B %A"))
