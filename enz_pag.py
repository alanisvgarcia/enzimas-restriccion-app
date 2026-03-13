import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Metilación y Enzimas de Restriccióm", page_icon="🧬")

st.title(" Consulta actividad de enzimas de Restricción")
st.write("Determina si una enzima cortará el ADN basándose en el estado de metilación.")

# 2. Datos de las enzimas
reglas_enzimas = {
    "HpaII": {
        "metilado": "no corta",
        "no metilado": "corta"
    },
    "McrBC": {
        "metilado": "corta",
        "no metilado": "no corta"
    }
}

# 3. Interfaz con "boxes" (cajas de selección y texto)
# Usamos un selectbox para evitar errores de escritura
enzima = st.selectbox("Selecciona la enzima:", ["HpaII", "McrBC"])

if enzima == "HpaII":
    st.image("imagenes/hpa2.jpg", caption="Mecanismo de HpaII: Bloqueada por metilación")
    st.info("HpaII es sensible a la metilación. Corta en CCGG solo si el ADN está libre de grupos metilo.")

elif enzima == "McrBC":
    st.image("imagenes/mcrbc.jpg", caption="Mecanismo de McrBC: Requiere metilación para cortar")
    st.warning("McrBC es una nucleasa que busca sitios metilados para activarse.")



# Usamos radio buttons para el estado
estado_enz = st.radio("¿Cuál es el estado de metilación del ADN?", ["metilado", "no metilado"])

# 4. Lógica de ejecución al presionar un botón
if st.button("Consultar"):
    resultado = reglas_enzimas[enzima][estado_enz]
    
    # Mostrar el resultado de forma visualmente atractiva
    if "no corta" in resultado:
        st.error(f"Resultado: Con el ADN **{estado_enz}**, la enzima {enzima} **{resultado}**.")
    else:
        st.success(f"Resultado: Con el ADN **{estado_enz}**, la enzima {enzima} **{resultado}**.")

# Pie de página informativo
st.info("Nota: HpaII es sensible a la metilación, mientras que McrBC requiere metilación para cortar.")
