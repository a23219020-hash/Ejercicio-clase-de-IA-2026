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

    st.markdown("""
    <div class="right-quote">
        "Would the valleys were your streets, and the green paths your alleys, 
        that you might seek one another through vineyards, and come with 
        the fragrance of the earth in your garments." <br>
        <strong>— From The Prophet by Kahlil Gibran</strong>
    </div>
    """, unsafe_allow_html=True)

# --- SECCIÓN: CONTENIDO ---
elif selected == "Contenido":
    st.header("Secciones del Contenido")
    
    with st.container():
        st.markdown("#### Tres Formas de Entender Nuestro 'Hogar'")
        c1, c2, c3 = st.columns(3)
        c1.metric("Foco", "Curiosidad")
        c2.metric("Foco", "Beneficio")
        c3.metric("Foco", "Noticia")
        
    st.markdown("---")
    
    st.subheader("La Ciencia del 'Apego Cultural'")
    st.write("Existen diferentes estilos de relación con nuestra patria:")
    
    with st.expander("Apego Seguro"):
        st.write("Sientes que tu país es un lugar de apoyo que te da confianza para explorar el mundo.")
    
    with st.expander("Apego Temeroso o Ansioso"):
        st.write("Te preocupa que tu cultura se pierda o que no seas 'lo suficientemente' parte de ella.")
    
    with st.expander("Apego Evitativo o Desapegado"):
        st.write("Mantienes una distancia emocional y no consideras que tu origen sea fundamental.")

    st.markdown("---")
    
    st.subheader("El Momento '¡Eureka!'")
    st.write("Lo que nos une a nuestra nación son nuestros **valores personales**:")
    
    col_v1, col_v2 = st.columns(2)
    with col_v1:
        st.warning("**Grupos Mayoritarios**\n\nMotor: Conservación (Estabilidad y tradiciones).")
    with col_v2:
        st.error("**Grupos Minoritarios**\n\nMotor: Poder (Estatus y éxito social).")

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
    Comprender este 'ancla invisible' nos ayuda a navegar mejor en un mundo cada vez más globalizado. 
    Al final del día, sentirnos seguros en nuestra identidad nos permite ser más abiertos y tolerantes con los demás.
    """)

# --- SECCIÓN: REFERENCIAS ---
elif selected == "Referencias":
    st.header("Referencias Bibliográficas")
    st.write("Haz clic en cada título para leer el resumen detallado del estudio:")
    
    # Reference 1
    with st.expander("Benish-Weisman, M. (2024)"):
        st.write("""
        **Resumen:** Este estudio longitudinal investiga cómo los valores humanos básicos de Schwartz motivan el desarrollo de la identidad nacional en jóvenes de grupos mayoritarios (judíos-israelíes) y minoritarios (árabes-israelíes). 
        Los hallazgos revelan que los valores de conservación (tradición, seguridad y conformidad) son los principales impulsores de la identidad nacional en la mayoría, ya que refuerzan la estabilidad del statu quo. 
        En contraste, para los jóvenes de minorías, la identidad nacional está más vinculada a los valores de poder, sugiriendo que la identificación con la nación mayoritaria puede ser vista como un recurso para alcanzar estatus o éxito social.
        """)

    # Reference 2
    with st.expander("Ferenczi & Marshall (2013)"):
        st.write("""
        **Resumen:** Las autoras aplican la teoría del apego de forma simbólica a la nación de origen, tratándola como un 'cuidador' que brinda seguridad emocional. El estudio identifica tres estilos de apego nacional: seguro-preocupado, temeroso y evitativo. 
        Los resultados indican que un apego seguro-preocupado hacia la patria predice una mayor identificación con la cultura de herencia y niveles más altos de bienestar subjetivo. 
        Por el contrario, en migrantes internacionales, el apego evitativo o de rechazo hacia su país de origen se asocia con una disminución en la identificación cultural y una menor adaptación emocional.
        """)

    # Reference 3
    with st.expander("Goedert, C. (2019)"):
        st.write("""
        **Resumen:** Investiga cómo los sentimientos de seguridad y los estilos de apego general de los ciudadanos nativos influyen en su apertura hacia los inmigrantes en Luxemburgo. El artículo distingue entre seguridad 'general' (rasgo de personalidad) y seguridad 'específica' (económica y cultural). 
        Los hallazgos muestran que las personas con un apego seguro tienen actitudes más positivas hacia la diversidad. 
        Sin embargo, la percepción de amenaza cultural o económica actúa como un predictor más fuerte de actitudes negativas que el estilo de apego general, sugiriendo que la sensación de inseguridad contextual es clave en el rechazo hacia el otro.
        """)

    # Reference 4
    with st.expander("Hong, Y-y. (2013)"):
        st.write("""
        **Resumen:** Este artículo introduce la Teoría del Apego Cultural, proponiendo que la cultura propia funciona como una 'base segura' que permite a los individuos explorar nuevos entornos culturales con confianza. 
        A través de varios experimentos, los autores demuestran que cuando se activa (o se hace priming) la seguridad cultural, los individuos muestran una mayor competencia transcultural y son menos propensos a reaccionar defensivamente ante amenazas externas. 
        La cultura se conceptualiza aquí no solo como conocimiento compartido, sino como un soporte emocional fundamental para la adaptación en un mundo globalizado.
        """)
