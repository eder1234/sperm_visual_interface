import pandas as pd
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

class FileMergeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Text File Merger")
        self.master.geometry("400x250")
        self.master.resizable(False, False)
        
        # Load and resize logo image
        logo_img = Image.open("logo.png")
        logo_img = logo_img.resize((150, 150), Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(logo_img)
        
        self.create_widgets()
    
    def create_widgets(self):
        # Add logo to GUI
        self.logo_label = tk.Label(self.master, image=self.logo)
        self.logo_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        
        # File 1 selection
        self.file1_label = tk.Label(self.master, text="Select trajectory file 1:")
        self.file1_label.grid(row=1, column=0, padx=5, pady=5)
        self.file1_button = tk.Button(self.master, text="Browse...", command=self.select_file1)
        self.file1_button.grid(row=1, column=1, padx=5, pady=5)
        self.file1_path = tk.StringVar()
        self.file1_entry = tk.Entry(self.master, textvariable=self.file1_path, state="readonly")
        self.file1_entry.grid(row=1, column=2, padx=5, pady=5)
        
        # File 2 selection
        self.file2_label = tk.Label(self.master, text="Select motility file 2:")
        self.file2_label.grid(row=2, column=0, padx=5, pady=5)
        self.file2_button = tk.Button(self.master, text="Browse...", command=self.select_file2)
        self.file2_button.grid(row=2, column=1, padx=5, pady=5)
        self.file2_path = tk.StringVar()
        self.file2_entry = tk.Entry(self.master, textvariable=self.file2_path, state="readonly")
        self.file2_entry.grid(row=2, column=2, padx=5, pady=5)
        
        # Merge button
        self.merge_button = tk.Button(self.master, text="Merge Files", command=self.merge_files)
        self.merge_button.grid(row=3, column=1, padx=5, pady=10)
    
    def select_file1(self):
        file_path = filedialog.askopenfilename(title="Select File 1", filetypes=(("Text Files", "*.txt"),))
        self.file1_path.set(file_path)
    
    def select_file2(self):
        file_path = filedialog.askopenfilename(title="Select File 2", filetypes=(("Text Files", "*.txt"),))
        self.file2_path.set(file_path)
    
    def merge_files(self):
        file1_path = self.file1_path.get()
        file2_path = self.file2_path.get()
        
        if file1_path and file2_path:
            df1 = pd.read_csv(file1_path, delimiter="\t")
            df2 = pd.read_csv(file2_path, delimiter="\t")
            merged_df = pd.merge(df1, df2, on="id")
            print(merged_df)
        else:
            print("Please select both files.")
        

if __name__ == "__main__":
    root = tk.Tk()
    app = FileMergeGUI(root)
    root.mainloop()

