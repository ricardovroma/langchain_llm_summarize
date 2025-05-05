import os

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chat_models import init_chat_model
from langchain.docstore.document import Document
from langchain_core.prompts import ChatPromptTemplate

from src.config import settings

# Threshold for determining large vs small text (in characters)
LARGE_TEXT_THRESHOLD = 1000

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = settings.get("OPENAI_API_KEY")


def summarize_small_text(text: str) -> str:
    docs = [Document(page_content=text)]

    llm = init_chat_model(settings.get("LLM_MODEL"), model_provider="openai")

    prompt = ChatPromptTemplate.from_template("Provide a brief summary of this short content: {context}")
    chain = create_stuff_documents_chain(llm, prompt)
    return chain.invoke({"context": docs})


def summarize_large_text(text: str) -> str:
    docs = [Document(page_content=text)]

    llm = init_chat_model(settings.get("LLM_MODEL"), model_provider="openai")

    prompt = ChatPromptTemplate.from_template(
        "Summarize this lengthy content in a comprehensive way. "
        "Focus on the main points and key details: {context}"
    )
    chain = create_stuff_documents_chain(llm, prompt)
    return chain.invoke({"context": docs})