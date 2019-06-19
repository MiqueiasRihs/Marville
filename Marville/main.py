from tkinter import *
  
class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.Container5 = Frame(master)
        self.Container5["padx"] = 20
        self.Container5.pack()

        self.Container6 = Frame(master)
        self.Container6["padx"] = 20
        self.Container6.pack()

        self.titulo = Label(self.primeiroContainer, text="PRODUTOS PROCURADOS")
        self.titulo["font"] = ("Helvetica", "13", "bold")
        self.titulo.pack()
  
        self.nomeLabel = Label(self.segundoContainer,text="Insira o nome do produto", font=self.fontePadrao)
        self.nomeLabel.pack(side=TOP)

        self.nomeLabel2 = Label(self.Container6,text=" ", font=self.fontePadrao)
        self.nomeLabel2.pack(side=BOTTOM)
  
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
        
  
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Salvar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.salvarProdutos
        self.autenticar.pack()

        self.titulo2 = Label(self.Container5, text="Lista de Produtos")
        self.titulo2["font"] = ("Arial", "10", "bold")
        self.titulo2.pack()
  
        self.barra = Scrollbar(self.Container5, orient=VERTICAL)
        self.listBox = Listbox(self.Container5, height=10, width=33, yscrollcommand=self.barra.set)
        self.barra.pack(side=RIGHT, fill=Y)
        self.listBox.pack()
        
        with open("BANCO.txt") as A:
            for i in A:
                print(self.listBox.insert(END, i))
            A.close()

#Método para salvar os produtos
    def salvarProdutos(self):
        with open("BANCO.txt", "a") as f:
            print(self.nome.get(), file=f)
        f.close()
        print(self.listBox.insert(END, self.nome.get()))
 
root = Tk()
root.title("MARVILLE")
root.iconbitmap(r"C:\Users\Miqueias\OneDrive\Codigos\Marville\icone.ico")
Application(root)
root.mainloop()