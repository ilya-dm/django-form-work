from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):

    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    form = ReviewForm
    list_reviews = Review.objects.filter(product_id=pk)
    request.session['is_review_exist'] = list()
    for i in list_reviews:
        if i.product_id not in request.session['is_review_exist']:
            request.session['is_review_exist'].append(i.product_id)

    context = {
        'form': form,
        'product': product,
        'reviews': list_reviews,
    }

    if request.method == "GET":
        if product.id in request.session['is_review_exist']:
            context.update({"is_review_exist": True})

        return render(request, template, context)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = Review()
        if form.is_valid():
            review.text = form.cleaned_data.get('text')
            review.product_id = pk
            review.save()
            request.session["is_review_exist"].append(pk)
            request.session.save()

        return redirect(request.path)
