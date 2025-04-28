import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from gemini_api import summarize_text

class GeminiSummarizerApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Description Summarizer (Gemini)")
        self.img_label = tk.Label(master)
        self.img_label.pack()
        self.desc_label = tk.Label(master, text="Enter a description of the image:")
        self.desc_label.pack()
        self.desc_entry = tk.Text(master, height=4, width=50)
        self.desc_entry.pack()
        self.summarize_btn = tk.Button(master, text="Summarize with Gemini", command=self.summarize)
        self.summarize_btn.pack()
        self.summary_label = tk.Label(master, text="Gemini summary will appear here.", wraplength=400, justify="left")
        self.summary_label.pack()
        self.select_btn = tk.Button(master, text="Select Image", command=self.select_image)
        self.select_btn.pack()
        self.current_img = None

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", ".jpg .jpeg .png .bmp")])
        if not file_path:
            return
        img = Image.open(file_path).convert("RGB")
        img.thumbnail((256, 256))
        self.img_label.config(image=ImageTk.PhotoImage(img))
        self.img_label.image = ImageTk.PhotoImage(img)
        self.current_img = file_path

    def summarize(self):
        desc = self.desc_entry.get("1.0", tk.END).strip()
        if not desc:
            messagebox.showwarning("Input required", "Please enter a description of the image.")
            return
        try:
            summary = summarize_text(desc)
        except Exception as e:
            summary = f"[Gemini API error: {e}]"
        self.summary_label.config(text=summary)

if __name__ == "__main__":
    root = tk.Tk()
    app = GeminiSummarizerApp(root)
    root.mainloop()
