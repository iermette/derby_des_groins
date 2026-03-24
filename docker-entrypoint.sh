#!/bin/bash
set -e

echo "Waiting for PostgreSQL..."
python -c "
import time, sys, os
for i in range(30):
    try:
        import psycopg2
        conn = psycopg2.connect(os.environ['DATABASE_URL'])
        conn.close()
        print('PostgreSQL is ready!')
        sys.exit(0)
    except Exception:
        time.sleep(1)
print('ERROR: PostgreSQL not ready after 30s')
sys.exit(1)
"

exec gunicorn \
    --bind 0.0.0.0:5001 \
    --workers 1 \
    --threads 4 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    --log-level info \
    "app:create_app()"
