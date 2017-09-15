web: gunicorn --env DJANGO_SETTINGS_MODULE=tweet_analysis.settings tweet_analysis.wsgi --log-file -
supervisor: supervisord -c supervisor.conf -n
process: python manage.py process_tasks