# One Line, One Laugh — make.fun entry
# Writes the entry line to /output/entry.txt (UTF-8, one line, <= 200 chars).
import os


LINE = "My smoke detector has never detected smoke. It just beeps at 3 AM to remind me it still exists."


def main():
    chars = len(LINE)
    if chars < 1 or chars > 200:
        raise ValueError(f"Line is {chars} chars, must be 1-200.")
    if not LINE.strip() or "\n" in LINE or "\r" in LINE:
        raise ValueError("Line must be non-blank and a single line.")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Read-back check: exactly one line, same content, valid UTF-8.
    with open("/output/entry.txt", encoding="utf-8") as f:
        back = f.read()
    assert back == LINE + "\n", "entry.txt round-trip mismatch"
    assert back.count("\n") == 1, "entry.txt must be exactly one line"
    print(f"Wrote {chars} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
