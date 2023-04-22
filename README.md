# 生成式大语言模型实现人类社会行为仿真模拟

这个库实现了 《Generative Agents: Interactive Simulacra of Human Behavior》这篇论文的简单实现

* 论文地址：https://arxiv.org/abs/2304.03442.
* 论文演示地址：https://reverie.herokuapp.com/arXiv_Demo/

*Read this in [English](README_en.md).*

## 安装

这些模型以notebooks的形式分发，可以很容易地在本地或谷歌Colab上运行。我们建议在本地运行时使用Jupyter Lab。notebooks应该可以直接在谷歌Colab上运行。
在chatGLM文件夹中，我默认填写的是chatGLM本地模型目录，请自行更换

# 如何使用

* 原项目地址： https://github.com/mkturkcan/generative-agents.

* 基于chatGLM运行的中文版本在： https://github.com/VinsonLaro/generative-agents/tree/main/notebook/chatGLM.
* 最稳定的版本在 https://github.com/VinsonLaro/generative-agents/tree/main/notebook/Release.
* 具有最新特性的WIP模型将在 https://github.com/VinsonLaro/generative-agents/tree/main/notebook/WIP.
* WIP库可在 https://github.com/VinsonLaro/generative-agents/tree/main/game_simulation.

## 世界设定

当前设定是一个D&D 5e初级冒险中芬达林小镇。选择这个场景是因为它比原始论文中描述的简单情景更自由。

## 限制

如论文中所述，该模型需要访问高质量的指令模型，如GPT-3。然而，该模型也需要许多高语境查询才能正常工作，这使得运行成本很高。因此，在这项工作中，我们使用低参数、可在本地运行的模型代替。

我们期望随着下一代指令调整模型的出现，这个存储库中的模型将表现更好。

## 未来

* 将代理人决策总结为表情符号。(WIP)
* 创建一组问题以更好地压缩代理上下文。
* 使用另一层提示词检查代理上下文是否压缩得很好。
* 使用chatRWKV中文模型或者其他模型进行推理
* 调整为中式修仙世界观

## 其他

原项目(Release和WIP)默认使用flan-alpaca-xl模型

flan-alpaca-xl(3B)模型进行推理，在3080ti 12G上成功运行,时长约为1-2小时
flan-alpaca-Large(770M)模型进行推理，在3060 6G上成功运行
chatGLM-6B-int4模型进行推理，在3080ti 12G上成功运行,时长约为2-3小时
chatGLM-6B-int4模型进行推理，在3060 6G上成功运行

效果上flan-alpaca-xl(3B)比chatGLM-6B-int4还要好，具体可以比较generative-data目录下的数据
我会尝试使用中文能力更好以及限制更少的模型进行推理