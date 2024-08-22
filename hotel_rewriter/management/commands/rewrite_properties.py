from django.core.management.base import BaseCommand
from hotel_rewriter.models import Property, PropertySummary
import ollama


class Command(BaseCommand):
    help = 'Rewrites property titles and descriptions, and generates summaries using Ollama'

    def handle(self, *args, **options):
        model = "gemma:2b"  # Make sure this matches the model you have in Ollama

        # Create an Ollama client with the correct host and port
        ollama_client = ollama.Client(host="http://localhost:8001")

        properties = Property.objects.all()
        for property in properties:
            # Rewrite title
            title_prompt = f"Rewrite the following property title to make it more appealing: {property.title}"
            title_response = ollama_client.generate(
                model=model, prompt=title_prompt)
            property.title = title_response['response'].strip()

            # Rewrite description
            desc_prompt = f"Rewrite the following property description to make it more engaging and informative: {property.description}"
            desc_response = ollama_client.generate(
                model=model, prompt=desc_prompt)
            property.description = desc_response['response'].strip()

            property.save()

            # Generate summary
            summary_prompt = f"Summarize the following property information:\nTitle: {property.title}\nDescription: {property.description}\nAmenities: {', '.join(property.amenities.values_list('name', flat=True))}\nLocations: {', '.join(property.locations.values_list('name', flat=True))}"
            summary_response = ollama_client.generate(
                model=model, prompt=summary_prompt)

            PropertySummary.objects.update_or_create(
                property=property,
                defaults={'summary': summary_response['response'].strip()}
            )

            self.stdout.write(self.style.SUCCESS(
                f'Successfully processed property {property.id}'))

        self.stdout.write(self.style.SUCCESS(
            'All properties have been processed'))
