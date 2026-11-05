"""Require an explicit, current upstream baseline before release validation."""
import json
import pathlib
import urllib.parse
import urllib.request

root = pathlib.Path(__file__).resolve().parents[1]
config = json.loads((root / '.stackline/release.json').read_text())
source = json.loads((root / 'package.json').read_text())
assert source['version'] == config['upstreamVersion'], 'Source and packed upstream versions differ'
url = 'https://registry.npmjs.org/' + urllib.parse.quote(config['upstream'], safe='') + '/latest'
with urllib.request.urlopen(url, timeout=30) as response:
    latest = json.load(response)
assert latest['name'] == config['upstream']
assert latest['version'] == config['upstreamVersion'], (
    f"Upstream {latest['name']} is {latest['version']}; review and update the pinned "
    f"{config['upstreamVersion']} baseline before declaring this package current."
)
assert latest['dist']['integrity'] == config['upstreamIntegrity']
print(f"Verified current upstream baseline: {latest['name']}@{latest['version']}")
