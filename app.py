import streamlit as st

# 1. Page Configuration (Minimalist Setup)
st.set_page_config(page_title="El Ancla Invisible", page_icon="⚓", layout="centered")

# Custom CSS for rounded borders and right-aligned quote
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stApp {
        border: 1px solid #e6e6e6;
        border-radius: 20px;
        padding: 20px;
    }
    .quote-container {
        text-align: right;
        font-style: italic;
        color: #555;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Header and Quote
st.title("El Ancla Invisible: Por Qué Tu Patria Se Siente Como una 'Madre' y Cómo Esto Moldea Tu Identidad")

st.markdown("""
<div class="quote-container">
    "Would the valleys were your streets, and the green paths your alleys, <br>
    that you might seek one another through vineyards, and come with <br>
    the fragrance of the earth in your garments." <br>
    <strong>— From The Prophet by Kahlil Gibran</strong>
</div>
""", unsafe_allow_html=True)

# 3. Introduction
st.write("""
¿Alguna vez te has preguntado por qué sentimos un nudo en la garganta al escuchar nuestro himno en el extranjero o por qué ciertos paisajes nos hacen sentir protegidos, como si estuviéramos en los brazos de un ser querido? 

No es solo patriotismo; la ciencia sugiere que nuestra relación con nuestro país de origen funciona de manera muy similar al vínculo emocional que un bebé desarrolla con sus padres.
""")

# 4. Three Ways of Understanding (Using Columns)
st.subheader("Tres Formas de Entender Nuestro 'Hogar'")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("**Curiosidad**")
    st.caption("¿Es tu país tu 'madre simbólica'? Descubre la psicología detrás del arraigo.")

with col2:
    st.success("**Beneficio**")
    st.caption("Cómo fortalecer tu identidad cultural puede mejorar tu bienestar emocional.")

with col3:
    st.warning("**Noticia**")
    st.caption("Nuevos estudios revelan que los valores son el motor secreto de la identidad.")

# 5. Core Content
st.markdown("### ¿Por qué nos importa tanto de dónde venimos?")
st.write("""
Entender nuestra conexión con la nación no es solo un ejercicio académico. Este vínculo influye directamente en nuestra salud mental y en cómo nos relacionamos con los demás. Cuando nos sentimos "seguros" en nuestra cultura, somos más propensos a ser abiertos y tolerantes.
""")

# Diagram of Attachment Styles


st.markdown("### La Ciencia del 'Apego Cultural'")
st.write("Los investigadores han descubierto que existen diferentes 'estilos' de relación con nuestra patria:")

# Using Expanders for the Styles
with st.expander("Apego Seguro"):
    st.write("Sientes que tu país es un lugar de apoyo que te da confianza para explorar el mundo.")

with st.expander("Apego Temeroso o Ansioso"):
    st.write("Te preocupa que tu cultura se pierda o que no seas 'lo suficientemente' parte de ella.")

with st.expander("Apego Evitativo o Desapegado"):
    st.write("Mantienes una distancia emocional y no consideras que tu origen sea fundamental.")

# 6. The Eureka Moment
st.divider()
st.markdown("### El Momento '¡Eureka!'")
st.write("Un estudio reciente reveló que lo que nos une a nuestra nación son nuestros **valores personales**:")

tab1, tab2 = st.tabs(["Grupos Mayoritarios", "Grupos Minoritarios"])
with tab1:
    st.write("**Motor:** La conservación (deseo de estabilidad y mantener las tradiciones).")
with tab2:
    st.write("**Motor:** El poder (búsqueda de estatus y éxito social).")

# 7. Conclusion
st.success("Nuestra identidad nacional no es una etiqueta estática, sino un proceso vivo que se alimenta de nuestra necesidad de seguridad y conexión.")

# 8. Interactive References (Dropdowns)
st.divider()
st.subheader("Referencias")
ref_choice = st.selectbox("Selecciona un artículo para ver el resumen:", [
    "Seleccionar...",
    "Benish-Weisman, M. (2024)",
    "Ferenczi & Marshall (2013)",
    "Goedert, C. (2019)",
    "Hong, Y-y. (2013)"
])

if ref_choice == "Benish-Weisman, M. (2024)":
    st.write("**Resumen:** Explora cómo los valores personales impulsan la identificación nacional en jóvenes de diversas procedencias.")
elif ref_choice == "Ferenczi & Marshall (2013)":
    st.write("**Resumen:** Analiza la asociación entre el apego a la patria y la identificación con la cultura de herencia.")
elif ref_choice == "Goedert, C. (2019)":
    st.write("**Resumen:** Investiga el sentimiento de seguridad de los nativos y sus actitudes hacia la aculturación de inmigrantes.")
elif ref_choice == "Hong, Y-y. (2013)":
    st.write("**Resumen:** Propone una nueva teoría para entender la competencia intercultural a través del apego cultural.")
