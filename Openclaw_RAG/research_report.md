# RAG-enhanced OpenClew Workflow Optimization 研究简报
申请人：XXX
申请ID：XXX
项目：MSc Agentic AI Systems

## 1. 研究问题
OpenClew 在复杂任务中上下文占比 ~95%，初始指令占比 ~5%，导致智能体执行过程中遗忘核心需求，输出偏差大、Token 消耗高。

## 2. 创新方案
基于 RAG 实现关键步骤动态上下文总结与检索增强，保留初始指令，压缩冗余信息。

## 3. 实验结果
- Token 消耗降低：60%~80%
- 响应速度提升：约40%
- 输出更贴合初始约束，任务准确率明显提升

## 4. 技术栈
LangChain / Chroma / GPT-3.5-turbo / Python
