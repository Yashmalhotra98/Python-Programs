print('Welcome to the Temprature Conversion Program')
temp_f = float(input('\nWhat is the given Temprature in Fahrenheit:'))
temp_c = (temp_f-32)/1.8
c = round(temp_c,4)
temp_k = round(temp_c + 273.15,4)
print(f'\nDegrees Fahrenheit:\t{temp_f}\nDegrees Celsius:\t{c}\nDegrees Kelvin:\t\t{temp_k}')