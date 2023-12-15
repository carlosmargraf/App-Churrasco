import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

class Prog():
    def __init__(self, topo):
        self.tela = topo
        self.tela.title('churras.com App')
        #  definição do tamanho da janela
        self.tela.geometry('531x480')
        #  impedir de redimensionar a janela
        self.tela.resizable(False, False)

    def calculo_carne (self, adulto_cerveja, adulto_naoalcool, criancas):
        carne_adulto = float(0.4)
        carne_crianca = float(0.2)
        op1 = (adulto_cerveja + adulto_naoalcool) * carne_adulto
        op_1 = criancas * carne_crianca
        total_carne = op1 + op_1
        return total_carne

    def calculo_carvao(self, total_carne):
        carvao = float(0.833)
        op4 = total_carne * carvao
        return op4

    def calculo_cerveja(self, adulto_cerveja):
        cerveja = int(5)
        op2 = adulto_cerveja * cerveja
        return op2

    def calculo_refri(self, adulto_naoalcool, criancas):
        refri_adulto = float(1.5)
        refri_crianca = float(0.75)
        op3 = adulto_naoalcool * refri_adulto
        op_3 = criancas * refri_crianca
        total_refri = op3 + op_3
        return total_refri

    def obter_resultado(self):
        adulto_cerveja = int(self.simbbalcool_entry.get())
        adulto_naoalcool = int(self.naobbalcool_entry.get())
        criancas = int(self.consumocrianca_entry.get())

        total_carne = self.calculo_carne(adulto_cerveja, adulto_naoalcool, criancas)
        op2 = self.calculo_cerveja(adulto_cerveja)
        total_refri = self.calculo_refri(adulto_naoalcool, criancas)
        op4 = self.calculo_carvao(total_carne)

        msg = f"{total_carne} Kg de carne"
        msg += f"\n{op2} Latas de cerveja"
        msg += f"\n{total_refri} Litros de refrigerente ou água"
        msg += f"\n{op4} Kg de carvão"
        messagebox.showinfo("Comprar para esse churrasco", msg)

    def cria_widgets(self):
        # criar os frames
        self.frame1 = tk.Frame(self.tela)
        self.frame1.pack(fill=tk.BOTH)
        self.frame2 = tk.Frame(self.tela)
        self.frame2.pack(fill = tk.BOTH, padx=10, pady=5)
        self.frame3 = tk.Frame(self.tela)
        self.frame3.pack(fill=tk.BOTH, padx=10, pady=5)
        self.frame4 = tk.Frame(self.tela)
        self.frame4.pack(fill=tk.BOTH, padx=10, pady=5)
        self.frame5 = tk.Frame(self.tela)
        self.frame5.pack(fill=tk.BOTH, padx=10, pady=5)

        # backgroud
        # frame1
        self.image = ImageTk.PhotoImage(Image.open("backgroud3.png"))
        self.painel = ttk.Label(self.frame1, image=self.image)
        self.painel.pack(side=tk.LEFT)

        # pessoas
        # frame2
        self.simbbalcool_label = ttk.Label(self.frame2, text="Aduldos que NÃO bebem bebidas alcoólicas:")
        self.simbbalcool_label.pack(side= tk.LEFT)
        self.simbbalcool_entry = ttk.Entry(self.frame2, width= 11)
        self.simbbalcool_entry.pack(side= tk.RIGHT)
        # frame3
        self.naobbalcool_label = ttk.Label(self.frame3, text="Adultos que bebem cerveja:")
        self.naobbalcool_label.pack(side=tk.LEFT)
        self.naobbalcool_entry = ttk.Entry(self.frame3, width=11)
        self.naobbalcool_entry.pack(side=tk.RIGHT)
        # frame4
        self.consumocrianca_label = ttk.Label(self.frame4, text="Quantidade de crianças:")
        self.consumocrianca_label.pack(side=tk.LEFT)
        self.consumocrianca_entry = ttk.Entry(self.frame4, width=11)
        self.consumocrianca_entry.pack(side=tk.RIGHT)

        # button calcular
        # frame5
        button = ttk.Button(self.frame5, text="Calcular", command= self.obter_resultado)
        button.pack(side=tk.RIGHT)

if __name__ == '__main__':
    tela = tk.Tk()
    app = Prog(tela)
    app.cria_widgets()
    tela.mainloop()