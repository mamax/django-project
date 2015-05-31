# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


# Views for Students
def students_list(request):
        students = (
                     {'id': 1,
                     'first_name': u'Віталій',
                     'last_name': u'Подоба',
                     'ticket': 235,
                     'image': 'img/me.jpeg'},

                     {'id': 2,
                     'first_name': u'Андрій',
                     'last_name': u'Корост',
                     'ticket': 2123,
                     'image': 'img/piv.png'},

                     {'id': 3,
                     'first_name': u'Андрій',
                     'last_name': u'Іванюк',
                     'ticket': 254,
                     'image': 'img/pod3.jpg'},
                    )
        return render(request, 'students/students_list.html',{'students': students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# Views for Groups
def groups_list(request):
        groups = (      {'id': 1,
                     'name': u'MтаM-21',
                     'captain': u'Подоба'},

                     {'id': 2,
                     'name': u'MтаM-22',
                     'captain': u'Ігор'},

                     {'id': 3,
                     'name': u'MтаM-23',
                     'captain': u'Віталій'},
                )
        return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)

# Views for Journal
def journal_list(request):
    return HttpResponse('<h1>Journal List</h1>')

def journal_view(request, gid):
    return HttpResponse('<h1>View Journal %s</h1>' % gid)

