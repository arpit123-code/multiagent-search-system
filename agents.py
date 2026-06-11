from langchain.agents import create_agent

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from tools import web_search, fetch_full_content
load_dotenv()
llm =ChatOllama(model="gemma4:e4b")

def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search],
    )

def build_read_agent():
    return create_agent(
        model=llm,
        tools=[fetch_full_content],
        system_prompt="""
You are a research assistant.

From the given text:
1. Extract ONLY ONE valid URL
2. The URL MUST belong to economictimes.indiatimes.com
3. Call the fetch_full_content tool with that URL

DO NOT guess URLs
DO NOT generate URLs
ONLY use URLs present in the input
"""
    )
    

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
Sources:
- Use ONLY the URLs provided below.
- List them clearly.
- Do NOT say "no URLs".

Be detailed, factual and professional."""),
])

writer_chain=writer_prompt|llm|StrOutputParser()

critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain=critic_prompt|llm|StrOutputParser()