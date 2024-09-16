import openai
import os
from langchain_openai import ChatOpenAI  # Updated import
from langchain.chains import ConversationChain, LLMChain
from langchain_core.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

# Set the OpenAI API key
OPENAI_API_KEY="<MY-KEY>"
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

# Initialize the OpenAI chat model with the latest OpenAI API
llm = ChatOpenAI(temperature=0.7, model="gpt-4")  # Use "gpt-4" or "gpt-3.5-turbo" 

memory = ConversationBufferMemory()

def generate_response(prompt_template, user_input):
    # Create the LLMChain with the prompt template and memory
    product_chain = LLMChain(
        llm=llm,
        prompt=prompt_template,
        memory=memory
    )
    # Run the LLMChain with the user input and get the response
    response = product_chain.run(user_input)
    return response