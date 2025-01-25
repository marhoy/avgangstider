FROM python:3.13-slim-bookworm

# Define some environment variables
ENV UV_NO_CACHE=true \
    UV_FROZEN=true \
    UV_NO_SYNC=true \
    UV_COMPILE_BYTECODE=true

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.5.24 /uv /uvx /bin/

# We want to run things as a non-privileged user
ENV USERNAME=flask
ENV PATH="$PATH:/home/$USERNAME/.local/bin:/home/$USERNAME/app/.venv/bin"

# Add user
RUN useradd -m $USERNAME
# If using an alpine image
# RUN addgroup -S $USERNAME && adduser -S $USERNAME -G $USERNAME

# Set up a workdir
WORKDIR /home/$USERNAME/app
RUN chown $USERNAME.$USERNAME .

# Everything below here runs as a non-privileged user
USER $USERNAME

# Install runtime dependencies (will be cached)
COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev --no-install-project

# Copy project files to container
COPY . .

# Install our own package
RUN RUN --mount=source=.git,target=.git,type=bind uv sync --no-dev

# Expose port 5000
EXPOSE 5000

# Run gunicorn
CMD ["gunicorn", "-c", "src/gunicorn_config.py", "avgangstider.flask_app:create_app()"]
