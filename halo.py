import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Plan Perfecto", layout="centered")

# --- TRUCO DEL BOTÓN IMPOSIBLE: EDICIÓN SOPA PHO ---
html_codigo = """
<div style="text-align: center; font-family: sans-serif; margin-top: 30px;">
    <h1 style="color: #ffffff;">Hola, Kehara</h1>
    <h3 style="color: #b0b0b0; line-height: 1.6; font-size: 20px;">
        Sabes, lo he estado pensando... ¿Qué tal si mejor voy hasta Playas de Tijuana para verte, qué te parece? <br>
        Al cabo que vivimos a ladito JAJAJA
    </h3>
    <hr style="border: 1px solid #333; margin: 20px 0;">
    
    <!-- Contenedor de botones -->
    <div id="contenedor-botones" style="position: relative; height: 220px; width: 100%; max-width: 500px; margin: 0 auto;">
        
        <!-- Botón SÍ -->
        <button onclick="aceptar()" style="
            position: absolute; 
            left: 15%; 
            top: 20%;
            padding: 15px 30px; 
            font-size: 18px; 
            background-color: #28a745; 
            color: white; 
            border: none; 
            border-radius: 8px; 
            cursor: pointer;
            width: 140px;">
            Sí, vamos
        </button>
        
        <!-- Botón NO -->
        <button id="btn-no" onmouseover="esquivar()" onclick="esquivar()" style="
            position: absolute; 
            left: 55%; 
            top: 20%;
            padding: 15px 30px; 
            font-size: 18px; 
            background-color: #dc3545; 
            color: white; 
            border: none; 
            border-radius: 8px; 
            cursor: pointer;
            width: 140px;
            transition: all 0.03s ease;">
            No, gracias
        </button>
    </div>
    
    <!-- Respuesta con el tremendo plot twist -->
    <div id="mensaje-final" style="display: none; padding: 20px; margin-top: 10px;">
        <h2 style="color: #2ac74e; font-weight: bold; line-height: 1.8; font-size: 25px;">
            Perfectooo, así paseamos en la playa y comemos mariscos que sé que a ti te encantan mucho 😎🤓😂
        </h2>
        <h2 style="color: #ffffff; font-weight: bold; line-height: 1.8; font-size: 25px; margin-top: 15px;">
            Ntc JAJAJA, te invito una sopa pho 🙂‍↕️✋🍲
        </h2>
    </div>
</div>

<script>
// Función para mover el botón "No"
function esquivar() {
    const btnNo = document.getElementById('btn-no');
    const anchoMax = 75; 
    const altoMax = 65;  
    
    const nuevoX = Math.floor(Math.random() * anchoMax);
    const nuevoY = Math.floor(Math.random() * altoMax);
    
    btnNo.style.left = nuevoX + '%';
    btnNo.style.top = nuevoY + '%';
}

// Función al darle clic al "Sí"
function aceptar() {
    document.getElementById('contenedor-botones').style.display = 'none';
    document.getElementById('mensaje-final').style.display = 'block';
}
</script>
"""

# Renderiza la página web en Streamlit
st.components.v1.html(html_codigo, height=700)