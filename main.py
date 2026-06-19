import tkinter as tk
import json
import calendar
from datetime import datetime
import os
from PIL import Image, ImageTk

# =======================
# 1. CONSTANTES GLOBAIS.
# =======================
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
        
        #Container principal da linha
        self.frame = tk.Frame(parent, bd=1, relief="ridge", padx=5, pady=2)
        self.frame.pack(fill="x", padx=5, pady=1)
        
        # Foto de perfil (Colaboradores)
        self.lbl_foto = tk.label(self.frame, text="[Foto]", width=8, height=3, bg="lightgray")
        self.lbl_foto.pack(side="left", padx=(0, 10))
        self._carregar_foto()
        
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
           
            
# Bloco de execução.                
if __name__ == "__main__":
    root = tk.TK()
    app = AppPonto(root)
    root.mainloop()           
    
    
                     
        
        
        