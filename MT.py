import pandas as pd
import pickle
import numpy as np
import tkinter as tk
import tkinter.font as tkFont
import requests
import json

class App:
    def __init__(self, root):
        # setting title
        root.title("Heart Diseases")
        # setting window size
        width = 671
        height = 429
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg="black")  # setting background color

        # Function to create label
        def create_label(text, x, y):
            label = tk.Label(root, text=text, bg="black", fg="white")
            label_font = tkFont.Font(family='sans-serif', size=10)
            label["font"] = label_font
            label.place(x=x, y=y, width=100, height=25)

        # Function to create entry
        def create_entry(x, y):
            entry = tk.Entry(root, borderwidth="1px", bg="white", fg="black")
            entry_font = tkFont.Font(family='sans-serif', size=10)
            entry["font"] = entry_font
            entry.place(x=x, y=y, width=120, height=25)
            return entry

        # Labels creation
        create_label("Age", 10, 60)
        create_label("Sex", 10, 110)
        create_label("ChestPainType", 10, 160)
        create_label("RestingBP", 10, 210)
        create_label("Cholesterol", 10, 260)
        create_label("FastingBS", 10, 310)
        create_label("RestingECG", 380, 60)
        create_label("MaxHR", 380, 110)
        create_label("ExerciseAngina", 380, 160)
        create_label("Oldpeak", 380, 210)
        create_label("ST_Slope", 380, 260)
        outputt = tk.Label(root, text="Output :", bg="black", fg="white")
        label_font = tkFont.Font(family='sans-serif', size=18)
        outputt["font"] = label_font
        outputt.place(x=380, y=360, width=100, height=25)

        # Entries creation
        self.entries = []
        self.entries.append(create_entry(130, 60))
        self.entries.append(create_entry(130, 110))
        self.entries.append(create_entry(130, 160))
        self.entries.append(create_entry(130, 210))
        self.entries.append(create_entry(130, 260))
        self.entries.append(create_entry(130, 310))
        self.entries.append(create_entry(490, 60))
        self.entries.append(create_entry(490, 110))
        self.entries.append(create_entry(490, 160))
        self.entries.append(create_entry(490, 210))
        self.entries.append(create_entry(490, 260))
        
        # Button creation
        button = tk.Button(root, text="Button", bg="#7bd88f", fg="black", command=self.GButton_812_command)
        button_font = tkFont.Font(family='sans-serif', size=10)
        button["font"] = button_font
        button.place(x=280, y=355, width=80, height=40)

        # Message creation
        self.MessageOut = tk.Message(root, font=tkFont.Font(family='sans-serif', size=10), bg="black", fg="white")
        self.MessageOut["justify"] = "center"
        self.MessageOut.place(x=470, y=340, width=150, height=100)

    def get_inputs(self):
        entry_values = []
        for entry in self.entries:
            entry_values.append(entry.get())
        return entry_values

    def GButton_812_command(self):
        inputtext = self.get_inputs()
        if any(entry == '' for entry in inputtext):
            self.MessageOut.config(text="All fields must be filled!")
        else:
            input_data = [inputtext]  # Wrap inputtext in a list to create a 2D array-like structure
            response = requests.post("http://127.0.0.1:5000/predict", json=input_data)
            if response.status_code == 200:
                predictions = response.json()
                dt_predictions = predictions["Decision Tree"]
                mlp_predictions = predictions["MLP"]
                
                dt_output = "\n".join([f"Decision Tree: {pred}" for pred in dt_predictions])
                mlp_output = "\n".join([f"MLP: {pred}" for pred in mlp_predictions])

                tk.Message(text=f"{dt_output}\n{mlp_output}")
                self.MessageOut.config(text=f"{dt_output}\n{mlp_output}")
            else:
                self.MessageOut.config(text="Error: Could not get a prediction")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()














# import tkinter as tk
# import tkinter.font as tkFont
# import pickle
# import numpy as np

# class App:
#     def __init__(self, root):
#         # setting title
#         root.title("Heart Diseases")
#         # setting window size
#         width = 671
#         height = 429
#         screenwidth = root.winfo_screenwidth()
#         screenheight = root.winfo_screenheight()
#         alignstr = '%dx%d+%d+%d' % (
#             width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
#         root.geometry(alignstr)
#         root.resizable(width=False, height=False)
#         root.configure(bg="black")  # setting background color

#         # Function to create label
#         def create_label(text, x, y):
#             label = tk.Label(root, text=text, bg="black", fg="white")
#             label_font = tkFont.Font(family='sans-serif', size=10)
#             label["font"] = label_font
#             label.place(x=x, y=y, width=100, height=25)

#         # Function to create entry
#         def create_entry(x, y):
#             entry = tk.Entry(root, borderwidth="1px", bg="white", fg="black")
#             entry_font = tkFont.Font(family='sans-serif', size=10)
#             entry["font"] = entry_font
#             entry.place(x=x, y=y, width=120, height=25)
#             return entry

#         # Labels creation
#         create_label("Age", 10, 60)
#         create_label("Sex", 10, 110)
#         create_label("ChestPainType", 10, 160)
#         create_label("RestingBP", 10, 210)
#         create_label("Cholesterol", 10, 260)
#         create_label("FastingBS", 10, 310)
#         create_label("RestingECG", 380, 60)
#         create_label("MaxHR", 380, 110)
#         create_label("ExerciseAngina", 380, 160)
#         create_label("Oldpeak", 380, 210)
#         create_label("ST_Slope", 380, 260)
#         outputt = tk.Label(root, text="Output :", bg="black", fg="white")
#         label_font = tkFont.Font(family='sans-serif', size=18)
#         outputt["font"] = label_font
#         outputt.place(x=380, y=360, width=100, height=25)

#         # Entries creation
#         self.entries = []
#         self.entries.append(create_entry(130, 60))
#         self.entries.append(create_entry(130, 110))
#         self.entries.append(create_entry(130, 160))
#         self.entries.append(create_entry(130, 210))
#         self.entries.append(create_entry(130, 260))
#         self.entries.append(create_entry(130, 310))
#         self.entries.append(create_entry(490, 60))
#         self.entries.append(create_entry(490, 110))
#         self.entries.append(create_entry(490, 160))
#         self.entries.append(create_entry(490, 210))
#         self.entries.append(create_entry(490, 260))
        
#         # Button creation
#         button = tk.Button(root, text="Button", bg="#7bd88f", fg="black", command=self.GButton_812_command)
#         button_font = tkFont.Font(family='sans-serif', size=10)
#         button["font"] = button_font
#         button.place(x=280, y=355, width=80, height=40)

#         # Message creation
#         self.MessageOut = tk.Message(root, font=tkFont.Font(family='sans-serif', size=10), bg="black", fg="white")
#         self.MessageOut["justify"] = "center"
#         self.MessageOut.place(x=470, y=340, width=150, height=100)

#         # Load models
#         with open("PCAX.pkl", "rb") as f:
#             self.PCAX = pickle.load(f)
#         with open("MLP.pkl", "rb") as m:
#             self.MLP = pickle.load(m)
#         with open("Scaler.pkl", "rb") as s:
#             self.scaler = pickle.load(s)  

#     def get_inputs(self):
#         entry_values = []
#         for entry in self.entries:
#             entry_values.append(entry.get())
#         return entry_values

#     def GButton_812_command(self):
#         inputtext = self.get_inputs()
#         if any(entry == '' for entry in inputtext):
#             self.MessageOut.config(text="All fields must be filled!")
#         else:
#             preprocessed_input = self.scaler.transform([inputtext])
#             scaled_input_pca = self.PCAX.transform(preprocessed_input)
#             prediction_MLP = self.MLP.predict(scaled_input_pca)
#             self.MessageOut['text'] = f"MLP Prediction: {prediction_MLP[0]}"

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()






























#  import tkinter as tk
# import tkinter.font as tkFont
# import pickle
# from sklearn.preprocessing import LabelEncoder

# class App:
#     def __init__(self, root):
#         # setting title
#         root.title("Heart Diseases")
#         # setting window size
#         width = 671
#         height = 429
#         screenwidth = root.winfo_screenwidth()
#         screenheight = root.winfo_screenheight()
#         alignstr = '%dx%d+%d+%d' % (
#             width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
#         root.geometry(alignstr)
#         root.resizable(width=False, height=False)
#         root.configure(bg="black")  # setting background color

#         # Function to create label
#         def create_label(text, x, y):
#             label = tk.Label(root, text=text, bg="black", fg="white")
#             label_font = tkFont.Font(family='sans-serif', size=10)
#             label["font"] = label_font
#             label.place(x=x, y=y, width=100, height=25)

#         # Function to create entry
#         def create_entry(x, y):
#             entry = tk.Entry(root, borderwidth="1px", bg="white", fg="black")
#             entry_font = tkFont.Font(family='sans-serif', size=10)
#             entry["font"] = entry_font
#             entry.place(x=x, y=y, width=120, height=25)
#             return entry

#         # Labels creation
#         create_label("Age", 10, 60)
#         create_label("Sex", 10, 110)
#         create_label("ChestPainType", 10, 160)
#         create_label("RestingBP", 10, 210)
#         create_label("Cholesterol", 10, 260)
#         create_label("FastingBS", 10, 310)
#         create_label("RestingECG", 380, 60)
#         create_label("MaxHR", 380, 110)
#         create_label("ExerciseAngina", 380, 160)
#         create_label("Oldpeak", 380, 210)
#         create_label("ST_Slope", 380, 260)
#         outputt = tk.Label(root, text="Output :", bg="black", fg="white")
#         label_font = tkFont.Font(family='sans-serif', size=18)
#         outputt["font"] = label_font
#         outputt.place(x=380, y=360, width=100, height=25)

#         # Entries creation
#         self.entries = []
#         self.entries.append(create_entry(130, 60))
#         self.entries.append(create_entry(130, 110))
#         self.entries.append(create_entry(130, 160))
#         self.entries.append(create_entry(130, 210))
#         self.entries.append(create_entry(130, 260))
#         self.entries.append(create_entry(130, 310))
#         self.entries.append(create_entry(490, 60))
#         self.entries.append(create_entry(490, 110))
#         self.entries.append(create_entry(490, 160))
#         self.entries.append(create_entry(490, 210))
#         self.entries.append(create_entry(490, 260))
        
#         # Button creation
#         button = tk.Button(root, text="Button", bg="#7bd88f", fg="black", command=self.GButton_812_command)
#         button_font = tkFont.Font(family='sans-serif', size=10)
#         button["font"] = button_font
#         button.place(x=280, y=355, width=80, height=40)

#         # Message creation
#         self.MessageOut = tk.Message(root, font=tkFont.Font(family='sans-serif', size=10), bg="black", fg="white")
#         self.MessageOut["justify"] = "center"
#         self.MessageOut.place(x=470, y=340, width=150, height=100)

#         # Load models
#         with open("PCAX.pkl", "rb") as f:
#             self.PCAX = pickle.load(f)
#         with open("MLP.pkl", "rb") as m:
#             self.MLP = pickle.load(m)
#         with open("label.pkl", "rb") as l:
#             self.label_encoders = pickle.load(l)
#         # Load MinMaxScaler
#         with open("Saclar.pkl", "rb") as s:
#             self.SCCCA = pickle.load(s)

#     def get_inputs(self):
#         entry_values = []
#         for entry in self.entries:
#             entry_values.append(entry.get())
#         return entry_values

#     def GButton_812_command(self):
#         inputtext = self.get_inputs()
#         if any(entry == '' for entry in inputtext):
#             self.MessageOut.config(text="All fields must be filled!")
#         else:
#             # Convert categorical values to numerical
#             if inputtext[1] == 'M':
#                 inputtext[1] = 1
#             else:
#                 inputtext[1] = 0

#             if inputtext[2] == 'ATA':
#                 inputtext[2] = 0
#             elif inputtext[2] == 'NAP':
#                 inputtext[2] = 1
#             elif inputtext[2] == 'ASY':
#                 inputtext[2] = 2
#             else:
#                 inputtext[2] = 3

#             if inputtext[6] == 'Normal':
#                 inputtext[6] = 1
#             elif inputtext[6] == 'ST':
#                 inputtext[6] = 2
#             else:
#                 inputtext[6] = 0

#             if inputtext[8] == 'N':
#                 inputtext[8] = 1
#             else:
#                 inputtext[8] = 0

#             if inputtext[10] == 'Up':
#                 inputtext[10] = 1
#             elif inputtext[10] == 'Flat':
#                 inputtext[10] = 2
#             else:
#                 inputtext[10] = 0

#             # Convert all remaining values to float
#             inputtext = [float(i) for i in inputtext]

#             preprocessed_input = self.SCCCA.transform([inputtext])
#             scaled_input_pca = self.PCAX.transform(preprocessed_input)
#             prediction_MLP = self.MLP.predict(scaled_input_pca)
#             self.MessageOut['text'] = f"MLP Prediction: {prediction_MLP[0]}"

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()





    # def preprocess_input(self, input_data):
    #     # Apply label encoding for specific columns
    #     encoded_input = input_data.copy()
    #     encoded_input[1] = self.label_encoders['Sex'].transform([encoded_input[1]])[0]  # assuming Sex is the second column
    #     encoded_input[2] = self.label_encoders['ChestPainType'].transform([encoded_input[2]])[0]
    #     encoded_input[6] = self.label_encoders['RestingECG'].transform([encoded_input[6]])[0]
    #     encoded_input[8] = self.label_encoders['ExerciseAngina'].transform([encoded_input[8]])[0]
    #     encoded_input[10] = self.label_encoders['ST_Slope'].transform([encoded_input[10]])[0]  # assuming ChestPainType is the third column
    #     # You can continue this for other columns as well
    #     scaled_input = self.scaler.transform([encoded_input])

    #     return encoded_input
























# import tkinter as tk
# import tkinter.font as tkFont

# class App:
#     def __init__(self, root):
#         # setting title
#         root.title("Heart Diseases")
#         # setting window size
#         width = 671
#         height = 429
#         screenwidth = root.winfo_screenwidth()
#         screenheight = root.winfo_screenheight()
#         alignstr = '%dx%d+%d+%d' % (
#             width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
#         root.geometry(alignstr)
#         root.resizable(width=False, height=False)
#         root.configure(bg="black")  # setting background color

#         # Function to create label
#         def create_label(text, x, y):
#             label = tk.Label(root, text=text, bg="black", fg="white")
#             label_font = tkFont.Font(family='sans-serif', size=10)
#             label["font"] = label_font
#             label.place(x=x, y=y, width=100, height=25)

#         # Function to create entry
#         def create_entry(x, y):
#             entry = tk.Entry(root, borderwidth="1px", bg="white", fg="black")
#             entry_font = tkFont.Font(family='sans-serif', size=10)
#             entry["font"] = entry_font
#             entry.place(x=x, y=y, width=120, height=25)
#             return entry

#         # Labels creation
#         create_label("Age", 10, 60)
#         create_label("Sex", 10, 110)
#         create_label("ChestPainType", 10, 160)
#         create_label("RestingBP", 10, 210)
#         create_label("Cholesterol", 10, 260)
#         create_label("FastingBS", 10, 310)
#         create_label("RestingECG", 380, 60)
#         create_label("MaxHR", 380, 110)
#         create_label("ExerciseAngina", 380, 160)
#         create_label("Oldpeak", 380, 210)
#         create_label("ST_Slope", 380, 260)
#         outputt = tk.Label(root, text="Output :", bg="black", fg="white")
#         label_font = tkFont.Font(family='sans-serif', size=18)
#         outputt["font"] = label_font
#         outputt.place(x=380, y=360, width=100, height=25)

#         # Entries creation
#         self.entries = []
#         self.entries.append(create_entry(130, 60))
#         self.entries.append(create_entry(130, 110))
#         self.entries.append(create_entry(130, 160))
#         self.entries.append(create_entry(130, 210))
#         self.entries.append(create_entry(130, 260))
#         self.entries.append(create_entry(130, 310))
#         self.entries.append(create_entry(490, 60))
#         self.entries.append(create_entry(490, 110))
#         self.entries.append(create_entry(490, 160))
#         self.entries.append(create_entry(490, 210))
#         self.entries.append(create_entry(490, 260))
        
#         # Button creation
#         button = tk.Button(root, text="Button", bg="#7bd88f", fg="black", command=self.GButton_812_command)
#         button_font = tkFont.Font(family='sans-serif', size=10)
#         button["font"] = button_font
#         button.place(x=280, y=355, width=80, height=40)

#         # Message creation
#         self.MessageOut = tk.Message(root, font=tkFont.Font(family='sans-serif', size=10), bg="black", fg="white")
#         self.MessageOut["justify"] = "center"
#         self.MessageOut.place(x=470, y=340, width=150, height=100)

#     def get_inputs(self):
#         entry_values = []
#         for entry in self.entries:
#             entry_values.append(entry.get())
#         return ','.join(entry_values)

#     def GButton_812_command(self):
#         inputtext = self.get_inputs()
#         if any(entry.get() == '' for entry in self.entries):
#             self.MessageOut.config(text="All fields must be filled!")
#         else:
#             self.MessageOut.config(text=inputtext)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()


# import pickle
# with open("PCAX.pkl", "rb") as f:
#     PCAX = pickle.load(f)
# with open("MLP.pkl", "rb") as m:
#     MLP = pickle.load(m)
# with open("PCAX.pkl", "rb") as d:
#     DT = pickle.load(d)
# with open("Saclar.pkl", "rb") as s:
#     Saclar = pickle.load(s)
