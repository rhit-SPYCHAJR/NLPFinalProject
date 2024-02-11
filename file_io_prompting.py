from langchain_community.llms import HuggingFaceHub

# Set your Hugging Face API token
huggingfacehub_api_token = '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'

# Define the LLM
llm = HuggingFaceHub(repo_id='tiiuae/falcon-7b-instruct', huggingfacehub_api_token=huggingfacehub_api_token)

qFile = open("q_occupations.txt", encoding="utf-8", mode = "r")
rFile = open("r_occupations.txt", "a")
question = qFile.readline()
while question:
  resp = llm.predict(question)
  rFile.write(resp + "\n")
  question = qFile.readline()
qFile.close()