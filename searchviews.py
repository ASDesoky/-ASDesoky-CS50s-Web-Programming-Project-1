# views.py
def search(request):
    query = request.GET.get("q", "")
    if util.get_entry(query):
        return redirect("entry", title=query)
    else:
        results = [entry for entry in util.list_entries() if query.lower() in entry.lower()]
        return render(request, "encyclopedia/search.html", {
            "query": query,
            "results": results
        })
