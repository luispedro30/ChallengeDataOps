import pandas as pd
import plotly.express as px
from flask import Flask, render_template, jsonify, request
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from data_processing import get_mongo_connection, insert_data_mongo
from insight import get_top_consuming_sectors, get_top_consuming_company, get_quantity_companys_by_sector
from api import get_data_api, insert_data_api

# Create Flask App
server = Flask(__name__, template_folder="templates")

# Create Dash App
app = dash.Dash(__name__, server=server, routes_pathname_prefix="/dashboard/")

# Load Data
data_path = "/app/data/dados_sensores_5000.parquet"
df = pd.read_parquet(data_path, engine="pyarrow")

# Connect to MongoDB
collection = get_mongo_connection() 
print("Conexão com o MongoDB estabelecida e coleção pronta!")
count = insert_data_mongo(df, collection)
print("oi")

@server.route("/api/data", methods=["GET"])
def get_data():
    data = get_data_api(collection)
    return jsonify(data)

@server.route("/api/data", methods=["POST"])
def insert_data():
    insert_result, updated_collection = insert_data_api(request.json, collection)
    
    # Check if insertion was successful and return response
    if insert_result.inserted_id:
        return jsonify({"message": f"Record inserted successfully with ID: {insert_result.inserted_id}"}), 201
    else:
        return jsonify({"message": "Failed to insert record."}), 400
    
@server.route('/api/top_consuming_companies', methods=['GET'])
def get_top_companies():
    collection = get_mongo_connection()
    
    df_top_consuming_companies = get_top_consuming_company(collection)
    
    top_companies_data = df_top_consuming_companies.to_dict(orient='records')
    
    return jsonify(top_companies_data)

@server.route('/api/number_companies_sector', methods=['GET'])
def get_number_companies_sector(): 
    collection = get_mongo_connection()
    
    df_number_companies_sector = get_quantity_companys_by_sector(collection)
    
    number_companies_sector_data = df_number_companies_sector.to_dict(orient='records')
    
    return jsonify(number_companies_sector_data)

# Dash Layout
app.layout = html.Div([
    html.H1("Dashboard - Consumo de Energia, Água e CO₂", style={"textAlign": "center"}),

    dcc.Tabs([
        dcc.Tab(
            label="Consumo por Setor",
            children=[
                dcc.Graph(
                    id="bar-chart-sectors",
                    figure=px.bar(get_top_consuming_sectors(collection), 
                                  x="setor", 
                                  y=["energia_kwh", "agua_m3", "co2_emissoes"], 
                                  title="Consumo de Energia, Água e CO₂ por Setor",
                                  labels={"value": "Consumo", "variable": "Recurso"},
                                  barmode="group")
                )
            ]
        ),
        
        dcc.Tab(
            label="Consumo por Empresa",
            children=[
                dcc.Graph(
                    id="bar-chart-companies",
                    figure=px.bar(get_top_consuming_company(collection), 
                                  x="empresa", 
                                  y=["energia_kwh", "agua_m3", "co2_emissoes"], 
                                  title="Consumo de Energia, Água e CO₂ por Empresa",
                                  labels={"value": "Consumo", "variable": "Recurso"},
                                  barmode="group")
                )
            ]
        ),

        dcc.Tab(
            label="Número de Empresas por Setor",
            children=[
                dcc.Graph(
                    id="bar-chart-companies-sector",
                    figure=px.bar(get_quantity_companys_by_sector(collection),
                                  x="setor", 
                                  y="numero_empresas",  
                                  title="Número de Empresas por Setor",
                                  labels={"numero_empresas": "Número de Empresas", "setor": "Setor"},
                                  barmode="group")
                )
            ]
        )
    ]),

    # Interval component to refresh data every few seconds
    dcc.Interval(
        id="interval-component",
        interval=1000,  # Update every 10 seconds
        n_intervals=0
    )
])

# Callback to update the graphs every time the interval triggers
@app.callback(
    [Output("bar-chart-sectors", "figure"),
     Output("bar-chart-companies", "figure"),
     Output("bar-chart-companies-sector", "figure")],
    [Input("interval-component", "n_intervals")]
)
def update_graphs(n):
    df_top_consuming_sectors = get_top_consuming_sectors(collection)
    df_top_consuming_companies = get_top_consuming_company(collection)
    df_number_companies_sector = get_quantity_companys_by_sector(collection)
    
    figure_sectors = px.bar(df_top_consuming_sectors,
                            x="setor", 
                            y=["energia_kwh", "agua_m3", "co2_emissoes"], 
                            title="Consumo de Energia, Água e CO₂ por Setor",
                            labels={"value": "Consumo", "variable": "Recurso"},
                            barmode="group")
    
    figure_companies = px.bar(df_top_consuming_companies,
                              x="empresa", 
                              y=["energia_kwh", "agua_m3", "co2_emissoes"], 
                              title="Consumo de Energia, Água e CO₂ por Empresa",
                              labels={"value": "Consumo", "variable": "Recurso"},
                              barmode="group")
    
    figure_companies_sector = px.bar(df_number_companies_sector,
                                     x="setor", 
                                     y="numero_empresas", 
                                     title="Número de Empresas por Setor",
                                     labels={"numero_empresas": "Número de Empresas", "setor": "Setor"},
                                     barmode="group")
    
    return figure_sectors, figure_companies, figure_companies_sector

# Flask Route for Main Page
@server.route("/")
def home():
    return render_template("index.html")

# Run the Server
if __name__ == "__main__":
    server.run(host='0.0.0.0', debug=True)
