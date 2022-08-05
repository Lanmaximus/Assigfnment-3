def values():
    lower_values = 0
    upper_values = 0
    for i in a:
        if i.islower():
         lower_values+=1
        elif i.isupper():
         upper_values+=1
    print(f'No of upper values is :',upper_values)
    print(f'No of lower values is :',lower_values)

a =  'The quick Brow Fox'
values()