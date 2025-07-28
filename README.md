# Rickroll ASCII Player ⚡

This project is a terminal and GUI-based animated player for Rick Astley's "Never Gonna Give You Up" rendered entirely in ASCII art. It also includes optional audio playback embedded directly using base64, allowing you to enjoy the iconic song without requiring any external media files.

Including three tools; mp4toframe.py which converts mp4 to frame files, frame2ascii.py which converts your frames to ascii text files and Mirrorframe.py which will mirror specific frames reversing in sequential order.

## Features

* ▶ Animated playback of frames as ASCII art
* 🎵 Embedded audio using base64 (no external MP3 file needed)
* 🔀 Looping support, reverse frame playback
* 🎨 Python-generated ASCII from images (no need for `img2txt`)
* ✔ Cross-platform: Works on Windows, macOS, and Linux

## How It Works

1. **Frame Extraction**: Video is converted to individual image frames (using ffmpeg).
2. **ASCII Conversion**: Frames are converted to ASCII art using Python (PIL + NumPy).
3. **Playback**:

   * In terminal (CLI)
   * In a custom `tkinter` or `PyQt6` GUI window
   * In the browser via Streamlit
4. **Audio**: Base64-encoded audio is streamed using browser-native playback (Streamlit) or from memory (GUI).

## Installation

```bash
# Clone the repo
https://github.com/your-username/rickroll-ascii

cd rickroll-ascii

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Terminal Player (no audio):

```bash
python asciiplayer.py
```

### rickroll player + base64 never gonna give you up

```bash
python rickrollplayer.py
```

## Customize Your Animation

* Replace frames in `frames/` folder
* Adjust frame range, resolution, and FPS in config
* Use your own audio (convert to base64 and paste into the script)

## License

This project is for educational and parody purposes only. The use of Rick Astley's content falls under fair use. Do not use for commercial redistribution.

---

Never gonna give you up, never gonna let you down ♪
