# Cuadro de Mandos: Análisis del Mercado de Autos Usados

Este proyecto consiste en una aplicación web interactiva desarrollada en Python utilizando **Streamlit**, **Pandas** y **Plotly Express**. El objetivo principal es proporcionar un tablero de control (dashboard) visual para explorar un conjunto de datos del inventario de vehículos usados en EE.UU., facilitando la identificación de patrones y distribuciones en los datos.

## Funcionalidades de la Aplicación

La aplicación proporciona herramientas interactivas que permiten al usuario generar gráficos personalizados bajo demanda:

*   **Encabezados Estructurados:** Navegación visual organizada mediante secciones claras para cada tipo de análisis.
*   **Construcción de Histogramas:** Un botón interactivo (`st.button`) que renderiza un histograma interactivo de Plotly para analizar la distribución del kilometraje (*odómetro*) de los autos.
*   **Análisis de Dispersión:** Una casilla de verificación (`st.checkbox`) que despliega de forma dinámica un gráfico de dispersión para evaluar la relación directa entre el año del modelo del vehículo y su precio de venta.

## Tecnologías Utilizadas

*   **Python 3.x**
*   **Streamlit** (Desarrollo del framework de la aplicación web)
*   **Pandas** (Manipulación y carga del conjunto de datos `.csv`)
*   **Plotly Express** (Creación de gráficos interactivos y dinámicos)
*   **Render** (Plataforma de despliegue en la nube)