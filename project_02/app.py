import streamlit as st
import numpy as np
import pandas as pd

def main():
  st.title("COC473 - Segundo trabalho prático")
  menu = ["1.1 - Método de Newton",
          "1.2 - Método de Broyden",
          "2.1.1 - Método da Bisseção",
          "2.1.2 - Método de Newton",
          "2.2.1 - Quadratura de Gauss",
          "2.2.2 - Quadratura Polinomial",
          "2.3.1 - Derivada Central",
          "2.3.2 - Derivada Passo a frente",
          "2.3.3 - Derivada Passo atrás",
          "2.4 - Derivada Extrapolação de Richard",
          "3 - Rugen-Kutta-Nystrom"]

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
          (c2, c3, c4), k = run_newton(max_iter, max_tol, X0, theta_dict)
          st.latex(f"c2 = {c2}")
          st.latex(f"c3 = {c3}")
          st.latex(f"c4 = {c4}")
          st.text(f"Número de iterações necessárias: {k}")



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
          (c2, c3, c4), k = run_broyden(max_iter, max_tol, X0, theta_dict)
          st.latex(f"c2 = {c2}")
          st.latex(f"c3 = {c3}")
          st.latex(f"c4 = {c4}")
          st.text(f"Número de iterações necessárias: {k}")


      except TypeError as e:
        st.error("Não foi possível calcular. Verifique os valores de entrada e tente novamente.")
      
      except Exception as e:
        st.error("Não convergiu!")



######################################## METODO DA BISSEÇÃO ################################
  if choice == "2.1.1 - Método da Bisseção":
    st.subheader("Implementação 2.1.1 - Método da Bisseção - Encontrar uma raiz no intervalo")
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

    if (a_input and b_input and max_tol and max_iter):
      try:
        c1_input = float(c1_input)
        c2_input = float(c2_input)
        c3_input = float(c3_input)
        c4_input = float(c4_input)
        a_input = float(a_input)
        b_input = float(b_input)
        max_tol = float(max_tol)
        max_iter = int(max_iter)
        button = st.button("Calcular")

        if button:
          constants = [c1_input, c2_input, c3_input, c4_input]
          x_root, k = run_bisseccao(constants, a_input, b_input, max_tol, max_iter)
          st.latex(f"Raiz = {x_root}")
          st.text(f"Número de iterações necessárias: {k}")

      except TypeError as e:
        st.error("Não foi possível calcular. Verifique os valores de entrada e tente novamente.")
      
      except Exception as e:
        st.error("Não convergiu!")
      
##########################################
######################################## METODO De  Newton ################################
  if choice == "2.1.2 - Método de Newton":
    st.subheader("Implementação 2.1.2 - Método de Newton - Encontrar uma raiz a partir de um x0")
    from algorithms.newton_root import run_newton_root

    st.text("Função f(x) dada por:")
    st.latex(r'''
      c_{1}\exp(c_{2}x) + c_{3}x^{c_{4}}
    ''')
    st.text("\n\n")
    st.text("Insira os valores das costantes.")
    c1_input = st.text_input("Insira o valor de c1", value=1, key="c1_value")
    c2_input = st.text_input("Insira o valor de c2", value=1, key="c2_value")
    c3_input = st.text_input("Insira o valor de c3", value=1, key="c3_value")
    c4_input = st.text_input("Insira o valor de c4", value=1, key="c4_value")

    x_0_input = st.text_input("Insira o valor de x0", value=1, key="x_0_value")
    max_iter = st.text_input("Insira o número máximo de iterações", value=100, key="max_iter")
    max_tol = st.text_input("Insira o valor de tolerância máxima", value=5e-4, key="max_tol")

    if (x_0_input and max_tol and max_iter):
      try:
        c1_input = float(c1_input)
        c2_input = float(c2_input)
        c3_input = float(c3_input)
        c4_input = float(c4_input)
        max_iter = int(max_iter)
        x_0_input = float(x_0_input)
        max_tol = float(max_tol)
        button = st.button("Calcular")

        if button:
          constants = [c1_input, c2_input, c3_input, c4_input]
          x_root, k = run_newton_root(constants, x_0_input, max_tol, max_iter)
          st.latex(f"Raiz = {x_root}")
          st.text(f"Número de iterações necessárias: {k}")


      except TypeError as e:
        st.error("Não foi possível calcular. Verifique os valores de entrada e tente novamente.")
      
      except Exception as e:
        st.error("Não convergiu!")
      
#############################QUADRATURA DE GAUSS############
  if choice == "2.2.1 - Quadratura de Gauss":
    st.subheader("Implementação 2.2.1 - Quadratura de Gauss - Calcula o valor da integral em um intervalo definido")
    from algorithms.gauss_quadrature import run_gauss_quadrature

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
    b_input = st.text_input("Insira o valor para b", value=1, key="b_interval")
    n_points = st.text_input("Insira o número de pontos (entre 2 e 10)", value=5, key="n_points_value")


    if (a_input and b_input and n_points):
      try:
        c1_input = float(c1_input)
        c2_input = float(c2_input)
        c3_input = float(c3_input)
        c4_input = float(c4_input)
        a_input = float(a_input)
        b_input = float(b_input)
        n_points = int(n_points)
        button = st.button("Calcular")

        if button:
          constants = [c1_input, c2_input, c3_input, c4_input]
          area = run_gauss_quadrature(constants, a_input, b_input, n_points)
          st.latex(f"Area = {area}")

      except TypeError as e:
        st.error("Não foi possível calcular. Verifique os valores de entrada e tente novamente.")
      
      except Exception as e:
        st.error("Não convergiu!")
############################ QUADRATURA POLINOMIAL ###########
  if choice == "2.2.2 - Quadratura Polinomial":
    st.subheader("Implementação 2.2.2 - Quadratura Polinomial - Calcula o valor da integral em um intervalo definido")
    from algorithms.polinomial_quadrature import run_polinomial_quadrature

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
    b_input = st.text_input("Insira o valor para b", value=1, key="b_interval")
    n_points = st.text_input("Insira o número de pontos (entre 2 e 10)", value=5, key="n_points_value")


    if (a_input and b_input and n_points):
      try:
        c1_input = float(c1_input)
        c2_input = float(c2_input)
        c3_input = float(c3_input)
        c4_input = float(c4_input)
        a_input = float(a_input)
        b_input = float(b_input)
        n_points = int(n_points)
        button = st.button("Calcular")

        if button:
          constants = [c1_input, c2_input, c3_input, c4_input]
          area = run_polinomial_quadrature(constants, a_input, b_input, n_points)
          st.latex(f"Area = {area}")

      except TypeError as e:
        st.error("Não foi possível calcular. Verifique os valores de entrada e tente novamente.")
      
      except Exception as e:
        st.error("Não convergiu!")
################ DERIVADA CENTRAL ################
  if choice == "2.3.1 - Derivada Central":
    st.subheader("Implementação 2.3.1 - Derivada Central - Calcula a derivada a partir de um ponto a e um delta x")
    from algorithms.derivatives import deriv_central

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

    a_input = st.text_input("Insira o valor de a", value=2, key="a_value")
    delta_x = st.text_input("Insira o valor de delta x", value=0.02, key="delta_x_value")

    if (a_input and delta_x):
      try:
        c1_input = float(c1_input)
        c2_input = float(c2_input)
        c3_input = float(c3_input)
        c4_input = float(c4_input)
        a_input = float(a_input)
        delta_x = float(delta_x)

        button = st.button("Calcular")

        if button:
          constants = [c1_input, c2_input, c3_input, c4_input]
          deriv_result = deriv_central(constants, a_input, delta_x)
          st.latex(f"Derivada = {deriv_result}")

      except TypeError as e:
        st.error("Não foi possível calcular. Verifique os valores de entrada e tente novamente.")
      
      except Exception as e:
        st.error("Um erro aconteceu!")

################# DERIVADA PASSO A FRENTE #########
  if choice == "2.3.2 - Derivada Passo a frente":
    st.subheader("Implementação 2.3.2 - Derivada Passo a frente - Calcula a derivada a partir de um ponto a e um delta x")
    from algorithms.derivatives import deriv_frente

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

    a_input = st.text_input("Insira o valor de a", value=2, key="a_value")
    delta_x = st.text_input("Insira o valor de delta x", value=0.02, key="delta_x_value")

    if (a_input and delta_x):
      try:
        c1_input = float(c1_input)
        c2_input = float(c2_input)
        c3_input = float(c3_input)
        c4_input = float(c4_input)
        a_input = float(a_input)
        delta_x = float(delta_x)

        button = st.button("Calcular")

        if button:
          constants = [c1_input, c2_input, c3_input, c4_input]
          deriv_result = deriv_frente(constants, a_input, delta_x)
          st.latex(f"Derivada = {deriv_result}")

      except TypeError as e:
        st.error("Não foi possível calcular. Verifique os valores de entrada e tente novamente.")
      
      except Exception as e:
        st.error("Um erro aconteceu!")
################# DERIVADA PASSO ATRÁS ########################

  if choice == "2.3.3 - Derivada Passo atrás":
    st.subheader("Implementação 2.3.3 - Derivada Passo atrás - Calcula a derivada a partir de um ponto a e um delta x")
    from algorithms.derivatives import deriv_tras

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

    a_input = st.text_input("Insira o valor de a", value=2, key="a_value")
    delta_x = st.text_input("Insira o valor de delta x", value=0.02, key="delta_x_value")

    if (a_input and delta_x):
      try:
        c1_input = float(c1_input)
        c2_input = float(c2_input)
        c3_input = float(c3_input)
        c4_input = float(c4_input)
        a_input = float(a_input)
        delta_x = float(delta_x)

        button = st.button("Calcular")

        if button:
          constants = [c1_input, c2_input, c3_input, c4_input]
          deriv_result = deriv_tras(constants, a_input, delta_x)
          st.latex(f"Derivada = {deriv_result}")

      except TypeError as e:
        st.error("Não foi possível calcular. Verifique os valores de entrada e tente novamente.")
      
      except Exception as e:
        st.error("Um erro aconteceu!")
########################### DERIVADA DE RICHARD #############################
  if choice == "2.4 - Derivada Extrapolação de Richard":
    st.subheader("Implementação 2.4 - Derivada Extrapolação de Richard - Calcula a derivada a partir de um valor inicial a e dois delta x")
    from algorithms.derivatives import deriv_richard

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

    a_input = st.text_input("Insira o valor de a", value=2, key="a_value")
    delta_x_1 = st.text_input("Insira o valor do primeiro delta x", value=0.5, key="delta_x_1_value")
    delta_x_2 = st.text_input("Insira o valor do segundo delta x", value=0.25, key="delta_x_2_value")


    if (a_input and delta_x_1 and delta_x_2):
      try:
        c1_input = float(c1_input)
        c2_input = float(c2_input)
        c3_input = float(c3_input)
        c4_input = float(c4_input)
        a_input = float(a_input)
        delta_x_1 = float(delta_x_1)
        delta_x_2 = float(delta_x_2)


        button = st.button("Calcular")

        if button:
          constants = [c1_input, c2_input, c3_input, c4_input]
          deriv_result = deriv_richard(constants, a_input, delta_x_1, delta_x_2)
          st.latex(f"Derivada = {deriv_result}")

      except TypeError as e:
        st.error("Não foi possível calcular. Verifique os valores de entrada e tente novamente.")
      
      except Exception as e:
        st.error(e)
        st.error("Um erro aconteceu!")
############################### RUGEN KUTTA NYSTROM

  if choice == "3 - Rugen-Kutta-Nystrom":
    st.subheader("Implementação 3 - Rugen-Kutta-Nystrom - Cálculo de EDO de segunda ordem")
    from algorithms.rugen_kutta_nystrom import run_runge_kutta_nystrom

    st.text("EDO y''(t) dada por:")
    st.latex(r'''
      \frac{a_{1}\sin(w_{1}t) + a_{2}\sin(w_{2}t) + a_{3}\sin(w_{3}t) - cy' - ky}{m}
    ''')
    st.text("\n\n")
    st.text("Insira os valores das costantes.")
    a1_input = st.text_input("Insira o valor de a1", value=2, key="a1_value")
    a2_input = st.text_input("Insira o valor de a2", value=2.1, key="a2_value")
    a3_input = st.text_input("Insira o valor de a3", value=1.35, key="a3_value")
    w1_input = st.text_input("Insira o valor de w1", value=0.05, key="w1_value")
    w2_input = st.text_input("Insira o valor de w2", value=1, key="w2_value")
    w3_input = st.text_input("Insira o valor de w3", value=2.1, key="w3_value")
    m_input = st.text_input("Insira o valor de m", value=1, key="m_value")
    c_input = st.text_input("Insira o valor de c", value=0.1, key="c_value")
    k_input = st.text_input("Insira o valor de k", value=3, key="k_value")
    delta = st.text_input("Insira o valor do passo", value=0.5, key="delta_value")
    t_maximum = st.text_input("Insira o valor máximo de t", value=360, key="t_maximum_value")

    if (a1_input and a2_input and a3_input and w1_input and w2_input and w3_input and m_input and c_input and k_input and delta and t_maximum):
      try:
        a1_input = float(a1_input)
        a2_input = float(a2_input)
        a3_input = float(a3_input)
        w1_input = float(w1_input)
        w2_input = float(w2_input)
        w3_input = float(w3_input)
        m_input = float(m_input)
        c_input = float(c_input)
        k_input = float(k_input)
        delta = float(delta)
        t_maximum = float(t_maximum)
        button = st.button("Calcular")

        if button:
          c_dict = {
            "a1": a1_input,
            "a2": a2_input,
            "a3": a3_input,
            "w1": w1_input,
            "w2": w2_input,
            "w3": w3_input,
            "m": m_input,
            "c": c_input,
            "k": k_input
          }

          df = run_runge_kutta_nystrom(delta, t_maximum, c_dict).astype(float)
          st.write(df)
          csv = df.to_csv().encode("utf-8")
          st.download_button("Download da tabela", csv, "runge_kutta_nystrom.csv", mime="text/csv")

          # st.text(df)
          # st.table(df)
          # st.latex(f"Derivada = {deriv_result}")

      except TypeError as e:
        st.error("Não foi possível calcular. Verifique os valores de entrada e tente novamente.")
      
      except Exception as e:
        print(e)
        st.error(e)
        st.error("Um erro aconteceu!")
##################################################################
  st.text("")
  st.text("")
  st.text("")
  st.text("")
  st.text("Criado por Henrique Chaves - 2021.1")

if __name__ == "__main__":
  main()