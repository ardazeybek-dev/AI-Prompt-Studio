import google.generativeai as genai

genai.configure(api_key="AIzaSyBSF5UbS4-6QXbeDjhgyoVtxx34GqCoYOc")

print("\n--- SENİN API ANAHTARINA AÇIK MODELLER ---")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
print("------------------------------------------\n")