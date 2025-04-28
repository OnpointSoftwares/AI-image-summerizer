import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from gemini_api import summarize_text

APP_BG = "#f2f2f7"
HEADER_BG = "#4a90e2"
HEADER_FG = "#fff"
BUTTON_BG = "#4a90e2"
BUTTON_FG = "#fff"
FONT_HEADER = ("Segoe UI", 16, "bold")
FONT_LABEL = ("Segoe UI", 12)
FONT_TEXT = ("Segoe UI", 11)
FONT_BUTTON = ("Segoe UI", 11, "bold")

class GeminiSummarizerApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Description Summarizer (Gemini)")
        master.configure(bg=APP_BG)
        master.geometry("520x600")
        master.resizable(False, False)

        self.header = tk.Label(master, text="Image → Gemini Summarizer", font=FONT_HEADER, bg=HEADER_BG, fg=HEADER_FG, pady=12)
        self.header.pack(fill="x")

        self.img_frame = tk.Frame(master, bg=APP_BG)
        self.img_frame.pack(pady=(20, 8))
        self.img_label = tk.Label(self.img_frame, bg=APP_BG, relief="groove", width=256, height=256)
        self.img_label.pack()

        self.select_btn = tk.Button(master, text="Select Image", command=self.select_image, bg=BUTTON_BG, fg=BUTTON_FG, font=FONT_BUTTON, width=18)
        self.select_btn.pack(pady=(0, 18))

        self.desc_label = tk.Label(master, text="Describe the image:", font=FONT_LABEL, bg=APP_BG)
        self.desc_label.pack(anchor="w", padx=30)
        self.desc_entry = tk.Text(master, height=4, width=54, font=FONT_TEXT, wrap="word", relief="solid", bd=1)
        self.desc_entry.pack(padx=30, pady=(0, 12))

        self.summarize_btn = tk.Button(master, text="Summarize with Gemini", command=self.summarize, bg=BUTTON_BG, fg=BUTTON_FG, font=FONT_BUTTON, width=22)
        self.summarize_btn.pack(pady=(0, 18))

        self.summary_title = tk.Label(master, text="Gemini Summary:", font=FONT_LABEL, bg=APP_BG)
        self.summary_title.pack(anchor="w", padx=30)
        self.summary_label = tk.Label(master, text="(Summary will appear here)", wraplength=440, justify="left", font=FONT_TEXT, bg=APP_BG, relief="solid", bd=1, padx=10, pady=10)
        self.summary_label.pack(padx=30, pady=(0, 12), fill="x")

        self.current_img = None

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", ".jpg .jpeg .png .bmp")])
        if not file_path:
            return
        img = Image.open(file_path).convert("RGB")
        img.thumbnail((256, 256))
        tk_img = ImageTk.PhotoImage(img)
        self.img_label.config(image=tk_img, width=img.width, height=img.height)
        self.img_label.image = tk_img
        self.current_img = file_path

    def summarize(self):
        desc = self.desc_entry.get("1.0", tk.END).strip()
        if not desc:
            messagebox.showwarning("Input required", "Please enter a description of the image.")
            return
        self.summary_label.config(text="Summarizing...", fg="#888")
        self.master.update_idletasks()
        try:
            summary = summarize_text(desc)
            self.summary_label.config(text=summary, fg="#222")
        except Exception as e:
            self.summary_label.config(text=f"[Gemini API error: {e}]", fg="#a00")

if __name__ == "__main__":
    root = tk.Tk()
    app = GeminiSummarizerApp(root)
    root.mainloop()
