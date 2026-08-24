import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Leer el archivo CSV desde la raíz del proyecto
car_data = pd.read_csv("notebooks/vehicles_us.csv")

# 2. Título principal de la aplicación web
st.header("Cuadro de Mandos: Análisis del Mercado de Autos Usados")

# 3. Sección informativa o introducción
st.write(
    "Utiliza las herramientas interactivas a continuación para explorar la distribución y variables del conjunto de datos de vehículos."
)

# --- BOTÓN INTERACTIVO PARA HISTOGRAMA ---
# Crear un botón que al hacer clic genera un histograma
build_histogram = st.button("Construir Histograma")

if build_histogram:  # Si el botón es pulsado
    st.write(
        "Creando un histograma para la columna de odómetro (kilometraje)"
    )

    # Crear el histograma interactivo con Plotly Express
    fig_hist = px.histogram(
        car_data, x="odometer", title="Distribución de Kilometraje (Odómetro)"
    )

    # Mostrar el gráfico interactivo en la app de Streamlit
    st.plotly_chart(fig_hist, use_container_width=True)


# --- CASILLA DE VERIFICACIÓN (CHECKBOX) PARA GRÁFICO DE DISPERSIÓN ---
# Crear una casilla de verificación para mostrar u ocultar un gráfico de dispersión
build_scatter = st.checkbox("Construir Gráfico de Dispersión")

if build_scatter:  # Si la casilla está marcada
    st.write(
        "Creando un gráfico de dispersión para analizar la relación entre Precio y Año del Modelo"
    )

    # Crear el gráfico de dispersión con Plotly Express
    fig_scatter = px.scatter(
        car_data,
        x="model_year",
        y="price",
        title="Relación entre Año del Modelo y Precio de Venta",
    )

    # Mostrar el gráfico interactivo en la app de Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)
