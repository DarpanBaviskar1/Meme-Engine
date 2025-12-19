# MemeEngine

**MemeEngine** is an autonomous meme generation and scheduling system. It fetches trending topics from online sources, generates humorous meme captions using large language models, overlays them on popular meme templates, and posts them to Instagram automatically on a daily schedule.

This project is developed as part of **Summer RAID 2025** under the **REALM OF ARTIFICIAL INTELLIGENCE AND DATA (RAID)** at **IIT Jodhpur**.

---

## Project Objectives

- Design a modular backend pipeline to automate meme creation.
- Fetch and process trending topics from news and social platforms.
- Generate engaging and humorous captions using LLMs.
- Use predefined meme templates for visual generation.
- Automate the scheduling and posting of memes on Instagram.
- Store all memes and metadata for analytics and future experimentation.

---

## Key Features

- **Trending Topic Ingestion**: NewsAPI, Google Trends (via PyTrends), Twitter (via Tweepy), Reddit (via PRAW).
- **Caption Generation**: Integration with OpenAI or open-source LLMs using prompt-based generation.
- **Meme Composition**: Text overlay on meme templates using Python Imaging Library (Pillow).
- **Post Scheduling**: Celery-based task queue with Redis, or cron-based automation.
- **Instagram Posting**: Uses Instagram Graph API for business accounts to publish memes programmatically.
- **Storage & Analytics**: Meme metadata stored in a PostgreSQL database; images stored via cloud storage (e.g., AWS S3).

---

## Technology Stack

| Component          | Technology / Library           |
|-------------------|--------------------------------|
| Backend Framework | Django, Django REST Framework  |
| Task Scheduling   | Celery + Redis / Cron Jobs     |
| Data Ingestion    | NewsAPI, PyTrends, PRAW, Tweepy|
| NLP & Captioning  | OpenAI GPT / Hugging Face LLMs |
| Image Processing  | Pillow, OpenCV, MemePy         |
| Database          | PostgreSQL                     |
| Instagram Posting | Instagram Graph API            |
| Deployment        | Docker, Gunicorn, Nginx        |

---

## Project Setup

### Prerequisites

- Python 3.10+
- PostgreSQL
- Redis (if using Celery)
- Django
- Virtual environment manager (`venv` or `virtualenv`)

### Development Setup

```bash
# Clone the repository
git clone https://github.com/your-username/memeengine.git
cd MemeEngine/backend

# Create virtual environment
# if you dont have uv already installed install it as astral-uv
uv venv --python 3.12
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file and set your values
cp .env.example .env

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Run development server
python manage.py runserver
