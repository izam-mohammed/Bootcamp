pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
}

recipes = {
    "Butter chicken": [
        "chicken",
              "lemon",
        "cumin",
        "paprika",
        "chilli powder",
        "yogurt",
        "oil",
        "onion",
        "garlic",
        "ginger",
        "tomato puree",
        "almonds",
        "rice",
        "coriander",
        "lime",
    ],
    "Chicken and chips": [
        "chicken",
        "potatoes",
        "salt",
        "malt vinegar",
    ],
    "Pizza": [
        "pizza",
    ],
    "Egg sandwich": [
        "egg",
        "bread",
        "butter",
    ],
    "Beans on toast": [
        "beans",
        "bread",
    ],
    "Spam a la tin": [
        "spam",
        "tin opener",
        "spoon",
    ],
}

while True:
    user = input("What do you want\n1- cook a dish\n2 - know the balance\n3 - exit menu\n")
    if user =="3":
        break
    elif user == "2":
        print("The balance are - ")
        for key, val in pantry.items():
            print(f"{key} = {val}")
        print("")
    elif user == "1":
        print("\n what do you want to cook - ")
        for index, val in enumerate(recipes.keys()):
            index += 1
            print(f"{index} - {val}")
        dish =  int(input()) 
        try :
            if dish <= len(recipes):
                dish_name = list(recipes.keys())[dish-1]
                dish_inc = recipes[dish_name]
                for i in dish_inc:
                    pantry[i] -= 1
                print (f"\ncooked {dish_name}!\n")
        except:
            print("\nIncredients are not enough\n")