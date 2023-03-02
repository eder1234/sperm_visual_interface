import tkinter as tk
import pandas as pd
from tkinter import filedialog

# Define the GUI
class TextToDataFrameGUI:
    def __init__(self, master):
        self.master = master
        master.title("Text to DataFrame Converter")

        # Create the buttons
        self.select_file_button = tk.Button(master, text="Select File", command=self.select_file)
        self.convert_button = tk.Button(master, text="Convert to DataFrame", command=self.convert_to_dataframe)

        # Create the labels
        self.file_label = tk.Label(master, text="")
        self.status_label = tk.Label(master, text="")
        self.df_label = tk.Label(master, text="")

        # Pack the widgets onto the window
        self.select_file_button.pack()
        self.convert_button.pack()
        self.file_label.pack()
        self.status_label.pack()
        self.df_label.pack()

    # Define the select file button behavior
    def select_file(self):
        # Open the file dialog box
        file_path = filedialog.askopenfilename()

        # Update the file label with the selected file path
        self.file_label.config(text="Selected file: " + file_path)

        # Save the file path as an instance variable for later use
        self.file_path = file_path

    # Define the convert to dataframe button behavior
    def convert_to_dataframe(self):
        try:
            # Read the text file into a pandas dataframe
            df = pd.read_csv(self.file_path, header=None)

            # Update the status label with the number of rows and columns in the dataframe
            self.status_label.config(text="DataFrame converted successfully! Shape: " + str(df.shape))

            # Display the dataframe in the df_label
            self.df_label.config(text=df.to_string(index=False, header=False))
        except:
            # Update the status label if there was an error
            self.status_label.config(text="Error: Unable to convert file to DataFrame.")
            self.df_label.config(text="")

# Create the main window and run the GUI
root = tk.Tk()
gui = TextToDataFrameGUI(root)
root.mainloop()
