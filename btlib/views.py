from django.shortcuts import render_to_response, get_object_or_404
from btlib.models import *
from django.conf import settings

"""
Main structure of the page will look like:

btlib
├── About
├── Feed
│   └── User
├── Index
├── Login
│   ├── Register
│   └── Reset
├── Novel
│   └── Language
│       └── Volume
│           ├── Chapter
│           │   └── Translator
│           └── Full
│               └── Translator
├── Project
│   └── Type
│       └── AppendNovel
└── User
    ├── Favorites
    ├── News
    ├── Settings
    └── Talk
"""

"""Main Page View

"""


def index(request):
    ln_list = Project.objects.filter(language__pk = settings.MAIN_LN_LANG)
    lang_list = Language.objects.exclude(pk = settings.MAIN_LN_LANG)
    return render_to_response('btlib/index.html', {'ln_list':ln_list, 'lang_list':lang_list})

