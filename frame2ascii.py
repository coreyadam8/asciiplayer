import os
import time
from pathlib import Path
from PIL import Image
import numpy as np

# Configuration
FRAME_DIR = Path("frames")
ASCII_DIR = Path("ascii_frames")
WIDTH, HEIGHT = 80, 40
FPS = 24

# ASCII characters from dark to light
ASCII_CHARS = "@%#*+=-:. "

ASCII_DIR.mkdir(exist_ok=True)

def image_to_ascii(image_path, width=WIDTH, height=HEIGHT):
    image = Image.open(image_path).convert("L")  # grayscale
    image = image.resize((width, height))

    pixels = np.array(image)
    # Normalize pixels to range 0-9 for ASCII chars index
    normalized = (pixels / 255) * (len(ASCII_CHARS) - 1)
    normalized = normalized.astype(int)

    lines = []
    for row in normalized:
        line = "".join(ASCII_CHARS[p] for p in row)
        lines.append(line)
    return "\n".join(lines)

print("[*] Converting frames to ASCII text files...")

frame_files = sorted(FRAME_DIR.glob("frame_*.png"))

for frame_file in frame_files:
    ascii_art = image_to_ascii(frame_file, WIDTH, HEIGHT)
    output_file = ASCII_DIR / f"{frame_file.stem}.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(ascii_art)

print(f"[*] Conversion done! ASCII frames saved to {ASCII_DIR}")

print("[*] Playing ASCII animation... (press Ctrl+C to stop)")

ascii_files = sorted(ASCII_DIR.glob("*.txt"))

try:
    while True:
        for ascii_file in ascii_files:
            os.system("cls" if os.name == "nt" else "clear")
            with open(ascii_file, "r", encoding="utf-8") as f:
                print(f.read())
            time.sleep(1 / FPS)
except KeyboardInterrupt:
    print("\n[*] Animation stopped.")
