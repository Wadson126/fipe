import os
import requests
import json

# ======================================================
# CONFIGURAÇÃO
# ======================================================

API_KEY = os.getenv("PORTAL_TRANSPARENCIA_API_KEY")

if not API_KEY:
    raise RuntimeError("Variável de ambiente PORTAL_TRANSPARENCIA_API_KEY não encontrada")

URL = "https://api.portaldatransparencia.gov.br/api-de-dados/servidores/funcoes-e-cargos"

HEADERS = {
    "chave-api-dados": API_KEY,
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0"
}

# ======================================================
# REQUISIÇÃO COM PAGINAÇÃO
# ======================================================

pagina = 1
todos_os_registros = []

while True:
    params = {"pagina": pagina}

    response = requests.get(
    URL,
    headers=HEADERS,
    params=params,
    timeout=15
)
    response.raise_for_status()  # erro HTTP real

    dados = response.json()

    # -------------------------------
    # TRATAMENTO DE ERRO DA API
    # -------------------------------
    if isinstance(dados, dict) and "Erro na API" in dados:
        raise RuntimeError(f"Erro retornado pela API: {dados['Erro na API']}")

    # -------------------------------
    # VALIDAÇÃO DE TIPO
    # -------------------------------
    if not isinstance(dados, list):
        raise RuntimeError(f"Formato inesperado da resposta: {type(dados)}")

    if not dados:
        break  # fim da paginação

    todos_os_registros.extend(dados)
    pagina += 1

# ======================================================
# RESULTADO
# ======================================================

print(f"Total de registros extraídos: {len(todos_os_registros)}")

# mostra um exemplo
print(json.dumps(todos_os_registros[0], indent=2, ensure_ascii=False))
