# ⏱️ Controle de Presença Corporativo Open-Source / Corporate Attendance Tracker

*(English version below)*

## 🇧🇷 Versão em Português

> Sistema open-source para controle de ponto corporativo. [cite_start]Desenvolvido em Python (Tkinter) com persistência local em JSON, geração automática de dados e foco em UX/UI. [cite: 197, 198]

Um aplicativo desktop desenvolvido para simplificar o gerenciamento de entrada e saída de colaboradores. Este projeto foi construído com foco em programação orientada a objetos e boas práticas de interface para ser intuitivo e direto ao ponto.

### 🚀 Como Instalar e Executar (Passo a Passo Fácil)

O projeto foi construído para ser "Plug and Play", ou seja, você não precisa instalar servidores complexos ou configurar bancos de dados. Siga os passos abaixo no seu terminal (ou prompt de comando):

**1. Baixe o projeto para o seu computador:**
`git clone https://github.com/SEU_USUARIO/sistema-ponto-open-source.git`

**2. [cite_start]Navegue até a pasta do projeto:** [cite: 242]
`cd sistema-ponto-open-source`

**3. [cite_start]Instale a dependência de imagens:** [cite: 242]
[cite_start]*(Isso permite que o sistema carregue as fotos dos colaboradores)* [cite: 242]
`pip install Pillow`

**4. [cite_start]Execute o aplicativo:** [cite: 242]
`python main.py`

> [cite_start]**💡 Nota importante:** Ao rodar pela primeira vez, os arquivos `dados_sistema.json` e `registro_ponto.txt` serão gerados automaticamente na sua máquina para fins de teste. [cite: 242] [cite_start]O sistema já nascerá com dados fictícios para você ver funcionando na prática! [cite: 243]

### ✨ Principais Funcionalidades
* **Gerenciamento de Status:** Controle em tempo real de entrada (IN) e saída (OUT), além de status especiais (Férias, Folga, Almoço) que bloqueiam campos automaticamente. [cite: 244]
* [cite_start]**Interface Fluida:** Barra de rolagem customizada para suportar grandes listas de funcionários sem quebrar o visual da tela. [cite: 245]
* [cite_start]**Auditoria Visível:** Todo evento é registrado com data e hora em um arquivo de texto local, e pode ser lido direto na tela do programa. [cite: 246]
* **Busca Avançada:** Um filtro para procurar pontos e ações por data específica ou nome do colaborador. [cite: 247]

### 📄 Licença
Este projeto está sob a Licença MIT. [cite: 248] Sinta-se livre para usá-lo, modificá-lo e distribuí-lo. [cite: 248] Veja o arquivo LICENSE para mais detalhes. [cite: 249]

---

## 🇺🇸 English Version

> Open-Source Corporate Attendance Tracker. [cite: 223] Status management, custom scrollbar UI, and automatically generated local database. (Python/Tkinter). [cite: 224]

A desktop application designed to streamline employee check-in and check-out management. This project was built with a strong focus on object-oriented programming and UX best practices to be intuitive and straightforward.

### 🚀 How to Install and Run (Easy Step-by-Step)

The project is built to run straight out of the box, with no complex database or server setup required. Just follow these simple steps in your terminal:

**1. Download the project to your computer:**
`git clone https://github.com/YOUR_USERNAME/sistema-ponto-open-source.git`

**2. [cite_start]Navigate to the project folder:** [cite: 249]
`cd sistema-ponto-open-source`

**3. [cite_start]Install the image handling dependency:** [cite: 249]
*(This allows the system to process and display employee avatars)* [cite: 249]
`pip install Pillow`

**4. [cite_start]Run the application:** [cite: 249]
`python main.py`

> [cite_start]**💡 Important Note:** Upon running the application for the first time, `dados_sistema.json` and `registro_ponto.txt` will be automatically generated on your machine for testing purposes. [cite: 249] [cite_start]The system comes with pre-populated dummy data so you can test it immediately! [cite: 250]

### ✨ Key Features
* **Status Management:** Real-time tracking for check-ins (IN) and check-outs (OUT), along with special statuses (Vacation, Day Off) that apply visual rules. [cite: 251]
* [cite_start]**Smooth Interface:** Custom scrollbar UI to allow navigation through large lists of employees without breaking the layout. [cite: 252]
* [cite_start]**Visible Audit Logs:** Every event is recorded with a timestamp in a local text file and displayed in an interactive panel within the app. [cite: 253]
* **Advanced Search:** Filter and audit historical logs by crossing text filters (Name) and specific dates. [cite: 254]

### 📄 License
This project is licensed under the MIT License. [cite: 255] Feel free to use, modify, and distribute it. [cite: 255] See the LICENSE file for more details. [cite: 256]
