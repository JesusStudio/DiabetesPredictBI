import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ===================================================
# CONFIGURACIÓN
# ===================================================

st.set_page_config(
    page_title="DiabetesPredictBI",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 DiabetesPredictBI")
st.markdown("### Dashboard Analítico para la Predicción de Diabetes")
st.markdown("---")

# ===================================================
# CARGAR DATOS
# ===================================================

df = pd.read_csv("dataset_personal.csv")

# ===================================================
# KPIs
# ===================================================

total = len(df)
diabetes = len(df[df["Diagnostico_Diabetes"]=="Si"])
porcentaje = diabetes/total*100

col1,col2,col3 = st.columns(3)

with col1:
    st.metric("👨‍⚕️ Total Pacientes", total)

with col2:
    st.metric("🩺 Casos de Diabetes", diabetes)

with col3:
    st.metric("📈 % Diabetes", f"{porcentaje:.2f}%")

st.markdown("---")

# ===================================================
# FILA 1
# ===================================================

col1,col2 = st.columns(2)

with col1:

    st.subheader("Pacientes por Grupo de Edad")

    conteo = df["Grupo_Edad"].value_counts()

    fig,ax = plt.subplots(figsize=(6,4))

    ax.bar(conteo.index,conteo.values)

    ax.set_xlabel("Grupo")

    ax.set_ylabel("Cantidad")

    st.pyplot(fig,use_container_width=True)

with col2:

    st.subheader("Distribución del Nivel de Glucosa")

    fig,ax = plt.subplots(figsize=(6,4))

    ax.hist(df["Glucosa"],bins=20)

    ax.set_xlabel("Glucosa")

    ax.set_ylabel("Frecuencia")

    st.pyplot(fig,use_container_width=True)

st.markdown("---")

# ===================================================
# FILA 2
# ===================================================

col1,col2 = st.columns([2,1])

with col1:

    st.subheader("Correlación entre Variables")

    corr = df[
        [
            "Edad",
            "IMC",
            "Glucosa",
            "Presion_Arterial",
            "Indice_Metabolico"
        ]
    ].corr()

    fig,ax = plt.subplots(figsize=(7,5))

    img = ax.imshow(corr)

    plt.colorbar(img)

    ax.set_xticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns,rotation=45)

    ax.set_yticks(range(len(corr.columns)))
    ax.set_yticklabels(corr.columns)

    st.pyplot(fig,use_container_width=True)

with col2:

    st.subheader("Resumen")

    st.write("**Pacientes Totales:**",total)

    st.write("**Con Diabetes:**",diabetes)

    st.write("**Sin Diabetes:**",total-diabetes)

    st.progress(int(porcentaje))

st.markdown("---")

# ===================================================
# STORYTELLING
# ===================================================

col1,col2 = st.columns(2)

with col1:

    st.subheader("📊 Hallazgos Principales")

    st.success("La glucosa es la variable con mayor relación con la diabetes.")

    st.success("Los pacientes con IMC alto presentan mayor riesgo.")

    st.success("La mayoría de casos corresponde a adultos y adultos mayores.")

with col2:

    st.subheader("💡 Recomendaciones")

    st.info("Realizar campañas preventivas para pacientes con IMC elevado.")

    st.info("Incrementar controles médicos para adultos mayores.")

    st.info("Promover hábitos saludables y actividad física.")

st.markdown("---")

st.caption("Business Intelligence & Big Data | Dashboard Analítico de Predicción de Diabetes")
