def count_even(num):
    count = 0
    even=[]
    for i in num:
        if i % 2 == 0:
            even.append(i)
            count += 1
    return count, even

n = [1,2,3,4,5,6,7,8,9,10]
res = count_even(n)
print(f"The count of even numbers is: {res}")