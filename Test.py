import streamlit as st

# 1. Page Config
st.set_page_config(page_title="El Ancla Invisible", page_icon="⚓", layout="centered")

# Custom CSS for the minimalist "Article" feel
st.markdown("""
    <style>
    .right-quote {
        text-align: right;
        font-style: italic;
        color: #555;
        border-right: 3px solid #ddd;
        padding-right: 15px;
        margin: 20px 0;
    }
    .main-header {
        font-family: 'Georgia', serif;
        color: #1a1a1a;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Navigation Sidebar
with st.sidebar:
    st.markdown("## 🧭 Navegación")
    selected = st.radio(
        "Selecciona una sección:",
        ["Portada", "Contenido", "Conclusiones", "Referencias"],
        index=0
    )
    st.divider()
    st.caption("Investigación y Divulgación")

# --- SECCIÓN: PORTADA ---
if selected == "Portada":
    st.title("El Ancla Invisible")
    st.markdown("### Por Qué Tu Patria Se Siente Como una 'Madre' y Cómo Esto Moldea Tu Identidad")
    
    st.write("---")
    
    # Right-aligned quote correctly indented
    st.markdown("""
        <div class="right-quote">
            "Would the valleys were your streets, and the green paths your alleys, 
            that you might seek one another through vineyards, and come with 
            the fragrance of the earth in your garments." <br>
            <strong>— From The Prophet by Kahlil Gibran</strong>
        </div>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        ¿Alguna vez te has preguntado por qué sentimos un nudo en la garganta al escuchar nuestro himno en el extranjero? 
        No es solo patriotismo; la ciencia sugiere que nuestra relación con nuestro país de origen funciona de 
        manera muy similar al vínculo emocional que un bebé desarrolla con sus padres.
        """)
    
    with col2:
        st.markdown("### ⚓")
        st.info("**Publicación:** Marzo 2026")

# --- SECCIÓN: CONTENIDO ---
elif selected == "Contenido":
    st.header("Secciones del Contenido")
    
    # 1. Tres Formas de Entender Nuestro "Hogar"
    with st.container():
        st.subheader("Tres Formas de Entender Nuestro 'Hogar'")
        st.markdown("""
        * **Curiosidad:** ¿Es tu país tu "madre simbólica"? Descubre la psicología detrás del arraigo nacional.
        * **Beneficio:** Cómo fortalecer tu identidad cultural puede mejorar tu bienestar emocional.
        *
