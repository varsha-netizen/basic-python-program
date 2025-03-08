def swap_cases(s):
    num = ""
    for  let in s:
        if  let.isupper() == True:
            num+=(let.lower())
        else:
            num+=(let.upper())
    return  num
s =input()
result = swap_cases(s)
print(result)