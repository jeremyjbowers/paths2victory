# Paths 2 Victory

Inspired by [this lovely Mike Bostock project](https://source.opennews.org/articles/nyts-512-paths-white-house/) and [this lovely NPR Viz project](http://blog.apps.npr.org/2012/11/13/election-2012-generating-the-combinations.html), this is a simple "paths to victory" generator for an arbitrary set of candidates in an electoral contest.

## Getting started

1. Start a Google sheet with your race ratings. Here's what we expect as headers:
```
state	first_results	ev	swing	swing2	90pct12hr rating
```
* `state`: string, a state abbreviation
* `first_results`: string, a parseable timestamp for a time when first results could be announced
* `ev`: int, a number of electoral votes
* `swing`: boolean, is this in a group of swing states?
* `swing2`: boolean, is this in an expanded group of swing states?
* `90pct12hr`: boolean, do we expect a large percentage of the total vote within 12 hours of poll closing?
* `rating`: int, range 3 to -3 where 3 is locked Democratic and -3 is locked Republican and 0 is a swing state

2. Export some environment variables. You need `SHEET_ID` to correspond to the ID of your Google sheet and `SHEET_RANGE` to correspond to the range of cells you'd like to capture for use.

3. Save your Google auth credentials as a JSON file. [This is a pretty good explainer.](https://cloud.google.com/docs/authentication/getting-started) Save the resulting file as `credentials.json` (it's gitignored) and make sure it's in the root of this project.

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
[
 {
  "evs": 271,
  "states": [
   {
    "state": "FL",
    "ev": 29
   },
   {
    "state": "PA",
    "ev": 20
   }
  ],
  "state_string": "FL (29), PA (20)",
  "num_states": 2
 },
 {
  "evs": 283,
  "states": [
   {
    "state": "FL",
    "ev": 29
   },
   {
    "state": "GA",
    "ev": 16
   },
   {
    "state": "MI",
    "ev": 16
   }
  ],
  "state_string": "FL (29), GA (16), MI (16)",
  "num_states": 3
 } ...
```