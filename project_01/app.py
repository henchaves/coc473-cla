import streamlit as st
import numpy as np
import base64
import pandas as pd

from utils import (
  decomposicao_lu,
  resolve_lu,
  decomposicao_cholesky,
  resolve_cholesky
)


def download_txt(filename, label=""):
  with open(filename, "r") as f:
    encoded_file = f.read().encode()
  b64 = base64.b64encode(encoded_file).decode()
  href = f'<a href="data:file/csv;base64,{b64}" download="{filename}" target="_blank">{label}</a>'
  return href

def convert_matrix_to_latex(np_array, label):
  m, n = np_array.shape
  latex_string = ""
  latex_string += str(label)
  latex_string += " = \n"
  latex_string += "\\begin{bmatrix}"
  for i in range(m):
    row_string = ""
    for j in range(n):
      row_string += str(np_array[i][j])
      if j != n-1:
        row_string += " & "
      else:
        row_string += " \\\\ "
    latex_string += row_string
  latex_string += "\\end{bmatrix}"
  return latex_string

def read_matrix(file_input):
  return pd.read_table(file_input, header=None, sep=" ").to_numpy()

def main():
  st.title("COC473 - Primeiro trabalho prático")
  # st.header("UFRJ - Escola Politécnica - Eng. de Computação e Informação")
  menu = ["Decomposição LU", "Decomposição de Cholesky", 
          "Tarefa 3"]
  choice = st.sidebar.selectbox("Implementações", menu)

  if choice == "Decomposição LU":
    st.subheader("Implementação 1.1 - Decomposição LU")

    st.markdown("<p>Forneça os arquivos da <strong>Matriz A</strong> e <strong>Vetor B</strong>, em arquivos no formato <strong>txt</strong>. Separe as colunas utilizando um espaço, conforme os exemplos:</p>", unsafe_allow_html=True)

    st.markdown(download_txt("src/matrix_A_lu_sample.txt", label="Download exemplo de Matriz A"), unsafe_allow_html=True)

    st.markdown(download_txt("src/vector_B_lu_sample.txt", label="Download exemplo do Vetor B"), unsafe_allow_html=True)

    st.markdown("<p>Faça os uploads abaixo:</p>", unsafe_allow_html=True)

    matrix_A_input = st.file_uploader("Matriz A", type="txt")
    if matrix_A_input:
      matrix_A = read_matrix(matrix_A_input)
      st.latex(convert_matrix_to_latex(matrix_A, "Matriz A"))

    vector_B_input = st.file_uploader("Vetor B", type="txt")
    if vector_B_input:
      vector_B = read_matrix(vector_B_input)
      st.latex(convert_matrix_to_latex(vector_B, "Vetor B"))
    
    if (matrix_A_input and vector_B_input):
      button = st.button("Calcular")
      if button:
        try:
          matrix_L, matrix_U = decomposicao_lu(matrix_A)
          vector_X = resolve_lu(matrix_L, matrix_U, vector_B)
          st.latex(convert_matrix_to_latex(matrix_L, "Matriz L"))
          st.latex(convert_matrix_to_latex(matrix_U, "Matriz U"))
          st.latex(convert_matrix_to_latex(vector_X, "Vetor X"))
        except:
          st.error("A combinação de vetor B e matriz A fornecida não tem solução.")

  elif choice == "Decomposição de Cholesky":
    st.subheader("Implementação 1.2 - Decomposição de Cholesky")

    st.markdown("<p>Forneça os arquivos da <strong>Matriz A</strong> e <strong>Vetor B</strong>, em arquivos no formato <strong>txt</strong>. Separe as colunas utilizando um espaço, conforme os exemplos:</p>", unsafe_allow_html=True)

    st.markdown(download_txt("src/matrix_A_cholesky_sample.txt", label="Download exemplo de Matriz A"), unsafe_allow_html=True)

    st.markdown(download_txt("src/vector_B_cholesky_sample.txt", label="Download exemplo do Vetor B"), unsafe_allow_html=True)

    st.markdown("<p>Faça os uploads abaixo:</p>", unsafe_allow_html=True)

    matrix_A_input = st.file_uploader("Matriz A", type="txt")
    if matrix_A_input:
      matrix_A = read_matrix(matrix_A_input)
      st.latex(convert_matrix_to_latex(matrix_A, "Matriz A"))

    vector_B_input = st.file_uploader("Vetor B", type="txt")
    if vector_B_input:
      vector_B = read_matrix(vector_B_input)
      st.latex(convert_matrix_to_latex(vector_B, "Vetor B"))
    
    if (matrix_A_input and vector_B_input):
      button = st.button("Calcular")
      if button:
        try:
          matrix_L = decomposicao_cholesky(matrix_A)
          vector_X = resolve_cholesky(matrix_L, vector_B)
          st.latex(convert_matrix_to_latex(matrix_L, "Matriz L"))
          st.latex(convert_matrix_to_latex(vector_X, "Vetor X"))
        except:
          st.error("A combinação de vetor B e matriz A fornecida não tem solução.")
  
  elif choice == "Tarefa 3":
    st.header("Implementação 3 - Tarefa 3")

if __name__ == "__main__":
  main()

