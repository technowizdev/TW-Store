from django.shortcuts import render, redirect, get_object_or_404
from .forms import LeadForm
from products.models import Product

def lead_create(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.product = product
            lead.save()
            # Optional: Email logic here
            return redirect('lead_thank_you')
    else:
        form = LeadForm(initial={'product': product})
    return render(request, 'leads/lead_form.html', {'form': form, 'product': product})

def lead_thank_you(request):
    return render(request, 'leads/thank_you.html')
