a=[100,200,760,900,786]
max1=max2=a[0]
for num in a:
    if num>max1:
        max2=max1
        max1=num
    elif num > max2 and num != max1:
        max2 = num    
print(max2)
