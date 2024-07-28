#  1
example = "Hardworker"
#  2
print(example[0])
#  3
print(example[-1])
#  4
num = len(example) // 2
if num % 2 == 0:
    num += 1
    print(example[num:len(example)])
else:
    print(example[num:len(example)])
print(num)
#  5
print(example[::-1])
#  6
print(example[1:len(example):2])

