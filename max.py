a=[100,200,760,900,786]
max=a[1]
for i in range(len(a)):
    if a[i]>max:
        sec=max
        max=a[i]
print(max)
