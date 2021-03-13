
import time
import math
prime_number=[]
n=1
time_start = time.time()
g=int(input())

sum_t=0.0
for i in range(g):



    a=0
    if n <= 1:
        print('False')
    else:
        for i in range(2, int(math.sqrt(n)) + 1):


                if n % i == 0:
                    print ('False')
                    a=1
                    break
        if a==0:
            print('ture')
            prime_number.append(n)


    n=n+1
time_end = time.time()
sum_t=(time_end - time_start)+sum_t

print(prime_number)
print(len(prime_number))
print('time cost', sum_t, 's')