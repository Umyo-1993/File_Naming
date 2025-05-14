# newfile.py
import os
from datetime import datetime

commit = input("Please enter your commit message: ").strip()
version = input("Please enter your version of the file here: ").strip()

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

safe_commit = "".join(c for c in commit if c.isalnum() or c in (" ", "_", "-")).rstrip().replace(" ", "_")
safe_version = "".join(c for c in version if c.isalnum() or c in ("_", "-", "."))

# Default extension (change if needed)
file_name = f"{safe_commit}_{timestamp}_v{safe_version}.txt"

# Create the file
with open(file_name, "w") as f:
    f.write("")  # Add default content if needed

print("✅ Created:", file_name)
