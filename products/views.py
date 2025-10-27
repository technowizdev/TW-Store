from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Review
from django.db.models import Avg

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'products/product_list.html', {'products': products, 'categories': categories})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    reviews = product.reviews.all().order_by('-created_at')

    # Average rating
    avg = reviews.aggregate(Avg('rating'))['rating__avg']
    avg_rating = round(avg, 1) if avg else 0

    # Calculate stars for average rating
    full_stars = range(int(avg_rating))
    half_star = (avg_rating - int(avg_rating)) >= 0.5
    empty_stars = range(5 - int(avg_rating) - (1 if half_star else 0))

    # Calculate stars for each individual review
    for review in reviews:
        review.full_stars = range(int(review.rating))
        review.half_star = (review.rating - int(review.rating)) >= 0.5
        review.empty_stars = range(5 - int(review.rating) - (1 if review.half_star else 0))

    context = {
        'product': product,
        'reviews': reviews,
        'avg_rating': avg_rating,
        'full_stars': full_stars,
        'half_star': half_star,
        'empty_stars': empty_stars,
    }

    return render(request, 'products/product_detail.html', context)

def add_review(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == "POST":
        user_name = request.POST.get("user_name")
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")

        # Save review
        Review.objects.create(
            product=product,
            user_name=user_name,
            rating=rating,
            comment=comment
        )
        return redirect('product_detail', slug=slug)

    # return redirect('product_detail', slug=slug)