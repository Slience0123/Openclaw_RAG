# RAG-enhanced OpenClew Workflow Optimization

## 项目简介
本项目针对OpenClew智能体框架在复杂任务执行中的核心痛点：
- 背景上下文占比约95%，初始核心指令仅占5%，智能体易遗忘初始需求
- 海量上下文输入导致token消耗高、模型响应慢、输出准确率低

结合RAG（检索增强生成）技术与自动化工作流生成研究方向，实现动态上下文总结与压缩模块，构建轻量化、高准确率的智能体执行流程。

## 核心创新
1. **RAG动态上下文优化**：在关键执行步骤通过向量检索+动态总结，替代海量上下文直接输入
2. **初始指令强绑定**：解决智能体执行过程中需求遗忘问题，保障输出一致性
3. **效率双提升**：显著降低token消耗，提升模型响应速度与任务执行准确率

## 技术栈
- **核心框架**：LangChain、OpenClew
- **向量数据库**：Chroma
- **大模型**：GPT-3.5-turbo
- **开发语言**：Python

## 文件结构
```plaintext
├── .env                # 环境变量配置（OpenAI API Key）
├── openclew_baseline.py # 复现原版OpenClew上下文爆炸痛点
├── rag_optimizer.py    # RAG动态上下文优化核心模块
├── compare_test.py     # 优化前后对比实验脚本
├── requirements.txt    # 项目依赖包
└── research_report.md  # 项目研究简报
