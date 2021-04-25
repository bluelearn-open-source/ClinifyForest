release: python manage.py migrate
web: daphne -p $PORT -b 0.0.0.0 ClinifyForest.asgi:application
worker: python manage.py runworker channels --settings=ClinifyForest.settings