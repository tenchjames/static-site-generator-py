

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# "):
            title = stripped[2:]
            title = title.strip()
            return title
    raise Exception("Title not found")
