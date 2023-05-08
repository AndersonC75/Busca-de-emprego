import requests
from bs4 import BeautifulSoup

def buscar_empregos(palavra_chave, localizacao):
    url_base = "https://www.apinfo.com/apinfo/"
    parametros = {
        "q": palavra_chave,
        "l": localizacao,
    }
    resposta = requests.get(url_base, params=parametros)

    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, "html.parser")
        resultados = soup.find_all("div", class_="jobsearch-SerpJobCard")

        with open("resultados.txt", "w", encoding="utf-8") as arquivo:
            for resultado in resultados:
                titulo = resultado.find("a", class_="jobtitle").text.strip()
                empresa = resultado.find("span", class_="company").text.strip()
                local = resultado.find("span", class_="location").text.strip()

                print(f"Vaga: {titulo}")
                print(f"Empresa: {empresa}")
                print(f"Local: {local}")
                print("-" * 80)

                arquivo.write(f"Vaga: {titulo}\n")
                arquivo.write(f"Empresa: {empresa}\n")
                arquivo.write(f"Local: {local}\n")
                arquivo.write("-" * 80 + "\n")
    else:
        print("Não foi possível obter os resultados. Tente novamente mais tarde.")

if __name__ == "__main__":
    palavra_chave = "analista de suporte pleno"
    localizacao = "São Paulo, SP - Zona Leste"
    buscar_empregos(palavra_chave, localizacao)
