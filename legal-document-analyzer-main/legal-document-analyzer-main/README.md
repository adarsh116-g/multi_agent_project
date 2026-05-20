# Intelligent Legal Document Analyzer

An AI-powered system that reads any legal contract PDF and automatically extracts key information, detects risky clauses, summarizes it in plain English, and generates a professional analysis report.

---

## What It Does
- Extracts full text from any legal PDF contract
- Identifies key entities — people, organizations, dates, money, and laws
- Classifies every clause as High Risk, Caution, or Safe with detailed explanation
- Summarizes the entire contract in simple plain English (no legal jargon)
- Answers any question about the document using a RAG-based Q&A chatbot
- Generates a downloadable professional PDF analysis report

---

## Technologies Used
| Tool | Purpose |
|------|---------|
| Google Colab (T4 GPU) | Cloud-based development and execution environment |
| pdfplumber | Extracts raw text from PDF files page by page |
| spaCy (en_core_web_sm) | Named Entity Recognition for legal entities |
| Hugging Face bart-large-mnli | Zero-shot classification for risk detection |
| Sentence Transformers (all-MiniLM-L6-v2) | Converts text to embeddings for semantic search |
| ChromaDB | Vector database for storing and searching document chunks |
| Groq API (Free) | LLM-powered summarization and Q&A chatbot |
| fpdf2 | Generates the final professional PDF report |



## How It Works
Legal PDF Contract
|
v
PDF Text Extraction (pdfplumber)
|
v
Named Entity Recognition (spaCy)
|
v
Risk Clause Classification (bart-large-mnli)
|
v
Plain English Summary (Groq API)
|
v
Q&A Chatbot (ChromaDB + Groq RAG Pipeline)
|
v
Professional PDF Report (fpdf2)

---

## How to Run
1. Open `legalanalyzer.ipynb` in Google Colab
2. Set runtime to T4 GPU (Runtime > Change Runtime Type)
3. Add your `GROQ_API_KEY` to Colab Secrets
4. Upload a legal PDF to your Google Drive documents folder
5. Run all cells in order from top to bottom

---

## Sample Output
Tested on a real Chase Bank Affiliate Agreement:
- 3 High Risk clauses detected (Indemnification Obligation, IP Theft, Excessive Liability Limitation)
- 1 Caution clause detected (Contractual Liability)
- Key entities extracted including organizations, dates, monetary values and legal references
- Full plain English summary generated explaining the contract in simple terms
- Professional PDF report downloaded successfully

---

## Challenges Solved During Development
- Original guide used paid Claude API — switched to free Groq API without breaking anything
- ChromaDB crashed with disk I/O error on Google Drive — fixed by using local Colab storage
- Colab session resets lost all variables — learned to re-run cells and maintain variable consistency
- fpdf2 newer version deprecated Arial font and ln parameter — updated to Helvetica and new_x/new_y syntax
- Emoji characters broke PDF latin-1 encoding — replaced with plain text labels

---

## Author
**Uday Mahaal**
Computer Science Student at Galgotias University
Built entirely using free and open-source tools.
GitHub: https://github.com/1545384241
