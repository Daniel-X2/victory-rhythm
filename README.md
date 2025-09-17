# 🎧 **Victory Rhythm**

> Um simples *player MP3* 

Você pode:
- Carregar um arquivo `*.mp3` (qualquer formato compatível com `pygame.mixer`);
- Tocar a música;

Os metadados (título, artista, álbum…) são armazenados em um pequeno banco SQLite gerenciado por **SQLAlchemy**.

---

## 📑 Sumário

1. [Visão geral](#-visão-geral)  
2. [Tecnologias e dependências](#-tecnologias-e-dependências)  
3. [Instalação rápida](#-instalação-rapida)  
4. [Como usar](#-como-usar)  
5. [Estrutura de pastas](#-estrutura-de-pastas)  
6. [Contribuindo](#-contribuindo)  
7. [Licença](#-licença)  

---

## 🔎 Visão geral

| ❓ Por quê? | ✅ O que faz |
|-------------|--------------|
| Reproduz arquivos MP3 usando `pygame.mixer` | Biblioteca leve e testada para áudio em Python |
| Interface moderna com `CustomTkinter` (tema escuro, widgets arredondados) | UI clean sem necessidade de HTML/CSS |
| Persistência de histórico e playlists via SQLite + SQLAlchemy | Simples e portátil |
| Suporte à capa de álbum usando `Pillow (PIL)` | Arte exibida dentro da UI |

---

## 🛠️ Tecnologias e dependências

| Categoria | Biblioteca | Versão de Exemplo | Uso no Projeto |
|-----------|------------|-------------------|----------------|
| **Áudio** | `pygame` | `2.5.2` | Reprodução de MP3 (pygame.mixer) |
| **DB / ORM** | `SQLAlchemy` | `2.0.34` | Camada de acesso a SQLite (metadata, playlists) |
| **Imagens** | `Pillow (PIL)` | `10.4.0` | Carregamento e redimensionamento de capas |
| **GUI** | `customtkinter` | `5.2.2` | Interface estilizada (temas, botões arredondados) |



> O arquivo `requirements.txt` já contém as versões testadas.  
> Para atualizar algo, basta rodar:  
> ```bash
> pip install -U <pacote>
> ```

---

## 🚀 Instalação rápida

```bash
# 1️⃣ Clone o repositório
git clone https://github.com/Daniel-X2/victory-rhythm.git
cd victory-rhythm

# 2️⃣ Crie um ambiente virtual (recomendado)
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows
.\.venv\Scripts\activate

# 3️⃣ Instale as dependências
pip install -r requirements.txt
```

### `requirements.txt` 

```txt
pygame==2.5.2
SQLAlchemy==2.0.34
Pillow==10.4.0
matplotlib==3.9.2
customtkinter==5.2.2
tinytag==2.1.2
```

> **Obs.:** `pygame` precisa dos codecs de áudio do sistema.  
> Em Ubuntu/Debian, sempre que necessário, instale:  
> ```bash
> sudo apt-get install -y ffmpeg libavcodec-extra
> ```

---

## ▶️ Como usar

```bash
# Dentro do ambiente virtual
python -m victory_rhythm

## 📂 Estrutura de pastas

---

## 🤝 Contribuindo

1. Fork o repositório.  
2. Crie uma branch para sua melhoria:  
   ```bash
   git checkout -b nome-da-feature
   ```  
3. Garanta que todos os testes passem (`pytest`).  
4. Atualize `requirements.txt` caso adicione novas bibliotecas.  
5. Abra um PR descrevendo a mudança.

**Regras de estilo**

| Item | Descrição |
|------|-----------|
| **PEP 8** | Use `flake8` ou `black` para formato. |
| **Documentação** | Docstrings claras para cada classe / função. |
| **Testes** | Sempre inclua testes unitários para lógicas novas (ex.: cálculo de espectro). |

---

## 📄 Licença

Distribuído sob a **MIT License** – sinta‑se livre para usar, modificar e redistribuir, desde que mantenha a atribuição original.  

```
MIT License
...
```

---

### Links Úteis

- **Código Fonte:** <https://github.com/Daniel-X2/victory-rhythm>  
- **Pacotes do PyPI:**  
  - `pygame` – <https://pypi.org/project/pygame/>  
  - `SQLAlchemy` – <https://pypi.org/project/SQLAlchemy/>  
  - `Pillow` – <https://pypi.org/project/Pillow/>  
  - `customtkinter` – <https://pypi.org/project/customtkinter/>  

💡 *Pronto para acompanhar o ritmo?*

