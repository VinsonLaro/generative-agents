# Generative Large Language Models for Human-Like Behavior

This repository includes a working version of the type of model described in Generative Agents: Interactive Simulacra of Human Behavior.

* paper：https://arxiv.org/abs/2304.03442.
* paper demo：https://reverie.herokuapp.com/arXiv_Demo/

## setup

The models are distributed as notebooks that are easy to run locally, or on Google Colab. We recommend the use of Jupyter Lab if running locally. The notebook(s) should work as-is on Google Colab.
notebooks in the chatGLM folder, I default to the chatGLM local model directory, which you need to replace

# How to Use

* forked from： https://github.com/mkturkcan/generative-agents.

* The Chatglm model Chinese version is at https://github.com/VinsonLaro/generative-agents/tree/main/notebook/chatGLM.
* The most stable model is available at https://github.com/VinsonLaro/generative-agents/tree/main/notebook/Release.
* WIP models with the latest features will be available in https://github.com/VinsonLaro/generative-agents/tree/main/notebook/WIP.
* A WIP library is available under https://github.com/VinsonLaro/generative-agents/tree/main/game_simulation.


## Model


The current model is a simulation of the town of Phandalin from an introductory D&D 5e adventure. This setting is chosen as it is much more free form than the simple scenario described in the original paper.

## Limitations

The model, as described in the paper, requires access to a very high quality instruction model such as GPT-3. However, the model also requires many high-context queries to work, making it expensive to run. As such, in this work we use low-parameter, locally runnable models instead. 

We expect that with the advent of the next generation of instruction-tuned models, the model in this repo will perform better.

## Future Steps

* Summarize agent decisions as emojis. (WIP)
* Create a family of questions to compress agent contexts better.
* Check if the agent contexts are compressed well with an another layer of prompts.
* Inference can be performed using the chatRWKV Chinese model or other models.
* Adjust to a Chinese-style worldview.

## Others

The original project (Release and WIP) uses the flan-alpaca-xl model by default.

Inference with the flan-alpaca-xl (3B) model was successful on a 3080ti 12G, with a runtime of approximately 1-2 hours.
Inference with the flan-alpaca-Large (770M) model was successful on a 3060 6G.
Inference with the chatGLM-6B-int4 model was successful on a 3080ti 12G, with a runtime of approximately 2-3 hours.
Inference with the chatGLM-6B-int4 model was also successful on a 3060 6G.

In terms of performance, the flan-alpaca-xl (3B) model is better than the chatGLM-6B-int4 model.  Specific comparisons can be made by comparing the data in the generative-data directory.
We will try to use models with better Chinese proficiency and fewer limitations for inference.