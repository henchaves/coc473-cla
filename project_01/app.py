import streamlit as st
import numpy as np
import base64


def download_txt(filename, label=""):
  with open(filename, "r") as f:
    encoded_file = f.read().encode()
  b64 = base64.b64encode(encoded_file).decode()
  href = f'<a href="data:file/csv;base64,{b64}" download="{filename}" target="_blank">{label}</a>'
  return href

def read_matrix():
  pass

def main():
  st.title("COC473 - Primeiro trabalho prático")
  # st.header("UFRJ - Escola Politécnica - Eng. de Computação e Informação")
  menu = ["Decomposição LU", "Tarefa 2", "Tarefa 3"]
  choice = st.sidebar.selectbox("Implementações", menu)

  if choice == "Decomposição LU":
    st.subheader("Implementação 1.1 - Decomposição LU")

    st.markdown("<p>Forneça os arquivos da <strong>Matriz A</strong> e <strong>Vetor B</strong>, em arquivos no formato <strong>txt</strong>. Separe as colunas utilizando um espaço, conforme os exemplos:</p>", unsafe_allow_html=True)

    st.markdown(download_txt("src/matrix_A_sample.txt", label="Download exemplo de Matriz A"), unsafe_allow_html=True)

    st.markdown(download_txt("src/vector_B_sample.txt", label="Download exemplo do Vetor B"), unsafe_allow_html=True)

    st.markdown("<p>Faça os uploads abaixo:</p>", unsafe_allow_html=True)

    matrix_A = st.file_uploader("Matriz A", type="txt")
    if matrix_A:
      st.latex(r"""
      Matriz A = 
      \begin{bmatrix}
      1 & 2 & 2 \\
      4 & 4 & 2 \\
      4 & 6 & 4\\
     \end{bmatrix}
      """)
    vector_B = st.file_uploader("Vetor B", type="txt")
    if vector_B:
      st.latex(r"""
      Vetor B = 
      \begin{bmatrix}
      3 \\
      6 \\
      10 \\
     \end{bmatrix}
      """)

  elif choice == "Tarefa 2":
    st.header("Implementação 2 - Tarefa 2")
  
  elif choice == "Tarefa 3":
    st.header("Implementação 3 - Tarefa 3")

if __name__ == "__main__":
  main()

