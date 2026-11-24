import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

st.header("2. Brilho")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
fator = st.slider("Brilho", 0.0, 2.0, 1.35)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
v = hsv[:, :, 2].astype(float)
v = v * fator
v = np.clip(v, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 2] = v
st.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB), caption="Foto com o brilho ajustado")

st.header("8. Negativo")
negativo = 255 - img
st.image(negativo, caption="Foto em negativo")

st.header("11. Espelhamento")
col1, col2 = st.columns(2)
col1.image(img[:, ::-1], caption="Espelho horizontal")
col2.image(img[::-1, :], caption="Espelho vertical")

st.header("19. Moldura")
altura, largura = img.shape[0], img.shape[1]
espessura = st.slider("Espessura", 1, 250, 65)
r = st.slider("R (vermelho)", 0, 255, 212)
g = st.slider("G (verde)", 0, 255, 175)
b = st.slider("B (azul)", 0, 255, 55)
nova = img.copy()
nova[:espessura, :] = (r, g, b)
nova[altura - espessura:, :] = (r, g, b)
nova[:, :espessura] = (r, g, b)
nova[:, largura - espessura:] = (r, g, b)
st.image(nova, caption="Foto com moldura")

st.header("20. Pixel art")
passo = st.slider("Tamanho do pixel", 1, 120, 32)
pequena = img[::passo, ::passo]
pixelada = pequena.repeat(passo, axis=0).repeat(passo, axis=1)
st.image(pixelada, caption="Foto em pixel art")