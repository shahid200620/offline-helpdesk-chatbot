\## Introduction



This project is about building an offline customer support chatbot using Ollama and Llama 3.2. The goal is to test how well a local model can handle customer queries without using any external APIs.



\---



\## Methodology



I created 20 customer queries related to an e-commerce store. These queries are simple and based on real customer issues like order tracking, payments, and returns.



Two prompting methods were used:

\- Zero-shot prompting

\- One-shot prompting



Zero-shot means asking directly without examples.  

One-shot means giving one example before asking the question.



The responses were evaluated based on:

\- Relevance

\- Coherence

\- Helpfulness



Each was scored from 1 to 5.



\---



\## Results and Analysis



After checking all responses, I noticed that one-shot prompting performs better in most cases.



Zero-shot responses were sometimes incomplete or unclear. In some cases, it even returned errors or very basic answers.



One-shot responses were more structured and helpful. The example in the prompt helped the model understand how to respond better.



For example, in queries like order tracking and returns, one-shot gave more complete answers compared to zero-shot.



\---



\## Conclusion



The local Llama 3.2 model works reasonably well for basic customer support tasks. It can answer common queries clearly, especially when guided properly.



However, it has some limitations like occasional errors and lack of real-time data.



Overall, one-shot prompting improves performance and makes responses more useful.



\---



\## Limitations



\- No access to real order data

\- Sometimes gives incomplete answers

\- Slow response time on local machine

