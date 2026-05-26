def cube(number):
    return number*number*number

def by_three(number):
    if number %7 ==0:
        return cube(number)
    else:
        return False
    
print(by_three(14))
print(by_three(4))