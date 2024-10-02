# views.py
import random

def random_page(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return redirect("entry", title=random_entry)

