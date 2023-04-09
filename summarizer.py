import pdfplumber
from llama_index import download_loader, GPTSimpleVectorIndex, Document
from io import BytesIO


def read_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        pages = []
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            text = page.extract_text()
            pages.append(text)
    return pages


def summarize_youtube_video(url, prompt):
    """Takes a url and prompt and delivers response"""
    YoutubeTranscriptReader = download_loader("YoutubeTranscriptReader")
    loader = YoutubeTranscriptReader()
    documents = loader.load_data(ytlinks=[url])
    index = GPTSimpleVectorIndex.from_documents(documents)
    response = index.query(prompt)
    return response


def summarize_wiki_article(page_name, prompt):
    """Takes a pagename and prompt and delivers response"""
    wikipedia_reader = download_loader("WikipediaReader")
    loader = wikipedia_reader()
    wikidocs = loader.load_data(pages=[page_name])
    index = GPTSimpleVectorIndex.from_documents(wikidocs)
    response = index.query(prompt)
    return response


def summarize_pdf(uploaded_file, prompt):
    pdf_file = BytesIO(uploaded_file.getbuffer())
    pages = read_pdf(pdf_file)
    documents = [Document(p) for p in pages]
    index = GPTSimpleVectorIndex.from_documents(documents)
    response = index.query(prompt)
    return response
