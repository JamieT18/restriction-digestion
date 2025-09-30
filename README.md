# In Silico Restriction Digest Tool

## Overview

This Python script simulates a **restriction digest**—a common molecular biology technique—on a user-provided DNA sequence using a list of specified restriction enzymes. The script identifies all cut sites based on the enzymes' recognition sequences and reports the resulting DNA fragment sizes. This tool is ideal for planning cloning strategies, analyzing DNA sequences, educational demonstrations, or quickly predicting gel electrophoresis results without laboratory work.

## Features

- **Simple command-line interface**
- **Flexible enzyme file format:** Supports comma or tab-separated values
- **Detailed output:** Reports enzyme cut sites, fragment lengths, and total DNA size
- **Multiple enzyme support:** Digest with one or many enzymes simultaneously
- **Error handling:** Informative messages for missing or malformed input files
- **Modular code:** Designed for easy extension or integration into other projects

## Input File Formats

### DNA Sequence File

- Plain text file
- Should contain a single DNA sequence (A, C, G, T only; other characters are ignored)

**Example (`dna.txt`):**
```
ACGTGATCGATCGATCGATCGGAATTCCGATCGATGCGTACGATCGATCGATCGATCG
```

### Restriction Enzyme File

- Each line: `EnzymeName,RecognitionSequence` or `EnzymeName<TAB>RecognitionSequence`
- Lines starting with `#` are treated as comments
- Only A, C, G, T supported in recognition sequence (IUPAC support can be added if needed)

**Example (`enzymes.txt`):**
```
EcoRI,GAATTC
BamHI,GGATCC
DpnI,GATC
# This is a comment and will be ignored
```

## Usage

1. Place `restriction_digest.py`, your DNA file, and your enzyme file in the same directory.
2. Run the script from the command line:

```bash
python restriction_digest.py dna.txt enzymes.txt
```

## Output

The script will display:
- The length of the input DNA
- The names and positions of all enzyme cut sites
- The number and lengths of DNA fragments produced

**Sample Output:**
```
--- Digest Results ---
Original DNA length: 56 bp
Cut sites:
  DpnI: position 5
  DpnI: position 9
  EcoRI: position 22
Number of fragments: 4
Fragment lengths (bp): [5, 4, 13, 34]
----------------------
```

## Troubleshooting

- **File not found:** Ensure the specified files exist and file names are correct.
- **Malformed enzyme lines:** Only lines with both enzyme name and valid recognition sequence (A, C, G, T) are processed.
- **No cut sites found:** Check that your recognition sequences match the DNA sequence.

## Extending the Script

Feel free to modify or extend the script for:
- Supporting IUPAC ambiguity codes in recognition sequences
- Outputting fragment sequences
- Generating graphical gel band predictions

## License

This project is released under the MIT License.

## Author

JamieT18

---
