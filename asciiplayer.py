import tkinter as tk
from pathlib import Path

ASCII_DIR = Path("ascii_frames")
FPS = 24  # frames per second
DELAY = int(1000 / FPS)  # tkinter delay in milliseconds

ascii_files = sorted(ASCII_DIR.glob("*.txt"))

class ASCIIPlayer(tk.Tk):
    def __init__(self, frames):
        super().__init__()
        self.frames = frames
        self.index = 0

        self.title("ASCII Animation Player")
        self.geometry("565x565")  # Adjust as needed

        # Use a Text widget with monospace font for better ASCII rendering
        self.text_widget = tk.Text(self, font=("Courier", 8), bg="tan", fg="black", bd=0)
        self.text_widget.pack(fill=tk.BOTH, expand=True)

        self.text_widget.configure(state=tk.DISABLED)  # start readonly

        self.play_frame()

    def play_frame(self):
        frame_file = self.frames[self.index]
        with open(frame_file, "r", encoding="utf-8") as f:
            content = f.read()

        self.text_widget.configure(state=tk.NORMAL)
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert(tk.END, content)
        self.text_widget.configure(state=tk.DISABLED)

        self.index = (self.index + 1) % len(self.frames)
        self.after(DELAY, self.play_frame)

if __name__ == "__main__":
    player = ASCIIPlayer(ascii_files)
    player.mainloop()
