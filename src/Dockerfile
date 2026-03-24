FROM python:3.10

# Create a folder /app if it doesn't exist,
# the /app folder is the current working directory
WORKDIR /app

# Copy necessary files to our app
COPY requirements.txt .

# Port will be exposed, for documentation only
EXPOSE 30000

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.6.17 /uv /uvx /bin/
ENV UV_SYSTEM_PYTHON=1 \
    UV_BREAK_SYSTEM_PACKAGES=true

# Disable pip cache to shrink the image size a little bit,
# since it does not need to be re-installed
RUN uv pip install -r requirements.txt --no-cache-dir

COPY models .
COPY app .

# CMD ["/bin/bash", "-c", "while true; do sleep 3600; done"]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "30000"]
