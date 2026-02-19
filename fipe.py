import streamlit as st
import requests 
import pandas as pd

@st.cache_data(ttl=86400)
def get_marcas(vehicleType):
    return requests.get(
        f"https://fipe.parallelum.com.br/api/v2/{vehicleType}/brands/"
    ).json()

@st.cache_data
def get_modelos(vehicleType, brandId):
    return requests.get(
        f"https://fipe.parallelum.com.br/api/v2/{vehicleType}/brands/{brandId}/models/"
    ).json()

@st.cache_data
def get_anos(vehicleType, brandId, modelId):
    return requests.get(
        f"https://fipe.parallelum.com.br/api/v2/{vehicleType}/brands/{brandId}/models/{modelId}/years"
    ).json()

@st.cache_data
def get_fipe(vehicleType, brandId, modelId, yearId):
    return requests.get(
        f"https://fipe.parallelum.com.br/api/v2/{vehicleType}/brands/{brandId}/models/{modelId}/years/{yearId}"
    ).json()

def formatar_ano(x):
    if x is None:
        return "Selecione..."
    
    nome = x["name"]

    if nome.startswith("32000"):
        return nome.replace("32000", "0 km")
    
    return nome

st.write("Selecione o tipo de veiculo: ")
tipos = [None, "cars", "motorcycles", "trucks"]
labels = {
    "cars": "Carros",
    "motorcycles": "Motocicletas",
    "trucks": "Caminhões"
}
with st.container(border=True):
    vehicleType = st.selectbox(
       "Tipos", 
       tipos, 
       format_func=lambda x: "Selecione..." if x is None else labels[x])

if vehicleType is not None:
   
  st.write("Selecione a marca do veículo:")

  marcas = get_marcas(vehicleType)
  with st.container(border=True):
    marca_selecionada = st.selectbox(
        "Marcas",
        [None] + marcas,
        format_func=lambda x: "Selecione..." if x is None else x["name"]
    )
  if marca_selecionada is not None:
    codigo_marca = marca_selecionada["code"]
    brandId = codigo_marca    

  

    st.write("Selecione o Modelo do veiculo: ")
    
    modelos = get_modelos(vehicleType, brandId)

    with st.container(border=True):
      modelo_selecionado = st.selectbox(
          "Modelos",
          [None] + modelos,
          format_func=lambda x: "Selecione..." if x is None else x["name"]
      )
    if modelo_selecionado is not None:
      modelId = modelo_selecionado["code"]
  
    

      st.write("Selecione o ano do veiculo: ")

      Ano = get_anos(vehicleType, brandId, modelId)

      with st.container(border=True):
        ano_selecionado = st.selectbox(
            "Ano",
            [None] + Ano,
            format_func=formatar_ano
        )
      if ano_selecionado is not None:
        yearId = ano_selecionado["code"]

      
        st.write("Fipe selecionada:")
        if modelo_selecionado:
            dados = get_fipe(vehicleType, brandId, modelId, yearId)
            df = pd.DataFrame([dados])
            df = df.rename(columns = {'price':'Preço',
                                      'brand':'Marca', 
                                      'model':'Modelo', 
                                      'modelYear':'Ano',
                                      'fuel': 'Combustível',
                                      'codeFipe': 'Codigo Fipe',
                                      'referenceMonth': 'Mês de Referência'
                                      })
            df = df.drop(columns = {'vehicleType', 'fuelAcronym'})
            st.dataframe(df, use_container_width=True, hide_index=True)







