
import requests
import random
from keys import app_id, app_key



# function that gets all the inputs from the user (language, type of search, ingredient and random/all recipes) and the first one to execute
def run():   
    # separates english and spanish navigation
    language = input("Do you want to search in English (enter: E) or Spanish (enter: S)? ").lower()
    
    # SPANISH
    if (language == "spanish" or language == "s"):
        api = "test-es"
        input_choice = input('Quiere elegir un ingrediente para buscar una receta (ingrese: I) o quiere elegir por cantidad de calorías(ingrese: C)? ').lower()
        
        #recipe search
        if (input_choice == 'i'):
            ingredient = input('Elija un ingrediente: ')
            input_random = input("¿Quiere una receta al azar (ingrese: R) o quiere revisar el catálogo (ingrese: C)? ").lower()

        # calls the function that decides if the user wants all the recipes or a random recipe
            random_ask(ingredient, api, input_random)
            
        #meal planner
        elif (input_choice== 'c'):
            calories = int(input("Cuántas calorías quiere consumir en una comida? "))
            meal_planner(calories, api)
        
    # ENGLISH   
    elif(language == "english" or language == "e"):
        api = "api"  
        input_choice = input('Do you want to choose by ingredient (enter: I) or by calories (enter: C)? ').lower()
        
        # recipe search
        if (input_choice == 'i'):
            ingredient = input('Enter an ingredient: ')
            input_random = input("Do you want a random recipe (enter: R) or do you want to check our catalogue (enter: C)? ").lower()
            
            # calls the function that decides if the user wants all the recipes or a random recipe
            random_ask(ingredient, api, input_random)
        
        # meal planner  
        elif (input_choice == 'c'):
            calories = int(input("what's the maximum calories for your meal? "))
            meal_planner(calories, api)
            
                  
    else:
        print("Enter a valid language ")
        run()



#  function that divides the search between random recipe and catalogue
def random_ask(ingredient, api, input_random):
    
    if(input_random == "r" or input_random == "random"):
        random_recipe_search(ingredient, api)
        
    elif(input_random =="c" or input_random =="check"):
        recipe_search(ingredient, api)
        
    else:
        input_random
    

          

# gets data from the API for the meal planner
def get_api_calorie_data(api, calories):
    if (api == "test-es"):
        calories_lang = "calorias"
    else:
        calories_lang = "calories"
        
    result = requests.get('https://{}.edamam.com/search?q={}={}&app_id={}&app_key={}'.format(api, calories_lang, calories, app_id, app_key))
    
    data = result.json()["hits"]
   
    return data

  
   
# gets data from the API for the recipe search
def get_api_data(api, ingredient):
   
    result = requests.get('https://{}.edamam.com/search?q={}&app_id={}&app_key={}'.format(api, ingredient, app_id,
    app_key))
    data = result.json()["hits"]
    
    return data

   
    

# function that prints all the recipes
def recipe_search(ingredient, api):  
    
    results = get_api_data(api, ingredient)
 
 #prints in console   
    for result in results:
        recipe = result['recipe']
        # print("Recipe:")
        print(recipe['label'])
        # print("Link:")
        print(recipe['uri'])
        print("==========================")
        
        
#saves recipes in a file
    with open("Recipes.txt", "a") as Recipes:
        for result in results:
            recipe = result['recipe']
            Recipes.write("\n")
            Recipes.write(f"{recipe['label']}\n")
            Recipes.write(f"URL: {recipe['uri']}\n")
            Recipes.write("\n")
            Recipes.write("========================================")
            
        Recipes.close()        
    
 
 

# function that prints a random recipe
def random_recipe_search(ingredient, api):
    
    all_recipes = get_api_data(api, ingredient)

    random_number = random.randint(0, len(all_recipes)-1)    
    random_recipe = all_recipes[random_number]
    recipe = random_recipe["recipe"]

#prints in console 
    print("\n")
    print(recipe["label"])
    if api == "test-es":
        print("Ingredientes:")
    else:
        print("Ingredients:")
    for ingredient in recipe["ingredientLines"]:
        print(f"-{ingredient}")
        
#saves recipe in a file
    with open("Recipes_random.txt", "a") as Recipes_random:
            Recipes_random.write("\n")
            Recipes_random.write(f"{recipe['label']}\n\n")
            for ingredient in recipe["ingredientLines"]:
                Recipes_random.write(f"-{ingredient}\n")
            Recipes_random.write("\n")
            Recipes_random.write("========================================")
            
            Recipes_random.close()
   

 
 # function for meal planner
def meal_planner(calories, api):
  
    results_meal = get_api_calorie_data(api, calories)

   
    # prints in console
    for result in results_meal[0:3]:
        recipe = result['recipe']
        # print("Recipe:")
        print(recipe['label'])
        print("------------------------------")
        if api == "test-es":
            print("Ingredientes:")
        else:
            print("Ingredients:") 
        for ingredient in recipe["ingredientLines"]:
            print(f"-{ingredient}")
        print("=============================")
        print("\n")
    
    #saves the recipes in a file      
        with open("Meal_planner.txt", "a") as Meal_planner:
            Meal_planner.write("\n")
            Meal_planner.write(f"{recipe['label']}\n\n")
            for ingredient in recipe["ingredientLines"]:
                Meal_planner.write(f"-{ingredient}\n")
            Meal_planner.write("\n")
            Meal_planner.write("========================================")
            
            Meal_planner.close()
           

    
 
    
# *******program starts here********          
run()

