# MANGIO!

Servicio de recomendación de una dieta a largo plazo con un objetivo saludable determinado en base a un criterio nutricional y las preferencias del usuario.

## Descripción

Mangio! es un proyecto universitario centrado en proponer un plan de alimentación saludable a un usuario. 

Se basa en inputs sacados de la báscula Xiaomi My Body (BMI, masa muscular...) y las preferencias personales (objetivos, ingredientes habituales, feedback) para seleccionar un conjunto de recetas óptimas para una dieta equilibrada.

Se emplea un dataset de recetas en español para las recomendaciones y se usa la base de datos BECDA para obtener los valores nutricionales correspondientes a cada una.

## Estructura

```
Mangio!  
├── run.py                      # flask app
├── app                         # mangio app
│   ├── data_processing         # data scripts for ingredient extraction...
│   ├── user                    # user data and profiles
│   └── recommender             # recommender logic
├── data                        # app data as csv 
├── notebooks                   # jupyter notebooks to test the application
└── webapp                      # vue front-end
```

## Tecnologías

Dependencias de python en requirements.txt

`pip install -r requirements.txt`

## Sources

https://github.com/IanHarvey/bluepy 

https://github.com/lolouk44/xiaomi_mi_scale
