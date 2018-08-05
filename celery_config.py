from celery import Celery

app = Celery('celery_config', broker='redis://:{password}@{name_of_cache}.redis.cache.windows.net:6379/0', include=['celery_client'])