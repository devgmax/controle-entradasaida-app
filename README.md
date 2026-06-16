# ⏱️ Controle de Presença Corporativo Open-Source / Corporate Attendance Tracker

*(English version below)*

## 🇧🇷 Versão em Português

> Sistema open-source para controle de ponto corporativo. Desenvolvido em Python (Tkinter) com persistência local em JSON, geração automática de dados e foco em UX/UI.

Um aplicativo desktop desenvolvido para simplificar o gerenciamento de entrada e saída de colaboradores. Este projeto foi construído com foco em programação orientada a objetos e boas práticas de interface para ser intuitivo e direto ao ponto.

### 🚀 Como Instalar e Executar (Passo a Passo Fácil)

O projeto foi construído para ser "Plug and Play", ou seja, você não precisa instalar servidores complexos ou configurar bancos de dados. Siga os passos abaixo no seu terminal (ou prompt de comando):

**1. Baixe o projeto para o seu computador:**
`git clone https://github.com/SEU_USUARIO/controle-entradasaida-app.git`

**2. Navegue até a pasta do projeto:**
`cd controle-entradasaida-app`

**3. Instale a dependência de imagens:**
*(Isso permite que o sistema carregue as fotos dos colaboradores)*
`pip install Pillow`

**4. Execute o aplicativo:**
`python main.py`

> **💡 Nota importante:** Ao rodar pela primeira vez, os arquivos `dados_sistema.json` e `registro_ponto.txt` serão gerados automaticamente na sua máquina para fins de teste. O sistema já nascerá com dados fictícios para você ver funcionando na prática!

### ✨ Principais Funcionalidades
* **Gerenciamento de Status:** Controle em tempo real de entrada (IN) e saída (OUT), além de status especiais (Férias, Folga, Almoço) que bloqueiam campos automaticamente.
* **Interface Fluida:** Barra de rolagem customizada para suportar grandes listas de funcionários sem quebrar o visual da tela.
* **Auditoria Visível:** Todo evento é registrado com data e hora em um arquivo de texto local, e pode ser lido direto na tela do programa.
* **Busca Avançada:** Um filtro para procurar pontos e ações por data específica ou nome do colaborador.

### 📄 Licença
Este projeto está sob a Licença MIT. Sinta-se livre para usá-lo, modificá-lo e distribuí-lo. Veja o arquivo LICENSE para mais detalhes.

---

## 🇺🇸 English Version

> Open-Source Corporate Attendance Tracker. Status management, custom scrollbar UI, and automatically generated local database. (Python/Tkinter).

A desktop application designed to streamline employee check-in and check-out management. This project was built with a strong focus on object-oriented programming and UX best practices to be intuitive and straightforward.

### 🚀 How to Install and Run (Easy Step-by-Step)

The project is built to run straight out of the box, with no complex database or server setup required. Just follow these simple steps in your terminal:

**1. Download the project to your computer:**
`git clone https://github.com/YOUR_USERNAME/controle-entradasaida-app.git`

**2. Navigate to the project folder:**
`cd controle-entradasaida-app`

**3. Install the image handling dependency:**
*(This allows the system to process and display employee avatars)*
`pip install Pillow`

**4. Run the application:**
`python main.py`

> **💡 Important Note:** Upon running the application for the first time, `dados_sistema.json` and `registro_ponto.txt` will be automatically generated on your machine for testing purposes. The system comes with pre-populated dummy data so you can test it immediately!

### ✨ Key Features
* **Status Management:** Real-time tracking for check-ins (IN) and check-outs (OUT), along with special statuses (Vacation, Day Off) that apply visual rules.
* **Smooth Interface:** Custom scrollbar UI to allow navigation through large lists of employees without breaking the layout.
* **Visible Audit Logs:** Every event is recorded with a timestamp in a local text file and displayed in an interactive panel within the app.
* **Advanced Search:** Filter and audit historical logs by crossing text filters (Name) and specific dates.

### 📄 License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it. See the LICENSE file for more details.
