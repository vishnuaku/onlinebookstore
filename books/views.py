from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Order
from django.urls import reverse_lazy
from django.db.models import Q # for search method
from django.http import JsonResponse
from django.views.generic import View
import json
from .forms import *
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail


# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Book  # Replace YourModel with the actual name of your model

class UpdateRatingView(View):
    def post(self, request, pk):
        book = Book.objects.get(pk=pk)
        rating = request.POST.get('rating')
        if rating:
            # Assuming rating is an integer between 1 and 5
            book.total_rating += int(rating)
            book.total_ratings += 1
            book.save()
        return redirect('detail', pk=pk)


class BooksListView(ListView):
    model = Book
    template_name = 'list.html'


class BooksDetailView(DetailView):
    model = Book
    template_name = 'detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        overall_rating = None
        if book.total_ratings > 0:
            overall_rating = book.total_rating / book.total_ratings
        context['overall_rating'] = overall_rating
        return context
class SearchResultsListView(ListView):
	model = Book
	template_name = 'search_results.html'

	def get_queryset(self): # new
		query = self.request.GET.get('q')
		return Book.objects.filter(
		Q(title__icontains=query) | Q(author__icontains=query)
		)

class BookCheckoutView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'checkout.html'
    login_url= 'login'


def paymentComplete(request):
	body = json.loads(request.body)
	print('BODY:', body)
	product = Book.objects.get(id=body['productId'])
	Order.objects.create(
		product=product
	)
	return JsonResponse('Payment completed!', safe=False)


def Payment(request):
	form = PaymentForm()
	if request.method == 'POST':
		form = PaymentForm(request.POST)
		if form.is_valid():
			subject = 'Payment Done'
			message = "Transaction id {{form.transid}}"
			recipient = '2200033283cseh@gmail.com'
			send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
			messages.success(request, 'Your order will be updated after payment verification')
			return redirect('Payment')
	return render(request, 'payment_success.html')

