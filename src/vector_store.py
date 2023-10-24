import os
import pinecone
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings

class VectorStore:
    def __init__(self, index_name="quickstart", dimension=1536, metric="cosine"):
        self.index_name = index_name
        self.dimension = dimension
        self.metric = metric

    def init_vector_store(self):
        pinecone.init(
            api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENV")
        )
        self.pinecone = pinecone
        if self.index_name not in pinecone.list_indexes():
            # create new index if not exist
            self.pinecone.create_index(
                self.index_name, dimension=self.dimension, metric=self.metric
            )  # dimension has to match embeddings dim
            self.describe_index(self.index_name)

    def describe_index(self):
        return self.pinecone.describe_index(self.index_name)

    def store_embeddings(self, pages, embedding = OpenAIEmbeddings(model_name="ada")):
        """
        embeddings = 
        """
        db = Pinecone.from_documents(pages, embedding, index_name=self.index_name)
        return db  # return db connection
