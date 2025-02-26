from django.shortcuts import render
from .models import Department
from django.core.paginator import Paginator


def department_tree(request):
    """Выводим все подразделения и работников."""
    departments_paginator = Department.objects.prefetch_related(
        "employees").all()

    # Добавим пагинатор
    paginator = Paginator(departments_paginator, 2)

    # Получим текущую страницу из GET-параметров
    page_number = request.GET.get('page')
    departments_paginator_list = paginator.get_page(page_number)
    context = {
        'departments_paginator_list': departments_paginator_list
    }
    return render(request, "employees/tree.html", context)
