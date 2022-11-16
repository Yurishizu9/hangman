'''
Given 2 variables, altitude (ft) and airspeed (knots)

Write a program that categorises entries into 'safe flying' and 'unsafe flying' based on the following criteria:

An altitude below 100ft or above 50000ft is considered unsafe flying
An airspeed below 60 knots or above 500 knots is considered unsafe flying
If altitude and airspeed are outside these ranges, the flight is considered as safe

'''

# %%
altitude = 70 #int(input('what is the altitude(ft): '))
airspeed = 0 #int(input('what is the airspeed(knots): '))

if 100 > altitude < 50000 and 60 > airspeed > 500:
    print('The flight is considered as safe')
else:
    print('unsafe for flying')



# %%
