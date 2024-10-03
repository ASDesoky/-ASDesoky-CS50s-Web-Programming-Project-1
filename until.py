import markdown2
import os

def list_entries():
    return [entry.replace(".md", "") for entry in os.listdir("entries") if entry.endswith(".md")]

def get_entry(title):
    try:
        with open(f"entries/{title}.md", "r") as f:
            return markdown2.markdown(f.read())
    except FileNotFoundError:
        return None

def save_entry(title, content):
    with open(f"entries/{title}.md", "w") as f:
        f.write(content)
