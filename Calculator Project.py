import tkinter as tk

def on_click(button_text):
    if button_text == "C":
        entry_var.set("")
    elif button_text == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except Exception:
            entry_var.set("Error")
    else:
        entry_var.set(entry_var.get() + button_text)

root = tk.Tk()
root.title("Calculator")
entry_var = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify='right', bd=10, relief=tk.GROOVE)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

for r, row in enumerate(buttons, 1):
    for c, button_text in enumerate(row):
        tk.Button(root, text=button_text, font=("Arial", 20), width=5, height=2,
                  command=lambda text=button_text: on_click(text)).grid(row=r, column=c)

root.mainloop()