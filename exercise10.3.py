from pathlib import Path

Path("pi_digits.txt").write_text(
    "3.1415926535\n"
    "  8979323846\n"
    "  2643383279\n"
)

print("=== file_reader.py ===")
path = Path("pi_digits.txt")
contents = path.read_text()

for line in contents.splitlines():
    print(line)

print()
print("=== pi_string.py ===")
pi_string = ""
for line in contents.splitlines():
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))