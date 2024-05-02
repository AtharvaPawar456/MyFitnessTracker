import requests

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "<s>[INST] What is your favourite condiment? [/INST]"
"Well, I'm quite partial to a good squeeze of fresh lemon juice. It adds just the right amount of zesty flavour to whatever I'm cooking up in the kitchen!</s> "
"[INST] Do you have mayonnaise recipes? [/INST]",
})
print("output: ", output)


'''
[{'generated_text': "<s>[INST] What is your favourite condiment? [/INST]Well, I'm quite partial to a good squeeze of fresh lemon juice. It adds just the right amount of zesty flavour to whatever I'm cooking up in the kitchen!</s> [INST] Do you have mayonnaise recipes? [/INST] Yes, I can certainly provide you with a simple homemade mayonnaise recipe! Here's one that requires only five ingredients and a blender or food processor:\n\nIngredients:\n- 1 egg yolk\n- 1 tablespoon Dijon mustard\n- 1 cup (200 ml) vegetable oil\n- 1-2 tablespoons white wine vinegar or lemon juice\n- Salt, to taste\n\nInstructions:"}]
'''