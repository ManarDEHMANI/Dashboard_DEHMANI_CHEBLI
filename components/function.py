#function.py
import dash
from data.get_data import station
import plotly.express as px

df = station()
def update_map_and_selectors(selected_region, selected_dept):
        trigger = dash.callback_context.triggered[0]['prop_id'].split('.')[0]

        if trigger == 'dept-dropdown' and selected_dept != 'Tous':
            filtered_df = df[df['Departement'] == selected_dept]
            selected_region = filtered_df['Region'].iloc[0] if not filtered_df.empty else 'Toutes'

        elif trigger == 'region-dropdown':
            if selected_region != 'Toutes':
                filtered_df = df[df['Region'] == selected_region]
                if not df[df['Departement'] == selected_dept]['Region'].equals(filtered_df['Region']):
                    selected_dept = 'Tous'
            else:
                filtered_df = df
                selected_dept = 'Tous'
        else:
            filtered_df = df

        fig = px.scatter_mapbox(filtered_df,
                                lat='Latitude',
                                lon='Longitude',
                                color='Region',
                                hover_data=['Station', "Departement", "Region"])
        fig.update_layout(
            mapbox=dict(
                center=dict(lat=46.6031, lon=1.8883),
                style="open-street-map",
                zoom=5,
            ),
            title=dict(
                text='Stations de mesure des températures en continu dans les cours d\'eau de France',
                font=dict(color='#4169E1', size=20),

            ),
            height=600,
            width=1000,
        )
        return fig, selected_region, selected_dept

def update_histogram(selected_years):
        filtered_df = df[
            (df['annee_mise_en_service'] >= selected_years[0]) & (df['annee_mise_en_service'] <= selected_years[1])]
        histogram_fig = px.histogram(filtered_df,
                                     x='annee_mise_en_service',
                                     height=600,
                                     width=1000,
                                     color_discrete_sequence=['#2ecc71']
                                     )

        histogram_fig.update_layout(
            title=dict(
                text='Nombre de stations par année de mise en service',
                font=dict(color='#e74c3c', size=20),
                x=0.5,
            ),
            bargap=0.1,
        )
        return histogram_fig

def update_histogram_superficie(_):
        # Ne pas utiliser selected_years pour filtrer les données
        histogram_superficie_fig = px.histogram(df,
                                                x='Supercifie_Topographique',
                                                height=600,
                                                width=1000,
                                                color_discrete_sequence=['#3498db']
                                                )

        histogram_superficie_fig.update_layout(
            title=dict(
                text='Distribution de la superficie topographique des stations',
                font=dict(color='#e74c3c', size=20),
                x=0.5,
            ),
            bargap=0.1,
        )
        return histogram_superficie_fig
