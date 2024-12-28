from argparse import ArgumentParser

from devtools import pprint

from .tmx import SearchMapsParameters, TrackmaniaExchange


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--author", required=True)
    return parser.parse_args()


def main():
    args = parse_args()

    tmx = TrackmaniaExchange()

    params = SearchMapsParameters(
        author=args.author,
    )

    for map in tmx.search_maps(params):
        pprint(map)


if __name__ == "__main__":
    main()
