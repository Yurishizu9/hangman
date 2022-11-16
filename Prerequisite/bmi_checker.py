'''
Given 2 variables, height and weight, calculate the BMI (weight / height ^2).

Using the parameter BMI, write a series of if statements that print the following outcomes:

Below 18.5 --> "Your BMI is x. You're in the underweight range."
Between 18.5 and 24.9 --> "Your BMI is x. You're in the healthy weight range."
Between 25 and 29.9 --> "Your BMI is x. You're in the overweight range."
Between 30 and 39.9 --> "Your BMI is x. You're in the obese range."
'''



#%%
height = 1.7 #float(input('what is your height(m): '))
weight = 135 #float(input('what is your weight(kg): '))


# %%
bmi = round(weight / (height**2), 1)


# %%
if bmi < 18.5:
    print(f'Your BMI is {bmi}. You\'re in the underweight range.')
elif bmi >= 18.5 and bmi <= 24.9:
    print(f'Your BMI is {bmi}. You\'re in the healthy weight range.')
elif bmi >= 25 and bmi <= 29.9:
    print(f'Your BMI is {bmi}. You\'re in the overweight range.')
elif bmi >= 30 and bmi <= 39.9:
    print(f'Your BMI is {bmi}. You\'re in the obese range.')

