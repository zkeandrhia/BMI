def Body_mass():
    weight = float(input('Weight in lbs: '))
    height = float(input('Height in inches: '))
    
    result = weight * 703/(height * height)
    
    if result > 18 and result <=25:
        print(f'\nBMI: {result} \nOptimal')
    elif result < 18:
        print(f'\nBMI: {result} \nUnderweight')
    elif result > 25:
        print(f'\nBMI: {result} \nOverweight')
   
Body_mass()