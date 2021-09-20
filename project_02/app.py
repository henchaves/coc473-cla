import streamlit as st
import numpy as np

from utils import (download_txt, 
                   convert_matrix_to_latex, 
                   read_matrix, 
                   save_file_as_txt)

# from algorithms.general import (verificar_matriz_quadrada, verifica_tamanho_vetor)

def main():
  st.title("COC473 - Segundo trabalho prático")
  menu = ["1.1 - Método de Newton",
          "1.2 - Método de Broyden",
          "2.1.1 - Método da Bisseção",
          "2.1.2 - Método de Newton"]
  choice = st.sidebar.selectbox("Implementações", menu)

  ################# NEWTON NL ######################
  if choice == "1.1 - Método de Newton":
    from algorithms.newton_nl import run_newton

    st.subheader("Implementação 1.1 - Método de Newton - Resolução de equação não linear")

    st.text("Sistema de Equações Não Lineares:")
    st.latex(r'''
      2c_{3}^2 + c_{2}^2 + 6c_{4}^2 = 1
    ''')

    st.latex(r'''
      8c_{3}^3 + 6c_{3}c_{2}^2 + 36c_{3}c_{2}c_{4} + 108c_{3}c_{4}^2 = \theta_{1}
    ''')

    st.latex(r'''
      60c_{3}^4 + 60c_{3}^{2}c_{2}^{2} + 576c_{3}^{2}c_{2}c_{4} + 2232c_{3}^{2}c_{4}^2 + 252c_{4}^{2}c_{2}^{2} + 1296c_{4}^{3}c_{2} + 3348c_{4}^4 + 24c_{2}^{3}c_{4} + 3c_{2} = \theta_{2}
    ''')
    st.text("\n\n")

    θ1_input = st.text_input("Insira um valor para θ1", value=0.75, key="nl_theta_1")
    θ2_input = st.text_input("Insira um valor para θ2", value=6.5, key="nl_theta_2")
    max_iter = st.text_input("Insira o número máximo de iterações", value=100, key="max_iter")
    max_tol = st.text_input("Insira o valor de tolerância máxima", value=1e-5, key="max_tol")

    if (θ1_input and θ2_input and max_iter and max_tol):
      try:
        θ1_input = float(θ1_input)
        θ2_input = float(θ2_input)
        max_iter = int(max_iter)
        max_tol = float(max_tol)
        button = st.button("Calcular")

        if button:
          X0 = np.array([[1], [0], [4]])
          theta_dict = {"θ1": θ1_input, "θ2": θ2_input}
          c2, c3, c4 = run_newton(max_iter, max_tol, X0, theta_dict)
          st.latex(f"c2 = {c2}")
          st.latex(f"c3 = {c3}")
          st.latex(f"c4 = {c4}")



      except TypeError as e:
        st.error("Não foi possível calcular. Verifique os valores de entrada e tente novamente.")
      
      except Exception as e:
        st.error("Não convergiu!")
      

  

  ################### BROYDEN NL ###########################
  if choice == "1.2 - Método de Broyden":
    st.subheader("Implementação 1.2 - Método de Broyden - Resolução de equação não linear")
    from algorithms.broyden_nl import run_broyden

    st.text("Sistema de Equações Não Lineares:")
    st.latex(r'''
      2c_{3}^2 + c_{2}^2 + 6c_{4}^2 = 1
    ''')

    st.latex(r'''
      8c_{3}^3 + 6c_{3}c_{2}^2 + 36c_{3}c_{2}c_{4} + 108c_{3}c_{4}^2 = \theta_{1}
    ''')

    st.latex(r'''
      60c_{3}^4 + 60c_{3}^{2}c_{2}^{2} + 576c_{3}^{2}c_{2}c_{4} + 2232c_{3}^{2}c_{4}^2 + 252c_{4}^{2}c_{2}^{2} + 1296c_{4}^{3}c_{2} + 3348c_{4}^4 + 24c_{2}^{3}c_{4} + 3c_{2} = \theta_{2}
    ''')
    st.text("\n\n")

    θ1_input = st.text_input("Insira um valor para θ1", value=0, key="nl_theta_1")
    θ2_input = st.text_input("Insira um valor para θ2", value=3, key="nl_theta_2")
    max_iter = st.text_input("Insira o número máximo de iterações", value=100, key="max_iter")
    max_tol = st.text_input("Insira o valor de tolerância máxima", value=1e-5, key="max_tol")

    if (θ1_input and θ2_input and max_iter and max_tol):
      try:
        θ1_input = float(θ1_input)
        θ2_input = float(θ2_input)
        max_iter = int(max_iter)
        max_tol = float(max_tol)
        button = st.button("Calcular")

        if button:
          X0 = np.array([[1], [0], [-0.2]])
          theta_dict = {"θ1": θ1_input, "θ2": θ2_input}
          c2, c3, c4 = run_broyden(max_iter, max_tol, X0, theta_dict)
          st.latex(f"c2 = {c2}")
          st.latex(f"c3 = {c3}")
          st.latex(f"c4 = {c4}")

      except TypeError as e:
        st.error("Não foi possível calcular. Verifique os valores de entrada e tente novamente.")
      
      except Exception as e:
        st.error("Não convergiu!")



######################################## METODO DA BISSEÇÃO ################################
  if choice == "2.1.1 - Método da Bisseção":
    st.subheader("Implementação 2.1.1 - Método da Bissação - Encontrar uma raiz no intervalo")
    from algorithms.bissection_root import run_bisseccao

    st.text("Função f(x) dada por:")
    st.latex(r'''
      c_{1}\exp(c_{2}x) + c_{3}x^{c_{4}}
    ''')
    st.text("\n\n")
    st.text("Insira os valores das costantes.")
    c1_input = st.text_input("Insira o valor de c1", value=1, key="c1_value")
    c2_input = st.text_input("Insira o valor de c2", value=1, key="c2_value")
    c3_input = st.text_input("Insira o valor de c3", value=1, key="c3_value")
    c4_input = st.text_input("Insira o valor de c4", value=0, key="c4_value")

    st.text("Insira os valores de a e b para definir o intervalo.")
    a_input = st.text_input("Insira o valor de a", value=0, key="a_interval")
    b_input = st.text_input("Insira o valor para b", value=10, key="b_interval")
    max_iter = st.text_input("Insira o número máximo de iterações", value=100, key="max_iter")
    max_tol = st.text_input("Insira o valor de tolerância máxima", value=1e-5, key="max_tol")

    if (a_input and b_input and max_tol):
      try:
        c1_input = float(c1_input)
        c2_input = float(c2_input)
        c3_input = float(c3_input)
        c4_input = float(c4_input)
        a_input = float(a_input)
        b_input = float(b_input)
        max_tol = float(max_tol)
        button = st.button("Calcular")

        if button:
          constants = [c1_input, c2_input, c3_input, c4_input]
          x_root = run_bisseccao(constants, a_input, b_input, max_tol, max_iter)
          st.latex(f"Raiz = {x_root}")

      except TypeError as e:
        st.error("Não foi possível calcular. Verifique os valores de entrada e tente novamente.")
      
      except Exception as e:
        st.error("Não convergiu!")
      
##########################################

########################################################
  st.text("")
  st.text("")
  st.text("")
  st.text("")
  st.text("Criado por Henrique Chaves - 2021.1")

if __name__ == "__main__":
  main()