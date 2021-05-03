#!/usr/bin/env python3
import sys
from pprint import pprint

from portmanteaur import get_words


def main() -> None:

    if len(sys.argv) < 2:
        print('Usage: portmanteaur [word] ...')
        sys.exit(1)

    words = get_words(sys.argv[1:])

    pprint(words)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
