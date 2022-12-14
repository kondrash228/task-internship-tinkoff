n = int(input())
s = str(input()).split(' ')
b = str(input())


def same_letters(s) -> bool:
    return min([len(x) for x in [set(x) for x in [s[x:x + 3] for x in range(len(s) - 2)]]]) == 1


arr = []
j = 0
i = 0
counter = 0

while j < len(s):
    if j == 0:
        arr.append(b[0:len(s[j])])
        b = b[len(s[j]):]
        j += 1
    else:
        arr.append(b[:len(s[j])])
        b = b[len(s[j]):]
        j += 1


for elem in arr:
    if same_letters(elem):
        counter += 1

print(counter)
