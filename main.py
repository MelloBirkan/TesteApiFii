import pandas as pd
import urllib.request
import json

# Lista de FIIs fornecida pelo investidor
fiis = ["alzr", "bcri", "brcr", "cpff", "cpts", "deva", "habt", "hctr", "hsml", "irdm", "knri", "mgff", "rbff", "rbrf", "recr", "rect", "urpr", "vghf", "vgip", "vslh", "xpci", "xplg", "xpml", "xppr"]

# Cria um DataFrame vazio
df = pd.DataFrame(columns=["Nome do Fundo", "Dividend Yield anual", "Valor atual da Cota", "Valor patrimonial por cota", "Valor do rendimento", "Status"])

# Processa cada FII da lista
for fii in fiis:
    # Solicita informações do FII
    url = f"http://dwebkit-api.tk/api/{fii}"
    response = urllib.request.urlopen(url)
    data = json.load(response)

    # Processa informações do FII
    nome = data.get("nomePregao")
    if nome is None:
        print(f"Erro ao processar FII {fii}: nomePregao não encontrado na resposta da API")
        continue
    dy = data.get("dividendYield")
    cota = data.get("valorAtual")
    patrimonio = data.get("valorPatrimonioPCota")
    rendimento = data["proximoRendimento"].get("rendimento") or data["ultimoRendimento"].get("rendimento")
    status = "COMPRAR" if cota < patrimonio else "AGUARDAR"

    # Adiciona informações do FII ao DataFrame
    row = {"Nome do Fundo": nome_fundo, "Dividend Yield": dy_anual, "Valor da Cota": valor_cota, "Valor Patrimonial por Cota": vp_cota, "Valor do Rendimento": rendimento, "Status": status}
df_row = pd.DataFrame(row, index=[0])
df = pd.concat([df, df_row], ignore_index=True)



# Grava DataFrame no arquivo CSV
df.to_csv("informacoes_fiis.csv", index=False)