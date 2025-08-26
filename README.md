# 🎧 **Victory Rhythm**

> Um simples *player MP3* + *visualizador de ritmo* feito em Python.

Você pode:
- Carregar um arquivo `*.mp3` (qualquer formato compatível com `pygame.mixer`);
- Tocar a música;
- Exibir em tempo real gráficos de amplitude e espectro, animações e imagens de capa usando  
  `matplotlib`, `Pillow` e `CustomTkinter`.

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
| Exibe gráficos de amplitude e espectro em tempo real (`matplotlib`) | Visualiza o “ritmo” enquanto a música toca |
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
| **Plot / Visual** | `matplotlib` | `3.9.2` | Gráficos de waveform e espectro em tempo real |
| **GUI** | `customtkinter` | `5.2.2` | Interface estilizada (temas, botões arredondados) |
| **Análise de áudio** | `numpy` / `scipy` | `1.26.4` / `1.14.1` | Processamento de dados para visualizações |
| **Env. Variables** | `python-dotenv` | `1.0.1` | Carrega variáveis de ambiente (p.ex.: caminho DB) |

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

### `requirements.txt` (exemplo)

```txt
pygame==2.5.2
SQLAlchemy==2.0.34
Pillow==10.4.0
matplotlib==3.9.2
customtkinter==5.2.2
numpy==1.26.4
scipy==1.14.1
python-dotenv==1.0.1
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
# ou
./run.sh
```

1. Clique no botão **Open** e selecione um arquivo MP3.  
2. A capa, título e artista serão exibidos automaticamente (se houver tags ID3).  
3. Passe **Play** – o áudio começa e, simultaneamente, gráficos de waveform e espectro são desenhados em tempo real.  
4. Use **Pause/Stop** ou ajuste o volume com o slider.  
5. O histórico da faixa tocada ficará salvo em `victory_rhythm.db` (SQLite) e pode ser visualizado na aba **History**.  
6. **Dica:** o player aceita playlists arrastando múltiplos MP3 na janela – elas são armazenadas como uma lista de IDs no mesmo banco.

---

## 📂 Estrutura de pastas

```
victory-rhythm/
│
├─ src/                            # Código fonte
│   ├─ __init__.py
│   ├─ main.py                  # Entrada da aplicação
│   ├─ player.py                # Wrapper pygame + controle
│   ├─ visualizer.py            # Matplotlib + atualização em tempo real
│   ├─ db.py                    # Modelo SQLAlchemy (Track, Playlist)
│   └─ ui/                      # Widgets CustomTkinter
│       ├─ main_window.py
│       └─ components.py
│
├─ assets/                          # Ícones padrão, tema CustomTkinter
│
├─ tests/                           # Testes unitários (pytest)
│
├─ requirements.txt
├─ .gitignore
├─ README.md
└─ victory_rhythm.db                # Criado na primeira execução (SQLite)
```

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
  - `matplotlib` – <https://pypi.org/project/matplotlib/>  
  - `customtkinter` – <https://pypi.org/project/customtkinter/>  

💡 *Pronto para acompanhar o ritmo?*

