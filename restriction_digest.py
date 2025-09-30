import re
import sys
from typing import Dict, List, Tuple, Optional

def parse_enzyme_file(filepath: str) -> Dict[str, str]:
    """
    Parses enzyme file. Supports comma or tab separation, ignores comments and empty lines.
    Returns {enzyme_name: recognition_sequence}.
    """
    enzymes = {}
    try:
        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                # Split by comma or tab
                parts = re.split('[,\t]', line)
                if len(parts) < 2:
                    continue  # skip malformed lines
                name, sequence = parts[0].strip(), parts[1].strip().upper()
                # Minimal validation: only ACGT (IUPAC support could be added)
                if not re.fullmatch(r'[ACGT]+', sequence):
                    continue
                enzymes[name] = sequence
    except FileNotFoundError:
        print(f"Error: Enzyme file not found at {filepath}")
        return {}
    return enzymes

def find_cut_sites(dna_sequence: str, enzyme_sequences: Dict[str, str]) -> List[Tuple[str, int]]:
    """
    Finds cut sites for all enzymes. Returns list of (enzyme, 1-based cut position).
    """
    cut_sites = []
    for enzyme, sequence in enzyme_sequences.items():
        for match in re.finditer(sequence, dna_sequence):
            cut_sites.append((enzyme, match.start() + 1))  # 1-based indexing
    cut_sites.sort(key=lambda x: x[1])
    return cut_sites

def digest_sequence(dna_sequence: str, cut_sites: List[int]) -> List[str]:
    """
    Returns the DNA fragments as strings after digesting at given cut site positions (1-based).
    """
    cut_sites = sorted(set(cut_sites))
    cut_sites.append(len(dna_sequence))
    start = 0
    fragments = []
    for cut in cut_sites:
        fragments.append(dna_sequence[start:cut])
        start = cut
    return fragments

def report_digest(dna_sequence: str, cut_site_info: List[Tuple[str, int]]):
    """
    Prints summary of digest, including enzyme cut sites and fragment lengths.
    """
    print("\n--- Digest Results ---")
    print(f"Original DNA length: {len(dna_sequence)} bp")
    if not cut_site_info:
        print("No cut sites found.")
        return
    print("Cut sites:")
    for enzyme, pos in cut_site_info:
        print(f"  {enzyme}: position {pos}")
    cut_positions = [pos for _, pos in cut_site_info]
    fragments = digest_sequence(dna_sequence, cut_positions)
    print(f"Number of fragments: {len(fragments)}")
    print(f"Fragment lengths (bp): {[len(frag) for frag in fragments]}")
    print("----------------------")

def main(dna_file: Optional[str] = None, enzyme_file: Optional[str] = None):
    if not dna_file or not enzyme_file:
        print("Usage: python restriction_digest.py <dna_file> <enzyme_file>")
        sys.exit(1)
    # Load DNA
    try:
        with open(dna_file, 'r') as f:
            dna_sequence = f.read().strip().upper()
            # Optionally, only keep ACGT
            dna_sequence = re.sub(r'[^ACGT]', '', dna_sequence)
    except FileNotFoundError:
        print(f"Error: DNA sequence file not found at {dna_file}")
        sys.exit(1)

    enzymes = parse_enzyme_file(enzyme_file)
    if not enzymes:
        print("No valid enzymes found.")
        sys.exit(1)
    # Digest and report
    cut_sites_info = find_cut_sites(dna_sequence, enzymes)
    report_digest(dna_sequence, cut_sites_info)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python restriction_digest.py <dna_file> <enzyme_file>")
