# 1987 - Creative Narrative Generator

A FastAPI-powered application for generating vivid, creative narratives blending 1980s aesthetics with Tokyo Drift-inspired car culture styling.

## Features

- 🎬 AI-powered narrative generation using LLM integration
- 🎨 Customizable prompt engineering for creative outputs
- 🚗 Specialized narrative generation for car/automotive themes
- 🎭 Era-specific styling (1980s nostalgia meets modern cinematic energy)
- 📝 RESTful API for narrative generation
- 🔧 Extensible architecture for future enhancements

## Tech Stack

- **Framework**: FastAPI
- **Language**: Python 3.10+
- **AI Integration**: OpenAI API (configurable)
- **Database**: SQLite (starter) / PostgreSQL (production)
- **Task Queue**: Celery (optional, for async processing)

## Project Structure

```
1987/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app initialization
│   ├── config.py               # Configuration management
│   ├── models/                 # Data models
│   │   ├── __init__.py
│   │   └── narrative.py        # Narrative data models
│   ├── services/               # Business logic
│   │   ├── __init__.py
│   │   ├── narrative_service.py # Narrative generation logic
│   │   └── llm_service.py      # LLM integration
│   ├── routers/                # API routes
│   │   ├── __init__.py
│   │   └── narratives.py       # Narrative endpoints
│   ├── prompts/                # Prompt templates
│   │   ├── __init__.py
│   │   ├── base_prompts.py
│   │   └── tokyo_drift_prompts.py
│   └── utils/                  # Utility functions
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── test_narratives.py
│   └── test_services.py
├── .env.example                # Environment variables template
├── .gitignore                  # Git ignore rules
├── requirements.txt            # Python dependencies
├── docker-compose.yml          # Docker Compose setup
├── Dockerfile                  # Docker configuration
└── README.md                   # This file
```

## Installation

### Prerequisites
- Python 3.10 or higher
- pip or conda
- OpenAI API key (or compatible LLM)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/kamy1812/1987.git
cd 1987
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your OpenAI API key and other settings
```

5. Run the application:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Usage

### Generate Narrative

**Endpoint**: `POST /api/v1/narratives/generate`

**Request Body**:
```json
{
  "style": "tokyo_drift_80s",
  "theme": "car_scene",
  "mood": "cinematic",
  "details": {
    "person_description": "person resembling user",
    "car_features": "modified drift car",
    "setting": "urban cityscape"
  }
}
```

**Response**:
```json
{
  "id": "uuid",
  "narrative": "vivid narrative text...",
  "style": "tokyo_drift_80s",
  "created_at": "2026-05-20T12:00:00Z"
}
```

## Configuration

Edit `.env` file to configure:

```bash
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4
DATABASE_URL=sqlite:///./narratives.db
LOG_LEVEL=INFO
```

## Development

### Running Tests

```bash
pytest tests/
```

### Code Formatting

```bash
black app/ tests/
flake8 app/ tests/
```

### Type Checking

```bash
mypy app/
```

## Docker

### Build and Run with Docker

```bash
docker-compose up --build
```

## API Documentation

Once running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Contributing

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Commit changes: `git commit -am 'Add feature'`
3. Push to branch: `git push origin feature/your-feature`
4. Submit a pull request

## License

MIT License - see LICENSE file for details

## Roadmap

- [ ] Advanced prompt engineering for nuanced narratives
- [ ] Image analysis integration for real image-based generation
- [ ] User authentication and narrative history
- [ ] Multiple LLM provider support
- [ ] Narrative templates and customization
- [ ] Performance optimization and caching
- [ ] WebSocket support for streaming narratives
- [ ] Admin dashboard

## Support

For issues, questions, or suggestions, please open a GitHub issue.
