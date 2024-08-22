# Hotel Property AI Rewriter

> This Django project uses Ollama to rewrite hotel property titles and descriptions, and generate summaries for each property.

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Speak2/Django_assignment/graphs/commit-activity)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Speak2/Django_assignment/issues)


## Table of Contents

1. [Key Features](#key-features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage](#usage)
6. [Database Creation guide ](#database-creation-guide )
9. [Project Structure](#project-structure)
10. [Technologies Used](#technologies-used)
11. [Troubleshooting](#troubleshooting)
11. [Development Tools](#development-tools)
12. [Author](#authors)
13. [License](#license)

## Key Features

- Automated rewriting of property titles and descriptions using AI
- Generation of property summaries
- Integration with Ollama for natural language processing
- PostgreSQL database for efficient data storage and retrieval
- Django management command for easy execution of the rewriting process

## Prerequisites
Tools and packages required to successfully install this project:
- Python 3.8+
- Django 3.2+
- PostgreSQL
- Ollama

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Speak2/llm_project
   cd <project-directory>
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Configure the project (see Configuration section below)

6. Run migrations:
   ```
   python manage.py migrate
   ```

7. Install and start Ollama:
   Follow the instructions at [Ollama's official website](https://ollama.ai/download) to install Ollama on your system.

8. Pull the required model (e.g., gemma2:2b):
   ```
   ollama pull gemma2:2b
   ```


## Configuration

1. **Create a New `config.py` File**:

   Please create a new file named `config.py` in the `Django_assignment/config.py` directory. Include the following code in this file, ensuring that you replace the placeholders with your specific database configuration details:
   ```python
   DJANGO_DATABASE_CONFIG = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'database_name',
    'USER': 'usernam',
    'PASSWORD': 'password',
    'HOST': 'localhost',
    'PORT': 'port_address',
   }
   ```

   Make sure to adjust these settings according to your PostgreSQL configuration.

2. For reference follow the `config-sample.txt` file in the root directory.
 
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

   ```bash
   llm_project/
   │
   ├── hotel_rewriter/   
   │   ├── management
   │   │  └── commands    
   │   │      └── rewrite_properties.py
   │   ├── migrations/
   │   ├── __init__.py                   
   │   ├── admin.py 
   │   ├── apps.py
   │   ├── models.py
   │   └── views.py
   ├── llm_project/   
   │   ├── __init__.py       
   │   ├── settings.py 
   │   ├── urls.py
   │   └── wsgi.py 
   ├── readme_img/ 
   ├── manage.py
   ├── config.py     # config.py file should be created here
   ├── config-sample.txt           
   ├── README.md   
   ├── requirements.txt      
   └── LICIENSE            
   ```


## Technologies Used

- Python 3.8+
- Django 3.2+
- PostgreSQL 12+
- Ollama (for AI-powered text generation)
- psycopg2 (PostgreSQL adapter for Python)

## Troubleshooting

If you encounter connection issues with Ollama, ensure that:
1. Ollama is running on your system
2. The Ollama service is accessible at `http://localhost:11434` (default)
3. The model specified in the command (e.g., "gemma2:2b") is available in your Ollama setup

## Development Tools

- Linter: flake8 (install from VS Code extension store)
- Code formatter: autopep8 (install from VS Code extension store)

linter and code code formatter has been used to maintain code quality

## Authors

This project is for Django admin panel practice created by me for assignment purposes during my internship days at w3 egnineers ltd. 
 
Nahid Mahamud  – nahid.nm91@gmail.com
 
 You can find me here at:
[Github](https://github.com/Speak2) 


## License

A short snippet describing the license (MIT, Apache etc).

This project is licensed under the MIT License - see the LICENSE.md file for details

MIT © Nahid Mahamud
