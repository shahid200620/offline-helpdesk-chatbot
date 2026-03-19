import requests
import json

url = "http://localhost:11434/api/generate"
model = "llama3.2:3b"

def ask_model(prompt):
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    try:
        res = requests.post(url, json=data)
        text = res.json()
        return text.get("response", "").strip()
    except:
        return "error"

f1 = open("prompts/zero_shot_template.txt", "r")
zero_temp = f1.read()
f1.close()

f2 = open("prompts/one_shot_template.txt", "r")
one_temp = f2.read()
f2.close()

queries = [
    "How can I track my order?",
    "My discount code is not working",
    "Can I return a product after delivery?",
    "Where can I see my past orders?",
    "How long does delivery take?",
    "I received a damaged item",
    "Can I change my shipping address?",
    "How do I cancel my order?",
    "Is cash on delivery available?",
    "Why is my payment failing?",
    "Do you offer international shipping?",
    "How can I contact support?",
    "Can I exchange a product?",
    "What payment methods do you accept?",
    "How do I apply a coupon?",
    "My order is delayed",
    "Can I reorder the same product?",
    "Is there any warranty on products?",
    "How do I reset my account password?",
    "Can I get a refund for my order?"
]

out = open("eval/results.md", "w")

out.write("| Query # | Customer Query | Method | Response | Relevance | Coherence | Helpfulness |\n")
out.write("|---------|----------------|--------|----------|-----------|-----------|-------------|\n")

i = 1

for q in queries:
    print("running:", q)
    p1 = zero_temp.replace("{query}", q)
    r1 = ask_model(p1)

    out.write(f"| {i} | {q} | Zero-Shot | {r1} |  |  |  |\n")

    p2 = one_temp.replace("{query}", q)
    r2 = ask_model(p2)

    out.write(f"| {i} | {q} | One-Shot | {r2} |  |  |  |\n")

    i += 1

out.close()

print("done")