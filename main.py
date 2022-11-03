from tkinter import Button, Label, Tk, colorchooser, ttk, messagebox
from tkinter import *
#from tkinter import colorchooser
#from janela import Janela


def mudarCorElementos():
  cor = colorchooser.askcolor(title="Alterar Cor")
  print(type(cor), cor)
  janela.configure(bg=cor[1])
  estiloTexto.configure(
    'TLabel',
    background=cor[1]
  )

def ativarMensagem():
  if comboMensagem.get() == "Info":
    messagebox.showinfo("Aviso", "Mensagem de aviso")
  elif comboMensagem.get() == "Warning":
    messagebox.showwarning("Cuidado", "Mensagem de cuidado")
  elif comboMensagem.get() == "Error":
    messagebox.showerror("Erro", "Mensagem de erro")
  elif comboMensagem.get() == "Confirm":
    messagebox.showerror("Confirma", "Mensagem de confirmar")
  else:
    messagebox.askretrycancel("Novamente", "Tentar novamente")


janela = Tk()
janela.geometry('500x500')
janela.title('Menu')
janela.configure(bg='#f1f1f1')

janela.columnconfigure(0, weight=1)

paddings = {'padx': 100, 'pady': 20, 'ipadx': 10, 'ipady': 10}

estiloTexto = ttk.Style()
estiloTexto.configure(
  'TLabel',
  font=('Times', 25),
  background='#f1f1f1'
)

estiloBotao = ttk.Style()
estiloBotao.configure('TButton', font=('Times', 20))

estiloComboBox = ttk.Style()
estiloComboBox.configure(
  'TCombobox',
  font=('Times', 20),
)

titulo = ttk.Label(text='Menu Exemplo')
titulo.grid(column=0, row=0, sticky=NS, pady=40)

botaoCorFundo = ttk.Button(text='Alterar Cor', command=mudarCorElementos)
botaoCorFundo.grid(column=0, row=1, sticky=EW, **paddings)

botaoMensagem = ttk.Button(text='Ativar Mensagem', command=ativarMensagem)
botaoMensagem.grid(column=0, row=2, sticky=EW, **paddings)

comboMensagem = ttk.Combobox(janela)
comboMensagem['values'] = ('Info', 'Warning', 'Error', 'Confirm', 'Try again')
print(comboMensagem.winfo_class())
comboMensagem.grid(column=0, row=3, sticky=EW, **paddings)

janela.mainloop()
