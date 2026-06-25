import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("DWZ Umrechner")

current_mode = "neu"  # Global für Funktionssicherheit
mode_var = tk.StringVar(value="neu")


def update_labels():
    global current_mode
    current_mode = mode_var.get()
    if current_mode == "neu":
        lbl_input.config(text="Alter DWZ:")
        lbl_output.config(text="Neuer DWZ:")
    else:
        lbl_input.config(text="Neuer DWZ:")
        lbl_output.config(text="Alter DWZ:")
    reset_fields()


def calculate():
    raw = entry.get().replace(',', '.')
    try:
        val = float(raw)
    except ValueError:
        messagebox.showerror("Fehler", "Bitte eine gültige Zahl eingeben.")
        return

    if current_mode == "neu":
        if val < 1000:
            res = val + 400
        elif 1000 <= val < 2110:
            res = 0.64 * val + 760
        else:
            res = val
    else:  # alt
        if val >= 2110:
            res = val
        elif val >= 1400:
            res = (val - 760) / 0.64
        else:
            res = val - 400

    lbl_exact.config(text=f"{res:.2f}")
    lbl_rounded.config(text=str(round(res)))
    entry.config(state='disabled')


def reset_fields():
    entry.config(state='normal')
    entry.delete(0, tk.END)
    lbl_exact.config(text="--")
    lbl_rounded.config(text="--")


def validate_char(char):
    """Erlaubt nur Ziffern sowie . und ,. Keine ; erlaubt."""
    return char in "0123456789.," or char == ""


# ─── Layout (zentriert, Basis-Tkinter) ───
main_frame = tk.Frame(root)
main_frame.pack(expand=True, fill="both", padx=20, pady=20)

# Modus-Auswahl oben
tk.Radiobutton(main_frame, text="Neu zu Alt", variable=mode_var, value="alt", command=update_labels).pack(pady=(15, 5), anchor="center")
tk.Radiobutton(main_frame, text="Alt zu Neu", variable=mode_var, value="neu", command=update_labels).pack(pady=5, anchor="center")

# Eingabe-Bereich
lbl_input = tk.Label(main_frame, text="Alter DWZ:")
lbl_input.pack(pady=(10, 2), anchor="center")

entry = tk.Entry(main_frame, width=30, justify="center")
vcmd = (root.register(validate_char), "%S")
entry.config(validate="key", vcmd=vcmd)
entry.pack(pady=5, anchor="center")

# Ausgabe-Bereich
lbl_output = tk.Label(main_frame, text="Neuer DWZ:")
lbl_output.pack(pady=(10, 2), anchor="center")

frame_res = tk.Frame(main_frame)
frame_res.pack(pady=5)
lbl_exact = tk.Label(frame_res, text="--")
lbl_exact.pack(side=tk.LEFT, padx=5)
lbl_symbol = tk.Label(frame_res, text="≈")
lbl_symbol.pack(side=tk.LEFT, padx=2)
lbl_rounded = tk.Label(frame_res, text="--")
lbl_rounded.pack(side=tk.LEFT, padx=5)

# Buttons unten
btn_frame = tk.Frame(main_frame)
btn_frame.pack(pady=(15, 0))
tk.Button(btn_frame, text="Berechnen", command=calculate).pack(side=tk.LEFT, padx=10)
tk.Button(btn_frame, text="Reset", command=reset_fields).pack(side=tk.LEFT, padx=10)

root.mainloop()
