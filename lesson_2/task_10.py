def bank(x, y):
    for _ in range(1, y+1):
        x += x*0.1
    
    print(x)
        
bank(int(input("Вклад: ")), int(input("Срок: ")))    