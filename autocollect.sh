#!/bin/bash

set -e

echo "Connecting into the virtualenv"
source venv/bin/activate
echo "Uploading static files..."
python manage.py collectstatic --noinput
echo "Disconnecting from the virtualenv"
deactivate
echo "Done."
exit 0
