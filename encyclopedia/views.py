import re, random

from django.shortcuts import render
from markdown2 import Markdown
from . import util

from django.core.files.storage import default_storage
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.contrib import messages

# Class for search form
class SearchForm(forms.Form):
    text = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Search Encyclopedia",
                                                                   "class": "search"}))

# Class for new page form
class NewPage(forms.Form):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Title", "class": "form-control"}))
    text = forms.CharField(label="", widget=forms.Textarea(attrs={"placeholder": "Text", "class": "form-control"}))

# Class for edit page form
class EditPage(forms.Form):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Title", "class": "form-control",
                                                                    'readonly':'readonly'}))
    text = forms.CharField(label="", widget=forms.Textarea(attrs={"placeholder": "Text", "class": "form-control"}))

# Index function
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(), "form": SearchForm()
    })

# To redirect /wiki
def wikiIndex(request):
    return HttpResponseRedirect(reverse("index"))

# wiki/<str:title>
def wiki(request, title):
    # util.py :)
    # Get a list of all articles
    _, filenames = default_storage.listdir("entries")
    titleList = list(sorted(re.sub(r"\.md$", "", filename) for filename in filenames if filename.endswith(".md")))
    # Variable for title
    textTitle = None
    # Go through the entire list and compare the title
    for t in titleList:
        if t.upper() == title.upper():
            textTitle = t
    # Get text from file
    pageMd = util.get_entry(title)
    # If the file is not found, then we report an error
    if pageMd is None:
        return render(request, "encyclopedia/error.html", {
            "msg": "Page not found", "form": SearchForm()
        })
    # https://github.com/trentm/python-markdown2#quick-usage
    md = Markdown()
    pageHtml = md.convert(pageMd)
    # Go to article page
    return render(request, "encyclopedia/page.html", {
        "title": textTitle, "text": pageHtml, "form": SearchForm()
    })

# Random page function
def rand(request):
    list = util.list_entries()

    return HttpResponseRedirect(reverse("wiki", args=[random.choice(list)]))

# Search function
def search(request):
    if request.method == "POST":
        # Get form data
        form = SearchForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            # Get a list of all articles
            listForSearch = util.list_entries()
            resultSearch = []
            # Check list, go to page if matches case insensitive
            # otherwise we add all the substrings to the list
            for a in listForSearch:
                if text.lower() == a.lower():
                    return HttpResponseRedirect(reverse("wiki", args=[text]))
                if text.lower() in a.lower():
                    resultSearch.append(a)
            # If nothing found render msg
            if len(resultSearch) == 0:
                return render(request, "encyclopedia/resultSearch.html", {
                    "result": resultSearch, "form": SearchForm(), "noResult": "Nothing found. Try again."
                })
            # Render result search
            return render(request, "encyclopedia/resultSearch.html", {
                "result": resultSearch, "form": SearchForm()
            })
        # If no valid redirect index
        return HttpResponseRedirect(reverse("index"))
    # Get
    return render(request, "encyclopedia/error.html", {
        "msg": "Page not found", "form": SearchForm()
    })

# Function for create new page
def newPage(request):
    if request.method == "POST":
        # Get form data
        form = NewPage(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            text = form.cleaned_data["text"]
            # list for check
            checkTitle = util.list_entries()
            # If the header exists, displays a message
            for t in checkTitle:
                if title.lower() == t.lower():
                    messages.warning(request, "A page with that title already exists! Change the title.", extra_tags="danger")
                    return render(request, "encyclopedia/newPage.html", {
                        "form": SearchForm(), "formNewPage": form
                    })
            # I ran into a problem when python added a caret character and did it after each edit.
            # This led to a lot of new lines. I managed to solve the problem this way.
            listTextNoR = text.split("\r")
            stringTextNoR = ''.join(listTextNoR)
            # Save file
            util.save_entry(title, stringTextNoR)
            # Go to the page of the created record
            return HttpResponseRedirect(reverse("wiki", args=[title]))
    # If get, then make a page to create a new entry
    return render(request, "encyclopedia/newPage.html", {
        "form": SearchForm(), "formNewPage": NewPage()
    })

# Function for edit page
def editPage(request, title):
    if request.method == "GET":
        # util.py :)
        # Get a list of all articles
        _, filenames = default_storage.listdir("entries")
        titleList = list(sorted(re.sub(r"\.md$", "", filename) for filename in filenames if filename.endswith(".md")))
        # Variable for title
        textTitle = None
        # If the title is found, go to the post editing page. Filling the form with existing text
        for t in titleList:
            if t.upper() == title.upper():
                textTitle = t

        pageMd = util.get_entry(title)

        dict = {'title': textTitle, 'text': pageMd}

        form = EditPage(initial = dict)

        return render(request, "encyclopedia/edit.html", {
            "form": SearchForm(), "formEditPage": form
        })

    if request.method == "POST":
        # Get data form
        form = EditPage(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            text = form.cleaned_data["text"]
            # I ran into a problem when python added a caret character and did it after each edit.
            # This led to a lot of new lines. I managed to solve the problem this way.
            listTextNoR = text.split("\r")
            stringTextNoR = ''.join(listTextNoR)
            # Save page
            util.save_entry(title, stringTextNoR)
            # Go to page
            return HttpResponseRedirect(reverse("wiki", args=[title]))