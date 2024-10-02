# util.py
import markdown2

def get_entry(title):
    try:
        with open(f"entries/{title}.md", "r") as f:
            return markdown2.markdown(f.read())
    except FileNotFoundError:
        return None
