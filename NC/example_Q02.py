from math import *
from random import *

for cus_no in range(1, 11):
    time = randrange(5, 51)
    if time <=15:
        print("[O] [{0}]번 손님 (소요시간 : {1}분)".format(cus_no, time))
    else:
        print("[ ] [{0}]번 손님 (소요시간 : {1}분)".format(cus_no, time))
