from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Department


def build_department_tree(departments, parent=None):
    """Рекурсивно строим дерево подразделений."""
    tree = []
    for department in departments:
        if department.parent == parent:
            children = build_department_tree(departments, department)
            tree.append({"department": department, "children": children})
    return tree


def department_tree(request):
    """Выводим дерево подразделений и работников."""
    all_departments = Department.objects.prefetch_related("employees").all()
    department_tree_structure = build_department_tree(all_departments)

    paginator = Paginator(department_tree_structure, 5)
    page_number = request.GET.get("page")
    departments_paginator_list = paginator.get_page(page_number)
    context = {"departments": departments_paginator_list}
    return render(
        request,
        "employees/tree.html",
        context
    )
