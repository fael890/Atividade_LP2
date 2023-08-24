# Atividade_LP2
Ferramentas básicas da biblioteca tkinter do python

<h1>Instalação</h1>
A biblioteca tkinter é built-in, portanto, não existe a necessidade de instalar nada além do python.

<h1>Utilizando a biblioteca</h1>
Para utilizar a biblioteca basta fazer o import da seguinte forma.

```
from tkinter import * 
```

Agora vamos para a etapa fundamental que seria a criação da janela, utilizando a função ``Tk()``.

```
janela = Tk()
```

Podemos modificar algumas propriedades básicas da janela, como tamanho, titulo, cor de fundo, entre outros.

```
janela.geometry('500x500')
janela.title('Menu')
janela.configure(bg='#f1f1f1')
```

No bloco de código anterior é importante dar uma atenção para o comando ``.configure()``. É com ele que vamos alterar o estilo e adicionar algumas características para os elementos que serão adicionados na janela.

Para adicionar elemetos na tela é bem simples, você pode instanciar a classe daquele elemento e utilizar a função ``pack()`` para colocar ele na janela.
As classes utilizadas no projeto foram Label, Button e Combobox. Além disso, os elementos abaixo foram criados com ferramenta ``Tk``, existe a possibilidade de criar com ttk que será apresentado no próximo tópico.
```
titulo = Label(text='Menu Exemplo')
titulo.pack()

botaoCorFundo = Button(text='Alterar Cor', command=mudarCorElementos)
botaoCorFundo.pack()
```

Porém para aplicar estilo nos elementos criados existe a necessidade de utilizar a ferramenta ``ttk`` que vem ao importar o tkinter. O ttk é utilizado para adicionar padrões de estilo nos elementos. Fazendo um paralelo grosseiro, o ``ttk`` seria o ``Tk`` com estilo e para criar um objeto do tipo ``ttk`` é super simples.
```
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
```
No código foi criado 3 elementos do tipo ttk botão, label e combobox. Para criar o tipo ttk basta utilizar ``ttk.Elemento()``
Além disso, no lugar do ``pack()`` foi utilizado o ``grid()`` que o conceito é o mesmo, adicionar as coisas na tela, porém o grid tem algumas propriedades para alinhar os elementos na tela.

Agora que temos elementos do tipo ttk é possível aplicar um estilo para eles.
```
estiloTexto = ttk.Style()
estiloTexto.configure(
  'TLabel',
  font=('Times', 25),
  background='#f1f1f1'
)

estiloBotao = ttk.Style()
estiloBotao.configure(
  'TButton', 
  font=('Times', 20)
)

estiloComboBox = ttk.Style()
estiloComboBox.configure(
  'TCombobox',
  font=('Times', 20),
)
```

Para finalizar seria legal apresentar sobre os botões e como acionar funções com eles.
```
def mudarCorElementos():
  cor = colorchooser.askcolor(title="Alterar Cor")
  print(type(cor), cor)
  janela.configure(bg=cor[1])
  estiloTexto.configure(
    'TLabel',
    background=cor[1]
  )

botaoCorFundo = ttk.Button(text='Alterar Cor', command=mudarCorElementos)
botaoCorFundo.grid(column=0, row=1, sticky=EW, **paddings)
```
O clique nesse botão aciona a função mudarCorElementos que exibe um janela para seleção de cor. Quando seleciona a cor você terá uma tupla com o código RGB e o hexcode, então você pode utilizar qual precisar, no caso do exemplo acima foi alterado a cor de fundo da janela para o valor dentro de cor[1] que seria um hexcode.
Para vincular a função no botão é necessário utilizar o ``command=nomeDaFuncao``

<h1>Observações</h1>
O tkinter é uma boa biblioteca para criação de interfaces gráficas, ainda mais quando você aplica um facilitador como Pygubu, que seria um programa de construções de interface baseado em tkinter, ou seja, você pode construir uma tela de forma intuitiva.
Na apresentação da ferramenta foi disponibilizado um exemplo e uma explicação extremamente superficial. A melhor coisa é procurar mais informações na documentação que está na seção de referências.

<h1>Referências</h1>

<a href='https://docs.python.org/3/library/tk.html'>Clique para acessar a documentação do tkinter!</a>

<a href='https://www.pythontutorial.net/tkinter/tkinter-ttk/'>Clique para acessar tutoriais sobre ttk!</a>




