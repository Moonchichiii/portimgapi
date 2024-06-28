#!/bin/bash

set -e

function error_exit {
    echo "$1" 1>&2
    exit 1
}

# Run the deploy.py script
echo "Running deploy.py to update Django template with Vite assets..."
python deploy.py || error_exit "Failed to update Django template with Vite assets."

echo "deploy.py script executed successfully."
