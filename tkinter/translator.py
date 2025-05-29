
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
import asyncio

translator = Translator()
async def translate_text():
    text = input_text.get()
    dest = dest_lang.get()
    try:
        translated = await translator.translate(text=text, dest=dest)
        if translated.text:
            output_text.set(translated.text)
            print(translated)
    except:
        output_text.set("Translation Error! Try Again...")


def start_translation():
    asyncio.run(translate_text())


window = tk.Tk()
window.title("Language Translator")
window.geometry("400x300")
# window.config(background="black")

input_text = tk.StringVar()
output_text = tk.StringVar()
current_dest = tk.StringVar()

tk.Label(window, text="Enter Text:").pack(pady=5)
tk.Entry(window, textvariable=input_text, width=40).pack()


tk.Label(window, text="Destination Language:").pack()
dest_lang = ttk.Combobox(window, textvariable=current_dest)
dest_lang["values"] = ('en', 'hi', 'ja', 'ko', 'fr')
dest_lang.set("hi")
dest_lang.pack()

tk.Button(window, text="Translate", command=start_translation).pack(pady=10)
tk.Label(window, text="Translation Result:").pack()
tk.Label(window, textvariable=output_text, wraplength=300, bg="lightyellow").pack(pady=5)

window.mainloop()
