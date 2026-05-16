import streamlit as st
import pandas as pd

st.set_page_config(page_title="LEAN MANAGEMENT SUITE", layout="wide")

# 1. BASE DE DATOS DE CONFIGURACIÓN (Esto simula tu base de datos adaptable)
# Aquí puedes meter CUALQUIER negocio en el futuro sin tocar el código de la app
PLANTILLAS_NEGOCIOS = {
    "Gimnasio (Superior Gym)": {
        "logo": "🏋️‍♂️",
        "5s_preguntas": [
            "Seiri (Clasificar): ¿Solo hay equipo necesario en sala?",
            "Seiton (Orden): ¿Las mancuernas y discos están en sus racks?",
            "Seiso (Limpieza): ¿El equipo y agarres están desinfectados?",
            "Seiketsu (Estandarizar): ¿Existen etiquetas de peso y áreas delimitadas?",
            "Shitsuke (Disciplina): ¿El staff sigue el rol de limpieza y orden?"
        ],
        "unidad_takt": "Socios esperados por turno"
    },
    "Tienda de Ropa / Retail": {
        "logo": "🛍️",
        "5s_preguntas": [
            "Seiri (Clasificar): ¿Hay prendas dañadas o fuera de temporada en exhibición?",
            "Seiton (Orden): ¿La ropa está acomodada por talla y color?",
            "Seiso (Limpieza): ¿Los probadores y espejos están impecables?",
            "Seiketsu (Estandarizar): ¿Los precios y ofertas están claramente visibles?",
            "Shitsuke (Disciplina): ¿El personal reacomoda las prendas después de que el cliente las ve?"
        ],
        "unidad_takt": "Clientes esperados por hora"
    }
}

# 2. SELECTOR DE MODELO DE NEGOCIO
st.sidebar.title("⚙️ Configuración del SGC")
tipo_negocio = st.sidebar.selectbox("Selecciona el Modelo de Negocio Activo", list(PLANTILLAS_NEGOCIOS.keys()))

# Cargar la configuración dinámica basada en la selección
config = PLANTILLAS_NEGOCIOS[tipo_negocio]

# 3. INTERFAZ ADAPTABLE
st.title(f"{config['logo']} LEAN APP - {tipo_negocio.upper()}")
st.markdown("---")

menu = ["Inicio", "Auditoría 5S", "Calculadora de Takt Time"]
choice = st.sidebar.selectbox("Herramienta Lean", menu)

if choice == "Inicio":
    st.subheader(f"Sistema de Gestión de Calidad Adaptable")
    st.write(f"Esta herramienta está optimizada actualmente para la estructura operativa de: **{tipo_negocio}**.")

elif choice == "Auditoría 5S":
    st.subheader("📋 Checksheet de Auditoría 5S")
    st.info("Esta auditoría se adaptó automáticamente a los estándares de tu sector.")
    
    # Generar las preguntas dinámicamente según el negocio seleccionado
    respuestas = []
    for pregunta in config["5s_preguntas"]:
        estado = st.checkbox(pregunta)
        respuestas.append(estado)
    
    score = sum(respuestas)
    total_preguntas = len(config["5s_preguntas"])
    st.metric("Puntaje de Calidad 5S", f"{score}/{total_preguntas}")

elif choice == "Calculadora de Takt Time":
    st.subheader("⏱️ Ritmo de Operación (Takt Time)")
    tiempo_disponible = st.number_input("Tiempo disponible de trabajo (en minutos)", min_value=1, value=480)
    demanda = st.number_input(f"Cantidad de {config['unidad_takt']}", min_value=1, value=50)
    
    takt_time = tiempo_disponible / demanda
    st.metric("Takt Time", f"{takt_time:.2f} min por unidad")
