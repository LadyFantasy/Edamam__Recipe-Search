# Application ID
# 71ca93f8
​
​
# Application Keys
# 11b48d20765f456984566e814c328384
​
​
# Properties
# State:	live
​
​
# To make a request to the Edamam API use the following URL:
# https://api.edamam.com/search?q={INGREDIENT}&app_id={YOUR_APP_KEY}&app_key={YOUR_APP_KEY}
​
​
# spanish API:  https://test-es.edamam.com/search?q={INGREDIENT}&app_id={YOUR_APP_KEY}&app_key={YOUR_APP_KEY}
​
​
    
#=================================================================================================================================
​
​
# PSEUDOCODE
# 1. Input(select a language EN for English / ES for Spanish)  DONE
# 2. Select search: by ingredient / weekly meal planner   HALF DONE
# Search by ingredient: show one random recipe for that ingredient   DONE
# Weekly meal planner: daily= input(What's your ideal daily intake of calories?)
# Day 1: recipe1 + recipe2 where recipe1[calories] in range = (0, daily / 2)
# and recipe2[calories] in range (daily-recipe1, daily)
​
​
​
​
​
​
# function that shows a weekly meal planner
#def weekly_meal_planner(intake, api):
    #     app_id = '71ca93f8'
    # app_key = '11b48d20765f456984566e814c328384'
    
    
    # result = requests.get(''.format()
    # data = result.json()
   
    #the maximum amount of calories that one of the recipes should have
    #meal = intake/2
    
# We need to print the link to two recipes per day, 7 times:
    # if recipe["calories"] <= meal:
    #   recipe1 = random_recipe["recipe"]   
    # if recipe["calories"] <= intake - meal (or in range meal, intake)
    #   recipe2 = random_recipe["recipe"] 
#############--##############
    
    
# function that gets all the inputs from the user (language, ingredient and random/all recipes) and the first one to execute
def run():   
    api = ""
    language = input("Do you want to navigate in English or Spanish? (spanish/english)")
    if(language == "spanish" or language == "s"):
        api = "test-es"
        # fn = input("¿Quiere buscar por ingrediente (inserte: i) o quiere un plan semanal de comidas por calorías (inserte: p)?")
        # if fn == "p" or "P":
        #   intake = input("¿Cuál es su consumo diario de calorías ideal?")
        # elif fn == "i" or "I":
        ingredient = input('Elija un ingrediente: ')
        input_random = input("¿Quiere una receta al azar (ingrese: R) o quiere revisar el catálogo (ingrese: C)? R/C ")
​
​
    elif(language == "english" or language == "e"):
        api = "api"
        # fn = input("Do you want to search by ingredient (enter: i) or do you want to see a suggested weekly meal planner by calories (enter: p)? ")
        # if fn == "p" or "P":
        #   intake = input("What's your ideal daily calorie intake?")
        # elif fn == "i" or "I":
        ingredient = input('Enter an ingredient: ')
        input_random = input("Do you want a random recipe (enter: R) or do you want to check our catalogue (enter: C)? R/C ")
​
​
# **********************************
# THINGS TO FIX SO FAR: the requests.get() is in both functions (recipe_search and random_recipe_search). 
# It's repetitive and should be in it's own function, but I tried and it didn't work
#
# When we print a recipe or random recipe, it would be good for the fields "recipe/link/ingredients"
# to be in Spanish if we're navigating in Spanish, I was not able to modify it
#
# I'm still trying to figure out how to include a meal planner and the logic inside of it
# I'm sorry there are some lines inside the search functions that I don't really get, I'm struggling with the API
# **********************************