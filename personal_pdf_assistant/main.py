from dotenv import find_dotenv, load_dotenv

from langchain.llms import OpenAI

if __name__ == "__main__":
    # PLACEHOLDER
    load_dotenv(find_dotenv("keys.env"))
    llm = OpenAI(model_name="text-davinci-003")
    # llm("explain large language models in one sentence")
