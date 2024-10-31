print("WELCOME TO RECIPE LIST")
print("--------------------")

recipe_book = []

recipe = True

while recipe:
    list =input("Enter your recipe list, Write 'STOP' to stop the list: ")
    if list.upper() == 'STOP':
        recipe = False
        
print(recipe_book)
