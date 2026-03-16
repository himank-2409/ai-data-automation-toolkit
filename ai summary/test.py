import google.generativeai as genai

genai.configure(api_key="AIzaSyBu5MLv1JMCwVmwDT04ho8H3w3-y99MQtM")

model = genai.GenerativeModel("gemini-3.1-pro-preview")

response = model.generate_content("Explain what data cleaning is in one paragraph")

print(response.text)