import streamlit as st
import numpy as np

from utils import (download_txt, 
                   convert_matrix_to_latex, 
                   read_matrix, 
                   save_file_as_txt)

# from algorithms.general import (verificar_matriz_quadrada, verifica_tamanho_vetor)

def main():
  st.title("COC473 - Segundo trabalho prático")
  menu = ["Método de Newton (Resolução de eq. NL)",
          "Método de Broyden (Resolução de eq. NL)"]
  choice = st.sidebar.selectbox("Implementações", menu)

  if choice == "Método de Newton (Resolução de eq. NL)":
    st.subheader("Implementação 1.1 - Método de Newton - Resolução de equação não linear")
  
  if choice == "Método de Broyden (Resolução de eq. NL)":
    st.subheader("Implementação 1.2 - Método de Broyden - Resolução de equação não linear")

  st.text("")
  st.text("")
  st.text("")
  st.text("")
  st.text("Criado por Henrique Chaves - 2021.1")

if __name__ == "__main__":
  main()