PHYLA, = glob_wildcards('picklists-phylum/picklist-{phylum}.csv')

print(f"got {len(PHYLA)} phyla.")
print(PHYLA[:5])

rule all:
    input:
        expand("merged/{phylum}.merged.sig.zip", phylum=PHYLA)

rule build_merge:
    input:
        picklist="picklists-phylum/picklist-{phylum}.csv",
        db="gtdb-rs220-k51.zip",
    output:
        "merged/{phylum}.merged.sig.zip",
    shell: """
        sourmash sig downsample --picklist {input.picklist}:ident:ident \
            {input.db} -k 51 --scaled 100_000 -o - | \
        sourmash sig merge - -o {output} --set-name {wildcards.phylum}
    """

rule plants_downsample:
    input: "genbank-plants-2024-07.k51.zip",
    output: "genbank-plants-2024.07.k51.s100_000.sig.zip",
    shell: """
       sourmash sig downsample {input} -k 51 --scaled 100_000 -o {output}
    """
