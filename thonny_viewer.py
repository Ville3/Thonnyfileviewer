import json
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter.filedialog import askopenfilename

#Request file's location
def file_open():
    window = tk.Tk()
    window.withdraw()
    filename = askopenfilename()
    window.destroy()
    return filename

#Open file
def open_log_file(filename):
    window = tk.Tk()
    window.geometry("1200x600")
    window.title("Ville's Thonny log file viewer - " + filename)

    text = tk.Text(window)

    with open(filename) as f:
        data = json.load(f)
        for rida in data:

            if rida['sequence'] == "Open":
                tk.Label(text="logged file's name: " + rida['filename']).pack()

            elif rida['sequence'] == "SaveAs":
                tk.Label(text="logged file was saved as: " + rida['filename']).pack()

            elif rida['sequence'] == "TextInsert" and rida['text_widget_class'] == "CodeViewText":
                text.insert(rida['index'], rida['text'])

            elif rida['sequence'] == "TextDelete" and rida['text_widget_class'] == "CodeViewText":
                if rida['trivial_for_coloring'] == True:
                    if rida['index2'] != "None":
                        text.tag_add("tagging_red", rida['index1'], rida['index2'])
                    else:
                        text.tag_add("tagging_red", rida['index1'])
                else:
                    if rida['index2'] != "None":
                        text.tag_add("tagging_yellow", rida['index1'], rida['index2'])
                    else:
                        text.tag_add("tagging_yellow", rida['index1'])

        #tags
        text.tag_config("tagging_red", background="red", foreground="black")
        text.tag_config("tagging_yellow", background="yellow", foreground="black")

        text.pack(expand=1, fill=tk.BOTH)

    #Disable edit
    text.config(state=tk.DISABLED)

    window.mainloop()

#Run
open_log_file(file_open())