import os

LINES = [
    "I am sorry I deleted your photos.",
    "In my defense, they were all the same sunset, and I have already apologized for that one too.",
]

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = "\n".join(LINES)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {os.path.join(out_dir, 'entry.txt')} ({len(text)} characters)")

if __name__ == "__main__":
    main()
