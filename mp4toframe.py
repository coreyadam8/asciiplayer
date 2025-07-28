import os
import subprocess
from pathlib import Path

# --- CONFIG ---
VIDEO_FILE = r"C:\Users\C\Downloads\New folder\rickroll\rickroll.mp4"
FRAME_DIR = Path("frames")
ASCII_DIR = Path("ascii_frames")
WIDTH, HEIGHT = 80, 40
FPS = 24

# --- Ensure directories exist ---
FRAME_DIR.mkdir(exist_ok=True)
ASCII_DIR.mkdir(exist_ok=True)

# --- Extract frames with ffmpeg ---
print("[*] Extracting frames with ffmpeg...")
subprocess.run([
    "ffmpeg", "-i", VIDEO_FILE,
    "-vf", f"scale={WIDTH}:{HEIGHT},fps={FPS}",
    str(FRAME_DIR / "frame_%04d.png")
])

# --- Convert frames to ASCII using img2txt ---
frame_files = sorted(FRAME_DIR.glob("frame_*.png"))

print("[*] Converting frames to ASCII with img2txt...")
for frame_file in frame_files:
    output_file = ASCII_DIR / f"{frame_file.stem}.txt"
    with open(output_file, "w") as out:
        subprocess.run(
            ["img2txt", "--width", str(WIDTH), "--height", str(HEIGHT), str(frame_file)],
            stdout=out
        )

print(f"[*] Done. ASCII frames saved to: {ASCII_DIR}")
