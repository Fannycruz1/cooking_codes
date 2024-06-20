
# I wanted to create a seperate menu for when the user would like to do something else after their 
# initial response 
# creating a function that will be used for the majority of the program 
def menu_setup() : 
    print("What else would you like to do? ")
    print("Choose one of the following options: ")
    print(" A. View current ingredients")
    print(" B. View shopping list ")
    print(" C. Add ingredients to the pantry ")
    print(" D. Throw an ingredient away")
    print(" E. Add ingredients to the shopping list ")  
    print(" F. Subtract ingredients from the shopping list")
    print(" G. Exit pantry")





# this is the main function that will be doing all of the technical work 
def main() :
    ingredient_list = {}
    shopping_list = {}
    print("Welcome to the pantry! ")
    print("Choose one of the following options: ")
    print(" A. View current ingredients")
    print(" B. View shopping list ")
    print(" C. Add ingredients to the pantry ")
    print(" D. Throw an ingredient away")
    print(" E. Add ingredients to the shopping list ")  
    print(" F. Subtract ingredients from the shopping list")
    print(" G. Exit pantry")


    user_choice = input()
    user_choice = user_choice.upper()

    while (user_choice != 'G'):

        # wantto create a while loop that didn't depend on any boolean value \
        # create a an if elif else structure for the options 
        
        if user_choice == 'A' :
            # account for there being nothing in the list 
            if len(ingredient_list) == 0:
                print("There are currently no ingredients!")
            else:
                print("Current ingredients:")
                for ingredient, amount in ingredient_list.items():
                    print(f"{amount}: {ingredient}")

        
        elif user_choice == 'B':
            if len(shopping_list) == 0:
                print("There are currently no ingredients on your shopping list!")
            else:
                print("Current shopping list:",shopping_list)
                for ingredient, amount in shopping_list.items():
                    print(f"{amount}: {ingredient}")
        
        elif user_choice == 'C' :
            print("Current Ingredient List:",ingredient_list)
            # allow the user to enter upper and lower case values 
            ingredient = input("Enter the name of the ingredient to add to the pantry: ").lower()
            amount = int(input(f"Enter the amount of {ingredient} to add: "))
            if ingredient in ingredient_list:
                ingredient_list[ingredient] += amount
            else:
                ingredient_list[ingredient] = amount
            print("Current pantry ingredients:", ingredient_list)
        
        elif user_choice == 'D' :
            if len(ingredient_list) == 0:
                print("There are currently no ingredients on your list!")
                break

            else:

                # use the enumerate function to allow the user to easily pick an ingredient to throw away 
                for index,ingredient in enumerate(ingredient_list.keys(),1):
                    print(f'{index}. {ingredient_list[ingredient]} - {ingredient} ')
            
                index_of_del_item = int(input("Enter the number of the ingredient you'd like to remove: "))
                
                # Check if the entered index is valid
                if 1 <= index_of_del_item <= len(ingredient_list):
                    ingredient_to_remove = list(ingredient_list.keys())[index_of_del_item - 1]
                    del ingredient_list[ingredient_to_remove]
                    print("Updated pantry:", ingredient_list)
                else:
                    print("Invalid index")

        

        
        elif user_choice == 'E' :
            print("Current shopping list:", shopping_list)
            ingredient = input("Enter the name of the ingredient to add to the shopping list: ").lower()
            amount = int(input(f"Enter the amount of {ingredient} to add: "))
            if ingredient in shopping_list:
                shopping_list[ingredient] += amount
            else:
                shopping_list[ingredient] = amount
            print("Current shopping list:", shopping_list)

        elif user_choice == 'F' :
            if len(shopping_list) == 0:
                print("There are currently no ingredients on the shopping list!")

            else:
                
                for index, ingredient in enumerate(shopping_list.keys(), 1):
                    print(f"{index}. {ingredient} - {shopping_list[ingredient]}")

                if 1 <= index_of_del_item <= len(shopping_list):
                    ingredient_to_remove = list(shopping_list.keys())[index_of_del_item - 1]
                    del shopping_list[ingredient_to_remove]
                    print("Updated shopping list:", shopping_list)
                else:
                    print("Invalid index")

        menu_setup()
        user_choice = input().upper()
        
            
        

if __name__ == "__main__":
    main()
