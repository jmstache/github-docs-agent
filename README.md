## 🎯 Final Goal

In this course, the ultimate goal is to build an **AI-powered conversational agent** that can understand and interact with your GitHub repositories.  

Think of it as your personal **AI assistant for documentation and code**:  
- Ask questions like *“How do I set up this project?”* or *“Where is the deployment script?”*  
- Get instant answers, with context pulled from the repo’s docs and source files.  
- Similar to **DeepWiki**, but tailored specifically to your GitHub repo.  

The script you see here is just **Step 1: Ingestion**.  
Next, we’ll move on to preprocessing, vectorization, and building a retrieval-augmented chatbot.

---

# GitHub Repo Markdown Parser

This is a simple Python script that downloads and parses all Markdown (`.md` / `.mdx`) files from any public GitHub repository.  
It extracts both the **content** and **frontmatter metadata** from the files, which can be useful for building documentation search tools, knowledge bases, or AI agent pipelines.

---

## ✨ Features
- Downloads repositories as ZIP archives from GitHub
- Unzips the repository contents
- Scans for Markdown files
- Parses **YAML frontmatter** metadata using [`python-frontmatter`](https://github.com/eyeseast/python-frontmatter)
- Prints out the number of parsed documents

---

## 🚀 Usage

### 1. Install dependencies (using [uv](https://github.com/astral-sh/uv))
If you don’t already have `uv` installed:

```bash
pip install uv
```

Then install the dependencies into an isolated environment:

```bash
uv init
uv add requests python-frontmatter
uv add --dev jupyter
```

### 2. Run the script
Run the script from the command line:

```bash
uv run main.py <repo_owner> <repo_name> [--branch <branch_name>]
```

- `<repo_owner>` → GitHub username or organization  
- `<repo_name>` → Repository name  
- `--branch` (optional) → Branch name, defaults to `main`  

#### Examples

Download the [DataTalksClub/faq](https://github.com/DataTalksClub/faq) repository (default branch `main`):

```bash
uv run script.py DataTalksClub faq
```

Download the [DataTalksClub/machine-learning-zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) repo, specifying the `master` branch:

```bash
uv run script.py DataTalksClub machine-learning-zoomcamp --branch master
```

---

## 📂 Output
The script prints the number of Markdown documents found:

```
Documents from DataTalksClub/machine-learning-zoomcamp: 42
```

Internally, each document is stored as a dictionary with:
- `content` → the Markdown body  
- `metadata` → parsed frontmatter (if present)  
- `filename` → the file path inside the repository  

---

## 🧑‍💻 About This Project
This script is adapted from the **AI Agents Crash Course** by [Alexey Grigorev](https://twitter.com/Al_Grigor).  

🚀 Day 1 of the course focuses on building a data ingestion pipeline that can:
- ✅ Download repos as zip archives  
- ✅ Parse frontmatter metadata  
- ✅ Extract content from Markdown files  

Next step: **chunking the data** for better search and retrieval performance!  

If you want to follow along with the course, you can sign up here:  
👉 [https://alexeygrigorev.com/aihero/](https://alexeygrigorev.com/aihero/)

---

## 📜 License
MIT License – feel free to use and adapt.
