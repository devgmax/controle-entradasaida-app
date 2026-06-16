# [cite_start]⏱️ Controle de Presença Corporativo Open-Source [cite: 205]

> Sistema open-source para controle de ponto corporativo. [cite_start]Desenvolvido em Python (Tkinter) com persistência local em JSON, geração automática de dados e foco em UX/UI[cite: 201, 202].

Um aplicativo desktop desenvolvido para simplificar o gerenciamento de entrada e saída de colaboradores. Este projeto foi construído com foco em **Programação Orientada a Objetos (POO)** e **boas práticas de interface gráfica (UX)** para contornar limitações de renderização em listas extensas.

## ✨ Funcionalidades

* [cite_start]**Gerenciamento de Status:** Controle em tempo real de entrada (IN) e saída (OUT), além de status especiais (Férias, Folga, Almoço) que aplicam regras visuais e bloqueiam campos[cite: 205].
* [cite_start]**Interface de Rolagem Customizada:** Utilização de `Canvas` acoplado com `Scrollbar` para permitir a navegação fluida em grandes listas de funcionários sem quebrar o layout[cite: 205].
* [cite_start]**Banco de Dados Plug-and-Play:** O sistema detecta a primeira execução e gera automaticamente um banco de dados local (JSON) populado com dados fictícios ("Dummy Data"), permitindo testes imediatos[cite: 205].
* [cite_start]**Auditoria e Logs:** Todo evento é registrado com data e hora em um arquivo local `.txt`, sendo exibido em um painel interativo na própria aplicação[cite: 204].
* **Busca Avançada:** Um sistema de modal que permite cruzar filtros textuais (Nome) e datas específicas para auditar o histórico de forma rápida.
* **Inteligência de Turno:** Identifica a virada do dia no sistema operacional e redefine automaticamente todos os colaboradores ativos para "OUT".

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Interface Gráfica:** Tkinter (Nativo) e ttk
* **Processamento de Imagens:** Pillow (PIL)
* **Persistência de Dados:** Módulos nativos `json` e `os`
* **Lógica Temporal:** Módulos nativos `datetime` e `calendar`

## 🚀 Como Executar o Projeto

O projeto foi construído para rodar de forma simples e direta, sem a necessidade de configurações complexas de banco de dados.

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/sistema-ponto-open-source.git](https://github.com/SEU_USUARIO/sistema-ponto-open-source.git)


   Instale a dependência de imagens:

Bash
pip install Pillow
Execute o aplicativo:

Bash
python main.py
