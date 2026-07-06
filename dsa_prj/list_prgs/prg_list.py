def find_max(num):
    m = num[0]          # fixed: indexing instead of calling
    for i in num:
        if i > m:
            m = i
    return m

n = [3, 7, 2, 9, 4]
res = find_max(n)
print(f"The largest number is:{res}")   # fixed: added f-prefix