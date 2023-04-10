import pdfplumber
from llama_index import LLMPredictor, PromptHelper, ServiceContext, download_loader, GPTSimpleVectorIndex, Document
from io import BytesIO
from langchain import OpenAI
import os


def configure_LLM(api_key):
    llm_predictor = LLMPredictor(llm=OpenAI(api_key=api_key,
                                            temperature=0.9, model_name="text-davinci-003"))
    prompt_helper = PromptHelper(
        max_input_size=4096, num_output=256, max_chunk_overlap=20)
    service_context = ServiceContext.from_defaults(
        llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    return service_context


def read_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        pages = []
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            text = page.extract_text()
            pages.append(text)
    return pages


def summarize_youtube_video(url, prompt, key):
    """Takes a url and prompt and delivers response"""
    YoutubeTranscriptReader = download_loader("YoutubeTranscriptReader")
    loader = YoutubeTranscriptReader()
    documents = loader.load_data(ytlinks=[url])
    index = GPTSimpleVectorIndex.from_documents(
        documents, service_context=configure_LLM(key))
    response = index.query(prompt)
    return response


def summarize_wiki_article(page_name, prompt, key):
    """Takes a pagename and prompt and delivers response"""
    wikipedia_reader = download_loader("WikipediaReader")
    loader = wikipedia_reader()
    wikidocs = loader.load_data(pages=[page_name])
    index = GPTSimpleVectorIndex.from_documents(
        wikidocs, service_context=configure_LLM(key))
    response = index.query(prompt)
    return response


def summarize_pdf(uploaded_file, prompt, key):
    pdf_file = BytesIO(uploaded_file.getbuffer())
    pages = read_pdf(pdf_file)
    documents = [Document(p) for p in pages]
    index = GPTSimpleVectorIndex.from_documents(
        documents, service_context=configure_LLM(key))
    response = index.query(prompt)
    return response
