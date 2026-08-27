import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Leer el archivo CSV desde la raíz del proyecto
car_data = pd.read_csv("vehicles_us.csv")

# 2. Título principal de la aplicación web
st.header("Cuadro de Mandos: Análisis del Mercado de Autos Usados en Estados Unidos")

# Encabezado de la sección del cuadro de mandos.
st.header("Cuadro de Mandos Interactivo")

# 3. Sección informativa o introducción
st.write(
    "Bienvenido al portal de análisis. Utiliza los componentes inferiores para interactuar con los datos del inventario de vehículos."
)

# Agregar una línea divisoria visual (Estetito)
st.markdown("---")

# --- SECCIÓN INTERACTIVA 1 ---
# Subencabezado para la sección del Histograma
st.subheader("1. Análisis de Distribución (Kilometraje)")

# --- BOTÓN INTERACTIVO PARA HISTOGRAMA ---
build_histogram = st.button("Construir Histograma")

if build_histogram:  # Si el botón es pulsado
    st.write("Creando un histograma para la columna de odómetro (kilometraje)")
    fig_hist = px.histogram(car_data, x="odometer", title="Distribución de Kilometraje (Odómetro)")

    st.plotly_chart(fig_hist, use_container_width=True)

# Agregar otra línea divisoria visual (Estetico)
st.markdown("---")

# --- SECCIÓN INTERACTIVA 2 ---
# Subencabezado para la sección del Gráfico de Dispersión
st.subheader("2. Análisis de Relaciones (Año vs Precio)")

build_scatter = st.checkbox("Construir Gráfico de Dispersión")

if build_scatter:
    st.write("Generando gráfico de dispersión interactivo...")
    fig_scatter = px.scatter(
        car_data,
        x="model_year",
        y="price",
        title="Relación entre Año del Modelo y Precio de Venta",
    )
    st.plotly_chart(fig_scatter, use_container_width=True)