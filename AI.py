import tkinter as tk
from tkinter import scrolledtext, filedialog
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from docx import Document  

model = SentenceTransformer('all-MiniLM-L6-v2')

document_content = []
document_embeddings = []

def load_document():
    global document_content, document_embeddings
    file_path = filedialog.askopenfilename(filetypes=[("Word files", "*.docx")])

    if file_path:
        
        document = Document(file_path)
        document_content = []
        
        for para in document.paragraphs:

            document_content.extend(para.text.split('. '))
        
        document_embeddings = model.encode(document_content)

        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f"Document loaded successfully!\n\n")
        chat_window.config(state=tk.DISABLED)
        print(f"Document loaded from {file_path}")

def get_response():
    user_query = user_input.get()
    
    if not document_content:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "Please load a document first!\n\n")
        chat_window.config(state=tk.DISABLED)
        return
    
    query_embedding = model.encode([user_query])
    
    similarities = cosine_similarity(query_embedding, document_embeddings)
    
    best_match_idx = similarities.argmax()
    bot_response = document_content[best_match_idx]
    
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"You: {user_query}\n")
    chat_window.insert(tk.END, f" {bot_response}\n\n")
    chat_window.config(state=tk.DISABLED)
    
    chat_window.yview(tk.END)
    
    user_input.delete(0, tk.END)

root = tk.Tk()
root.config(bg="black")
root.title("Document-Based AI Chatbot")

chat_window = scrolledtext.ScrolledText(root, width=50, height=25, wrap=tk.WORD, state=tk.DISABLED)
chat_window.grid(row=0, column=0, padx=50, pady=25)

user_input = tk.Entry(root, width=50)
user_input.grid(row=1, column=0, padx=50, pady=25)

send_button = tk.Button(root, text=">>", width=5, command=get_response)
send_button.grid(row=2, column=0, padx=10, pady=10)

load_button = tk.Button(root, text="Load Document", width=20, command=load_document)
load_button.grid(row=3, column=0, padx=30, pady=30)

root.mainloop()

