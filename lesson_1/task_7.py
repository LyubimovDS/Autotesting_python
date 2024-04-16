number = ''

def print_num(num):
    global number
    number += num
    return number
    
for _ in range(11):
    print_num(input())

print(number)