import tkinter as tk
from tkinter import ttk
import json
import calendar
from datetime import datetime
import os
from PIL import Image, ImageTk

# ======================================
# 1. CONSTANTES GLOBAIS E FUNÇÃO DE LOG.
# ======================================
ARQUIVO_MEMORIA = "dados_sistema.json"
ARQUIVO_LOG = "registro_ponto.txt"

"""Função de log"""
def registrar_log(mensagem):
    """"Salva a ação com data e hora no arquivo de texto local."""
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    try:
        with open(ARQUIVO_LOG, "a", encoding="utf-8") as f:
            f.write(f"[{agora}] {mensagem}\n")
    except Exception as e:
        print("Erro ao salvar log:", e)  
        
# =============================================
# 2. COMPONENTES VISUAIS 
# =============================================      

class FuncionarioRow:
    def __init__(self, parent, nome, app):
        self.app = app
        self.nome = nome
        self.is_in = False
        
        # Container principal da linha
        self.frame = tk.Frame(parent, bd=1, relief="ridge", padx=5, pady=2)
        self.frame.pack(fill="x", padx=5, pady=1)
        
        # Foto de perfil (Foto)
        self.lbl_foto = tk.Label(self.frame, text="[Foto]", width=8, height=3, bg="lightgray")
        self.lbl_foto.pack(side="left", padx=(0, 10))
        self.carregar_foto()
        
        # Informações e Botão IN/OUT
        self.lbl_nome = tk.Label(self.frame, text=nome, width=18, anchor="w", font=("Arial", 11, "bold"))
        self.lbl_nome.pack(side="left")
        
        self.btn_status = tk.Button(
            self.frame, text="OUT", bg="red", fg="white", width=8, font=("Arial", 10, "bold"),
        command=self.toggle_status    
        )
        self.btn_status.pack(side="left", padx=15)
        
        # SELETOR DE STATUS ESPECIAL
        self.status_var = tk.StringVar(value="Ativo")
        self.opt_status = ttk.Combobox(
            self.frame, textvariable=self.status_var,
            values=["Ativo", "Folga", "Férias", "Almoço", "Reunião"],
            width=12, state="readonly"
        )
        self.opt_status.pack(side="left", padx=15)
        self.opt_status.bind("<<ComboboxSelected>>", self.update_special_status)
        self.opt_status.bind("<MouseWheel>", lambda e: "break") # Evita scroll acidental
        
    def carregar_foto(self):
        """Tenta carregar o avatar da pasta 'fotos', caso exista."""
        caminho_foto = os.path.join("fotos", f"{self.nome}.png")
        if not os.path.exists(caminho_foto):
            caminho_foto = os.path.join("fotos", f"{self.nome}.jpg")
            
        if os.path.exists(caminho_foto):
            try:
                img = Image.open(caminho_foto).resize((80, 80))
                self.photo = ImageTk.PhotoImage(img)
                self.lbl_foto.config(image=self.photo, width=80, height=80, text="")
            except Exception as e:
                print(f"Erro ao carregar foto de {self.nome}:", e)
                
    def toggle_status(self):
        """Inverte IN/OUT se o funcionário estiver Ativo"""
        if self.status_var.get() != "Ativo": return
        
        self.is_in = not self.is_in
        cor, texto = ("green", "IN") if self.is_in else ("red", "OUT")
        self.btn_status.config(text=texto, bg=cor)
        
        status_txt = "ENTROU (IN)" if self.is_in else "SAIU (OUT)"
        registrar_log(f"{self.nome} {status_txt}") 
        
        self.app.salvar_dados()
        self.app.atualizar_log_tela()
        
    def update_special_status(self, event=None):
        """Altera o botão com base no status especial e retorna para IN ao voltar para Ativo."""
        status = self.status_var.get()
        
        if status != "Ativo":
            self.btn_status.config(text=status.upper(), bg="gray")
            self.is_in = False
        else:
            self.is_in = True
            self.btn_status.config(text="IN", bg="green")
            
        registrar_log(f"Status de {self.nome} alterado para {status.upper()}.")
        self.app.salvar_dados()
        self.app.atualizar_log_tela()
        
#=============================
# APLICAÇÃO PRINCIPAL (Layout)                                    
#=============================
class AppPonto:
    def __init__(self, root):
        #==================================
        # CONFIGURAÇÃO RAIZ E INICIALIZAÇÃO
        #==================================
        self.root = root
        self.root.title("Controle de Presença Corporativo - Open Source")
        self.root.geometry("1050x700")
        
        self.preparar_ambiente_ficticio()
        self.funcionarios_rows = []
        
        self._configurar_layout()
        self.carregar_dados()
        registrar_log("--- SISTEMA INICIADO ---")
        self.atualizar_log_tela()
    
    def preparar_ambiente_ficticio(self):
        """"Cria o JSON base se o app for aberto pela primeira vez."""
        if not os.path.exists(ARQUIVO_MEMORIA):
           equipe = [
               "Gerente de Projetos", "Tech Lead", "Dev Senior", "Dev Pleno", 
               "Dev Backend", "Dev Frontend", "Dev Full Stack", "QA Analyst",
               "UX Designer", "Estagiário 01", "Estagiário 02", "Analista de Suporte"
           ]
           dados_padrao = {nome: {"is_in": False, "status": "Ativo"} for nome in equipe}
           dados_padrao["DATA_SISTEMA"] = datetime.now().strftime("%Y-%m-%d")
           
        try:
            with open(ARQUIVO_MEMORIA, "w", encoding="utf-8") as f:
                   json.dump(dados_padrao, f, ensure_ascii=False, indent=4)
        except Exception as e:
                pass
            