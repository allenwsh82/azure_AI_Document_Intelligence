# 🚀 Azure Document Intelligence with Streamlit UI – Enterprise-Ready in 30 Minutes

This project demonstrates how to build a lightweight, production-ready front end using Streamlit to interface with Microsoft Azure Document Intelligence. It’s designed for enterprise scenarios such as invoice, receipt, ID, and business card processing—delivered in a clean, drag-and-drop web UI.

**Implementation idea:**

<img width="1000" height="600" alt="AZ_Document_Intelligence" src="https://github.com/user-attachments/assets/4e5c4556-6470-4eb7-be99-6e1ddfa94019" />

**🔧 Features**
- Seamless integration with Azure Document Intelligence API (prebuilt-invoice model)
- Drag-and-drop support for PDF, JPG, PNG, JPEG
- Real-time extraction of:
- Named Fields
- Extracted Tables
- Extracted Key-Value Pairs
- Clean, responsive UI powered by Streamlit
- Modular Python codebase for easy extension and customization
  
**📦 Tech Stack**
- Azure Document Intelligence (formerly Form Recognizer)
- Python 3.10+
- Streamlit
- Visual Studio Code (recommended IDE)

**🛠️ Setup Instruction**

1) Create a Document Intelligence resource in the Azure Portal

<br/>

<img width="1000" height="800" alt="Form_Recognizer" src="https://github.com/user-attachments/assets/20a65ef1-2985-4da9-9731-4c360ef1f638" />

<br/>


2) Retrieve your API Key and Endpoint

<br/>

<img width="831" height="451" alt="Screenshot 2025-09-29 150044" src="https://github.com/user-attachments/assets/9c8a3c20-588a-4fea-bdfe-af5d4fae5617" />

<br/>

3) Clone this repo:
   ``` 
   git clone https://github.com/allenwsh82/azure_AI_Document_Intelligence
   ```
4) Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5) Add your credntials into the application.py
   
6) Run the application with this command:
   ```
   streamlit run application.py
   ```

7) This should open up a webpage with localhost:8501 in your browser:

<br/>

<img width="1000" height="800" alt="Streamlit_LocalHost_Webpage" src="https://github.com/user-attachments/assets/86b93857-6f70-4c66-a892-7c37099365d5" />

<br/>
<br/>

**📊 Output Example**

Once uploaded, the document is parsed and displayed in structured sections:
- Extracted Fields: Key-value pairs like invoice number, date, total
- Named Fields: Semantic labels for easier downstream use
- Tables: Line items and structured data rendered cleanly
  
**💡 Use Cases**

- Invoice automation
- Identity document parsing
- Receipt digitization
- Business card extraction
- Credit card form processing
  
**📌 Notes**

- This is a serverless, pay-as-you-go solution—ideal for scalable enterprise deployments
- You can easily swap Streamlit with other front-end frameworks like React, Flask, or FastAPI
