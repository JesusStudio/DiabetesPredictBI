import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Configuración
# -----------------------------
st.set_page_config(
    page_title="Dashboard - Predicción de Diabetes",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Dashboard Analítico - Predicción de Diabetes")

# -----------------------------
# Cargar datos
# -----------------------------
df = pd.read_csv("dataset_personal.csv")

# =============================
# KPI
# =============================

total = len(df)

diabetes = len(df[df["Diagnostico_Diabetes"]=="Si"])

porcentaje = diabetes/total*100

col1,col2,col3 = st.columns(3)

col1.metric("Total Pacientes",total)

col2.metric("Pacientes con Diabetes",diabetes)

col3.metric("Porcentaje Diabetes",f"{porcentaje:.2f}%")

st.divider()

# =============================
# Gráfico de Barras
# =============================

st.subheader("Pacientes por Grupo de Edad")

conteo = df["Grupo_Edad"].value_counts()

fig,ax = plt.subplots()

ax.bar(conteo.index,conteo.values)

ax.set_xlabel("Grupo de Edad")

ax.set_ylabel("Cantidad")

st.pyplot(fig)

# =============================
# Histograma
# =============================

st.subheader("Distribución del Nivel de Glucosa")

fig,ax = plt.subplots()

ax.hist(df["Glucosa"],bins=20)

ax.set_xlabel("Glucosa")

ax.set_ylabel("Frecuencia")

st.pyplot(fig)

# =============================
# Heatmap
# =============================

st.subheader("Correlación entre Variables")

corr = df[["Edad","IMC","Glucosa","Presion_Arterial","Indice_Metabolico"]].corr()

fig,ax = plt.subplots()

imagen = ax.imshow(corr)

plt.colorbar(imagen)

ax.set_xticks(range(len(corr.columns)))

ax.set_xticklabels(corr.columns,rotation=45)

ax.set_yticks(range(len(corr.columns)))

ax.set_yticklabels(corr.columns)

st.pyplot(fig)

# =============================
# Storytelling
# =============================

st.header("Hallazgos Principales")

st.success("1. Los pacientes con mayor glucosa presentan mayor probabilidad de diabetes.")

st.success("2. El IMC elevado incrementa significativamente el riesgo.")

st.success("3. Los adultos mayores concentran la mayor cantidad de casos.")

st.header("Recomendaciones")

st.info("• Implementar campañas preventivas para pacientes con IMC alto.")

st.info("• Incrementar controles médicos en adultos mayores.")

st.info("• Promover actividad física y alimentación saludable.")
