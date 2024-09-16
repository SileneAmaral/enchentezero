import tkinter as tk
import sqlite3
import pandas as pd

janela = tk.Tk()
janela.title('Projeto Enchente Zero® 2024')
janela. geometry("730x350")

conexao = sqlite3.connect('dados.db')


c = conexao.cursor()
#

#
c.execute("""CREATE TABLE morador (
     nome text,
     endereco text,
     email text,
     telefone text,
     localizacao text

    )""")
#

conexao.commit()


conexao.close()



def cadastrar_morador():
    conexao = sqlite3.connect('dados.db')
    c = conexao.cursor()


    c.execute("INSERT INTO morador VALUES (:nome,:endereco,:email,:telefone, :localizacao)",
              {
                  'nome': entry_nome.get(),
                  'endereco': entry_endereco.get(),
                  'email': entry_email.get(),
                  'telefone': entry_telefone.get(),
                  'localizacao': entry_localizacao.get()
              })



    conexao.commit()


    conexao.close()


    entry_nome.delete(0,"end")
    entry_endereco.delete(0,"end")
    entry_email.delete(0,"end")
    entry_telefone.delete(0,"end")
    entry_localizacao.delete(0,"end")

def limpar_campos():
        entry_nome.delete(0, tk.END)
        entry_endereco.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_localizacao.delete(0, tk.END)


label_nome = tk.Label(janela, text='Nome Completo')
label_nome.grid(row=0,column=0, padx=10, pady=10)

label_endereco = tk.Label(janela, text='Endereço completo')
label_endereco.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='E-mail')
label_email.grid(row=2, column=0 , padx=10, pady=10)

label_telefone = tk.Label(janela, text='Telefone')
label_telefone.grid(row=3, column=0, padx=10, pady=10)

label_localizacao = tk.Label(janela, text='Localização')
label_localizacao.grid(row=4, column=0, padx=10, pady=10)


entry_nome = tk.Entry(janela, width =60)
entry_nome.grid(row=0,column=1, padx=10, pady=10)

entry_endereco = tk.Entry(janela, width =60)
entry_endereco.grid(row=1, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, width =60)
entry_email.grid(row=2, column=1 , padx=10, pady=10)

entry_telefone = tk.Entry(janela, width =60)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)

entry_localizacao = tk.Entry(janela, width =60)
entry_localizacao.grid(row=4, column=1, padx=10, pady=10)


botao_cadastrar = tk.Button(text='Cadastrar Morador', command=cadastrar_morador)
botao_cadastrar.grid(row=5, column=1,columnspan=2, padx=10, pady=10 , ipadx = 80)

limpar_botao = tk.Button(text="Limpar Dados", command=limpar_campos)
limpar_botao.grid(row=6, column=1,columnspan=2, padx=10, pady=10 , ipadx = 80)

janela.mainloop()






