import tkinter as tk
from datetime import datetime

def show_message():
    name = entry.get() or "World"
    time_str = datetime.now().strftime("%H:%M:%S")
    label.config(text=f"猜到了")

app = tk.Tk()
app.title("友好的提醒")
app.geometry("300x150")

tk.Label(app, text="又在摸鱼?").pack(pady=5)
entry = tk.Entry(app)
entry.pack(pady=5)

tk.Button(app, text="Enter", command=show_message).pack(pady=10)

label = tk.Label(app, text="")
label.pack()

app.mainloop()

###