import requests
from django.core.management.base import BaseCommand
from planets.models import Planet  # Replace with your actual app name

class Command(BaseCommand):
    help = 'Fetch planet data from SWAPI GraphQL and store it in the database'

    def handle(self, *args, **kwargs):
        url = 'https://swapi-graphql.netlify.app/.netlify/functions/index'
        # Minified query with operation name
        query = "query Query { allPlanets { planets { name population terrains climates } } }"
        
        # Send GET request with query as a URL parameter
        response = requests.get(url, params={'query': query})

        try:
            data = response.json()
        except ValueError:
            self.stdout.write(self.style.ERROR("Invalid JSON response from SWAPI"))
            return

        if 'data' not in data or 'allPlanets' not in data['data']:
            self.stdout.write(self.style.ERROR(f"Failed to fetch data from SWAPI\nResponse: {data}"))
            return

        planets = data['data']['allPlanets']['planets']

        for planet in planets:
            # Handle null values appropriately
            population = planet.get('population')
            # Convert population to integer if possible, else None
            if population is not None:
                try:
                    population = int(population)
                except (TypeError, ValueError):
                    population = None

            # Convert list fields to comma-separated strings (if not null)
            terrains = ', '.join(planet['terrains']) if planet.get('terrains') else ''
            climates = ', '.join(planet['climates']) if planet.get('climates') else ''

            Planet.objects.update_or_create(
                name=planet['name'],
                defaults={
                    'population': population,
                    'terrains': terrains,
                    'climates': climates,
                }
            )

        self.stdout.write(self.style.SUCCESS("Successfully fetched and saved planet data."))