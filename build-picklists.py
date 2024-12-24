#! /usr/bin/env python
import csv
import argparse
from collections import defaultdict


def main():
    p = argparse.ArgumentParser()
    p.add_argument('tax_csv')
    args = p.parse_args()

    rows_by_rank = defaultdict(list)

    n_rows = 0
    with open(args.tax_csv, 'r', newline='') as fp:
        r = csv.DictReader(fp)

        for row in r:
            phylum = row['phylum']
            rows_by_rank[phylum].append(row)
            n_rows += 1

    print(f"read {n_rows} rows")

    for n, (name, rows) in enumerate(rows_by_rank.items()):
        print(f'... {name}')
        with open(f'picklists-phylum/picklist-{name}.csv', 'w', newline='') as outfp:
            w = csv.DictWriter(outfp, fieldnames=rows[0].keys())
            w.writeheader()
            for row in rows:
                w.writerow(row)


if __name__ == '__main__':
    main()
