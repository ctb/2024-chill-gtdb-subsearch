# 2024-chill-gtdb-subsearch

Build merged rank-level (currently: phylum) sketches for all of GTDB.

First:
```
mkdir -p picklists-phylum/
build-picklists.py gtdb-rs220lineages.csv
```

Then,
```
snakemake -j 4
```