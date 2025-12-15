#! /usr/bin/env bash

set -e
set -x

# Let the DB start
python app/db_wakeup.py

# Run migrations
alembic upgrade head

python app/main.py