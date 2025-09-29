# application.py
import streamlit as st
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
import os

# Azure credentials
endpoint = "<Put your endpoint here after you have created your Azure Document Intelligence Resources>"
key = "<Put your key here after you have created your Azure Document Intelligence Resources>"
model_id = "prebuilt-invoice"

# Initialize client
client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Initialize Title and Logo
st.logo("Azure_Image.png",link=None, icon_image=None, size="large")
st.set_page_config(page_title="Azure Document Intelligence", layout="wide")
st.title("📄 Azure Document Intelligence with Streamlit :green[By Allen Wong] (allenwsh@gmail.com) :sunglasses:")

uploaded_file = st.file_uploader("Upload a document (PDF, JPG, PNG)", type=["pdf", "jpg", "png"])

if uploaded_file:
    st.success("File uploaded successfully!")
    poller = client.begin_analyze_document(model_id=model_id, document=uploaded_file)
    result = poller.result()

    st.subheader("📊 Extracted Tables")
    for table in result.tables:
        table_data = [["" for _ in range(table.column_count)] for _ in range(table.row_count)]
        for cell in table.cells:
            table_data[cell.row_index][cell.column_index] = cell.content
        st.table(table_data)

    st.subheader("📋 Extracted Fields")
    for doc in result.documents:
        for name, field in doc.fields.items():
            confidence = f"{field.confidence:.2f}" if field.confidence is not None else "N/A"
            st.write(f"**{name}**: {field.value} (Confidence: {confidence})")

    st.subheader("📋 Named Fields (Key-Value Pairs)")
    for doc in result.documents:
        for name, field in doc.fields.items():
            value = field.value if field.value else "N/A"
            confidence = f"{field.confidence:.2f}" if field.confidence is not None else "N/A"
            st.write(f"**{name}**: {value} (Confidence: {confidence})")

