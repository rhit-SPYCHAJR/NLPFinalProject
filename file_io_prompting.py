from langchain_community.llms import HuggingFaceHub

# Set your Hugging Face API token
huggingfacehub_api_token = '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'

# Define the LLM
llm = HuggingFaceHub(repo_id='tiiuae/falcon-7b-instruct', huggingfacehub_api_token=huggingfacehub_api_token)

mode = 1

qFile = open("q_multi_factor.txt", encoding="utf-8", mode = "r")
rFile = open("r_multi_factor_f.txt", "a")
question = qFile.readline()
line = " "
if mode == 1:
  while question:
    resp = llm.predict(question)
    rFile.write(resp + "\n")
    question = qFile.readline()
else:
  while line:
    line = qFile.readline()
    question += line
  resp = llm.predict(question)
  rFile.write(resp + "\n")
qFile.close()
rFile.close()