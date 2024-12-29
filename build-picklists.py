#! /usr/bin/env python
import csv
import argparse
from collections import defaultdict


def main():
    p = argparse.ArgumentParser()
    p.add_argument('tax_csv')
    p.add_argument('-r', '--rank', default="phylum")
    args = p.parse_args()

    rows_by_rank = defaultdict(list)
    rank = args.rank
    assert rank in ['phylum', 'genus', 'species',
                    'family', 'order', 'class']

    n_rows = 0
    with open(args.tax_csv, 'r', newline='') as fp:
        r = csv.DictReader(fp)

        for row in r:
            name = row[rank]
            assert name
            rows_by_rank[name].append(row)
            n_rows += 1

    print(f"read {n_rows} rows from '{args.tax_csv}'")

    output_rows = 0
    for n, (name, rows) in enumerate(rows_by_rank.items()):
        if n and n % 100 == 0:
            print(f'... {n} names of {len(rows_by_rank)} total; {output_rows} rows of {n_rows} total.')
        with open(f'picklists-{rank}/picklist-{name}.csv', 'w', newline='') as outfp:
            w = csv.DictWriter(outfp, fieldnames=rows[0].keys())
            w.writeheader()
            for row in rows:
                w.writerow(row)
            output_rows += len(rows)


if __name__ == '__main__':
    main()
