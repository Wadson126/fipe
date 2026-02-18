# streamlit run d:/Projetos/ESTUDOS_PYTHON/fipe.py

import streamlit as st
import requests 
import pandas as pd


st.write("Selecione o tipo de veiculo: ")
tipos = [None, "cars", "motorcycles", "trucks"]
with st.container(border=True):
    vehicleType = st.selectbox(
       "Tipos", 
       tipos, 
       format_func=lambda x: "Selecione..." if x is None else x)

if vehicleType is not None:
   
  st.write("Selecione a marca do veículo:")

  response = requests.get(f"https://fipe.parallelum.com.br/api/v2/{vehicleType}/brands/")
  marcas = response.json()
  with st.container(border=True):
    marca_selecionada = st.selectbox(
        "Marcas",
        [None] + marcas,
        format_func=lambda x: "Selecione..." if x is None else x["name"]
    )
  if marca_selecionada is not None:
    codigo_marca = marca_selecionada["code"]
    # st.write("Código da marca:", codigo_marca)
    brandId = codigo_marca    

  

    st.write("Selecione o Modelo do veiculo: ")
    response = requests.get(f"https://fipe.parallelum.com.br/api/v2/{vehicleType}/brands/{brandId}/models/")
    modelos = response.json()

    with st.container(border=True):
      modelo_selecionado = st.selectbox(
          "Modelos",
          [None] + modelos,
          format_func=lambda x: "Selecione..." if x is None else x["name"]
      )
    if modelo_selecionado is not None:
      modelId = modelo_selecionado["code"]
    # st.write("Código do modelo:", modelId)
    

      st.write("Selecione o ano do veiculo: ")
      response = requests.get(f"https://fipe.parallelum.com.br/api/v2/{vehicleType}/brands/{brandId}/models/{modelId}/years")
      Ano = response.json()

      with st.container(border=True):
        ano_selecionado = st.selectbox(
            "Ano",
            [None] + Ano,
            format_func=lambda x: "Selecione..." if x is None else x["name"]
        )
      if ano_selecionado is not None:
        yearId = ano_selecionado["code"]

      
        st.write("Fipe selecionada:")
        if modelo_selecionado:
            response = requests.get(f"https://fipe.parallelum.com.br/api/v2/{vehicleType}/brands/{brandId}/models/{modelId}/years/{yearId}")
            dados = response.json()
            df = pd.DataFrame([dados])
            st.dataframe(df, use_container_width=True)







