# Author U Mo , dated 13/05/25
from datetime import datetime
# Get commit message and version from user
commit = input("Please enter your commit message: ").strip()
version = input("Please enter your version of the file here: ").strip()
# Get current date and time
now = datetime.now()

# Format for safe filename
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

# Sanitize commit message and version to be filename-safe
safe_commit = "".join(c for c in commit if c.isalnum() or c in (" ", "_", "-")).rstrip()
safe_version = "".join(c for c in version if c.isalnum() or c in ("_", "-", "."))  # allow version like 1.0.0
# Build the filename
file_name = f"{safe_commit}_{timestamp}_v{safe_version}"
print("Your file name is:", file_name)
