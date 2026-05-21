import tkinter as tk

from interface import InterfaceFilmes


def main():

    janela = tk.Tk()

    InterfaceFilmes(janela)

    janela.mainloop()


if __name__ == "__main__":
    main()