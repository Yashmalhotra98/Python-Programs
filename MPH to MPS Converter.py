print('Welcome to the MPH to MPS Conversion App')
s_mph = float(input('What is your speed in miles per hour:'))
s_mps = s_mph *0.44704
s_mps_rounded = round(s_mps, 2)
print(f'Your speed in meter per second is {s_mps_rounded}.')