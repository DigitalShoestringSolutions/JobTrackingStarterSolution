from channels.routing import ProtocolTypeRouter, URLRouter
import channels.staticfiles
from channels.auth import AuthMiddlewareStack
import dashboard.routing


application = ProtocolTypeRouter({
        'websocket': AuthMiddlewareStack(
            URLRouter(
                dashboard.routing.websocket_urlpatterns
            )
        ),
    })
