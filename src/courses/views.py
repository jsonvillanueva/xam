from django.shortcuts import get_object_or_404, redirect, render

from .forms import CourseForm
from .models import Course


def courses_view(request, *args, **kwargs):
    queryset = Course.objects.all()
    context = {
        "course_list": queryset,
    }
    return render(request, "courses.html", context)


def course_detail_view(request, id, *args, **kwargs):
    obj = get_object_or_404(Course, id=id)
    context = {"obj": obj}
    return render(request, "courses/detail.html", context)


def course_create_view(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CourseForm()

    context = {
        "form": form,
    }
    return render(request, "courses/create.html", context)


def course_delete_view(request, id):
    obj = get_object_or_404(Course, id=id)

    if request.method == "POST":
        obj.delete()
        return redirect("../../")
    context = {
        "obj": obj,
    }
    return render(request, "courses/delete.html", context)
