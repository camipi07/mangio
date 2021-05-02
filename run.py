from flask import Flask, render_template, jsonify, request
from random import *
import json
from flask_cors import CORS, cross_origin
import requests
from app.user.user import User, createNewUser
from app.recommender.recommender import getRecommendation, getReroll
import os
import pandas as pd

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")
cors = CORS(app, support_credentials=True,
            resources={r"/api/*": {"origins": "*"}})
app.config['TESTING'] = True




@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


@app.route('/availableUsers', methods=['GET'])
@cross_origin()
def get_available_users():
    '''
    Devuelve lista de JSONs con todos los usuarios del sistema
    '''
    files = os.listdir("./app/user/users")
    predetermined_profiles = []
    for filename in files:
        with open("./app/user/users/"+filename, "r") as json_file:
            predetermined_profiles.append(json.load(json_file))

    profiles_dict = {}
    profiles_dict["users"] = predetermined_profiles

    response = app.response_class(
        response=json.dumps(profiles_dict),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/predeterminedUserProfiles', methods=['GET'])
@cross_origin()
def get_predetermined_profiles():
    '''
    Devuelve array de JSONs con todos los usuarios predeterminados del sistema.
    '''

    files = os.listdir("./app/user/predetermined_profiles")
    predetermined_profiles = []
    for filename in files:
        with open("./app/user/predetermined_profiles/"+filename, "r") as json_file:
            predetermined_profiles.append(json.load(json_file))

    profiles_dict = {}
    profiles_dict["predetermined_profiles"] = predetermined_profiles

    response = app.response_class(
        response=json.dumps(profiles_dict),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/recomendacion', methods=['GET', 'POST'])
@cross_origin()
def recommendate():
    user = request.get_json()
    data = getRecommendation(user['username'])
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/reroll', methods=['GET', 'POST'])
@cross_origin()
def reroll():
    params = request.get_json()
    reroll = getReroll(params['username'], params['recipe_id'], params['food_type'])
    response = app.response_class(
        response=json.dumps(reroll),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/newUser', methods=['GET','POST'])
@cross_origin()
def create_user():
    '''Crea un nuevo usuario del sistema y almacena sus datos en un JSON'''
    print("User creation")
    print("Is request json: ", request.is_json)
    new_user_data = request.get_json()
    print("JSON content: ", new_user_data)
    print("Tastes user: ", new_user_data["preferences"])
    new_user = createNewUser(new_user_data)

    new_user_json = json.dumps(new_user.__dict__)

    response = app.response_class(
        response=new_user_json,
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/newRecipe', methods=['GET','POST'])
@cross_origin()
def create_recipe():
    '''Crea una nueva receta y la añade al sistema (vinculada a un usuario)'''
    print("Recipe creation")
    print("Is request json: ", request.is_json)
    new_recipe_data = request.get_json()
    print("JSON content: ", new_recipe_data)
    
    
    all_ingredients = []
    
    for ingredient in new_recipe_data["ingredients"]:
        ingredient_string = ingredient['quantity']+ " " + ingredient['unit'] + " " + ingredient['name'].lower()
        all_ingredients.append(ingredient_string)

    user_recipes_df = pd.read_csv("./data/user_recipes.csv", usecols =["Creador","Nombre","Comensales","Ingredientes"])


    d = {'Creador': [new_recipe_data["creator"]], 'Nombre': [new_recipe_data["recipe_name"]], 'Comensales': [new_recipe_data["comensales"]], "Ingredientes" : [', '.join(all_ingredients)]}
    new_recipe_df = pd.DataFrame(data=d)

    user_recipes_df = user_recipes_df.append(new_recipe_df)
    user_recipes_df.to_csv("./data/user_recipes.csv")
    print("Nueva receta añadida al df de recetas de usuarios")

    #TODO: añadir parseamiento de ingredientes de la receta para extraer valores nutricionales

    response = app.response_class(
        response=new_recipe_data,
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")
