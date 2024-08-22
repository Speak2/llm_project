# Hotel Property Rewriter

This Django project uses Ollama to rewrite hotel property titles and descriptions, and generate summaries for each property.



## Prerequisites

- Python 3.8+
- PostgreSQL 12+
- Ollama

## Setup



## Database Creation Guide

1. Install PostgreSQL if you haven't already.

2. Log in to PostgreSQL as a superuser:
   ```
   sudo -u postgres psql
   ```

3. Create a new database:
   ```sql
   CREATE DATABASE notun_database;
   ```

4. Create a new user (if needed):
   ```sql
   CREATE USER postgres WITH PASSWORD 'p@stgress';
   ```

5. Grant privileges to the user:
   ```sql
   GRANT ALL PRIVILEGES ON DATABASE notun_database TO postgres;
   ```

6. Exit PostgreSQL:
   ```
   \q
   ```

## Configuration

1. Create a `config.py` file in your project's root directory with the following content:

   ```python
   DJANGO_DATABASE_CONFIG = {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'notun_database',
       'USER': 'postgres',
       'PASSWORD': 'p@stgress',
       'HOST': 'localhost',
       'PORT': '5433',
   }
   ```

2. In your project's `settings.py`, import and use this configuration:

   ```python
   from config import DJANGO_DATABASE_CONFIG

   DATABASES = {
       'default': DJANGO_DATABASE_CONFIG
   }
   ```

3. Ensure that your `settings.py` includes the necessary apps and middleware for your project.

## Usage

1. Ensure Ollama is running:
   ```
   ollama run gemma:2b
   ```

2. Run the property rewriter command:
   ```
   python manage.py rewrite_properties
   ```

This command will:
- Rewrite the title and description of each property in the database
- Generate a summary for each property
- Save the updated information and new summaries to the database

## Project Structure

- `hotel_rewriter/`: Main Django app
  - `models.py`: Contains the database models (Property, PropertySummary, etc.)
  - `management/commands/rewrite_properties.py`: Contains the Django management command for rewriting properties
- `config.py`: Contains database configuration
- `requirements.txt`: List of Python dependencies

## Troubleshooting

If you encounter connection issues with Ollama, ensure that:
1. Ollama is running on your system
2. The Ollama service is accessible at `http://localhost:11434` (default)
3. The model specified in the command (e.g., "gemma:2b") is available in your Ollama setup

For database connection issues:
1. Verify that PostgreSQL is running on port 5433
2. Check that the database credentials in `config.py` are correct
3. Ensure that the `postgres` user has the necessary permissions on `notun_database`

## Contributing

[Include instructions for how others can contribute to your project]

## License

[Specify the license under which your project is released]
