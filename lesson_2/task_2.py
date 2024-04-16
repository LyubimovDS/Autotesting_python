def is_year_leap(year):
    
    if year % 400 == 0:
            print(f"Год {year} високосный")
            
    elif year % 4 == 0: 
            
        if year % 100 == 0:
            print(f"Год {year} невисокосный")
            
        else:
            print(f"Год {year} високосный")
    
    else:
        print(f"Год {year} невисокосный")
    
    
is_year_leap(int(input()))
