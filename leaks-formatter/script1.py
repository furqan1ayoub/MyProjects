def logins_parser(input_file, output_file):
    try:
        with open(input_file, "r",errors="ignore") as infile: #errors hai ignore them  or we speak utf-8 if you speak garbage i will ignore you
            for line in infile:
                if "/:" in line:
                    parts = line.strip().split("/:", 1)  # only split once
                    if len(parts) == 2:
                        formatted = f"{parts[0]} -> {parts[1]}"
                        save_to_file(output_file, formatted)
                    else:
                        print(f"SKIPPED MALFORMED LINE: {line.strip()}")
    except FileNotFoundError:
        print("❌ File not found. Check the input filename.")
    except Exception as e:
        print("❌ Unexpected error:", e)

def save_to_file(filename, content):
    try:
        with open(filename, "a", ) as outfile:
            outfile.write(content + "\n")
    except Exception as e:
        print("❌ Failed to write to file:", e)

# === RUN SCRIPT ===
if __name__ == "__main__":
    input_filenam=input("ENTER THE FILE-NAME ")
    output_name = input("ENTER OUTPUT FILE NAME (no extension): ") + ".txt"
    logins_parser(input_filenam, output_name)
