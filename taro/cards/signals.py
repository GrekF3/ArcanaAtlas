from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CardsDesk, Card, CHOICES
 
 
@receiver(post_save, sender=CardsDesk)
def create_cards_for_deck(sender, instance, created, **kwargs):
    if created:
        types = []
        for card_type in CHOICES:
            for type in card_type[1]:
                types.append(type)
        cards = (Card(card_type=card_type[0], desk=instance) for card_type in types)

        Card.objects.bulk_create(cards)
        