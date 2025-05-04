def find_the_power_of_element(a , power):
    # divide 
    # small problem
    if power == 1:
        return a
    elif power == 0:
        return 1
    # large problem
    else:
        mid = power // 2
        a = find_the_power_of_element(a , mid)
        result = a * a
        if power % 2 == 0:
            result =  print(result) 
        else:
            result =  print(result  * a)
    return result
        
a = 10
power = 10
find_the_power_of_element(a , power)
