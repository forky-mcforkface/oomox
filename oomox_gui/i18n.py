import os
import gettext


LOCALEDIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '..', 'locale'
)
TRANSLATION = gettext.translation(
    'oomox',
    localedir=LOCALEDIR,
    fallback=True
)


def translate(msg: str) -> str:
    return TRANSLATION.gettext(msg)


def translate_many(singular: str, plural: str, count: int) -> str:
    return TRANSLATION.ngettext(singular, plural, count)
