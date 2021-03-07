"""
# random list with size 10, (0, 20)
# N = 10
# M = 20
from random import randint
lst1 = []
M = 20 # ขนาด 20
N = 10 # จำนวนของใน list ตั้งแต่ 0 - 10
for i in range(N):
    lst1.append(randint(0,M))  #append คือการเพิ่มของใน list นั้น
print(lst1)
"""

