from argparse import ArgumentParser
from pathlib import Path

from devtools import pprint

from .tmx import SearchMapsParameters, TrackmaniaExchange


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--author", required=True)
    parser.add_argument("--output", default="maps")
    return parser.parse_args()


def main():
    args = parse_args()

    output = Path(args.output)

    tmx = TrackmaniaExchange()

    params = SearchMapsParameters(
        author=args.author,
    )

    count = 0
    for map in tmx.search_maps(params):
        print(f"Downloading {map.name}")
        tmx.download_map(output / f"{map.name}.Map.Gbx", map.map_id)
        count += 1

    print(f"Downloaded {count} maps")


if __name__ == "__main__":
    main()
