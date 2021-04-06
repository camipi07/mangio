import pandas as pd
import numpy as np

from config import recipes, ingredients, nvalues, images

wanted_columns = ['Recipe_id','Categoria','Nombre','Valoracion','Dificultad','Tipo']
macros = ['energia','grasa','proteina','fibra','carbohidratos','Recipe_id']

def recipes2dict(recommendations):
    '''
    :param recommendations: dict with recipe recommendation ids and type of food
                            example: {74146: 'comida', 19602: 'snack']}

    :return recom: dictionary containing all the relevant information regarding the recipes
    '''
    recom = recipes[recipes['Recipe_id'].isin(recommendations)].replace(np.nan,'None')
    updateRecipeName(recom)
    ing = ingredients[ingredients['Recipe_id'].isin(recommendations)].replace(np.nan,'None')
    img = images.replace(np.nan,'None')

    recom = recom[wanted_columns]

    recom['Comida'] = recom['Recipe_id'].apply(lambda x: recommendations[x]) # set type of food
    recom = recom.merge(nvalues[macros], on='Recipe_id') # add nutritional values
    recom = recom.merge(img, on='Recipe_id')
    recom = recom.to_dict('records')

    # append ingredients
    for recipe in recom:
        recipe['Ingredientes'] =  ing[ing['Recipe_id']==recipe['Recipe_id']].set_index('Recipe_id').to_dict('records')
    
    return recom

def updateRecipeName(df):
    df['Nombre'] = df['Nombre'].str.replace('Receta de ','')
    df['Nombre'] = df['Nombre'].str.capitalize()