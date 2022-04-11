first_num = int(input("enter the first num : "))
second_num = int(input("enter the first num : "))
num = 1
for x in range(first_num,second_num):
    if x > 1:
        for y in range(2,x):
            if(x%y)==0:
                break
        else:
             num = x
print(num)  
