from openai import OpenAI
from app.knowledge.retriever import retrieve_context
from app.knowledge.retriever import get_trustpartners_collection

client = OpenAI()

# Permanent Company Context
COMPANY_CONTEXT = """
You are an AI assistant for Trust Partners, a Singapore-based professional services firm.

Company Name:
Trust Partners

Our Services:
- Employment Services
- HR Services
- Consultancy Services

Office Address:
60 Paya Lebar Road
#06-28, Paya Lebar Square
Singapore 409051

Contact Details:
Mobile: +65 8992 2786
Email: contactus@trustpartners.sg

Behavior Rules:
- Always answer professionally and clearly
- If asked about services or contact details, use the information above
- Do not invent services or addresses
- If information is not known, respond cautiously
"""

def chat_with_knowledge(question: str) -> str:
    collection = get_trustpartners_collection()
    context = retrieve_context(collection, question)

    prompt = f"""
            {COMPANY_CONTEXT}

            Retrieved Knowledge (if relevant):
            {context if context.strip() else "No specific retrieved context."}

            User Question:
            {question}
        """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": COMPANY_CONTEXT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
