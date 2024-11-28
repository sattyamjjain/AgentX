from core.document_handler import DocumentHandler


def test_document_handler():
    handler = DocumentHandler()
    documents = handler.load_documents()
    assert len(documents) > 0
