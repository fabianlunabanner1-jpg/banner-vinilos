import streamlit as st
import urllib.parse

# Configuración base adaptada a pantallas de celulares
st.set_page_config(page_title="Catálogo Emprende", page_icon="📱", layout="centered")

# --- BASE DE DATOS DE RUBROS (Con links simulados a Redes Sociales) ---
datos_rubros = {
    "💈 Barbería & Peluquería": {
        "subtitulo": "Cortá a tiempo. Estilo, comunidad y buena atención.",
        "telefono": "5491112345678",
        "instagram": "https://instagram.com/barberia_demo_sanvicente",
        "facebook": "https://facebook.com/barberia_demo_sanvicente",
        "bg_color": "#111827",      # Gris Oscuro
        "card_color": "#1F2937",    # Gris Carbón
        "text_color": "#F3F4F6",    # Blanco Hueso
        "accent_color": "#D97706",  # Oro / Bronce
        "btn_text": "#FFFFFF",
        "items": [
            {"nombre": "Corte de Cabello Tradicional", "precio": "$ 6.000", "desc": "Corte clásico o moderno con asesoramiento de estilo y peinado con pomada.", "img": "https://images.unsplash.com/photo-1503951914875-452162b0f3f1?w=500&q=80"},
            {"nombre": "Combo Completo (Pelo + Barba)", "precio": "$ 9.500", "desc": "El servicio definitivo para renovar tu look. Incluye bebida de cortesía.", "img": "https://images.unsplash.com/photo-1585747860715-2ba37e788b70?w=500&q=80"}
        ],
        "accion": "Reservar Turno"
    },
    "💅 Estética (Uñas y Pestañas)": {
        "subtitulo": "Resaltá tu mirada y cuidá tus manos. Atención personalizada.",
        "telefono": "5491187654321",
        "instagram": "https://instagram.com/estetica_demo_nails",
        "facebook": "https://facebook.com/estetica_demo_nails",
        "bg_color": "#FFF1F2",      # Rosa Pastels
        "card_color": "#FFFFFF",    # Blanco puro
        "text_color": "#4C0519",    # Guinda
        "accent_color": "#F43F5E",  # Rosa encendido
        "btn_text": "#FFFFFF",
        "items": [
            {"nombre": "Esculpidas en Gel / Acrílico", "precio": "$ 14.000", "desc": "Estructura perfecta con largo personalizado, incluye esmaltado semipermanente.", "img": "https://images.unsplash.com/photo-1604654894610-df490651e56c?w=500&q=80"},
            {"nombre": "Lifting + Tinte de Pestañas", "precio": "$ 8.500", "desc": "Arqueado natural de tus pestañas junto con una dosis de color negro intenso.", "img": "https://images.unsplash.com/photo-1583001931096-959e9a1a6223?w=500&q=80"}
        ],
        "accion": "Pedir Turno"
    }
}

# --- CONTROL LATERAL DEMO ---
st.sidebar.markdown("### 🛠️ Personalización")
rubro_seleccionado = st.sidebar.selectbox("Elegí el rubro para ver el diseño:", list(datos_rubros.keys()))

config = datos_rubros[rubro_seleccionado]

# --- INYECCIÓN DE ESTILOS CSS ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: {config['bg_color']} !important; }}
    
    .producto-card {{
        background-color: {config['card_color']};
        padding: 18px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.04);
        margin-bottom: 20px;
    }}
    
    .titulo-app {{ color: {config['text_color']}; font-family: Arial; font-weight: 800; text-align: center; margin-bottom: 2px; }}
    .sub-app {{ color: {config['text_color']}; opacity: 0.8; text-align: center; font-size: 15px; margin-bottom: 25px; }}
    .nombre-prod {{ color: {config['text_color']}; font-weight: bold; margin: 0; }}
    .precio-prod {{ color: {config['accent_color']}; font-size: 20px; font-weight: bold; margin: 5px 0; }}
    .desc-prod {{ color: {config['text_color']}; opacity: 0.85; font-size: 14px; }}
    
    /* Botón de WhatsApp */
    .btn-whatsapp {{
        display: block;
        text-align: center;
        background-color: {config['accent_color']};
        color: {config['btn_text']} !important;
        padding: 10px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        font-size: 14px;
        margin-top: 12px;
    }}
    
    /* Botones de Redes Sociales */
    .btn-red {{
        display: inline-block;
        width: 45%;
        text-align: center;
        padding: 8px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        font-size: 13px;
        margin: 5px;
        color: white !important;
    }}
    .btn-instagram {{ background-color: #E1306C; }} /* Color oficial Instagram */
    .btn-facebook {{ background-color: #1877F2; }}  /* Color oficial Facebook */
    </style>
    """, unsafe_allow_html=True)

# --- VISTA DE LA APP ---
st.markdown(f"<h1 class='titulo-app'>{rubro_seleccionado}</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='sub-app'>{config['subtitulo']}</p>", unsafe_allow_html=True)

# Lista de Productos
for item in config["items"]:
    st.markdown('<div class="producto-card">', unsafe_allow_html=True)
    col_img, col_info = st.columns([1, 1.8], gap="medium")
    
    with col_img:
        st.markdown(f'<img src="{item["img"]}" style="width:100%; border-radius:12px; object-fit: cover; aspect-ratio: 1/1;">', unsafe_allow_html=True)
        
    with col_info:
        st.markdown(f"<h4 class='nombre-prod'>{item['nombre']}</h4>", unsafe_allow_html=True)
        st.markdown(f"<div class='precio-prod'>{item['precio']}</div>", unsafe_allow_html=True)
        st.markdown(f"<p class='desc-prod'>{item['desc']}</p>", unsafe_allow_html=True)
        
        texto_mensaje = f"Hola! Me interesa el servicio: {item['nombre']} ({item['precio']})."
        link_ws = f"https://wa.me/{config['telefono']}?text={urllib.parse.quote(texto_mensaje)}"
        st.markdown(f"<a class='btn-whatsapp' href='{link_ws}' target='_blank'>💬 {config['accion']}</a>", unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

# --- SECCIÓN DE REDES SOCIALES (La interrelación) ---
st.write("##")
st.markdown("<p style='text-align: center; font-weight: bold; margin-bottom: 5px;'>📱 Seguinos en nuestras redes:</p>", unsafe_allow_html=True)

# Contenedor centrado para los botones de redes
st.markdown(f"""
    <div style='text-align: center;'>
        <a class='btn-red btn-instagram' href='{config['instagram']}' target='_blank'>📸 Instagram</a>
        <a class='btn-red btn-facebook' href='{config['facebook']}' target='_blank'>👥 Facebook</a>
    </div>
""", unsafe_allow_html=True)

st.write("##")
st.markdown(f"<p style='text-align: center; color: {config['text_color']}; opacity: 0.5; font-size: 11px;'>Desarrollado en San Vicente • Prototipo Digital PYME</p>", unsafe_allow_html=True)