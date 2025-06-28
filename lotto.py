import random
lotto = []
start = 1
while start <= 45:
    lotto.append(start) # 1 ~ 45추가
    start += 1 # start = start + 1
size = len(lotto) # 45

l = []
i = 1
while i <= 6:
    size -= 1                # 0 ~ 44
    idx = random.randint(0, size)
    result = lotto.pop(idx)
    i += 1
    l.append(result)

print(l)