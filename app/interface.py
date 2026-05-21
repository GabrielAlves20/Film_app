import tkinter as tk
from tkinter import messagebox

from functions import (
    enviar_requisicao,
    salvar_recomendacoes,
    carregar_recomendacoes
)


class InterfaceFilmes:

    def __init__(self, janela):

        self.janela = janela

        self.janela.title(
            "Sistema de Filmes"
        )

        self.janela.geometry("700x600")

        self.criar_componentes()


    def criar_componentes(self):

        titulo = tk.Label(
            self.janela,
            text="🎬 RECOMENDADOR DE FILMES",
            font=("Arial", 18)
        )

        titulo.pack(pady=10)


        label_genero = tk.Label(
            self.janela,
            text="Gênero:"
        )

        label_genero.pack()

        self.entrada_genero = tk.Entry(
            self.janela,
            width=50
        )

        self.entrada_genero.pack(pady=5)


        label_descricao = tk.Label(
            self.janela,
            text="Descrição:"
        )

        label_descricao.pack()

        self.entrada_descricao = tk.Entry(
            self.janela,
            width=50
        )

        self.entrada_descricao.pack(pady=5)


        botao_recomendar = tk.Button(
            self.janela,
            text="Receber Recomendações",
            width=30,
            height=2,
            command=self.receber_recomendacoes
        )

        botao_recomendar.pack(pady=10)


        botao_historico = tk.Button(
            self.janela,
            text="Ver Recomendações Anteriores",
            width=30,
            height=2,
            command=self.ver_historico
        )

        botao_historico.pack(pady=10)


        self.resultado_texto = tk.Text(
            self.janela,
            width=80,
            height=20
        )

        self.resultado_texto.pack(pady=20)


    def receber_recomendacoes(self):

        genero = self.entrada_genero.get()

        descricao = self.entrada_descricao.get()

        if not genero or not descricao:

            messagebox.showwarning(
                "Aviso",
                "Preencha todos os campos."
            )

            return

        try:

            filmes = enviar_requisicao(
                genero,
                descricao
            )

            salvar_recomendacoes(filmes)

            self.resultado_texto.delete(
                1.0,
                tk.END
            )

            for filme in filmes:

                self.resultado_texto.insert(
                    tk.END,
                    f"🎬 {filme.get('titulo')}\n"
                )

                self.resultado_texto.insert(
                    tk.END,
                    f"⭐ Nota: {filme.get('nota')}\n"
                )

                self.resultado_texto.insert(
                    tk.END,
                    f"📖 {filme.get('sinopse')}\n"
                )

                self.resultado_texto.insert(
                    tk.END,
                    "-" * 50 + "\n"
                )

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )


    def ver_historico(self):

        conteudo = carregar_recomendacoes()

        self.resultado_texto.delete(
            1.0,
            tk.END
        )

        self.resultado_texto.insert(
            tk.END,
            conteudo
        )