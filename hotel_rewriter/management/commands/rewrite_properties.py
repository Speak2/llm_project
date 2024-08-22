# core/management/commands/rewrite_properties.py

from django.core.management.base import BaseCommand
from hotel_rewriter.models import Property, PropertySummary
import ollama


class Command(BaseCommand):
    help = 'Rewrites property titles and descriptions, and generates summaries using Ollama'

    def handle(self, *args, **options):
        model = "llama2"  # You can change this to any model available in Ollama

        properties = Property.objects.all()
        for property in properties:
            # Rewrite title
            title_prompt = f"Rewrite the following property title to make it more appealing: {property.title}"
            title_response = ollama.generate(model=model, prompt=title_prompt)
            property.title = title_response['response'].strip()

            # Rewrite description
            desc_prompt = f"Rewrite the following property description to make it more engaging and informative: {property.description}"
            desc_response = ollama.generate(model=model, prompt=desc_prompt)
            property.description = desc_response['response'].strip()

            property.save()

            # Generate summary
            summary_prompt = f"Summarize the following property information:\nTitle: {property.title}\nDescription: {property.description}\nAmenities: {', '.join(property.amenities.values_list('name', flat=True))}\nLocations: {', '.join(property.locations.values_list('name', flat=True))}"
            summary_response = ollama.generate(
                model=model, prompt=summary_prompt)

            PropertySummary.objects.update_or_create(
                property=property,
                defaults={'summary': summary_response['response'].strip()}
            )

            self.stdout.write(self.style.SUCCESS(
                f'Successfully processed property {property.id}'))

        self.stdout.write(self.style.SUCCESS(
            'All properties have been processed'))
