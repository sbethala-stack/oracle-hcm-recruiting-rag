import json
import os
import chromadb
from openai import OpenAI
from dotenv import load_dotenv

print("Step 1: Loading environment...")
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("ERROR: OPENAI_API_KEY not found in .env file")
    exit()
print(f"Step 2: API key loaded ({api_key[:10]}...)")

# ── Load both guides ──────────────────────────────────────────────────────────
print("Step 3: Loading chunks from both guides...")

all_chunks = []

guide_files = [
    "data/oracle_hcm_recruiting_rag_chunks.json",       # Implementing Recruiting
    "data/oracle_hcm_using_recruiting_rag_chunks.json", # Using Recruiting
]

for filepath in guide_files:
    if not os.path.exists(filepath):
        print(f"  WARNING: {filepath} not found — skipping")
        continue
    with open(filepath, "r") as f:
        chunks = json.load(f)
    # Filter very short chunks
    chunks = [c for c in chunks if len(c["content"]) >= 100]
    guide_name = chunks[0].get("guide", "Unknown") if chunks else filepath
    print(f"  Loaded {len(chunks)} chunks from: {guide_name}")
    all_chunks.extend(chunks)

print(f"Step 4: {len(all_chunks)} total chunks ready across both guides")

# ── Connect to ChromaDB ───────────────────────────────────────────────────────
print("Step 5: Connecting to ChromaDB...")
chroma_client = chromadb.PersistentClient(path=".chroma")
collection = chroma_client.get_or_create_collection(name="oracle_recruiting")
print("Step 6: ChromaDB connected")

existing = collection.count()
if existing > 0:
    print(f"Database already has {existing} chunks.")
    print("To re-ingest from scratch, delete the .chroma folder and run again.")
else:
    print("Step 7: Starting embeddings — this takes 3-5 minutes...")
    client = OpenAI(api_key=api_key)
    batch_size = 50

    for i in range(0, len(all_chunks), batch_size):
        batch = all_chunks[i : i + batch_size]
        texts  = [c["content"] for c in batch]
        ids    = [c["chunk_id"] for c in batch]
        metadatas = [
            {
                "chapter": c.get("chapter", ""),
                "section": c.get("section", ""),
                "guide":   c.get("guide", "Implementing Recruiting"),
                "source":  c.get("source", "Oracle HCM Cloud Recruiting (2026)")
            }
            for c in batch
        ]

        response = client.embeddings.create(
            input=texts,
            model="text-embedding-3-small"
        )
        embeddings = [r.embedding for r in response.data]

        collection.add(
            documents=texts,
            embeddings=embeddings,
            ids=ids,
            metadatas=metadatas
        )
        print(f"  Stored {min(i + batch_size, len(all_chunks))}/{len(all_chunks)} chunks")

    print(f"\nDone! Database is ready with {len(all_chunks)} chunks from both guides.")