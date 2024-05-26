import os
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain.agents import tool
from langchain.chains.conversation.base import ConversationChain
from langchain.memory import ConversationBufferMemory

nvapi_key = os.getenv("NVIDIA_API_KEY")
if not nvapi_key:
    raise ValueError("NVIDIA API Key is not set")

llm = ChatNVIDIA(model="mistralai/mixtral-8x7b-instruct-v0.1")

# Define tools
@tool
def get_word_length(word: str) -> int:
    """Returns the length of a word."""
    return len(word)

tools = [get_word_length]

# Create a single conversation chain with memory
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

def get_chatbot_response(prompt):
    # Get response from the bot
    result = conversation.invoke(prompt)
    # Update memory buffer
    return result['response']
