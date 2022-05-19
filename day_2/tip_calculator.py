print('Welcome to the tip calculator!')
check = float(input('What was the total bill?'))
tip = int(input('How much tip would you like to give? 10, 12, or 15?'))
people_count = int(input('How many people to split the bill?'))

tip_per_people = check * tip / 100 / people_count
amount_check_per_person = check / people_count + tip_per_people
print(f'Each person should pay: ${amount_check_per_person}')