from django.core.management.base import BaseCommand
from hotel_rewriter.models import Property, PropertySummary
import ollama


class Command(BaseCommand):
    help = (
        'Rewrites property titles and descriptions, and generates'
        ' summaries using Ollama'
    )

    def handle(self, *args, **options):
        model = "gemma2:2b"

        properties = Property.objects.all()
        for property in properties:
            # Rewrite title
            title_prompt = (
                "Be consistent: just make up a new hotel title from the given "
                "hotel title, nothing else, and don't provide any formatting. "
                f"Try to make the title appealing: {property.title}"
            )
            title_response = ollama.generate(
                model=model, prompt=title_prompt)
            property.title = title_response['response'].strip()
            print(property.title)

            # Rewrite description
            desc_prompt = (
                "Be consistent: just write the hotel description in plain text"
                " using the hotel title and its location. It should be "
                "appealing; lie if you have to, and don't include the hotel"
                f" title in the response. property-title: {property.title} "
                f"and location: {property.locations}"
            )
            desc_response = ollama.generate(model=model, prompt=desc_prompt)
            property.description = desc_response['response'].strip()

            property.save()

            # Generate summary
            summary_prompt = (
                "Be consistent: Summarize the following property information "
                f"in two to three sentences:\nTitle: {property.title}\n"
                f"Description: {property.description}\nLocations: "
                f"{''.join(property.locations.values_list('name', flat=True))}"
            )
            summary_response = ollama.generate(
                model=model, prompt=summary_prompt)

            PropertySummary.objects.update_or_create(
                property=property,
                defaults={'summary': summary_response['response'].strip()}
            )
            # print(summary_response['response'].strip())

            self.stdout.write(self.style.SUCCESS(
                f'Successfully processed property {property.id}'))

        self.stdout.write(self.style.SUCCESS(
            'All properties have been processed'))
