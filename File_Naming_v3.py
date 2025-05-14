import os
from datetime import datetime
# I am using HTML template not to use any thirdparty library
# Get user input
commit = input("Please enter your commit message: ").strip()
version = input("Please enter your version of the file here: ").strip()

# Generate timestamp
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

# Sanitize inputs for filename
safe_commit = "".join(c for c in commit if c.isalnum() or c in (" ", "_", "-")).rstrip().replace(" ", "_")
safe_version = "".join(c for c in version if c.isalnum() or c in ("_", "-", "."))

# Create file name with .doc extension
file_name = f"{safe_commit}_{timestamp}_v{safe_version}.doc"

# Create HTML content
html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Commit Info</title>
</head>
<body>
    <h1>Commit Message Document</h1>
    <p><strong>Commit:</strong> {commit}</p>
    <p><strong>Version:</strong> {version}</p>
    <p><strong>Timestamp:</strong> {timestamp}</p>
</body>
</html>
"""

# Write the content to a .doc file
with open(file_name, "w", encoding="utf-8") as f:
    f.write(html_content)

# Open the file
try:
    if os.name == 'nt':  # Windows
        os.startfile(file_name)
    elif os.name == 'posix':
        import sys
        os.system(f'open "{file_name}"' if sys.platform == 'darwin' else f'xdg-open "{file_name}"')
except Exception as e:
    print("Couldn't open the file automatically:", e)

print("✅ Created and opened:", file_name)
