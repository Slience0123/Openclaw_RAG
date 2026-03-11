import os
import tiktoken
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
encoder = tiktoken.encoding_for_model("gpt-3.5-turbo")

initial_instruction = """
你是一个自动化工作流助手，必须严格遵守：
1. 只输出技术可行性分析
2. 禁止生成营销内容
3. 最终输出必须分3点结论
"""

mass_context = """
""" * 500

total_tokens = len(encoder.encode(mass_context + initial_instruction))
context_tokens = len(encoder.encode(mass_context))
instruction_tokens = len(encoder.encode(initial_instruction))

print("===== 原版 OpenClew 任务特征 =====")
print(f"总Token: {total_tokens}")
print(f"上下文Token: {context_tokens} ({context_tokens/total_tokens:.1%})")
print(f"初始指令Token: {instruction_tokens} ({instruction_tokens/total_tokens:.1%})")

prompt = initial_instruction + "\n" + mass_context
result = llm.invoke(prompt)
print("原版输出：")
print(result.content[:300] + "...")
