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






