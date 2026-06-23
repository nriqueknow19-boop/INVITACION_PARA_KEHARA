import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Un Lirio Especial", layout="centered")

# --- LIRIO STARGAZER MÁGICO CON TALLO ESTILIZADO Y HOJAS GRÁCILES ---
html_lirio_stargazer = """
<div class="contenedor-principal">
    <div class="sparkle s1"></div>
    <div class="sparkle s2"></div>
    <div class="sparkle s3"></div>
    <div class="sparkle s4"></div>
    <div class="sparkle s5"></div>
    <div class="sparkle s6"></div>

    <div class="flower-structure">
        <div class="flower-head">
            <div class="petal back-petal left-back"></div>
            <div class="petal back-petal right-back"></div>
            <div class="petal back-petal top-back"></div>
            
            <div class="petal mid-petal left-mid"></div>
            <div class="petal mid-petal right-mid"></div>
            
            <div class="petal front-petal left-front"></div>
            <div class="petal front-petal right-front"></div>
            <div class="petal front-petal center-front"></div>
            
            <div class="flower-core">
                <div class="pistil-main"></div>
                <div class="stamen st1"><div class="anther"></div></div>
                <div class="stamen st2"><div class="anther"></div></div>
                <div class="stamen st3"><div class="anther"></div></div>
                <div class="stamen st4"><div class="anther"></div></div>
                <div class="stamen st5"><div class="anther"></div></div>
            </div>
            
            <div class="inner-glow"></div>
        </div>

        <div class="stem-container">
            <div class="main-stem"></div>
            
            <div class="botanical-leaf leaf-high-left"></div>
            <div class="botanical-leaf leaf-high-right"></div>
            <div class="botanical-leaf leaf-mid-left"></div>
            <div class="botanical-leaf leaf-low-right"></div>
        </div>
    </div>
    
    <div class="mensaje-romantico">
        Para ti... ✨
    </div>
</div>

<style>
/* Fondo místico y elegante con degradado radial */
body {
    background: radial-gradient(circle at center, #1b0c24 0%, #06020c 100%);
    margin: 0;
    overflow: hidden;
}

.contenedor-principal {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 95vh;
    font-family: 'Cinzel', 'Playfair Display', 'Segoe UI', serif;
    position: relative;
}

/* Contenedor completo del Lirio */
.flower-structure {
    position: relative;
    width: 320px;
    height: 480px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* Cabeza del Lirio (Pétalos) */
.flower-head {
    position: relative;
    width: 320px;
    height: 240px;
    display: flex;
    justify-content: center;
    align-items: flex-end;
    z-index: 10;
}

/* Base de diseño estilizado para pétalos alargados y puntiagudos tipo Stargazer */
.petal {
    position: absolute;
    bottom: 10px;
    transform-origin: bottom center;
    /* Forma alargada de lirio con puntas finas */
    border-radius: 50% 50% 45% 45% / 80% 80% 20% 20%;
    box-shadow: inset 0px 4px 15px rgba(255, 255, 255, 0.4), 0px 8px 20px rgba(0, 0, 0, 0.6);
    animation-fill-mode: forwards;
    animation-timing-function: cubic-bezier(0.25, 0.8, 0.25, 1);
}

/* --- DEGRADADOS DE COLOR INTENSO (Stargazer: Fucsia encendido a bordes blancos) --- */
.center-front {
    width: 54px;
    height: 140px;
    background: linear-gradient(to top, #ff1493, #ff69b4, #fff0f5);
    z-index: 15;
    animation: open-center 2.5s forwards;
}

.left-front {
    width: 50px;
    height: 135px;
    background: linear-gradient(to top, #e60073, #ff409f, #ffffff);
    z-index: 14;
    animation: open-left-front 2.5s forwards;
}

.right-front {
    width: 50px;
    height: 135px;
    background: linear-gradient(to top, #e60073, #ff409f, #ffffff);
    z-index: 14;
    animation: open-right-front 2.5s forwards;
}

.left-mid {
    width: 52px;
    height: 150px;
    background: linear-gradient(to top, #cc0066, #ff1493, #ffb3d9);
    z-index: 12;
    animation: open-left-mid 2.5s forwards;
}

.right-mid {
    width: 52px;
    height: 150px;
    background: linear-gradient(to top, #cc0066, #ff1493, #ffb3d9);
    z-index: 12;
    animation: open-right-mid 2.5s forwards;
}

.left-back {
    width: 56px;
    height: 160px;
    background: linear-gradient(to top, #99004d, #cc0066, #ff66b2);
    z-index: 8;
    animation: open-left-back 2.5s forwards;
}

.right-back {
    width: 56px;
    height: 160px;
    background: linear-gradient(to top, #99004d, #cc0066, #ff66b2);
    z-index: 8;
    animation: open-right-back 2.5s forwards;
}

.top-back {
    width: 48px;
    height: 155px;
    background: linear-gradient(to top, #800040, #b3005c, #ff4d94);
    z-index: 7;
    animation: open-top-back 2.5s forwards;
}

/* --- ANIMACIONES DE APERTURA REALISTA DE LOS PÉTALOS --- */
@keyframes open-center {
    0% { transform: scale(0.15) rotate(0deg); opacity: 0; filter: blur(2px); }
    35% { opacity: 1; filter: blur(0); }
    100% { transform: scale(1) translateY(12px); }
}
@keyframes open-left-front {
    0% { transform: scale(0.15) rotate(0deg); opacity: 0; }
    100% { transform: scale(1) rotate(-28deg) translateX(-22px) translateY(8px); }
}
@keyframes open-right-front {
    0% { transform: scale(0.15) rotate(0deg); opacity: 0; }
    100% { transform: scale(1) rotate(28deg) translateX(22px) translateY(8px); }
}
@keyframes open-left-mid {
    0% { transform: scale(0.15) rotate(0deg); opacity: 0; }
    100% { transform: scale(1) rotate(-58deg) translateX(-38px) translateY(-2px); }
}
@keyframes open-right-mid {
    0% { transform: scale(0.15) rotate(0deg); opacity: 0; }
    100% { transform: scale(1) rotate(58deg) translateX(38px) translateY(-2px); }
}
@keyframes open-left-back {
    0% { transform: scale(0.15) rotate(0deg); opacity: 0; }
    100% { transform: scale(1) rotate(-85deg) translateX(-48px) translateY(-14px); }
}
@keyframes open-right-back {
    0% { transform: scale(0.15) rotate(0deg); opacity: 0; }
    100% { transform: scale(1) rotate(85deg) translateX(48px) translateY(-14px); }
}
@keyframes open-top-back {
    0% { transform: scale(0.15) translateY(0); opacity: 0; }
    100% { transform: scale(1) translateY(-35px) scaleY(0.95); opacity: 0.85; }
}

/* --- CENTRO BOTÁNICO: PISTILO Y ESTAMBRES CON ANTERAS --- */
.flower-core {
    position: absolute;
    bottom: 15px;
    width: 40px;
    height: 70px;
    z-index: 20;
}

/* Pistilo central verde claro */
.pistil-main {
    position: absolute;
    bottom: 0;
    left: 18px;
    width: 5px;
    height: 65px;
    background: linear-gradient(to top, #70e000, #ccff33);
    border-radius: 3px;
    box-shadow: 0 0 8px rgba(112, 224, 0, 0.4);
    opacity: 0;
    animation: fade-in-element 2s 1.2s forwards;
}
.pistil-main::after {
    content: '';
    position: absolute;
    top: -4px;
    left: -2px;
    width: 9px;
    height: 6px;
    background: #38b000;
    border-radius: 50%;
}

/* Filamentos de los estambres */
.stamen {
    position: absolute;
    bottom: 0;
    width: 2px;
    background: linear-gradient(to top, #ff99c8, #ffffff);
    transform-origin: bottom center;
    opacity: 0;
    animation: fade-in-element 2s 1.4s forwards;
}
/* Anteras cargadas de polen dorado en la punta */
.anther {
    position: absolute;
    top: -5px;
    left: -3px;
    width: 8px;
    height: 4px;
    background: #e65c00;
    border-radius: 3px;
    box-shadow: 0 0 6px #ff9900;
}

.st1 { height: 50px; left: 8px; transform: rotate(-20deg); }
.st2 { height: 58px; left: 13px; transform: rotate(-8deg); }
.st3 { height: 60px; left: 20px; transform: rotate(5deg); }
.st4 { height: 54px; left: 26px; transform: rotate(18deg); }
.st5 { height: 48px; left: 32px; transform: rotate(30deg); }

@keyframes fade-in-element {
    0% { opacity: 0; }
    100% { opacity: 1; }
}

/* Resplandor luminoso en el fondo del cáliz */
.inner-glow {
    position: absolute;
    bottom: -5px;
    width: 120px;
    height: 120px;
    background: radial-gradient(circle, rgba(255, 20, 147, 0.45) 0%, rgba(0,0,0,0) 70%);
    z-index: 5;
    opacity: 0;
    animation: fade-in-element 3s 0.8s forwards;
}

/* --- EL TALLO Y LAS HOJAS SEPARADAS DE FORMA NATURAL --- */
.stem-container {
    position: relative;
    width: 100%;
    height: 240px;
    display: flex;
    justify-content: center;
    z-index: 5;
}

/* Tallo firme y orgánico */
.main-stem {
    width: 7px;
    height: 0px;
    background: linear-gradient(to right, #132a13, #31572c, #4f772d);
    border-radius: 4px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.4);
    animation: grow-main-stem 2.2s cubic-bezier(0.25, 0.8, 0.25, 1) forwards;
}

@keyframes grow-main-stem {
    0% { height: 0px; opacity: 0; }
    20% { opacity: 1; }
    100% { height: 230px; opacity: 1; }
}

/* Hojas de contorno estilizado distribuidas a lo largo del tallo */
.botanical-leaf {
    position: absolute;
    width: 75px;
    height: 28px;
    background: linear-gradient(to bottom right, #132a13, #3f5e3d, #4f772d);
    opacity: 0;
    transform-origin: bottom center;
    box-shadow: inset 0px 2px 4px rgba(255,255,255,0.15), 0px 4px 8px rgba(0,0,0,0.3);
}

/* Hoja Alta - Izquierda (Cerca de la flor) */
.leaf-high-left {
    left: 95px;
    top: 30px;
    border-radius: 0 100% 0 100% / 0 100% 0 100%;
    animation: deploy-leaf-left 1.8s ease-in-out 1.2s forwards;
}

/* Hoja Alta - Derecha (Un poco más abajo que la anterior) */
.leaf-high-right {
    right: 90px;
    top: 65px;
    border-radius: 100% 0 100% 0 / 100% 0 100% 0;
    animation: deploy-leaf-right 1.8s ease-in-out 1.4s forwards;
}

/* Hoja Media - Izquierda */
.leaf-mid-left {
    left: 90px;
    top: 110px;
    border-radius: 0 100% 0 100% / 0 100% 0 100%;
    animation: deploy-leaf-left 1.8s ease-in-out 1.6s forwards;
}

/* Hoja Baja - Derecha (Cerca de la base) */
.leaf-low-right {
    right: 95px;
    top: 155px;
    border-radius: 100% 0 100% 0 / 100% 0 100% 0;
    animation: deploy-leaf-right 1.8s ease-in-out 1.8s forwards;
}

/* Animaciones individuales para el despliegue de las hojas */
@keyframes deploy-leaf-left {
    0% { transform: scale(0) rotate(35deg); opacity: 0; }
    100% { transform: scale(1) rotate(-12deg); opacity: 0.95; }
}
@keyframes deploy-leaf-right {
    0% { transform: scale(0) rotate(-35deg); opacity: 0; }
    100% { transform: scale(1) rotate(12deg); opacity: 0.95; }
}

/* --- PARTÍCULAS / CHISPAS MÁGICAS EN MOVIMIENTO --- */
.sparkle {
    position: absolute;
    width: 5px;
    height: 5px;
    background-color: #fff3b0;
    border-radius: 50%;
    box-shadow: 0 0 10px 2px #fff3b0, 0 0 18px #ffffff;
    opacity: 0;
}
.s1 { left: 35%; top: 20%; animation: magic-float 4.5s infinite 0.5s; }
.s2 { left: 65%; top: 15%; animation: magic-float 3.8s infinite 1.2s; }
.s3 { left: 20%; top: 35%; animation: magic-float 5.2s infinite 0s; }
.s4 { left: 78%; top: 40%; animation: magic-float 4.1s infinite 1.8s; }
.s5 { left: 50%; top: 8%; animation: magic-float 4.8s infinite 2.2s; }
.s6 { left: 45%; top: 55%; animation: magic-float 5.5s infinite 1.0s; }

@keyframes magic-float {
    0% { transform: translateY(140px) scale(0); opacity: 0; }
    50% { opacity: 1; transform: translateY(0px) scale(1.2); }
    100% { transform: translateY(-140px) scale(0); opacity: 0; }
}

/* Mensaje Romántico Final */
.mensaje-romantico {
    margin-top: 15px;
    font-size: 25px;
    color: #ffffff;
    font-weight: 300;
    letter-spacing: 5px;
    opacity: 0;
    text-shadow: 0 0 12px rgba(255, 255, 255, 0.5);
    animation: display-text 2s ease-in-out 2.5s forwards;
}
@keyframes display-text {
    0% { opacity: 0; transform: translateY(12px); }
    100% { opacity: 0.85; transform: translateY(0); }
}
</style>
"""

# Renderizar de forma limpia el componente HTML interactivo en Streamlit
st.components.v1.html(html_lirio_stargazer, height=760)