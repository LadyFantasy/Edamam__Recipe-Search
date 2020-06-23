# Application ID
# 71ca93f8


# Application Keys
# 11b48d20765f456984566e814c328384


# search example: "https://api.edamam.com/search?q=chicken&app_id=${YOUR_APP_ID}&app_key=${YOUR_APP_KEY}&from=0&to=3&calories=591-722&health=alcohol-free"

# To make a request to the Edamam API use the following URL:
# https://api.edamam.com/search?q={INGREDIENT}&app_id={YOUR_APP_KEY}&app_key={YOUR_APP_KEY}


# spanish API:  https://test-es.edamam.com/search?q={INGREDIENT}&app_id={YOUR_APP_KEY}&app_key={YOUR_APP_KEY}


    
#=================================================================================================================================


# PSEUDOCODE
# 1. Input(select a language EN for English / ES for Spanish)  DONE
# 2. Select search: by ingredient / weekly meal planner   HALF DONE
# Search by ingredient: show one random recipe for that ingredient   DONE
# Weekly meal planner: input(What's your ideal daily intake of calories?) int*7:
# show 14 random recipes that add up to the total



import requests
import random


def get_api_data(api, ingredient):
    app_id = '71ca93f8'
    app_key = '11b48d20765f456984566e814c328384'
          
    result = requests.get('https://{}.edamam.com/search?q={}&app_id={}&app_key={}'.format(api, ingredient, app_id,
    app_key))
    data = result.json()["hits"]
    
    return data


# function that searches all the recipes
def recipe_search(ingredient, api, language):  
    
    results = get_api_data(api, ingredient)
    
    for result in results:
        recipe = result['recipe']
        # print("Recipe:")
        print(recipe['label'])
        # print("Link:")
        print(recipe['uri'])
        print("==========================")
    
 
# function that searches a random recipe
def random_recipe_search(ingredient, api, language):
    
    all_recipes = get_api_data(api, ingredient)

    random_number = random.randint(0, len(all_recipes)-1)
    
    random_recipe = all_recipes[random_number]
    recipe = random_recipe["recipe"]

      
    print(recipe["label"])
    print(recipe["uri"])
    print("Ingredients:")
    for ingredient in recipe["ingredientLines"]:
        print(f"-{ingredient}")
   
    
    
    
# function that gets all the inputs from the user (language, ingredient and random/all recipes) and the first one to execute
def run():   

    language = input("Do you want to search in English or Spanish? ").lower()
    if(language == "spanish" or language == "s"):
        api = "test-es"
        ingredient = input('Elija un ingrediente: ')
        input_random = input("¿Quiere una receta al azar (ingrese: R) o quiere revisar el catálogo (ingrese: C)? R/C ").lower()
    elif(language == "english" or language == "e"):
        api = "api"
        ingredient = input('Enter an ingredient: ')
        input_random = input("Do you want a random recipe (enter: R) or do you want to check our catalogue (enter: C)? R/C ").lower()
    else:
        print("Enter a valid language")
        language = input("Do you want to search in English or Spanish? ")
    
    
    
    if(input_random == "r" or input_random == "random" or input_random == "RANDOM"):
        random_recipe_search(ingredient, api, language)
    elif(input_random =="c" or input_random =="check"or input_random =="CHECK"):
        recipe_search(ingredient, api, language)
    else:
        input_random
    
    return        
        
run()



# **********************************
# THINGS TO FIX SO FAR: the requests.get() is in both functions (recipe_search and random_recipe_search). It's repetitive and should be in it's own function, but I tried and it didn't work
# **********************************


