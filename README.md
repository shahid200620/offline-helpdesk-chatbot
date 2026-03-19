## Offline Helpdesk Chatbot

This project is a simple offline customer support chatbot built using Ollama and Llama 3.2.

The main idea is to check whether a local language model can handle basic e-commerce customer queries without sending any data to external servers.

---

## What I did

I created around 20 customer queries related to common problems like order tracking, payments, delivery issues, and returns.

Then I tested two approaches:
- Zero-shot prompting (no example given)
- One-shot prompting (one example provided)

Both responses were compared and evaluated manually.

---

## How it works

The Python script sends a prompt to the local Ollama server.  
The model generates a response, and the results are saved in a markdown file.

Everything runs locally, so no internet is needed after setup.

---

## Project Structure

- chatbot.py → main script
- prompts/ → contains prompt templates
- eval/ → contains results and scores
- report.md → final analysis
- setup.md → setup steps

---

## How to run

1. Install Ollama  
2. Pull the model:
   ollama pull llama3.2:3b  
3. Install required libraries:
   pip install requests datasets  
4. Run:
   python chatbot.py  

---

## Output

All responses and evaluation scores are stored in:
eval/results.md

---

## Final Note

From my observation, one-shot prompting gave better and more complete answers compared to zero-shot. The model works well for basic queries but still has some limitations.
