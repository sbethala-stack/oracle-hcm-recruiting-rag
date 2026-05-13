# Oracle HCM Recruiting Cloud — RAG Assistant

A domain-specific Retrieval-Augmented Generation (RAG) system built over Oracle HCM Cloud's official Recruiting module documentation. Enables consultants and administrators to ask natural language questions and get precise, sourced answers — without reading 650+ pages of Oracle documentation.

---

## The Problem It Solves

Oracle Recruiting Cloud implementation projects involve two dense official guides totalling 650+ pages. During a live implementation, a consultant who needs to know — right now — how to configure a career site for multiple languages, or which roles are required to approve a job offer, has to manually search through hundreds of pages to find the answer.

This assistant answers those questions in seconds, citing the exact Oracle source.

---

## Knowledge Base

Built from two official Oracle Fusion Cloud Talent Management guides (2026):

| Guide | Purpose | Pages | Chunks |
|-------|---------|-------|--------|
| Implementing Recruiting (G34431-09) | System configuration and setup for implementors | 450 | 1,123 |
| Using Recruiting (G34440-07) | Day-to-day recruiter and end-user operations | 218 | 412 |
| **Total** | | **668** | **1,527** |

Both guides are unified into a single vector database so every query searches across configuration and operational content simultaneously.

**Author of both guides:** Viviane Filloles, Oracle Corporation

---

## Example Questions It Can Answer

- "How do I configure a career site for multiple languages?"
- "What roles and privileges are needed to approve a job offer?"
- "How does candidate selection process automation work?"
- "What is the difference between a disqualification question and a prescreening question?"
- "How do I enable LinkedIn Apply on a career site?"
- "What happens when a candidate accepts a job offer?"
- "How does a recruiter fill a requisition automatically?"
- "How do I set up interview scheduling with Microsoft Teams?"

---

## How It Works

When a user asks a question, six things happen in sequence:

1. The question is sent to OpenAI and converted into a vector (1,536 numbers representing its meaning)
2. That vector is compared against all 1,527 stored chunk vectors in ChromaDB locally on the machine
3. The 5 most semantically similar chunks are retrieved
4. Those chunks are assembled into a prompt alongside the original question
5. GPT-4o-mini reads the chunks and writes a synthesized answer in plain English
6. The answer is displayed with source citations (chapter, section, chunk ID, link to docs.oracle.com)

GPT never sees the full knowledge base — only the 5 retrieved chunks. This keeps answers grounded in actual Oracle documentation and prevents hallucination.

---

## Project Structure

```
oracle-hcm-recruiting-rag/
│
├── data/
│   ├── oracle_hcm_recruiting_rag_chunks.json         # Implementing Recruiting — 1,123 chunks
│   ├── oracle_hcm_recruiting_rag.md                  # Implementing Recruiting — full markdown
│   ├── oracle_hcm_using_recruiting_rag_chunks.json   # Using Recruiting — 412 chunks
│   └── oracle_hcm_using_recruiting_rag.md            # Using Recruiting — full markdown
│
├── src/
│   ├── ingest.py        # Loads both guides into ChromaDB vector database
│   └── app.py           # Streamlit chat interface
│
├── .env                 # Your OpenAI API key (never committed to GitHub)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Chunk Format

Each chunk in the JSON files contains:

```json
{
  "chunk_id": "OHR-REC-0089",
  "chapter": "Career Sites",
  "section": "Configure Language Settings",
  "content": "To support multiple languages on a career site, administrators must first enable...",
  "guide": "Implementing Recruiting",
  "source": "Oracle HCM Cloud Implementing Recruiting (2026)"
}
```

Chunk ID prefixes:
- `OHR-REC-XXXX` — Implementing Recruiting guide
- `OHR-USE-XXXX` — Using Recruiting guide

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11+ | Core language |
| OpenAI `text-embedding-3-small` | Converts text to semantic vectors |
| OpenAI `gpt-4o-mini` | Generates answers from retrieved chunks |
| ChromaDB | Local vector database — stores and searches 1,527 chunk vectors |
| Streamlit | Browser-based chat interface |
| python-dotenv | Manages API key securely via .env file |

Total cost to build and run: approximately $0.20 for ingestion, ~$0.001 per query.

---

## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/YOUR-USERNAME/oracle-hcm-recruiting-rag.git
cd oracle-hcm-recruiting-rag
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv

# Mac / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your OpenAI API key
Create a `.env` file in the root folder:
```
OPENAI_API_KEY=sk-proj-your-key-here
```
Get a key at https://platform.openai.com/api-keys. Add $5 credit — this project uses less than $0.25 total.

### 5. Build the vector database
```bash
python src/ingest.py
```
This embeds all 1,527 chunks and stores them in ChromaDB locally. Takes 3-5 minutes, runs once.

### 6. Launch the app
```bash
streamlit run src/app.py
```
Opens automatically at http://localhost:8501.

---

## Chapters Covered

### Implementing Recruiting (1,123 chunks)
Overview of Recruiting, Career Sites, Job Application Flows, Candidate Selection Processes, Recruiting Content Library, Notifications, Candidate Messaging, Job Requisition Templates, Job Requisitions, Prescreening Questionnaires, Candidate Interviews, Interview Feedback, Candidates and Candidate Job Applications, Candidate Pools, Talent Community, Candidate Sources, Candidate Referrals, Recruiting Campaigns, Recruiting Agencies, Job Offer Letter Templates, Job Offers, Grid Views, Recruiting Activity Center, Oracle AI Apps in Recruiting, Dynamic Skills, Opportunity Marketplace, Lookups, Geography Hierarchies, Fast Formulas, Candidate Data Archiving, Third Party Integration, Scheduled Processes, Security for Recruiting, Personalization

### Using Recruiting (412 chunks)
Overview of Recruiting, Job Requisitions, Job Requisition Posting and Sourcing, Prescreening Questionnaires, Screening Services, Candidate Search, Prospects and Candidates, Candidate Job Applications, Candidate Pools and Talent Community, Recruiting Campaigns, Recruiting Agencies, Candidate Selection Processes, Candidate Interviews, Interview Feedback, Job Offers, Opportunity Marketplace

---

## Disclaimer

This project uses knowledge derived from Oracle's publicly available documentation for educational and portfolio purposes. All Oracle product names and trademarks belong to Oracle Corporation. Source: [docs.oracle.com](https://docs.oracle.com/en/cloud/saas/talent-management/)