t = ()
for i in range(3):
    x = int(input())
    s = x**2
    if s % 2 == 0:
        print("Even")
    else:
        print("Odd")
    t += (s,)
l = list(t)
sum = 0
for i in l:
    sum += i
if sum > 1:
    for i in range(2, int(sum**0.5)+1):
        if sum % i == 0:
            break
    else:
        print("Prime")
else:
    print("Not Prime")
