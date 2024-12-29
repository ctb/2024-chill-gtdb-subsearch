RANK = 'genus'
NAMES, = glob_wildcards(f'picklists-{RANK}/picklist-{{name}}.csv')

print(f"got {len(NAMES)} names at rank {RANK}.")
print(NAMES[:5])

rule all:
    input:
        expand(f"merged-{RANK}/{{name}}.merged.sig.zip", name=NAMES)

rule build_merge:
    input:
        picklist=f"picklists-{RANK}/picklist-{{name}}.csv",
        db="gtdb-rs220-k51.zip",
    output:
        f"merged-{RANK}/{{name}}.merged.sig.zip",
    shell: """
        sourmash sig downsample --picklist {input.picklist}:ident:ident \
            {input.db} -k 51 --scaled 100_000 -o - | \
        sourmash sig merge - -o {output} --set-name {wildcards.name}
    """

rule plants_downsample:
    input: "genbank-plants-2024-07.k51.zip",
    output: "genbank-plants-2024.07.k51.s100_000.sig.zip",
    shell: """
       sourmash sig downsample {input} -k 51 --scaled 100_000 -o {output}
    """
