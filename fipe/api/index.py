import requests
import pandas as pd

def handler(request):
    query = request.get("query", {})

    vehicleType = query.get("type")
    brandId = query.get("brand")
    modelId = query.get("model")
    yearId = query.get("year")

    if not vehicleType:
        return {
            "statusCode": 200,
            "body": "Informe ?type=cars|motorcycles|trucks"
        }

    # 1) Lista marcas
    if vehicleType and not brandId:
        url = f"https://fipe.parallelum.com.br/api/v2/{vehicleType}/brands/"
        data = requests.get(url).json()
        return {
            "statusCode": 200,
            "body": data
        }

    # 2) Lista modelos
    if brandId and not modelId:
        url = f"https://fipe.parallelum.com.br/api/v2/{vehicleType}/brands/{brandId}/models/"
        data = requests.get(url).json()
        return {
            "statusCode": 200,
            "body": data
        }

    # 3) Lista anos
    if modelId and not yearId:
        url = f"https://fipe.parallelum.com.br/api/v2/{vehicleType}/brands/{brandId}/models/{modelId}/years"
        data = requests.get(url).json()
        return {
            "statusCode": 200,
            "body": data
        }

    # 4) Retorna FIPE final
    if yearId:
        url = f"https://fipe.parallelum.com.br/api/v2/{vehicleType}/brands/{brandId}/models/{modelId}/years/{yearId}"
        data = requests.get(url).json()
        return {
            "statusCode": 200,
            "body": data
        }

    return {
        "statusCode": 400,
        "body": "Parâmetros inválidos"
    }
