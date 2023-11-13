from personal_pdf_assistant.vector_store import VectorStore


def test_vector_store_init():
    vs = VectorStore()
    assert vs.index_name == "quickstart"
    assert vs.dimension == 1536
    assert vs.metric == "cosine"
