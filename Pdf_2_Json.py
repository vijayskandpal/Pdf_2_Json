import streamlit as st
from PyPDF2 import PdfReader 
import json
import os

# Function to save JSON file
def save_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# File paths
output_json_filename = 'New_json_File.json'

st.title("PDF to JSON Converter")

# File uploader
uploaded_file = st.file_uploader(label='Upload a PDF File', type='.pdf')

if uploaded_file is not None:
    # Creating a pdf reader object
    reader = PdfReader(uploaded_file)
    all_text = []

    for page in reader.pages:
        # Extract text from the page
        text = page.extract_text()
        # Append the text to the list
        all_text.append(text)

    pdf_data = {
        "num_pages": len(reader.pages),
        "text_per_page": all_text
    }

    # Save the data to a JSON file
    save_json(pdf_data, output_json_filename)
    st.success("Text extracted from PDF and saved to JSON successfully.")

# Sidebar for folder selection
#selected_folder = st.sidebar.selectbox("Select Folder to Save JSON File", os.listdir())
save_folder = os.path.join(os.getcwd())#, selected_folder)

# Download button
if st.button("Convert JSON File"):
    if os.path.exists(output_json_filename):
        with open(output_json_filename, 'r') as file:
            file_contents = file.read()
        st.download_button(label="Download JSON", data=file_contents, file_name=output_json_filename, mime="application/json")
    else:
        st.warning("JSON file does not exist. Please upload a PDF file first.")
