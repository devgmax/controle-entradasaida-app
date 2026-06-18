import tkinter as tk
import json
import os
import calendar
from datetime import datetime

# =======================
# 1. CONSTANTES GLOBAIS.
# =======================
ARQUIVO_MEMORIA = "dados_sistema.json"
ARQUIVO_LOG = "registro_ponto.txt"

def registrar_log(mensagem):
    """"Salva a ação com data e hora no arquivo de texto local."""
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    try:
        with open(ARQUIVO_LOG, "a", encoding="utf-8") as f:
            f.write(f"[{agora}] {mensagem}\n")
    except Exception as e:
        print("Erro ao salvar log:", e)        

class AppPonto:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle de Entrada e Saída")
        self.root.geometry("1050x700")
        
        # Verifica e cria os dados fictícios se for a primeira vez rodando.
        self.preparar_ambiente_ficticio()
        
        # Cabeçalho Principal
        titulo = tk.label(root, text="Controle de Entrada e Saída", font=("Arial", 16, "bold"))
        titulo.pack(pady=10)
        
        # Assinatura
        assinatura = tk.Label(root, text="© Gabriel Max - Desenvolvido para Portfólio", font=("Arial", 9, "italic"), fg="gray")
        assinatura.pack(side="bottom", pady=5)
        
        # ----------------- LAYOUT BASE (Wireframe) -----------------
        self.container_esquerda = tk.Frame(root, bd=2, relief="groove")
        self.container_esquerda.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        tk.Label(self.container_esquerda, text="Lista de Colaboradores (Em Construção)", font=("Arial", 12), fg="gray").pack(pady=250)

        self.frame_lateral = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10)
        self.frame_lateral.pack(side="right", fill="y", padx=15, pady=10)
        
        tk.Label(self.frame_lateral, text="Painel de Ferramentas", font=("Arial", 12), fg="gray").pack(pady=250)
        
        
    def preparar_ambiente_ficticio(self):
        # Cria um banco de dados de teste automaticamente se for a primeira  execução
        if not os.path.exists(ARQUIVO_MEMORIA):
            dados_padrao = {
                "Dev Pleno": {"is_in": False, "obs": "", "status": "Ativo"},
                "Dev Backend": {"is_in": False, "obs": "", "status": "Ativo"},
                "Dev Senior": {"is_in": False, "obs": "", "status": "Ativo"},
                "Estagiário": {"is_in": False, "obs": "", "status": "Ativo"},
                "Dev Full Stack": {"is_in": False, "obs": "", "status": "Ativo"},
                "Gerente de Projetos": {"is_in": False, "obs": "", "status": "Ativo"}
            }
            try:
                with open (ARQUIVO_MEMORIA, "w", encoding="utf-8") as f:
                    json.dump(dados_padrao, f, ensure_ascii=False, indent=4)
                print("Banco de dados fictício criado com sucesso!")
            except Exception as e:
                print(f"Erro ao criar banco de dados inicial: {e}")
                
                
# Componentização da linha dos colaboradores

class FuncionarioRow:
    def __init__(self, parent, nome):
        self.nome = nome
        self.is_in = False # O status padrão que iniciar o app é todos em OUT (Falso).
        
        # Container Visual que segura os elementos do funcionário específica
        self.frame = tk.Frame(parent, bd=1, relief="ridge", padx=5, pady=5)
        self.frame.pack(fill="x", padx=10, pady=2)
        
        # Nome do funcionário alinhado à esquerda.
        self.lbl_nome = tk.Label(self.frame, text=nome, width=20, anchor="w", font=("Arial", 11, "bold"))
        self.lbl_nome.pack(side="left") 
        
        # Botão interativo de Status.
        self.btn_status = tk.Button(
            self.frame, text="OUT", bg="red", fg="white",
            width=8, font=("Arial", 10, "bold"),
            command=self.toggle_status
        )
        self.btn_status.pack(side="left", padx=15)
    
    def toggle_status(self):
        """Inverte o status e atualiza a interface visualmente."""
        self.is_in = not self.is_in
        if self.is_in:
            self.btn_status.config(text="IN", bg="green")
        else:
            self.btn_status.config(text="OUT", bg="red")   
                                
# Bloco de execução.                
if __name__ == "__main__":
    root = tk.TK()
    app = AppPonto(root)
    root.mainloop()           
    
    
                     
        
        
        