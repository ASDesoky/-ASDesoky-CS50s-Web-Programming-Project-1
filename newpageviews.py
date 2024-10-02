# views.py
def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        if util.get_entry(title):
            return render(request, "encyclopedia/create.html", {
                "error": "An entry with this title already exists."
            })
        util.save_entry(title, content)
        return redirect("entry", title=title)
    return render(request, "encyclopedia/create.html")
