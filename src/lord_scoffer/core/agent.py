from langchain_openai import ChatOpenAI
from prompts import build_prompt
from config.settings import settings

def build_response(message: str):
    # Initialize the ChatOpenAI model with the specified settings
    llm = ChatOpenAI(
        temperature=settings.TEMPERATURE,
        model=settings.MODEL_NAME,
        api_key=settings.OPENAI_API_KEY
    )

    # Build the prompt using the provided message
    prompt = build_prompt(message)

    # Generate a response using the OpenAI API
    chain = prompt | llm
    response = chain.invoke({
        "input": message
    })

    return response.content