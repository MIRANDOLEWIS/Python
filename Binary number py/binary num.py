num = 233

def ans(n):
    if n > 1:
        ans(n//2)

        print(n%2,end="")

ans(num)
