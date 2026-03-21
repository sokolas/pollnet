import json
import yaml

with open("cargo-sources.json") as f:
    data = json.load(f)

with open("pollnet-cargo-sources.yaml", "w") as f:
    yaml.dump(data, f, sort_keys=False)
    