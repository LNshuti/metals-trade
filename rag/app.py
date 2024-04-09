# create a streamlit rag chatbot to interact with the document index 
# Use an Anthropic Agent over RAG pipeline 

# TODO: 
# 1. Convert code to Streamlit application
# 2. Implement Reranking and evaluation 
# 3. Track metrics and use for optimization 

from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.anthropic import Anthropic
from llama_index.core.agent import FunctionCallingAgentWorker
from llama_index.core.agent import AgentRunner

embed_model = OpenAIEmbedding(api_key="sk-...")
query_llm = Anthropic(model="claude-3-haiku-20240307", api_key="sk-ant-...")

# load data
minerals_docs = SimpleDirectoryReader(
    input_files=["../documents/critical-minerals-africa-senior-study-group-final-report.pdf"]
).load_data()
# build index
minerals_index = VectorStoreIndex.from_documents(
    minerals_docs, embed_model=embed_model
)
minerals_engine = minerals_index.as_query_engine(similarity_top_k=3, llm=query_llm)
query_engine_tool = QueryEngineTool(
    query_engine=minerals_engine,
    metadata=ToolMetadata(
        name="minerals_doc",
        description=(
            "Provides information about Africa's key mineral exports by Country. "
            "Use a detailed plain text question as input to the tool."
        ),
    ),
)

agent_worker = FunctionCallingAgentWorker.from_tools(
    [query_engine_tool], llm=llm, verbose=True
)
agent = AgentRunner(agent_worker)

response = agent.chat("Tell me both the risk factors and tailwinds the United States versus China in Africa's mineral trade?")
print(str(response))

# Reference: LLamaIndex Example Implementation of the ANTHROPIC Agent. https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/agent/anthropic_agent.ipynb
