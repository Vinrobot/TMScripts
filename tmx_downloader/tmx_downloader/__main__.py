from argparse import ArgumentParser, BooleanOptionalAction
from pathlib import Path

from .tmx import SearchMapsParameters, TrackmaniaExchange


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--author", required=True)
    parser.add_argument("--output", default="maps")
    parser.add_argument("--force", default=False, action=BooleanOptionalAction)
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
        map_file = output / f"{map.name}.Map.Gbx"

        if args.force or not map_file.exists():
            print(f"Downloading {map.name}")
            tmx.download_map(map_file, map.map_id)
            count += 1
        else:
            print(f"Skipping {map.name}: File already exists")

    print(f"Downloaded {count} maps")


if __name__ == "__main__":
    main()
