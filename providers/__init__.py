from .here import Here
from .openrouteservice import Openrouteservice
from .tomtom import TomTom
from .graphhopper import GraphHopper
from .yandex import Yandex

__PROVIDERS__ = [
    TomTom(),
    GraphHopper(),
    Openrouteservice(),
    Here(),
    Yandex()
]


def get_provider_titles():
    return [provider.title for provider in __PROVIDERS__]


def get_provider_by_title(title):
    for provider in __PROVIDERS__:
        if provider.title == title:
            return provider

    raise Exception('Undefined provider:' + title)
