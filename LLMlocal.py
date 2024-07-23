



import tkinter as tk
from tkinter import filedialog, scrolledtext
import os
from transformers import pipeline

class LLMCustomerSupportApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LLM Customer Support")
        self.root.geometry("800x600")

        self.file_paths = []
        # Use o modelo distilbert com pytorch
        self.model = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

        # Botão para carregar pasta
        self.load_folder_button = tk.Button(self.root, text="Carregar Pasta", command=self.load_folder)
        self.load_folder_button.pack(pady=10)

        # Campo de pergunta
        self.question_label = tk.Label(self.root, text="Pergunta:")
        self.question_label.pack(pady=5)
        self.question_entry = tk.Entry(self.root, width=100)
        self.question_entry.pack(pady=5)

        # Botão para enviar pergunta
        self.ask_button = tk.Button(self.root, text="Enviar Pergunta", command=self.ask_question)
        self.ask_button.pack(pady=10)

        # Campo de resposta
        self.response_label = tk.Label(self.root, text="Resposta:")
        self.response_label.pack(pady=5)
        self.response_text = scrolledtext.ScrolledText(self.root, width=100, height=20)
        self.response_text.pack(pady=5)

    def load_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.file_paths = [os.path.join(folder_selected, f) for f in os.listdir(folder_selected)]
            self.response_text.insert(tk.END, f"Carregados {len(self.file_paths)} arquivos da pasta.\n")

    def ask_question(self):
        question = self.question_entry.get()
        if not question:
            self.response_text.insert(tk.END, "Por favor, insira uma pergunta.\n")
            return

        if not self.file_paths:
            self.response_text.insert(tk.END, "Por favor, carregue uma pasta com arquivos primeiro.\n")
            return

        context = self.load_and_combine_files()
        response = self.query_llm(question, context)
        self.response_text.insert(tk.END, f"Pergunta: {question}\nResposta: {response}\n\n")

    def load_and_combine_files(self):
        combined_text = ""
        for file_path in self.file_paths:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                combined_text += file.read() + "\n"
        return combined_text

    def query_llm(self, question, context):
        inputs = {
            "question": question,
            "context": context
        }
        response = self.model(inputs)
        return response['answer']

if __name__ == "__main__":
    root = tk.Tk()
    app = LLMCustomerSupportApp(root)
    root.mainloop()
