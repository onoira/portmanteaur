"""portmanteau - Generate portmanteau for name generation"""

__all__ = [
    '__author__',
    '__author_email__',
    '__license__',
    '__version__',
    'default_headers',
    'default_user_agent',
    'get_word',
    'get_words',
    'get_version'
]

from portmanteaur.__version__ import __author__
from portmanteaur.__version__ import __author_email__
from portmanteaur.__version__ import __license__
from portmanteaur.__version__ import __version__
from portmanteaur.__version__ import VERSION as __VERSION

from portmanteaur._portmanteaur import default_headers
from portmanteaur._portmanteaur import default_user_agent
from portmanteaur._portmanteaur import get_word
from portmanteaur._portmanteaur import get_words


def get_version() -> tuple[int, int, int]:
    return __VERSION
