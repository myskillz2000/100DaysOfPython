'''Making a Body Mass Index
We are going to start by making a conversion of meters to inches and then
kilograms into pounds.'''

meter_conversion = 0.0254
kg_conversion = 0.4535924

height = input("enter your height in inches: ")
weight = input("enter your weight in pounds: ")

m_height = int(height)*meter_conversion
k_weight = int(weight)*kg_conversion

BMI = k_weight / m_height**2
print(BMI)