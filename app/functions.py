import requests

WEBHOOK_URL = "http://localhost:5678/webhook-test/recomendar-filmes"


def enviar_requisicao(genero, descricao):

    payload = {
        "genero": genero,
        "descricao": descricao
    }

    response = requests.post(
        WEBHOOK_URL,
        json=payload
    )

    response.raise_for_status()

    return response.json()


def salvar_recomendacoes(filmes):

    with open(
        "recomendacoes.txt",
        "a",
        encoding="utf-8"
    ) as arquivo:

        for filme in filmes:

            arquivo.write(f"🎬 {filme.get('titulo')}\n")
            arquivo.write(f"⭐ Nota: {filme.get('nota')}\n")
            arquivo.write(f"📖 {filme.get('sinopse')}\n")
            arquivo.write("-" * 50 + "\n")


def carregar_recomendacoes():

    try:

        with open(
            "recomendacoes.txt",
            "r",
            encoding="utf-8"
        ) as arquivo:

            return arquivo.read()

    except FileNotFoundError:

        return "Nenhuma recomendação salva ainda."