from document_retrieval import DocumentRetrieval

def test_retrieval():
    dr = DocumentRetrieval()
    sample_text = "Sample PDF text for testing."
    dr.documents = [sample_text]
    dr.build_index()
    result = dr.retrieve("PDF text")
    assert result == sample_text
