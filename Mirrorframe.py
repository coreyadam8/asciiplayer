from pathlib import Path
import shutil

# Configuration
frame_dir = Path("frames")
start = 4821
end = 4877

# Output filenames start after original end
next_frame_num = end + 1

# Create reversed frame list (excluding the last frame to avoid a repeat)
frames_to_duplicate = list(range(end - 1, start - 1, -1))  # 4876 → 4821

for i, original_num in enumerate(frames_to_duplicate):
    src = frame_dir / f"frame_{original_num:04}.png"
    dst = frame_dir / f"frame_{next_frame_num + i:04}.png"

    if not src.exists():
        print(f"[!] Missing: {src}")
        continue

    shutil.copy(src, dst)
    print(f"[*] Copied {src.name} -> {dst.name}")

print("Frame duplication completed.")
