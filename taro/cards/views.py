from django.shortcuts import render
from .models import CardsDesk, Card

from django.views.generic import ListView, DetailView


class CardsDeskListView(ListView):
    model = CardsDesk
    template_name = "cards.html"
    context_object_name = 'desk_list'

    def get_queryset(self):
        qs = CardsDesk.objects.all()
        return qs

class CardsDeskDetailView(ListView):
    model = Card
    template_name = "card_detail.html"
    context_object_name = 'cards_list'
    slug_field = 'desk_slug'
    slug_url_kwarg = 'desk_slug'
    

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["desk"] = CardsDesk.objects.get(desk_slug=self.kwargs['desk_slug'])

        context['Woods_list'] = Card.objects.all().filter(desk__desk_slug=self.kwargs['desk_slug'], card_type__startswith = 'Woods')
        context['Swords_list'] = Card.objects.all().filter(desk__desk_slug=self.kwargs['desk_slug'], card_type__startswith = 'Swords')
        context['Penta_list'] = Card.objects.all().filter(desk__desk_slug=self.kwargs['desk_slug'], card_type__startswith = 'Penta')
        context['Cups_list'] = Card.objects.all().filter(desk__desk_slug=self.kwargs['desk_slug'], card_type__startswith = 'Cups')
        context['Grant_list'] = Card.objects.all().filter(desk__desk_slug=self.kwargs['desk_slug'], card_type__startswith = 'Grant')

        return context
    

    def get_queryset(self):

        desk = CardsDesk.objects.get(desk_slug=self.kwargs['desk_slug'])
        cards = Card.objects.filter(desk=desk)
        qs = cards
        return qs
    


class CardDetailView(DetailView):
    model = Card
    template_name = "card-desk-detail.html"
    context_object_name = "card"
    slug_field = 'desk_slug'
    slug_url_kwarg = 'desk_slug'

    
    