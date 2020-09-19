# Paths 2 Victory

Inspired by (this lovely Mike Bostock project)[https://source.opennews.org/articles/nyts-512-paths-white-house/] and (this lovely NPR Viz project)[http://blog.apps.npr.org/2012/11/13/election-2012-generating-the-combinations.html], this is a simple "paths to victory" generator for an arbitrary set of candidates in an electoral contest.

## Getting started

Start a Google sheet with your race ratings. Here's what we expect as headers:
```
state	first_results	ev	swing	swing2	90pct12hr rating
```
`state`: string, a state abbreviation
`first_results`: string, a parseable timestamp for a time when first results could be announced
`ev`: int, a number of electoral votes
`swing`: boolean, is this in a group of swing states?
`swing2`: boolean, is this in an expanded group of swing states?
`90pct12hr`: boolean, do we expect a large percentage of the total vote within 12 hours of poll closing?
`rating`: int, range 3 to -3 where 3 is locked Democratic and -3 is locked Republican and 0 is a swing state

Export your Google credentials as a JSON object. (This is a pretty good explainer.)[https://cloud.google.com/docs/authentication/getting-started] Save this file as `credentials.json` (it's gitignored) in the root of this project.

## Usage
```sh
mkvirtualenv p2v
git clone git@github.com:jeremyjbowers/paths2victory.git
cd paths2victory
pip install -r requirements.txt
p2v.py
```

This produces a JSON file for each of the candidates listed in `settings.CANDIDATES` using their `slug` as the namespace for the file.

### Sample output
```
Joe Biden has 222 locked-in EVs
Winning path: Joe Biden 270 EVs via NV (6), NE02 (1), MI (16), WI (10), NH (4), AZ (11)
Winning path: Joe Biden 270 EVs via NV (6), NE02 (1), MI (16), WI (10), NC (15)
Winning path: Joe Biden 270 EVs via NV (6), NE02 (1), MI (16), PA (20), NH (4), ME02 (1)
Winning path: Joe Biden 270 EVs via NV (6), NE02 (1), MI (16), NH (4), NC (15), IA (6)
Winning path: Joe Biden 270 EVs via NV (6), NE02 (1), MI (16), OH (18), IA (6), ME02 (1)
Winning path: Joe Biden 270 EVs via NV (6), NE02 (1), WI (10), PA (20), NH (4), IA (6), ME02 (1)
Winning path: Joe Biden 270 EVs via NV (6), NE02 (1), WI (10), PA (20), AZ (11)
Winning path: Joe Biden 270 EVs via NV (6), NE02 (1), WI (10), NH (4), AZ (11), NC (15), ME02 (1)
Winning path: Joe Biden 270 EVs via NV (6), NE02 (1), WI (10), NH (4), AZ (11), GA (16)
Winning path: Joe Biden 270 EVs via NV (6), NE02 (1), WI (10), NC (15), GA (16)
Winning path: Joe Biden 270 EVs via NV (6), NE02 (1), PA (20), NH (4), AZ (11), IA (6)
Winning path: Joe Biden 270 EVs via NV (6), NE02 (1), PA (20), NH (4), GA (16), ME02 (1)
Winning path: Joe Biden 270 EVs via NV (6), NE02 (1), PA (20), NC (15), IA (6)
Winning path: Joe Biden 270 EVs via NV (6), NE02 (1), NH (4), NC (15), GA (16), IA (6)
Winning path: Joe Biden 270 EVs via NV (6), NE02 (1), FL (29), AZ (11), ME02 (1)
Winning path: Joe Biden 270 EVs via NV (6), NE02 (1), GA (16), OH (18), IA (6), ME02 (1)
Winning path: Joe Biden 270 EVs via NV (6), MI (16), WI (10), NH (4), AZ (11), ME02 (1)
Winning path: Joe Biden 270 EVs via NV (6), MI (16), WI (10), NC (15), ME02 (1)
Winning path: Joe Biden 270 EVs via NV (6), MI (16), WI (10), GA (16)
Winning path: Joe Biden 270 EVs via NV (6), MI (16), PA (20), IA (6)
Winning path: Joe Biden 270 EVs via NV (6), MI (16), NH (4), NC (15), IA (6), ME02 (1)
Winning path: Joe Biden 270 EVs via NV (6), MI (16), NH (4), GA (16), IA (6)
Winning path: Joe Biden 270 EVs via NV (6), MI (16), AZ (11), NC (15)
Winning path: Joe Biden 270 EVs via NV (6), WI (10), PA (20), AZ (11), ME02 (1)
Winning path: Joe Biden 270 EVs via NV (6), WI (10), NH (4), AZ (11), GA (16), ME02 (1)
Winning path: Joe Biden 270 EVs via NV (6), WI (10), AZ (11), NC (15), IA (6)
Winning path: Joe Biden 270 EVs via NV (6), WI (10), NC (15), GA (16), ME02 (1)
Winning path: Joe Biden 270 EVs via NV (6), PA (20), NH (4), AZ (11), IA (6), ME02 (1)
Winning path: Joe Biden 270 EVs via NV (6), PA (20), NH (4), OH (18)
Winning path: Joe Biden 270 EVs via NV (6), PA (20), NC (15), IA (6), ME02 (1)
Winning path: Joe Biden 270 EVs via NV (6), PA (20), GA (16), IA (6)
Winning path: Joe Biden 270 EVs via NV (6), NH (4), NC (15), GA (16), IA (6), ME02 (1)
Winning path: Joe Biden 270 EVs via NV (6), AZ (11), NC (15), GA (16)
Winning path: Joe Biden 270 EVs via NE02 (1), MI (16), WI (10), PA (20), ME02 (1)
Winning path: Joe Biden 270 EVs via NE02 (1), MI (16), WI (10), NH (4), AZ (11), IA (6)
Winning path: Joe Biden 270 EVs via NE02 (1), MI (16), WI (10), NH (4), GA (16), ME02 (1)
Winning path: Joe Biden 270 EVs via NE02 (1), MI (16), WI (10), NC (15), IA (6)
Winning path: Joe Biden 270 EVs via NE02 (1), MI (16), PA (20), NH (4), IA (6), ME02 (1)
Winning path: Joe Biden 270 EVs via NE02 (1), MI (16), PA (20), AZ (11)
Winning path: Joe Biden 270 EVs via NE02 (1), MI (16), NH (4), AZ (11), NC (15), ME02 (1)
Winning path: Joe Biden 270 EVs via NE02 (1), MI (16), NH (4), AZ (11), GA (16)
Winning path: Joe Biden 270 EVs via NE02 (1), MI (16), NC (15), GA (16)
Winning path: Joe Biden 270 EVs via NE02 (1), WI (10), PA (20), AZ (11), IA (6)
Winning path: Joe Biden 270 EVs via NE02 (1), WI (10), PA (20), GA (16), ME02 (1)
Winning path: Joe Biden 270 EVs via NE02 (1), WI (10), NH (4), AZ (11), NC (15), IA (6), ME02 (1)
Winning path: Joe Biden 270 EVs via NE02 (1), WI (10), NH (4), AZ (11), GA (16), IA (6)
Winning path: Joe Biden 270 EVs via NE02 (1), WI (10), NH (4), NC (15), OH (18)
Winning path: Joe Biden 270 EVs via NE02 (1), WI (10), NC (15), GA (16), IA (6)
Winning path: Joe Biden 270 EVs via NE02 (1), PA (20), NH (4), GA (16), IA (6), ME02 (1)
Winning path: Joe Biden 270 EVs via NE02 (1), PA (20), AZ (11), NC (15), ME02 (1)
Winning path: Joe Biden 270 EVs via NE02 (1), PA (20), AZ (11), GA (16)
Winning path: Joe Biden 270 EVs via NE02 (1), NH (4), AZ (11), NC (15), GA (16), ME02 (1)
Winning path: Joe Biden 270 EVs via NE02 (1), FL (29), AZ (11), IA (6), ME02 (1)
Winning path: Joe Biden 270 EVs via NE02 (1), FL (29), OH (18)
Winning path: Joe Biden 270 EVs via MI (16), WI (10), NH (4), AZ (11), IA (6), ME02 (1)
Winning path: Joe Biden 270 EVs via MI (16), WI (10), NH (4), OH (18)
Winning path: Joe Biden 270 EVs via MI (16), WI (10), NC (15), IA (6), ME02 (1)
Winning path: Joe Biden 270 EVs via MI (16), WI (10), GA (16), IA (6)
Winning path: Joe Biden 270 EVs via MI (16), PA (20), AZ (11), ME02 (1)
Winning path: Joe Biden 270 EVs via MI (16), NH (4), AZ (11), GA (16), ME02 (1)
Winning path: Joe Biden 270 EVs via MI (16), AZ (11), NC (15), IA (6)
Winning path: Joe Biden 270 EVs via MI (16), NC (15), GA (16), ME02 (1)
Winning path: Joe Biden 270 EVs via WI (10), PA (20), AZ (11), IA (6), ME02 (1)
Winning path: Joe Biden 270 EVs via WI (10), PA (20), OH (18)
Winning path: Joe Biden 270 EVs via WI (10), NH (4), AZ (11), GA (16), IA (6), ME02 (1)
Winning path: Joe Biden 270 EVs via WI (10), NH (4), NC (15), OH (18), ME02 (1)
Winning path: Joe Biden 270 EVs via WI (10), NH (4), GA (16), OH (18)
Winning path: Joe Biden 270 EVs via WI (10), NC (15), GA (16), IA (6), ME02 (1)
Winning path: Joe Biden 270 EVs via PA (20), NH (4), OH (18), IA (6)
Winning path: Joe Biden 270 EVs via PA (20), AZ (11), GA (16), ME02 (1)
Winning path: Joe Biden 270 EVs via NH (4), FL (29), NC (15)
Winning path: Joe Biden 270 EVs via NH (4), AZ (11), NC (15), OH (18)
Winning path: Joe Biden 270 EVs via FL (29), OH (18), ME02 (1)
Winning path: Joe Biden 270 EVs via AZ (11), NC (15), GA (16), IA (6)
Donald Trump has 163 locked-in EVs
Winning path: Donald Trump 270 EVs via NV (6), NE02 (1), MI (16), WI (10), PA (20), NH (4), FL (29), NC (15), IA (6)
Winning path: Donald Trump 270 EVs via NV (6), NE02 (1), MI (16), WI (10), PA (20), NH (4), AZ (11), NC (15), OH (18), IA (6)
Winning path: Donald Trump 270 EVs via NV (6), NE02 (1), MI (16), WI (10), PA (20), NH (4), NC (15), GA (16), OH (18), ME02 (1)
Winning path: Donald Trump 270 EVs via NV (6), NE02 (1), MI (16), WI (10), PA (20), FL (29), OH (18), IA (6), ME02 (1)
Winning path: Donald Trump 270 EVs via NV (6), NE02 (1), MI (16), WI (10), NH (4), FL (29), GA (16), OH (18), IA (6), ME02 (1)
Winning path: Donald Trump 270 EVs via NV (6), NE02 (1), MI (16), WI (10), FL (29), AZ (11), NC (15), OH (18), ME02 (1)
Winning path: Donald Trump 270 EVs via NV (6), NE02 (1), MI (16), WI (10), FL (29), AZ (11), GA (16), OH (18)
Winning path: Donald Trump 270 EVs via NV (6), NE02 (1), MI (16), PA (20), NH (4), FL (29), NC (15), GA (16)
Winning path: Donald Trump 270 EVs via NV (6), NE02 (1), MI (16), PA (20), NH (4), AZ (11), NC (15), GA (16), OH (18)
Winning path: Donald Trump 270 EVs via NV (6), NE02 (1), MI (16), PA (20), FL (29), AZ (11), OH (18), IA (6)
Winning path: Donald Trump 270 EVs via NV (6), NE02 (1), MI (16), PA (20), FL (29), GA (16), OH (18), ME02 (1)
Winning path: Donald Trump 270 EVs via NV (6), NE02 (1), MI (16), NH (4), FL (29), AZ (11), NC (15), OH (18), IA (6), ME02 (1)
Winning path: Donald Trump 270 EVs via NV (6), NE02 (1), MI (16), NH (4), FL (29), AZ (11), GA (16), OH (18), IA (6)
Winning path: Donald Trump 270 EVs via NV (6), NE02 (1), MI (16), FL (29), NC (15), GA (16), OH (18), IA (6)
Winning path: Donald Trump 270 EVs via NV (6), NE02 (1), WI (10), PA (20), NH (4), FL (29), NC (15), GA (16), IA (6)
Winning path: Donald Trump 270 EVs via NV (6), NE02 (1), WI (10), PA (20), NH (4), AZ (11), NC (15), GA (16), OH (18), IA (6)
Winning path: Donald Trump 270 EVs via NV (6), NE02 (1), WI (10), PA (20), FL (29), GA (16), OH (18), IA (6), ME02 (1)
Winning path: Donald Trump 270 EVs via NV (6), NE02 (1), WI (10), FL (29), AZ (11), NC (15), GA (16), OH (18), ME02 (1)
Winning path: Donald Trump 270 EVs via NV (6), NE02 (1), PA (20), FL (29), AZ (11), NC (15), OH (18), IA (6), ME02 (1)
Winning path: Donald Trump 270 EVs via NV (6), NE02 (1), PA (20), FL (29), AZ (11), GA (16), OH (18), IA (6)
Winning path: Donald Trump 270 EVs via NV (6), NE02 (1), NH (4), FL (29), AZ (11), NC (15), GA (16), OH (18), IA (6), ME02 (1)
Winning path: Donald Trump 270 EVs via NV (6), MI (16), WI (10), PA (20), NH (4), FL (29), NC (15), IA (6), ME02 (1)
Winning path: Donald Trump 270 EVs via NV (6), MI (16), WI (10), PA (20), NH (4), FL (29), GA (16), IA (6)
Winning path: Donald Trump 270 EVs via NV (6), MI (16), WI (10), PA (20), NH (4), AZ (11), NC (15), OH (18), IA (6), ME02 (1)
Winning path: Donald Trump 270 EVs via NV (6), MI (16), WI (10), PA (20), NH (4), AZ (11), GA (16), OH (18), IA (6)
Winning path: Donald Trump 270 EVs via NV (6), MI (16), WI (10), PA (20), FL (29), AZ (11), NC (15)
Winning path: Donald Trump 270 EVs via NV (6), MI (16), WI (10), PA (20), NC (15), GA (16), OH (18), IA (6)
Winning path: Donald Trump 270 EVs via NV (6), MI (16), WI (10), NH (4), FL (29), AZ (11), NC (15), GA (16)
Winning path: Donald Trump 270 EVs via NV (6), MI (16), WI (10), FL (29), AZ (11), GA (16), OH (18), ME02 (1)
Winning path: Donald Trump 270 EVs via NV (6), MI (16), PA (20), NH (4), FL (29), AZ (11), NC (15), IA (6)
Winning path: Donald Trump 270 EVs via NV (6), MI (16), PA (20), NH (4), FL (29), NC (15), GA (16), ME02 (1)
Winning path: Donald Trump 270 EVs via NV (6), MI (16), PA (20), NH (4), AZ (11), NC (15), GA (16), OH (18), ME02 (1)
Winning path: Donald Trump 270 EVs via NV (6), MI (16), PA (20), FL (29), AZ (11), OH (18), IA (6), ME02 (1)
Winning path: Donald Trump 270 EVs via NV (6), MI (16), NH (4), FL (29), AZ (11), GA (16), OH (18), IA (6), ME02 (1)
Winning path: Donald Trump 270 EVs via NV (6), MI (16), FL (29), NC (15), GA (16), OH (18), IA (6), ME02 (1)
Winning path: Donald Trump 270 EVs via NV (6), WI (10), PA (20), NH (4), FL (29), NC (15), GA (16), IA (6), ME02 (1)
Winning path: Donald Trump 270 EVs via NV (6), WI (10), PA (20), NH (4), AZ (11), NC (15), GA (16), OH (18), IA (6), ME02 (1)
Winning path: Donald Trump 270 EVs via NV (6), WI (10), PA (20), FL (29), AZ (11), NC (15), GA (16)
Winning path: Donald Trump 270 EVs via NV (6), PA (20), NH (4), FL (29), AZ (11), NC (15), GA (16), IA (6)
Winning path: Donald Trump 270 EVs via NV (6), PA (20), FL (29), AZ (11), GA (16), OH (18), IA (6), ME02 (1)
Winning path: Donald Trump 270 EVs via NE02 (1), MI (16), WI (10), PA (20), NH (4), FL (29), AZ (11), NC (15), ME02 (1)
Winning path: Donald Trump 270 EVs via NE02 (1), MI (16), WI (10), PA (20), NH (4), FL (29), AZ (11), GA (16)
Winning path: Donald Trump 270 EVs via NE02 (1), MI (16), WI (10), PA (20), NH (4), NC (15), GA (16), OH (18), IA (6), ME02 (1)
Winning path: Donald Trump 270 EVs via NE02 (1), MI (16), WI (10), PA (20), FL (29), NC (15), GA (16)
Winning path: Donald Trump 270 EVs via NE02 (1), MI (16), WI (10), PA (20), AZ (11), NC (15), GA (16), OH (18)
Winning path: Donald Trump 270 EVs via NE02 (1), MI (16), WI (10), FL (29), AZ (11), NC (15), OH (18), IA (6), ME02 (1)
Winning path: Donald Trump 270 EVs via NE02 (1), MI (16), WI (10), FL (29), AZ (11), GA (16), OH (18), IA (6)
Winning path: Donald Trump 270 EVs via NE02 (1), MI (16), PA (20), NH (4), FL (29), NC (15), GA (16), IA (6)
Winning path: Donald Trump 270 EVs via NE02 (1), MI (16), PA (20), NH (4), AZ (11), NC (15), GA (16), OH (18), IA (6)
Winning path: Donald Trump 270 EVs via NE02 (1), MI (16), PA (20), FL (29), GA (16), OH (18), IA (6), ME02 (1)
Winning path: Donald Trump 270 EVs via NE02 (1), MI (16), FL (29), AZ (11), NC (15), GA (16), OH (18), ME02 (1)
Winning path: Donald Trump 270 EVs via NE02 (1), WI (10), PA (20), NH (4), FL (29), AZ (11), NC (15), GA (16), ME02 (1)
Winning path: Donald Trump 270 EVs via NE02 (1), WI (10), FL (29), AZ (11), NC (15), GA (16), OH (18), IA (6), ME02 (1)
Winning path: Donald Trump 270 EVs via MI (16), WI (10), PA (20), NH (4), FL (29), AZ (11), GA (16), ME02 (1)
Winning path: Donald Trump 270 EVs via MI (16), WI (10), PA (20), FL (29), AZ (11), NC (15), IA (6)
Winning path: Donald Trump 270 EVs via MI (16), WI (10), PA (20), FL (29), NC (15), GA (16), ME02 (1)
Winning path: Donald Trump 270 EVs via MI (16), WI (10), PA (20), AZ (11), NC (15), GA (16), OH (18), ME02 (1)
Winning path: Donald Trump 270 EVs via MI (16), WI (10), NH (4), FL (29), AZ (11), NC (15), GA (16), IA (6)
Winning path: Donald Trump 270 EVs via MI (16), WI (10), FL (29), AZ (11), GA (16), OH (18), IA (6), ME02 (1)
Winning path: Donald Trump 270 EVs via MI (16), PA (20), NH (4), FL (29), NC (15), GA (16), IA (6), ME02 (1)
Winning path: Donald Trump 270 EVs via MI (16), PA (20), NH (4), AZ (11), NC (15), GA (16), OH (18), IA (6), ME02 (1)
Winning path: Donald Trump 270 EVs via MI (16), PA (20), FL (29), AZ (11), NC (15), GA (16)
Winning path: Donald Trump 270 EVs via WI (10), PA (20), NH (4), FL (29), AZ (11), NC (15), OH (18)
Winning path: Donald Trump 270 EVs via WI (10), PA (20), FL (29), AZ (11), NC (15), GA (16), IA (6)
```