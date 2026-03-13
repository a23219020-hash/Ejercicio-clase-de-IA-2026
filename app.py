import streamlit as st
with st.sidebar:
    st.title("Navegación")
    selected = st.radio(
        "Ir a:",
        ["Portada", "Contenido", "Conclusiones", "Referencias"]
    )
# 1. Page Config
st.set_page_config(page_title="El Ancla Invisible", page_icon="⚓", layout="wide")

# Custom CSS for the "Minimalist" and "Right-Aligned" requirements
st.markdown("""
    <style>
    .right-quote {
        text-align: right;
        font-style: italic;
        color: #666;
        border-right: 4px solid #eee;
        padding-right: 20px;
        margin: 20px 0;
    }
    .main-card {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #f0f2f6;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar Navigation
with st.sidebar:
    st.title("Navegación")
    selected = option_menu(
        menu_title=None,
        options=["Portada", "Contenido", "Conclusiones", "Referencias"],
        icons=["house", "book", "check-circle", "list-stars"],
        menu_icon="cast",
        default_index=0,
    )

# --- SECCIÓN: PORTADA ---
if selected == "Portada":
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    col_a, col_b = st.columns([2, 1])
    
    with col_a:
        st.title("El Ancla Invisible")
        st.subheader("Por Qué Tu Patria Se Siente Como una 'Madre' y Cómo Esto Moldea Tu Identidad")
        st.write("---")
        st.markdown("**Artículo de Divulgación Científica**")
        st.write("Explorando el vínculo psicológico entre el individuo y su nación.")
    
    with col_b:
        # A placeholder for a visual element or icon
        st.markdown("# ⚓")
        st.info("Lectura estimada: 5 min")

    st.markdown("""
    <div class="right-quote">
        "Would the valleys were your streets, and the green paths your alleys, 
        that you might seek one another through vineyards, and come with 
        the fragrance of the earth in your garments." <br>
        <strong>— Kahlil Gibran, The Prophet</strong>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- SECCIÓN: CONTENIDO ---
elif selected == "Contenido":
    st.header("Secciones del Contenido")
    
    # Using Containers for clean separation
    with st.container():
        st.markdown("### 1. El Vínculo Primordial")
        st.write("""
        ¿Alguna vez te has preguntado por qué sentimos un nudo en la garganta al escuchar nuestro himno? 
        La ciencia sugiere que nuestra relación con nuestro país funciona de manera muy similar al 
        vínculo emocional que un bebé desarrolla con sus padres.
        """)
        
        # Columns for the "Three ways of understanding"
        c1, c2, c3 = st.columns(3)
        c1.metric("Curiosidad", "Madre Simbólica")
        c2.metric("Beneficio", "Bienestar Emocional")
        c3.metric("Noticia", "Valores Personales")

    st.write("---")

    with st.container():
        st.markdown("### 2. La Ciencia del Apego Cultural")
        st.write("Existen diferentes 'estilos' de relación con nuestra patria:")
        
        tab_seguro, tab_ansioso, tab_evitativo = st.tabs(["Apego Seguro", "Apego Ansioso", "Apego Evitativo"])
        
        with tab_seguro:
            st.write("**Definición:** Tu país es un lugar de apoyo que te da confianza para explorar el mundo.")
        with tab_ansioso:
            st.write("**Definición:** Te preocupa que tu cultura se pierda o no ser 'lo suficientemente' parte de ella.")
        with tab_evitativo:
            st.write("**Definición:** Mantienes una distancia emocional; tu origen no es fundamental para quién eres.")

    st.write("---")

    with st.container():
        st.markdown("### 3. El Hallazgo 'Eureka'")
        st.write("Lo que nos une a nuestra nación son nuestros **valores personales**:")
        
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.markdown("> **Grupos Mayoritarios:** Motor = Conservación (estabilidad y tradición).")
        with col_m2:
            st.markdown("> **Grupos Minoritarios:** Motor = Poder (estatus y éxito social).")

# --- SECCIÓN: CONCLUSIONES ---
elif selected == "Conclusiones":
    st.header("Conclusiones y Reflexión Final")
    
    st.success("""
    Nuestra identidad nacional no es una etiqueta estática, sino un **proceso vivo** que se alimenta 
    de nuestra necesidad de seguridad y conexión. Sentirnos "en casa" actúa como un escudo protector 
    que mejora nuestra satisfacción con la vida y reduce el estrés.
    """)
    
    st.markdown("#### Reflexión")
    st.write("""
    En un mundo globalizado, comprender este 'ancla invisible' no es para cerrarnos al resto, 
    sino para navegar con mayor seguridad. ¿Cuál es tu estilo de apego con tu tierra hoy?
    """)

# --- SECCIÓN: REFERENCIAS ---
elif selected == "Referencias":
    st.header("Referencias Bibliográficas")
    st.write("Selecciona una fuente para leer el resumen del estudio:")

    refs = {
        "Benish-Weisman, M., et al. (2024)": "Analiza cómo los valores de conservación y poder median la identificación nacional en jóvenes.",
        "Ferenczi, N., & Marshall, T. C. (2013)": "Explora el apego a la patria y su asociación con la identidad cultural.",
        "Goedert, C., et al. (2019)": "Investiga sentimientos de seguridad y actitudes hacia la aculturación.",
        "Hong, Y.-y., et al. (2013)": "Propone una nueva teoría para entender la competencia transcultural."
    }

    for title, summary in refs.items():
        with st.expander(title):
            st.write(f"**Resumen:** {summary}")
