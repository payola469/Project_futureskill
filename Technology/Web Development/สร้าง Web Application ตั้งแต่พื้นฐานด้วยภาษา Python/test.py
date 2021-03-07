from random import randint #import randint
def generate_random_list(M,N):
    return [randint(0,M) for i in range(N)]

lst1 = generate_random_list(M=10, N=3) # M = จำนวน 0-10  N จำนวน 3 รอบ

print(lst1)