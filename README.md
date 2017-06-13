# Flix CLI

## Introduction
Get movie and theater information (powered (unofficially) by Flixster) without having to leave the command line!

## Installation
`pip install flix`

## Usage

* `-n` or `--name` to filter by a specific movie name
* `-t` or `--tomorrow` to filter by movies playing tomorrow
* `-m` or `--month` to select a month
* `-d` or `--day` to select a day
  * There are weekday (e.g. `mon`, `tue`, etc.) choices, which will return results for the next given weekday
  * For any valid month & day combination, results will be returned for the *next* month & day combination.
  * There are also date values (e.g. `1`, `2`, `3`, etc.)
* `-l` or `--limit` to select the number of theaters to return movie options for.
  * Defaults to `2`
  * Selection must be non-zero
  * Maximum value is `5`

### Time Hierarchy
1. The `--tomorrow` flag is set
2. A weekday (`mon`, `tue`, etc.) is chosen
3. Month & day combination

### Examples
