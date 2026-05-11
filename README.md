# Oracle HCM Recruiting Cloud — RAG Assistant

A domain-specific Retrieval-Augmented Generation (RAG) system built over Oracle HCM Cloud's official Recruiting module documentation. Enables consultants and administrators to query 1,500+ pages of Oracle Recruiting documentation using natural language.

## What It Does
Instead of searching through hundreds of pages of Oracle documentation, consultants can ask plain English questions and get precise, sourced answers instantly.

**Example questions it can answer:**
- "How do I configure a career site for multiple languages?"
- "What roles are needed to approve a job offer?"
- "How does candidate selection process automation work?"
- "What is the difference between a disqualification question and a prescreening question?"
- "How does a recruiter fill a requisition automatically?"

## Knowledge Base
Built from two official Oracle guides (2026):
- **Implementing Recruiting** — 1,123 chunks — system configuration and setup
- **Using Recruiting** — 412 chunks — recruiter and end-user operations
- **Total:** 1,527 semantic chunks across 35 modules

## Tech Stack
- Python 3.11+
- OpenAI API (text-embedding-3-small + gpt-4o-mini)
- ChromaDB (local vector database)
- Streamlit (chat interface)

## Project Structure
oracle-hcm-recruiting-rag/
├── data/
│   ├── oracle_hcm_recruiting_rag_chunks.json
│   ├── oracle_hcm_recruiting_rag.md
│   ├── oracle_hcm_using_recruiting_rag_chunks.json
│   └── oracle_hcm_using_recruiting_rag.md
├── src/
│   ├── ingest.py
│   └── app.py
├── requirements.txt
└── README.md
## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/YOUR-USERNAME/oracle-hcm-recruiting-rag.git
cd oracle-hcm-recruiting-rag
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your OpenAI API key
Create a `.env` file in the root folder:
OPENAI_API_KEY=sk-proj-your-key-here
### 5. Build the vector database
```bash
python src/ingest.py
```

### 6. Launch the app
```bash
streamlit run src/app.py
```

Open http://localhost:8501 in your browser.

## Disclaimer
This project uses knowledge derived from Oracle's publicly available documentation for educational and portfolio purposes. All Oracle product names and trademarks belong to Oracle Corporation. Source: docs.oracle.com
