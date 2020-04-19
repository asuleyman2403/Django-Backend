from django.apps import AppConfig


class OnlineShopConfig(AppConfig):
    name = 'online_shop'

    def ready(self):
        import online_shop.signals
