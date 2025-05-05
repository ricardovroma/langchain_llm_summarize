# LangChain LLM Summarize

A FastAPI application that provides text summarization capabilities using OpenAI's language models through the LangChain framework.

### Using Docker (Recommended)

1. Build the Docker image:
   ```bash
   docker build -t langchain-summarize-app .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 -e OPENAI_API_KEY=xxx langchain-summarize-app
   ```

   Or using Docker Compose:
   ```bash
   export OPENAI_API_KEY=your_openai_api_key
   docker-compose up
   ```

## Usage

Once the application is running, you can access:

- API documentation: http://localhost:8000/docs

### Running Tests / Lint

```bash
make check
```

## Continuous Integration

This project uses GitHub Actions for continuous integration. The CI pipeline automatically:

- Runs linting checks
- Executes tests with code coverage requirements

The CI workflow runs on every push to the main branch and on pull requests.
