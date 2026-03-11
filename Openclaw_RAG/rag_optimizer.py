import os
import tiktoken
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
embedding = OpenAIEmbeddings()
encoder = tiktoken.encoding_for_model("gpt-3.5-turbo")

class RAGContextOptimizer:
    def __init__(self):
        self.db = Chroma(embedding_function=embedding)
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)

    def build_knowledge_base(self, long_text):
        chunks = self.splitter.split_text(long_text)
        self.db.add_texts(chunks)

    def dynamic_retrieve_summary(self, query, top_k=3):
        docs = self.db.similarity_search(query, k=top_k)
        context = "\n".join([doc.page_content for doc in docs])
        summary_prompt = f"请精简总结以下内容，保留核心事实，不超过200字：{context}"
        summary = llm.invoke(summary_prompt).content
        return summary

if __name__ == "__main__":
    initial_instruction = """
    必须严格遵守：
    1. 只输出技术可行性分析
    2. 禁止生成营销内容
    3. 最终输出分3点结论
    """

    mass_context = """
    """ * 500

    optimizer = RAGContextOptimizer()
    optimizer.build_knowledge_base(mass_context)

    optimized_context = optimizer.dynamic_retrieve_summary(initial_instruction)
    optimized_prompt = initial_instruction + "\n关键上下文摘要:\n" + optimized_context

    optimized_tokens = len(encoder.encode(optimized_prompt))
    original_tokens = len(encoder.encode(initial_instruction + mass_context))

    print("===== RAG优化后 =====")
    print(f"优化前Token: {original_tokens}")
    print(f"优化后Token: {optimized_tokens}")
    print(f"Token减少: {(original_tokens - optimized_tokens)/original_tokens:.1%}")

    res = llm.invoke(optimized_prompt)
    print("\n优化后输出：")
    print(res.content)
