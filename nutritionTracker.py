# Khang Nguyen
# CS361 Individual Project Milestone #1
# Nutritional lookup and tracker

import sys

# temporary nutrition database
nutriData = {
    'labels': ['calories', 'water, g', 'protein, g', 'carbs, g', 'sugar, g', 'fiber, g', 'fat, g'],
    'apple': [94.6, 156, 0.43, 25.1, 18.9, 4.37, 0.3],
    'banana': [89, 75, 1.1, 22.8, 12.2, 2.6, 0.3],
    'carrot': [41, 88, 0.9, 9.6, 4.7, 2.8, 0.2],
    'return': []  # to exit to the main menu
}
log = [0]*7  # initialize array to log nutritional data
vowels = ['a', 'e', 'i', 'o', 'u']
options = ['1', '2', '3']

print("Welcome to a nutritional lookup and log.")
while True:
    option = 0  # reset option selection
    while option not in options:
        option = input("Please select one of the following by typing in the option's number: \n"
                       "[1] Lookup the nutritional facts for a food\n"  # database search/return later
                       "[2] Display the combined nutritional information logged\n"  # to be implemented later
                       "[3] Exit the system\n")

    if option == '1':
        lookup = ''  # initialize string to query
        while lookup not in nutriData.keys():
            lookup = input("Please type in a food to lookup (in lowercase). "
                           "The prompt will reappear if the food is not found, "
                           "or type 'return' to return to the main menu: ")
        if lookup == 'return':
            continue
        elif lookup[0] in vowels:  # for proper grammar
            print(f"The nutritional details for a serving of an {lookup} is as follows:")
        else:
            print(f"The nutritional details for a serving of a {lookup} is as follows:")
        for i in range(7):  # to iterate through nutritional value labels
            print(f"{nutriData['labels'][i]}: {nutriData[lookup][i]}")

        logChoice = ''
        while logChoice not in ['y', 'n']:
            logChoice = input(f"Would you like to add {lookup} nutritional data to the log? Select 'y' or 'n': ")
        if logChoice == 'y':
            servings = input("Enter the number of servings to log: ")
            for i in range(7):
                log[i] += float(servings) * float(nutriData[lookup][i])
            print(f"Your {lookup} nutritional data was logged!")
        continue
    elif option == '2':
        print("The nutritional data logged is as follows:")
        for i in range(7):
            print(f"{nutriData['labels'][i]}: {int(log[i])}")
        continue
    elif option == '3':
        print("You have chosen to exit. Goodbye!")
        sys.exit()

