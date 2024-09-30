#!/bin/bash

if [ -d "./embeddings" ]; then
    echo "Removing ./embeddings directory..."
    rm -rf ./embeddings
    echo "./embeddings directory removed."
else
    echo "./embeddings directory does not exist."
fi

if [ -d "./.cache" ]; then
    echo "Removing ./.cache directory..."
    rm -rf ./.cache
    echo "./.cache directory removed."
else
    echo "./.cache directory does not exist."
fi

echo "Removing all __pycache__ directories..."
find . -type d -name "__pycache__" -exec rm -rf {} +
echo "All __pycache__ directories removed."

# Optional: Remove all .pyc files (compiled Python files)
# echo "Removing all .pyc files..."
# find . -type f -name "*.pyc" -exec rm -f {} +
# echo "All .pyc files removed."

echo "Clean up complete!"
