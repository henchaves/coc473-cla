import pandas as pd
import base64
from datetime import datetime
import numpy as np
import os

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

def save_file_as_txt(np_array, path, label=None):
  if not label:
    time_now = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
    label = f"{time_now}.txt"
    
  label = os.path.join(path, label)
  pd.DataFrame(np_array).to_csv(label, index=False, header=False)
  return label