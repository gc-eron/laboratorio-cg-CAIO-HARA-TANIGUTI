import numpy as np
import streamlit as st

def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Bandeira dos Emirados Árabes Unidos")

bandeira = np.zeros((12, 24, 3), dtype=np.uint8)
bandeira[0:4, :] = (0, 132, 61)      # verde  
bandeira[4:8, :] = (255, 255, 255)   # branco 
bandeira[8:12, :] = (0, 0, 0)        # preto
bandeira[:, 0:6] = (200, 16, 46)     # vermelho

st.image(ampliar(bandeira))

