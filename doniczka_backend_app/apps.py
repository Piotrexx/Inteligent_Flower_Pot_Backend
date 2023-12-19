from django.apps import AppConfig
from raspcode.read_hum_and_water import check
import threading

class DoniczkaBackendAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'doniczka_backend_app'

    def ready(self):
        t1 = threading.Thread(target=check)
        t1.start()
        t1.join()