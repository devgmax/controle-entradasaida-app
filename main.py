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
    
    def _configurar_layout(self):
        #================================================
        # LADO ESQUERDO (Lista com Scrollbar) E TÍTULOS.
        #================================================ 
        """MOnta todas as divisões da tela principal."""
        tk.Label(self.root, text="Controle de Entrada e Saída", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(self.root, text="© 2026 Gabriel Max • Licença MIT (GitHub: devgmax)", font=("Arial", 9, "Italic"), fg="gray").pack(side="bottom", pady=5)
        
        # -- Lado Esquerdo: Lista com Scroll
        container_esquerda = tk.Frame(self.root)
        container_esquerda.pack(side="left", fill="both", expand=True)
        
        self.canvas = tk.Canvas(container_esquerda, borderwidth=0, highlightthickness=0)
        self.scrollbar = tk.Scrollbar(container_esquerda, orient="vertical", command=self.canvas.yview)
        self.frame_funcionarios = tk.Frame(self.canvas)
        
        self.frame_funcionarios.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.frame_funcionarios, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Inicializa a lista visual da equipe a partir do arquivo de dados local
        with open(ARQUIVO_MEMORIA, "r", encoding="utf-8") as f:
            nomes = [k for k in json.load(f).keys() if k != "DATA_SISTEMA"]
            for nome in nomes:
                row = FuncionarioRow(self.frame_funcionarios, nome, self)
                self.funcionarios_rows.append(row)
        
        #==============================
        # LADO DIREITO E CAIXAS DE LOGS
        #==============================
        frame_lateral = tk.Frame(self.root, bd=2, relief="groove", padx=10, pady=10)
        frame_lateral.pack(side="right", fill="y", padx=15, pady=5)
         
        tk.Label(frame_lateral, text="Calendário", font=("Arial", 12, "bold")).pack(pady=(0, 5))
        self.frame_calendario = tk.Frame(frame_lateral)
        self.frame_calendario.pack(pady=5)
        
        agora = datetime.now()
        self.ano_atual, self.mes_atual = agora.year, agora.month
        self.desenhar_calendario()
        
        tk.Frame(frame_lateral, height=2, bg="gray").pack(fill="x", pady=10)
        tk.Button(frame_lateral, text="🔍 Busca Avançada", bg="#0052cc", fg="white", font=("Arial", 10, "bold"), command=self.abrir_janela_busca).pack(fill="x", pady=5)
        tk.Frame(frame_lateral, height=2, bg="gray").pack(fill="x", pady=10)
        
        tk.Label(frame_lateral, text="Histórico Recente", font=("Arial", 12, "bold")).pack(pady=(5, 5))
        frame_log = tk.Frame(frame_lateral)
        frame_log.pack(fill="both", expand=True)
        
        self.caixa_log = tk.Text(frame_log, width=45, height=12, state="disabled", font=("Arial", 9))
        scroll_log = tk.Scrollbar(frame_log, command=self.caixa_log.yview)
        self.caixa_log.configure(yscrollcommand=scroll_log.set)
        self.caixa_log.pack(side="left", fill="both", expand=True)
        scroll_log.pack(side="right", fill="y")
        
    # = LOGICA DO CALENDÁRIO E BUSCA =
    
    # -- MOTORES DO CALENDÁRIO E DE BUSCA AVANÇADA --
    def desenhar_calendario(self):
        for widget in self.frame_calendario.winfo_children(): widget.destroy()

        meses_pt = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}
        frame_nav = tk.Frame(self.frame_calendario)
        frame_nav.grid(row=0, column=0, columnspan=7, pady=5)

        tk.Button(frame_nav, text="<", command=self.mes_anterior, width=2).pack(side="left", padx=5)
        tk.Label(frame_nav, text=f"{meses_pt[self.mes_atual]} {self.ano_atual}", font=("Arial", 10, "bold"), width=15).pack(side="left")
        tk.Button(frame_nav, text=">", command=self.mes_proximo, width=2).pack(side="left", padx=5)

        for col, dia in enumerate(["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]):
            tk.Label(self.frame_calendario, text=dia, font=("Arial", 9, "bold")).grid(row=1, column=col)

        hoje = datetime.now()
        for row_idx, semana in enumerate(calendar.monthcalendar(self.ano_atual, self.mes_atual)):
            for col_idx, dia in enumerate(semana):
                if dia != 0:
                    cor_fundo = "lightblue" if (dia == hoje.day and self.mes_atual == hoje.month and self.ano_atual == hoje.year) else "SystemButtonFace"
                    btn = tk.Button(self.frame_calendario, text=str(dia), width=3, bg=cor_fundo, command=lambda d=dia, m=self.mes_atual, a=self.ano_atual: self.buscar_log_do_dia(d, m, a))
                    btn.grid(row=row_idx+2, column=col_idx, padx=1, pady=1)

    def mes_anterior(self):
        self.mes_atual, self.ano_atual = (12, self.ano_atual - 1) if self.mes_atual == 1 else (self.mes_atual - 1, self.ano_atual)
        self.desenhar_calendario()

    def mes_proximo(self):
        self.mes_atual, self.ano_atual = (1, self.ano_atual + 1) if self.mes_atual == 12 else (self.mes_atual + 1, self.ano_atual)
        self.desenhar_calendario()

    def buscar_log_do_dia(self, dia, mes, ano):
        data_fmt = f"{dia:02d}/{mes:02d}/{ano}"
        self._exibir_modal_resultados(f"Histórico do dia {data_fmt}", lambda linha: data_fmt in linha, f"Nenhum ponto registrado no dia {data_fmt}.")

    def abrir_janela_busca(self):
        janela = tk.Toplevel(self.root)
        janela.title("Buscar Histórico")
        janela.geometry("500x450")
        janela.grab_set()

        tk.Label(janela, text="Filtros de Pesquisa\n(Ex: DD/MM/AAAA)", font=("Arial", 12, "bold")).pack(pady=10)
        frame_filtros = tk.Frame(janela)
        frame_filtros.pack(pady=5)

        tk.Label(frame_filtros, text="Nome:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        ent_nome = tk.Entry(frame_filtros, width=25)
        ent_nome.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_filtros, text="Data:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        ent_data = tk.Entry(frame_filtros, width=25)
        ent_data.grid(row=1, column=1, padx=5, pady=5)

        frame_res = tk.Frame(janela)
        caixa_res = tk.Text(frame_res, state="disabled", font=("Arial", 9))
        scroll_res = tk.Scrollbar(frame_res, command=caixa_res.yview)
        caixa_res.configure(yscrollcommand=scroll_res.set)

        def executar_busca():
            termo_n, termo_d = ent_nome.get().lower().strip(), ent_data.get().strip()
            caixa_res.config(state="normal")
            caixa_res.delete(1.0, tk.END)
            try:
                with open(ARQUIVO_LOG, "r", encoding="utf-8") as f:
                    linhas = [l for l in f.readlines() if termo_n in l.lower() and termo_d in l]
                    if linhas:
                        for l in linhas: caixa_res.insert(tk.END, l)
                    else:
                        caixa_res.insert(tk.END, "Nenhum registro encontrado.")
            except:
                caixa_res.insert(tk.END, "Arquivo de log inexistente.")
            caixa_res.config(state="disabled")

        tk.Button(janela, text="🔍 Buscar", bg="green", fg="white", font=("Arial", 10, "bold"), command=executar_busca).pack(pady=10)
        frame_res.pack(fill="both", expand=True, padx=15, pady=10)
        caixa_res.pack(side="left", fill="both", expand=True)
        scroll_res.pack(side="right", fill="y")

    def _exibir_modal_resultados(self, titulo, condicao_filtro, msg_vazio):
        """Método auxiliar para renderizar a janela de resultados de logs."""
        janela = tk.Toplevel(self.root)
        janela.title(titulo)
        janela.geometry("550x400")
        janela.grab_set()

        tk.Label(janela, text=titulo, font=("Arial", 12, "bold")).pack(pady=10)
        frame = tk.Frame(janela)
        frame.pack(fill="both", expand=True, padx=15, pady=10)
        
        caixa = tk.Text(frame, state="normal", font=("Arial", 9))
        scroll = tk.Scrollbar(frame, command=caixa.yview)
        caixa.configure(yscrollcommand=scroll.set)
        caixa.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        try:
            with open(ARQUIVO_LOG, "r", encoding="utf-8") as f:
                linhas = [l for l in f.readlines() if condicao_filtro(l)]
                if linhas:
                    for l in linhas: caixa.insert(tk.END, l)
                else:
                    caixa.insert(tk.END, msg_vazio)
        except:
            caixa.insert(tk.END, "O arquivo de log ainda não existe.")
        caixa.config(state="disabled")    
           
        
                         