import os
import chromadb
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Page config
st.set_page_config(
    page_title="Oracle HCM Recruiting Assistant",
    page_icon="🔷",
    layout="wide"
)

st.title("🔷 Oracle HCM Recruiting — Implementation Assistant")
st.markdown(
    "Ask any question about implementing Oracle Recruiting Cloud. "
    "Answers are grounded in the official Oracle implementation guide."
)
st.divider()

# Load the vector database
@st.cache_resource
def load_db():
    chroma_client = chromadb.PersistentClient(path=".chroma")
    return chroma_client.get_collection(name="oracle_recruiting")

try:
    collection = load_db()
except Exception as e:
    st.error(f"Database error: {e}")
    st.stop()

def search_knowledge_base(query, n_results=5):
    """Find the most relevant chunks for the query."""
    response = client.embeddings.create(
        input=[query],
        model="text-embedding-3-small"
    )
    query_embedding = response.data[0].embedding

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        include=["documents", "metadatas", "distances"]
    )
    return results

def generate_answer(query, results):
    """Generate a grounded answer using retrieved chunks."""
    chunks_text = ""
    sources = []
    for i, (doc, meta) in enumerate(
        zip(results["documents"][0], results["metadatas"][0])
    ):
        chunks_text += f"\n\n[Chunk {i+1} — {meta['chapter']} > {meta['section']}]\n{doc}"
        sources.append(meta)

    system_prompt = """You are an expert Oracle HCM Recruiting Cloud implementation consultant assistant.
Your job is to help consultants and administrators implement Oracle Recruiting Cloud for their clients.

Answer questions based ONLY on the provided knowledge base chunks.
Be practical, precise, and structured. Use numbered steps when explaining procedures.
Always end your answer with a "Sources" section listing which chapters/sections you referenced.
If the chunks don't contain enough information, say so clearly.
Do not invent configuration steps or feature names."""

    user_prompt = f"""Question: {query}

Knowledge Base Excerpts:
{chunks_text}

Provide a clear, practical answer for an Oracle Recruiting Cloud implementor."""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.1,
        max_tokens=1200
    )
    return response.choices[0].message.content, sources

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Suggested questions for new users
if not st.session_state.messages:
    st.markdown("**Try asking:**")
    suggestions = [
        "How do I configure a career site for multiple languages?",
        "What roles and privileges are needed to approve a job offer?",
        "How does candidate selection process automation work?",
        "What is the difference between a disqualification question and a prescreening question?",
        "How do I enable LinkedIn Apply on a career site?",
        "What are the steps to set up interview scheduling with Microsoft Teams?",
    ]
    cols = st.columns(2)
    for i, suggestion in enumerate(suggestions):
        if cols[i % 2].button(suggestion, key=f"sug_{i}"):
            st.session_state.messages.append(
                {"role": "user", "content": suggestion}
            )
            with st.chat_message("user"):
                st.markdown(suggestion)
            with st.chat_message("assistant"):
                with st.spinner("Searching knowledge base..."):
                    results = search_knowledge_base(suggestion)
                    answer, sources = generate_answer(suggestion, results)
                st.markdown(answer)
                with st.expander("📚 View source chunks used"):
                    for j, meta in enumerate(sources):
                        st.markdown(
                            f"**{j+1}. {meta['chapter']} → {meta['section']}**  \n"
                            f"*{meta['source']}*  \n"
                            f"[Oracle Documentation](https://docs.oracle.com/en/cloud/saas/talent-management/)"
                        )
            st.session_state.messages.append({"role": "assistant", "content": answer})
            st.rerun()

# Chat input
if prompt := st.chat_input("Ask about Oracle Recruiting Cloud implementation..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Searching knowledge base..."):
            results = search_knowledge_base(prompt)
            answer, sources = generate_answer(prompt, results)
        st.markdown(answer)

        # Show sources in expander
        with st.expander("📚 View source chunks used"):
            for i, meta in enumerate(sources):
                st.markdown(
                    f"**{i+1}. {meta['chapter']} → {meta['section']}**  \n"
                    f"*{meta['source']}*  \n"
                    f"[Oracle Documentation](https://docs.oracle.com/en/cloud/saas/talent-management/)"
                )

    st.session_state.messages.append({"role": "assistant", "content": answer})