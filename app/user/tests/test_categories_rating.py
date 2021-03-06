preferences = [
        {
            "categories": [
                "Pollo",
                "Verduras",
                "Arroz"
            ],
            "rating": "like"
        },
        {
            "categories": [
                "Pescado",
                "Patatas"
            ],
            "rating": "like"
        },
        {
            "categories": [
                "Carne",
                "Legumbres"
            ],
            "rating": "super"
        },
        {
            "categories": [
                "Pescado",
                "Verduras",
                "Arroz"
            ],
            "rating": "nope"
        },
        {
            "categories": [
                "Carne",
                "Pasta"
            ],
            "rating": "like"
        },
        {
            "categories": [
                "Carne",
                "Patatas"
            ],
            "rating": "super"
        },
        {
            "categories": [
                "Verduras",
                "Huevos"
            ],
            "rating": "nope"
        },
        {
            "categories": [
                "Pollo",
                "Arroz"
            ],
            "rating": "nope"
        },
        {
            "categories": [
                "Legumbres"
            ],
            "rating": "like"
        },
        {
            "categories": [
                "Verduras",
                "Pasta"
            ],
            "rating": "nope"
        },
        {
            "categories": [
                "Pescado",
                "Legumbres"
            ],
            "rating": "super"
        },
        {
            "categories": [
                "Pollo",
                "Pasta"
            ],
            "rating": "like"
        },
        {
            "categories": [
                "Huevos",
                "Patatas"
            ],
            "rating": "nope"
        },
        {
            "categories": [
                "Carne",
                "Arroz"
            ],
            "rating": "like"
        }
    ]



ocurrences = {"Carne":4,
    "Pollo":3,
    "Pescado":3,
    "Legumbres":3,
    "Verduras":5,
    "Patatas":3,
    "Arroz":4,
    "Pasta":3,
    "Huevos":3
    }
     
            
    
def get_ratings(preferences):
    
    

    ratings = {
    "Carne":0,
    "Pollo":0,
    "Pescado":0,
    "Legumbres":0,
    "Verduras":0,
    "Patatas":0,
    "Arroz":0,
    "Pasta":0,
    "Huevos":0
    }
    
    for preference in preferences:
        
        for i, category in enumerate(preference["categories"]):
            
            factors = [1,0.75,0.75] #factor de correci??n seg??n la importancia (distinci??n entre ingredientes principales y secundarios)
            
            if preference["rating"] == "like":
                
                ratings[category] += 1/ocurrences[category] * factors[i]
                
            elif preference["rating"] == "nope":
                
                ratings[category] -= 1/ocurrences[category] * factors[i]

            elif preference["rating"] == "super":
                
                ratings[category] += 1.1/ocurrences[category] * factors[i]

    return ratings       

                
print(get_ratings(preferences))