# logviz — visualize your logs in the 

Version 0.1.0

---

# Install

```Shell
pipx install logviz*.whl
```

`.whl` builds are available in Releases. Alternatively, clone and build from source using `uv` or whatever your favorite tooling is.

# Run

```bash
$> logviz -h
usage: logviz [-h] -f [FILES ...] [-t TIMELINE TIMELINE TIMELINE] [-b BAR BAR] [-o OUTPUT_DIRECTORY]

A utility that processes reports from plain text formats such as csv and returns summary visualizations of the file

options:
  -h, --help            show this help message and exit
  -f [FILES ...], --files [FILES ...]
                        path of the data file to visualize
  -t TIMELINE TIMELINE TIMELINE, --timeline TIMELINE TIMELINE TIMELINE
                        Generates a timeline from the file based on a count of unique values of the specified column. Syntax: -t {required: time column} {required: time bucket size
                        (minutes)} {required: column to plot over time}
  -b BAR BAR, --bar BAR BAR
                        Generates a histogram from the data based on specified values 'entity column' and 'data column'. Syntax: -b (--bar) {x-axis column data} {y-axis column
                        data}
  -o OUTPUT_DIRECTORY, --output_directory OUTPUT_DIRECTORY
                        path of the directory to save the plots in. Default: ./plots
```

## Examples

### Timelines

```bash
$> logviz -f log_file.csv --timeline timestamp 15 event_type
[-] Working: log_file.csv
[✓] Data from file: log_file.csv processed
[-] Generating timeline: log_file
[✓] Plot saved: ./plots/timeline_log_file
[✓] Plot generation complete
[✓] Plots saved at: {current directory}/plots
$> tree
.
├── log_file.csv
└── plots
    └── timeline_log_file.png <--- The generated timeline
```

### Histograms

```bash
$ logviz -f log_file.csv -b user activity
[-] Working: example_reports/log_file.csv
[✓] Data from file: example_reports/log_file.csv processed
[-] Generating bar graph: log_file
[✓] Plot saved: ./plots/bar_log_file
[✓] Plot generation complete
[✓] Plots saved at: {current directory}/plots
$ tree
.
├── log_file.csv
└── plots
    └── bar_log_file.png <--- The generated histogram
```

---

# Features
- ✅ `-t | --timeline` — Generate a timeline from the file
          -t {time column} {time bucket size in minutes} {column}
- ✅ `-b | --bar` — Generate a histogram from the file
          -b {x axis} {y axis}
          Example: `-b user activity`
          Generates a stacked histogram with user as the x axis and counts of their activity types (such as `Login Success`, `Login Failure`, etc.) on the y axis

---

# Prebuilt Binaries

Downloaded from Releases and install with pipx (see [Install](#Install))

# Build From Source

```bash
$ git clone https://github.com/Jaighk/logviz && cd logviz
$ uv build
$ pipx install dist/*.whl
```

Or build and install with your favorite tooling

---

## Versioning & Upgrades

- Follows **SemVer** (`MAJOR.MINOR.PATCH`).
- Breaking changes only in `MAJOR` releases.
- See CHANGELOG.md for details.

---

## Roadmap
- [ ] Expand format support, starting with `json`


## Changelog
See CHANGELOG.md. Highlights:
- `v0.1.0`: Initial release

---

## Support

- Issues: https://github.com/Jaighk/logviz/issues

---

## License
MIT © Jacob Parker  — see LICENSE
