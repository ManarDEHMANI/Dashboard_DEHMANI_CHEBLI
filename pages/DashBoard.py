# Importations princiaples
from dash import html, dcc
from components.callbacks import (
    region_dropdown,
    dept_dropdown,
    year_slider,
    material_dropdown,
    group_dropdown,
    sous_group_dropdown,
)

# Définition du layout (structure) de l'application pour le Dashboard
layout_DashBoard = html.Div(className='custom-row',
    children=[
        html.H1("Dashboard Environnemental",style={'text-align': 'center','color':'White','margin-bottom':'50px'}),  # Titre principal du tableau de bord

        html.Div(
            [
                html.Div(region_dropdown),  # Sélecteur de région
                html.Div(dept_dropdown),  # Sélecteur de département
            ],
            style={
               "width": "100%",
                "margin": "auto",
               
            },
            #className='col-6',  # Diviser en deux colonnes
        ),
        # Carte des stations météorologiques
        html.Div(
            dcc.Graph(id="map_station", figure={}),style={
                    'display': 'flex',
                'align-items': 'center',
                'justify-content': 'center',
                'height': '600px',
                
        },
        ),  

       # html.Div(year_slider),  # Sélecteur d'année avec slider

        html.Div(
            [
                html.Div([dcc.Graph(id="hist_annee", figure={}, responsive=True),html.Div(year_slider,style={'padding':'10px',})],
                 style={'padding-bottom':'10px','width': '100%', 'height': '500px','overflow': 'auto'}
                         ),
                html.Div([dcc.Graph(id="hist_superficie", figure={}, responsive=True)],
                 style={'width': '100%', 'height': '500px', 'overflow': 'auto'}
                 ),
            ],
           # className='col-6',
            style={'display':'flex'},
            
        ),

        html.Div(className='bg-black',children=[material_dropdown, group_dropdown], style={'display': 'flex',
        },),  # Sélecteur de matériaux d'emballage

        html.Div(
         children= [
                html.Div([dcc.Graph(id="score_material", figure={})], style={'width': '100%', 'height': '500px','overflow': 'auto'}),  # Histogramme de coût énergétique
                html.Div([dcc.Graph(id="impact-climat-utilisation-sol", figure={})], style={'width': '100%', 'height': '500px','overflow': 'auto'}),  # Histogramme d'impact climatique sur l'utilisation du sol
            ],
            #className='col-6',  # Diviser en deux colonnes
             style={'display': 'flex'},
        ),

        html.Div(sous_group_dropdown),  # Sélecteur de sous-groupe d'aliments

        html.Div(
            dcc.Graph(id="impact-climat-ozone", figure={})
        ),  # Histogramme d'impact climatique sur la couche d'ozone
    ],
     style={'backgroundColor': 'black'},
)
