import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")
