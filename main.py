import pandas as pd
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

import functions

class FileMergeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("LenSperm")
        self.master.geometry("450x300")
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
        self.file1_label = tk.Label(self.master, text="Select trajectory file:")
        self.file1_label.grid(row=1, column=0, padx=5, pady=5)
        self.file1_button = tk.Button(self.master, text="Browse...", command=self.select_file1)
        self.file1_button.grid(row=1, column=1, padx=5, pady=5)
        self.file1_path = tk.StringVar()
        self.file1_entry = tk.Entry(self.master, textvariable=self.file1_path, state="readonly")
        self.file1_entry.grid(row=1, column=2, padx=5, pady=5)
        
        # File 2 selection
        self.file2_label = tk.Label(self.master, text="Select motility file:")
        self.file2_label.grid(row=2, column=0, padx=5, pady=5)
        self.file2_button = tk.Button(self.master, text="Browse...", command=self.select_file2)
        self.file2_button.grid(row=2, column=1, padx=5, pady=5)
        self.file2_path = tk.StringVar()
        self.file2_entry = tk.Entry(self.master, textvariable=self.file2_path, state="readonly")
        self.file2_entry.grid(row=2, column=2, padx=5, pady=5)
        
        # Merge button
        self.merge_button = tk.Button(self.master, text="Create master dataframe", command=self.merge_files)
        self.merge_button.grid(row=3, column=1, padx=5, pady=10)
    
    def select_file1(self):
        file_path = filedialog.askopenfilename(title="Select trajectory file", filetypes=(("Text Files", "*.txt"),))
        self.file1_path.set(file_path)
    
    def select_file2(self):
        file_path = filedialog.askopenfilename(title="Select motility file", filetypes=(("Text Files", "*.txt"),))
        self.file2_path.set(file_path)
    
    def merge_files(self):
        traj_path = self.file1_path.get()
        mot_path = self.file2_path.get()
        traj_col_names = ["name", "date", "quantity", "exposure", "tracked_id", "x", "y"]
        
        if traj_path and mot_path:
            df1 = pd.read_csv(traj_path, names=traj_col_names)
            traj_df = functions.trajFrame(df1)
            traj_df = traj_df.sort_values(by=['name', 'date', 'quantity', 'exposure', 'tracked_id'])
            traj_name_list = traj_df["name"].values.tolist()
            traj_date_list = traj_df["date"].values.tolist()
            traj_quantity_list = traj_df["quantity"].values.tolist()
            traj_exposure_list = traj_df["exposure"].values.tolist()
            traj_tracked_id_list = traj_df["tracked_id"].values.tolist()
            traj_traj_list = traj_df["traj"].values.tolist() 
            
            mot_df = pd.read_csv("Motility_Results-partial.txt", engine='python') 
            id_ = [x for x in range(mot_df.shape[0])]
            mot_df["id"] = id_
            mot_df = mot_df.sort_values(by=['ID1', 'ID2', 'ID3', 'ID4', 'id'])
            mot_VCL_list = mot_df["VCL"].values.tolist()
            mot_VAP_list = mot_df["VAP"].values.tolist()
            mot_VSL_list = mot_df["VSL"].values.tolist()
            mot_LIN_list = mot_df["LIN"].values.tolist()
            mot_STR_list = mot_df["STR"].values.tolist()
            mot_WOB_list = mot_df["WOB"].values.tolist()
            mot_BeatCross_list = mot_df["BeatCross"].values.tolist()
            mot_ALH_list = mot_df["ALH"].values.tolist()

            master_dict = {"name":traj_name_list, "date":traj_date_list, "quantity":traj_quantity_list, 
                        "exposure":traj_exposure_list, "tracked_id":traj_tracked_id_list, "traj":traj_traj_list,
                        "VCL":mot_VCL_list, "VAP":mot_VAP_list, "VSL":mot_VSL_list, "LIN":mot_LIN_list, "STR":mot_STR_list,
                        "WOB":mot_WOB_list, "BeatCross":mot_BeatCross_list, "ALH":mot_ALH_list}
            
            master_df = pd.DataFrame(master_dict)
            print(master_df)
        else:
            print("Please select both files.")
        

if __name__ == "__main__":
    root = tk.Tk()
    app = FileMergeGUI(root)
    root.mainloop()

