from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, HttpResponseRedirect, HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from .forms import ProductCategoryUpdateForm

# Create your views here.


@csrf_exempt
def category(request):
    query = "SELECT * FROM product_category"
    result = execute_query(query)
    context = {'categories': result}
    return render(request, 'category.html', context)


@csrf_exempt
def details(request, product_category):
    query = f"SELECT * FROM product WHERE category='{product_category}'"
    query1 = f"SELECT * FROM product_category WHERE nama_kategori='{product_category}'"
    result = execute_query(query)
    result1 = execute_query(query1)
    context = {'products': result, 'deskripsi': result1[0]}
    return render(request, 'details.html', context)


@csrf_exempt
def update_desc(request, product_category):
    if request.method == 'POST':
        form = ProductCategoryUpdateForm(request.POST)
        if form.is_valid():
            desc = form.cleaned_data['desc']
            with connection.cursor() as cursor:
                cursor.execute(f"UPDATE product_category SET deskripsi = '{desc}' WHERE nama_kategori = '{product_category}';")
            print("sukses")
            return HttpResponseRedirect(f'/api/categories/details/{product_category}')
    else:
        form = ProductCategoryUpdateForm()

    context = {'category': product_category, 'form': form}
    return render(request, 'forms.html', context)


def execute_query(query):
    result = None
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result
