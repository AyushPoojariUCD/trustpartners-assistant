from agents import Agent, Runner
from app.knowledge.retriever import retrieve_context, get_trustpartners_collection
from app.knowledge.guardrails import is_disallowed_question, guardrail_response


# Trust Partners Company Context
TRUST_PARTNERS_CONTEXT = """
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


# Trust Partners Agent
trustpartners_agent = Agent(
    name="TrustPartnersAssistant",
    instructions=TRUST_PARTNERS_CONTEXT,
    model="gpt-4o-mini"
)


# Agent-powered RAG chat
async def chat_with_knowledge(question: str) -> str:
    # Guardrail check
    if is_disallowed_question(question):
        return guardrail_response()

    # Retrieve RAG context
    collection = get_trustpartners_collection()
    context = retrieve_context(collection, question)

    # Inject retrieved knowledge into agent input
    agent_input = f"""
                    Retrieved Knowledge (if relevant):
                    {context if context.strip() else "No specific retrieved context."}

                    User Question:
                    {question}
                """

    # Run agent
    result = await Runner.run(
        trustpartners_agent,
        agent_input,
    )

    return result.final_output
