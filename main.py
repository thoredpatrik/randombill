
#Random bill-generator
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
number_of_names =len (names)
who_pays = random.randint(0,number_of_names-1)
name_who_pays = names[who_pays]
print(f"{name_who_pays} is going to buy the meal today!")