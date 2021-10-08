# 12. через sys.argv() ввести координаты центра и радиус круга, потом в
# бескон цикле вводить координаты точек и писать точка в круге или нет
# и так до 0, 0
import sys
import math
cx, cy, r = map(int, sys.argv[1:])

while True:
    px, py = map(int, input().split())
    if px == py and py == 0: break
    pr = math.sqrt((cx - px)**2 + (cy - py)**2)
    if pr <= r:
        print("в круге")
    else:
        print("не в круге")