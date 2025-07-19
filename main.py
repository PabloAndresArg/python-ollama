import ollama

prompt = "dame un script de python que imprima 'Hola, mundo!'"

response = ollama.chat(model="deepseek-r1:7b", messages=[{"role": "user", "content": prompt}])

print(response["message"]["content"])
