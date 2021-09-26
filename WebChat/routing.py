from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack

from django.conf.urls import url



from Polls.consumers import ChatConsumer

application = ProtocolTypeRouter({
    'websocket':AllowedHostsOriginValidator(
        AuthMiddlewareStack(

            URLRouter(
                [
                    url(r"update/",ChatConsumer)
                ]
            )


        )


    )
})





