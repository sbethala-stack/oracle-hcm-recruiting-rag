# Oracle HCM Recruiting — RAG Knowledge Base

## Project Overview
This project implements a **Retrieval-Augmented Generation (RAG)** system over Oracle HCM Cloud's Recruiting module documentation. The goal is to enable natural-language querying of the Oracle HCM Implementing Recruiting guide — allowing HR admins, implementors, and business analysts to get precise, context-aware answers without reading 450 pages of documentation.

## Source Document
- **Title:** Oracle Fusion Cloud Talent Management — Implementing Recruiting  
- **Version:** G34431-09 (2026)  
- **Pages:** 450  
- **Author:** Viviane Filloles, Oracle Corporation

## Repository Structure
```
oracle-hcm-recruiting-rag/
│
├── data/
│   ├── oracle_hcm_recruiting_rag.md          # Humanized full-text (Markdown, ~1MB)
│   └── oracle_hcm_recruiting_rag_chunks.json # Structured chunks with metadata (JSON)
│
├── notebooks/
│   └── rag_pipeline.ipynb                    # End-to-end RAG demo (to be added)
│
├── src/
│   └── ingest.py                             # Chunk loading + embedding script (to be added)
│
└── README.md
```

## Data Format

### JSON Chunks (`oracle_hcm_recruiting_rag_chunks.json`)
Each chunk contains:
```json
{
  "chunk_id": "OHR-REC-0051",
  "chapter": "Career Sites",
  "section": "Configure a Career Site",
  "content": "You configure external career sites by enabling and configuring different options...",
  "source": "Oracle HCM Cloud Implementing Recruiting (2026)"
}
```

### Markdown (`oracle_hcm_recruiting_rag.md`)
Full document organized by chapter with section headers, suitable for direct ingestion into vector stores.

## Stats
- **Total chunks:** 1,191
- **Chapters covered:** 35
- **Avg chunk size:** ~720 characters
- **Format:** Semantic sections aligned to Oracle's documentation structure

## Chapters Covered
| # | Chapter | Chunks |
|---|---------|--------|
| 1 | Overview of Recruiting | 48 |
| 2 | Career Sites | 216 |
| 3 | Job Application Flows | 69 |
| 4 | Candidate Selection Processes | 57 |
| 5 | Recruiting Content Library | 34 |
| 6 | Notifications | 23 |
| 7 | Candidate Messaging | 1 |
| 8 | Job Requisition Templates | 21 |
| 9 | Job Requisitions | 98 |
| 10 | Prescreening Questionnaires and Questions | — |
| 11 | Candidate Interviews | 44 |
| 12 | Interview Feedback Questionnaires | — |
| 13 | Candidates and Candidate Job Applications | 69 |
| 14 | Candidate Pools | 10 |
| 15 | Talent Community | 6 |
| 16 | Candidate Sources | 24 |
| 17 | Candidate Referrals | 4 |
| 18 | Recruiting Campaigns | 11 |
| 19 | Recruiting Agencies | 12 |
| 20 | Job Offer Letter Templates | 29 |
| 21 | Job Offers | 126 |
| 22 | Grid Views | 8 |
| 23 | Recruiting Activity Center | 62 |
| 24 | Recruiting Features Configuration Report | — |
| 25 | Oracle AI Apps in Recruiting | — |
| 26 | Dynamic Skills in Recruiting | — |
| 27 | Opportunity Marketplace | 36 |
| 28–35 | Lookups, Geography, Security, etc. | 100+ |

## RAG Pipeline (Planned)
1. **Embed** chunks using `text-embedding-3-small` (OpenAI) or `nomic-embed-text` (local)
2. **Store** in a vector DB — ChromaDB (local) or Pinecone (cloud)
3. **Query** via LangChain or LlamaIndex with a Claude/GPT backbone
4. **Answer** with cited chunk IDs for traceability

## Use Cases
- "How do I configure a career site for multiple languages?"
- "What roles are needed to approve a job offer?"
- "How does the candidate selection process automation work?"
- "What is the difference between a disqualification question and a prescreening question?"
- "How do I enable LinkedIn Apply on a career site?"

## Tech Stack (Planned)
- Python 3.11+
- LangChain or LlamaIndex
- ChromaDB / Pinecone
- OpenAI or Anthropic API
- Streamlit (demo UI)

## Author
Built as part of a portfolio project combining ERP domain expertise (Oracle HCM) with modern AI/RAG architecture.