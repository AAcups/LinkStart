import os
from tkinter import Tk, Canvas, Label
import subprocess
def read_shortcut_data(directory):
    data = []
    config_path = os.path.join(directory, "config", "config.txt")
    try:
        with open(config_path, "r", encoding="utf-8") as file:
            data = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Config file not found at {config_path}")
    return data

def open_shortcut(shortcut_path):
    try:
        #os.system(shortcut_path)
        subprocess.run([shortcut_path], shell=True)
    except Exception as e:
        print(f"Error opening shortcut {shortcut_path}: {e}")



def on_label_click(event):
    label = event.widget
    grid_info = label.grid_info()
    row = grid_info['row']
    if 0 < row <= len(data):
        pwd = os.getcwd()
        path = os.path.join('link', data[row-1] + ".lnk")
        shortcut_path = os.path.join(pwd, path)

        open_shortcut(shortcut_path)


def create_gui(data):
    root = Tk()
    root.title("Shortcut Viewer")
    root.geometry("400x400")
    text1="直接点击下面的文字，即可启用对应的工具"
    instruction_label = Label(root, text=text1)
    instruction_label.grid()
    canvas = Canvas(root, width=300, height=-300)

    canvas.grid(row=1, column=0)
    for i, item in enumerate(data):
        label = Label(root, text=item, fg="blue", underline=-1)
        label.grid(row=i+1, column=0,sticky='w', padx=10)
        label.bind("<Button-1>", on_label_click)  # Bind left mouse button click event

    root.mainloop()

if __name__ == "__main__":
    directory_path = os.getcwd()  # Use current working directory
    data = read_shortcut_data(directory_path)
    create_gui(data)
