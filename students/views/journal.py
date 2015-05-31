# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Journal
def journal_list(request):
    return render(request, 'students/journal_list.html', {})

def journal_view(request, gid):
    return HttpResponse('<h1>View Journal %s</h1>' % gid)

