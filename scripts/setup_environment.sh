#!/bin/bash

set -e

# Install Poetry if not installed
if ! command -v poetry &> /dev/null
then
    echo "Poetry not found. Installing Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="$HOME/.local/bin:$PATH"
else
    echo "Poetry is already installed."
fi

# Install dependencies
echo "Installing dependencies using Poetry..."
poetry install --no-root

echo "Environment setup complete."