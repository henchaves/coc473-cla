import streamlit as st
import numpy as np

from utils import (download_txt, 
                   convert_matrix_to_latex, 
                   read_matrix, 
                   save_file_as_txt)

from algorithms.general import (verificar_matriz_quadrada, verifica_tamanho_vetor)

def main():
  st.title("COC473 - Primeiro trabalho prático")
  menu = ["Decomposição LU", "Decomposição de Cholesky", 
          "Procedimento Iterativo Jacobi", "Procedimento Iterativo Gauss-Seidel",
          "Método da Potência", "Método de Jacobi",
          "Interpolação", "Regressão", "Determinante"]
  choice = st.sidebar.selectbox("Implementações", menu)

  if choice == "Decomposição LU":
    from algorithms.lu import decomposicao_lu, resolve_lu

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
          if not verificar_matriz_quadrada(matrix_A):
            raise Exception("Matriz A não é quadrada.")
          if not verifica_tamanho_vetor(matrix_A, vector_B):
            raise Exception("Vetor B não possui tamanho adequado.")
          matrix_L, matrix_U = decomposicao_lu(matrix_A)
          vector_X = resolve_lu(matrix_L, matrix_U, vector_B)

          matrix_L = np.round(matrix_L, 3)
          matrix_U = np.round(matrix_U, 3)
          vector_X = np.round(vector_X, 3)
          if np.isnan(matrix_L.sum()) or np.isnan(matrix_U.sum()):
            if np.isnan(vector_X.sum()):
              raise Exception("Um erro ocorreu ao calcular. Por favor forneça outras valores para Matriz A e vetor B.")
          st.latex(convert_matrix_to_latex(matrix_L, "Matriz L"))
          st.latex(convert_matrix_to_latex(matrix_U, "Matriz U"))
          st.latex(convert_matrix_to_latex(vector_X, "Vetor X"))
        except Exception as e:
          st.error(e)

  elif choice == "Decomposição de Cholesky":
    from algorithms.cholesky import decomposicao_cholesky, resolve_cholesky
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
          if not verificar_matriz_quadrada(matrix_A):
            raise Exception("Matriz A não é quadrada.")
          if not verifica_tamanho_vetor(matrix_A, vector_B):
            raise Exception("Vetor B não possui tamanho adequado.")

          matrix_L = decomposicao_cholesky(matrix_A)
          vector_X = resolve_cholesky(matrix_L, vector_B)
          
          matrix_L = np.round(matrix_L, 3)
          vector_X = np.round(vector_X, 3)

          if np.isnan(matrix_L.sum()) or np.isnan(vector_X.sum()):
            raise Exception("Um erro ocorreu ao calcular. Por favor forneça outras valores para Matriz A e vetor B.")

          st.latex(convert_matrix_to_latex(matrix_L, "Matriz L"))
          st.latex(convert_matrix_to_latex(vector_X, "Vetor X"))
        except Exception as e:
          st.error(e)

  elif choice == "Procedimento Iterativo Jacobi":
    from algorithms.jacobi import resolve_jacobi

    st.subheader("Implementação 1.3 - Procedimento Iterativo Jacobi")

    st.markdown("<p>Forneça os arquivos da <strong>Matriz A</strong> e <strong>Vetor B</strong>, em arquivos no formato <strong>txt</strong>. Separe as colunas utilizando um espaço, conforme os exemplos:</p>", unsafe_allow_html=True)

    st.markdown(download_txt("src/matrix_A_jacobi_sample.txt", label="Download exemplo de Matriz A"), unsafe_allow_html=True)

    st.markdown(download_txt("src/vector_B_jacobi_sample.txt", label="Download exemplo do Vetor B"), unsafe_allow_html=True)

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
          
          if not verificar_matriz_quadrada(matrix_A):
            raise Exception("Matriz A não é quadrada.")
          if not verifica_tamanho_vetor(matrix_A, vector_B):
            raise Exception("Vetor B não possui tamanho adequado.")

          vector_X, historico_erro, iteracoes = resolve_jacobi(matrix_A, vector_B)
          vector_X = np.round(vector_X, 3)

          if np.isnan(vector_X.sum()):
            raise Exception("Um erro ocorreu ao calcular. Por favor forneça outras valores para Matriz A e vetor B.")

          st.latex(convert_matrix_to_latex(vector_X, "Vetor X"))
          st.text(f"Número de iterações = {iteracoes}")

          historico_erro = np.array(historico_erro).reshape(-1, 1)
          uri_historico_erro = save_file_as_txt(historico_erro, path="temp")

          st.markdown(download_txt(uri_historico_erro, label="Download histórico de erro"), unsafe_allow_html=True)
        except Exception as e:
          st.error(e)

  elif choice == "Procedimento Iterativo Gauss-Seidel":
    from algorithms.gauss_seidel import resolve_gauss_seidel

    st.subheader("Implementação 1.4 - Procedimento Iterativo Gauss-Seidel")

    st.markdown("<p>Forneça os arquivos da <strong>Matriz A</strong> e <strong>Vetor B</strong>, em arquivos no formato <strong>txt</strong>. Separe as colunas utilizando um espaço, conforme os exemplos:</p>", unsafe_allow_html=True)

    st.markdown(download_txt("src/matrix_A_gauss_seidel_sample.txt", label="Download exemplo de Matriz A"), unsafe_allow_html=True)

    st.markdown(download_txt("src/vector_B_gauss_seidel_sample.txt", label="Download exemplo do Vetor B"), unsafe_allow_html=True)

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
          if not verificar_matriz_quadrada(matrix_A):
            raise Exception("Matriz A não é quadrada.")
          if not verifica_tamanho_vetor(matrix_A, vector_B):
            raise Exception("Vetor B não possui tamanho adequado.")

          vector_X, historico_erro, iteracoes = resolve_gauss_seidel(matrix_A, vector_B)
          vector_X = np.round(vector_X, 3)

          st.latex(convert_matrix_to_latex(vector_X, "Vetor X"))
          st.text(f"Número de iterações = {iteracoes}")

          if np.isnan(vector_X.sum()):
            raise Exception("Um erro ocorreu ao calcular. Por favor forneça outras valores para Matriz A e vetor B.")

          historico_erro = np.array(historico_erro).reshape(-1, 1)
          uri_historico_erro = save_file_as_txt(historico_erro, path="temp")

          st.markdown(download_txt(uri_historico_erro, label="Download histórico de erro"), unsafe_allow_html=True)
        except Exception as e:
          st.error(e)
  
  elif choice == "Método da Potência":
    from algorithms.potencia_eigen import power_method_eigen

    st.subheader("Implementação 2.1 - Método da Potência")

    st.markdown("<p>Forneça o arquivo da <strong>Matriz A</strong> no formato <strong>txt</strong>. Separe as colunas utilizando um espaço, conforme o exemplo:</p>", unsafe_allow_html=True)

    st.markdown(download_txt("src/matrix_A_power_sample.txt", label="Download exemplo de Matriz A"), unsafe_allow_html=True)

    st.markdown("<p>Faça o upload abaixo:</p>", unsafe_allow_html=True)

    matrix_A_input = st.file_uploader("Matriz A", type="txt")
    if matrix_A_input:
      matrix_A = read_matrix(matrix_A_input)
      st.latex(convert_matrix_to_latex(matrix_A, "Matriz A"))
    
    if (matrix_A_input):
      button = st.button("Calcular")
      if button:
        try:
          if not verificar_matriz_quadrada(matrix_A):
            raise Exception("Matriz A não é quadrada.")

          autovalor, autovetor, historico_erro, iteracoes = power_method_eigen(matrix_A)
          autovalor = np.round(autovalor, 3)
          autovetor = np.round(autovetor, 3)

          if np.isnan(autovetor.sum()):
            raise Exception("Um erro ocorreu ao calcular. Por favor forneça outras valores para Matriz A.")

          st.latex(f"λ = {autovalor}")
          st.latex(convert_matrix_to_latex(autovetor, "v"))

          st.text(f"Número de iterações = {iteracoes}")

          historico_erro = np.array(historico_erro).reshape(-1, 1)
          uri_historico_erro = save_file_as_txt(historico_erro, path="temp")

          st.markdown(download_txt(uri_historico_erro, label="Download histórico de erro"), unsafe_allow_html=True)

        except Exception as e:
          st.error(e)

  elif choice == "Método de Jacobi":
    from algorithms.jacobi_eigen import jacob_eigen

    st.subheader("Implementação 2.2 - Método de Jacobi")

    st.markdown("<p>Forneça o arquivo da <strong>Matriz A</strong> no formato <strong>txt</strong>. Separe as colunas utilizando um espaço, conforme o exemplo:</p>", unsafe_allow_html=True)

    st.markdown(download_txt("src/matrix_A_jacobi_eigen_sample.txt", label="Download exemplo de Matriz A"), unsafe_allow_html=True)

    st.markdown("<p>Faça o upload abaixo:</p>", unsafe_allow_html=True)

    matrix_A_input = st.file_uploader("Matriz A", type="txt")
    if matrix_A_input:
      matrix_A = read_matrix(matrix_A_input)
      st.latex(convert_matrix_to_latex(matrix_A, "Matriz A"))
    
    if (matrix_A_input):
      button = st.button("Calcular")
      if button:
        try:
          if not verificar_matriz_quadrada(matrix_A):
            raise Exception("Matriz A não é quadrada.")

          autovalores, autovetores, iteracoes = jacob_eigen(matrix_A)
          autovalores = np.round(autovalores, 3)
          autovetores = np.round(autovetores, 3)

          if np.isnan(autovetores.sum()):
            raise Exception("Um erro ocorreu ao calcular. Por favor forneça outras valores para Matriz A.")

          for i in range(len(autovalores)):
            st.latex(f"λ{i+1} = {autovalores[i]}")
            st.latex(convert_matrix_to_latex(autovetores[:, i].reshape(-1, 1), "v1"))
          st.text(f"Número de iterações = {iteracoes}")
        except Exception as e:
          st.error(e)
  
  elif choice == "Interpolação":
    from algorithms.interpolacao import interpolacao_lagrange

    st.subheader("Implementação 3.1 - Interpolação")

    st.markdown("<p>Forneça o arquivo dos pares de  <strong>x</strong> e <strong>y</strong>, nessa ordem, no formato <strong>txt</strong>. Separe <strong>x</strong> e <strong>y</strong> utilizando um espaço, e os pares por linhas, conforme o exemplo:</p>", unsafe_allow_html=True)

    st.markdown(download_txt("src/matrix_xy_interpolacao_sample.txt", label="Download exemplo de pares x e y"), unsafe_allow_html=True)

    st.markdown("<p>Faça o upload abaixo:</p>", unsafe_allow_html=True)

    matrix_xy_input = st.file_uploader("Pares x e y", type="txt")
    if matrix_xy_input:
      matrix_xy = read_matrix(matrix_xy_input)
      try:
        vector_x = matrix_xy[:, 0].reshape(-1, 1)
        vector_y = matrix_xy[:, 1].reshape(-1, 1)
        print(vector_x)
        print(vector_y)
        st.latex(convert_matrix_to_latex(vector_x, "Vector X"))
        st.latex(convert_matrix_to_latex(vector_y, "Vector Y"))
      except Exception as e:
        st.error("Arquivo fornecido não corresponde com as especificações mencionadas acima.")
    
    st.text("Insira o valor de x para calcular a interpolação:")
    x_input = st.text_input("Insira aqui um valor de x")

    if (matrix_xy_input and x_input):
      button = st.button("Calcular")
      if button:
        try:
          expr, lagrange = interpolacao_lagrange(vector_x, vector_y)
          st.latex(f"f(x) =")
          st.latex(expr)

          x_input = float(x_input)
          y = lagrange(x_input)
          y = np.round(y, 3)
          st.latex(f"y = {y}")
        except Exception as e:
          st.error(e)
  
  elif choice == "Regressão":
    from algorithms.regressao import regressao_multilinear

    st.subheader("Implementação 3.2 - Regressão")

    st.markdown("<p>Forneça o arquivo dos pares de  <strong>x</strong> e <strong>y</strong>, nessa ordem, no formato <strong>txt</strong>. Separe <strong>x</strong> e <strong>y</strong> utilizando um espaço, e os pares por linhas, conforme o exemplo:</p>", unsafe_allow_html=True)

    st.markdown(download_txt("src/matrix_xy_regressao_sample.txt", label="Download exemplo de pares x e y"), unsafe_allow_html=True)

    st.markdown("<p>Faça o upload abaixo:</p>", unsafe_allow_html=True)

    matrix_xy_input = st.file_uploader("Pares x e y", type="txt")
    if matrix_xy_input:
      matrix_xy = read_matrix(matrix_xy_input)
      try:
        vector_x = matrix_xy[:, 0].reshape(-1, 1)
        vector_y = matrix_xy[:, 1].reshape(-1, 1)
        print(vector_x)
        print(vector_y)
        st.latex(convert_matrix_to_latex(vector_x, "Vector X"))
        st.latex(convert_matrix_to_latex(vector_y, "Vector Y"))
      except Exception as e:
        st.error("Arquivo fornecido não corresponde com as especificações mencionadas acima.")
    
    st.text("Insira o grau da regressão (padrão = 1):")
    grau_input = st.text_input("Insira aqui o grau", value="1")

    st.text("Insira o valor de x para calcular a interpolação:")
    x_input = st.text_input("Insira aqui um valor de x")

    if (matrix_xy_input and x_input and grau_input):
      button = st.button("Calcular")
      if button:
        try:
          grau = int(grau_input)
          expr, regressao = regressao_multilinear(vector_x, vector_y, grau=grau)
          st.latex(f"f(x) =")
          st.latex(expr)

          x_input = float(x_input)
          y = regressao(x_input)
          y = np.round(y, 3)
          st.latex(f"y = {y}")
        except Exception as e:
          st.error(e)

  elif choice == "Determinante":
    st.subheader("Implementação Extra - Determinante")
    st.markdown("<p>Forneça o arquivo da <strong>Matriz A</strong> no formato <strong>txt</strong>. Separe as colunas utilizando um espaço, conforme o exemplo:</p>", unsafe_allow_html=True)

    st.markdown(download_txt("src/matrix_A_power_sample.txt", label="Download exemplo de Matriz A"), unsafe_allow_html=True)

    st.markdown("<p>Faça o upload abaixo:</p>", unsafe_allow_html=True)

    matrix_A_input = st.file_uploader("Matriz A", type="txt")
    if matrix_A_input:
      matrix_A = read_matrix(matrix_A_input)
      st.latex(convert_matrix_to_latex(matrix_A, "Matriz A"))
    
    if (matrix_A_input):
      button = st.button("Calcular")
      if button:
        try:
          if not verificar_matriz_quadrada(matrix_A):
            raise Exception("Matriz A não é quadrada.")

          det = np.linalg.det(matrix_A)
          det = np.round(det, 3)

          st.text(f"Det(A) = {det}")

        except Exception as e:
          st.error("Não foi possível calcular a determinante.")

  st.text("")
  st.text("")
  st.text("")
  st.text("")
  st.text("Criado por Henrique Chaves - 2021.1")

if __name__ == "__main__":
  main()

