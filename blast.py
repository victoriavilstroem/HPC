from Bio.Blast import NCBIWWW, NCBIXML
import time
from multiprocessing import Pool
import subprocess

# Function to perform a BLAST search for a single query sequence
def blast_search(query_sequence):
    print("Starting BLAST search...")
    result_handle = NCBIWWW.qblast("blastn", "nt", query_sequence)
    blast_records = NCBIXML.parse(result_handle)
    
    # Collect results as dictionaries
    results = []
    for blast_record in blast_records:
        for alignment in blast_record.alignments[:3]:  # Top 3 results
            for hsp in alignment.hsps:
                results.append({
                    "Hit ID": alignment.accession,
                    "Title": alignment.title,
                    "Score": hsp.score,
                    "E-value": hsp.expect
                })
    return results

# Helper function to process each chunk
def process_chunk(sequences_chunk):
    chunk_results = []
    for sequence in sequences_chunk:
        chunk_results.extend(blast_search(sequence))
    return chunk_results

# Function to run BLAST searches in parallel
def run_blast_parallel(sequences, num_processors=4):
    chunk_size = max(1, len(sequences) // num_processors)
    sequence_chunks = [sequences[i:i + chunk_size] for i in range(0, len(sequences), chunk_size)]
    
    start_time = time.time()
    with Pool(num_processors) as pool:
        results = pool.map(process_chunk, sequence_chunks)
    
    # Flatten the list of results
    flat_results = [hit for sublist in results for hit in sublist]
    duration = time.time() - start_time
    print(f"Parallel processing completed in {duration:.2f} seconds.")
    return flat_results

# Main execution
if __name__ == "__main__":
    # Example DNA sequences to search
    sequences_to_search = [
        "ATTCTTCCCAGGACCTCAGCGCAGCCCTGGCCCAGGAAGGCAGGAGACAGAGGCCAGGACGGTCCAGAGGTGTCGAAATGTCCTGGGGACCTGAGCAGCAGCCACCAGGGAAGAGGCAGGGAGGGAGCTGAGGACCAGGCTTGGTTGTGAGAATCCCTGAGCCCAGGCGGTAGATGCCAGGAGGTGTCTGGACTGGCTGGGCCATGCCTGGGCTGACCTGTCCAGCCAGGGAGAGGGTGTGAGGGCAGATCTGGGGGTGCCCAGATGGAAGGAGGCAGGCATGGGGGACACCCAAGGCCCCCTGGCAGCACCATGAACTAAGCAGGACACCTGGAGGGGA",
        "GCCATTGTAATGGGCCGCATGGAACAGAACAAAGTGGTCGGTGTTGCAGCCTAGGAGCTCGTTCGTGACAGTCTGCAATAGCGGTGGCGCTGAGGCGCGCGAATAGCGTGTGAGACAAATAGACAGGAGATTTGTTGACTCTTATACACTGGTTACCGAGAGGTGATGGTCGCTGTTCGGTGTCTACACGACTACCCGGAATACATCGTCAGAGGGGGCTGGAATTGCCCGCAGGTGGTGGTGGAAGATGCAGATCCAGTTTCGATGCAGAAAGCGCAGAGATGTTGGAACGGAATCAGGAGTCAACGAACGAACGAACGAACGAACGAAAGT",
        "TTTGCTATCGTGTCGCTCGCGGTGATAGTGACTTCAGCATCAGGATGGAAGAGCTTCGTGCCGACCTGGTTGCGAGTCTGGCCGAACAGGTGCTTGGAACGATGCTTTGCCTGCGGAGCGGAAGGCTTCTTGAAGGTGAACGGCTGCGGAGTGGAAAGTTCGAACTTTGGATCAGCGGATGTTGGAGCAGGGTGTGAGTGCCAGTCCGGAAGGGATCGTTGCGTCTGTGCCGTGTGAAGGGAATGGGCTGCTCGTGGAAGCTTCACTGACGGCGGGAAGCTTGAGCTCGGGAACACGCTGCGTTTGGCAGTGCGGCAACTCGTCCTGGG",
        "ATTCTTCCCAGGACCTCAGCGCAGCCCTGGCCCAGGAAGGCAGGAGACAGAGGCCAGGACGGTCCAGAGGTGTCGAAATGTCCTGGGGACCTGAGCAGCAGCCACCAGGGAAGAGGCAGGGAGGGAGCTGAGGACCAGGCTTGGTTGTGAGAATCCCTGAGCCCAGGCGGTAGATGCCAGGAGGTGTCTGGACTGGCTGGGCCATGCCTGGGCTGACCTGTCCAGCCAGGGAGAGGGTGTGAGGGCAGATCTGGGGGTGCCCAGATGGAAGGAGGCAGGCATGGGGGACACCCAAGGCCCCCTGGCAGCACCATGAACTAAGCAGGACACCTGGAGGGGA",
        "GCCATTGTAATGGGCCGCATGGAACAGAACAAAGTGGTCGGTGTTGCAGCCTAGGAGCTCGTTCGTGACAGTCTGCAATAGCGGTGGCGCTGAGGCGCGCGAATAGCGTGTGAGACAAATAGACAGGAGATTTGTTGACTCTTATACACTGGTTACCGAGAGGTGATGGTCGCTGTTCGGTGTCTACACGACTACCCGGAATACATCGTCAGAGGGGGCTGGAATTGCCCGCAGGTGGTGGTGGAAGATGCAGATCCAGTTTCGATGCAGAAAGCGCAGAGATGTTGGAACGGAATCAGGAGTCAACGAACGAACGAACGAACGAACGAAAGT",
        "TTTGCTATCGTGTCGCTCGCGGTGATAGTGACTTCAGCATCAGGATGGAAGAGCTTCGTGCCGACCTGGTTGCGAGTCTGGCCGAACAGGTGCTTGGAACGATGCTTTGCCTGCGGAGCGGAAGGCTTCTTGAAGGTGAACGGCTGCGGAGTGGAAAGTTCGAACTTTGGATCAGCGGATGTTGGAGCAGGGTGTGAGTGCCAGTCCGGAAGGGATCGTTGCGTCTGTGCCGTGTGAAGGGAATGGGCTGCTCGTGGAAGCTTCACTGACGGCGGGAAGCTTGAGCTCGGGAACACGCTGCGTTTGGCAGTGCGGCAACTCGTCCTGGG"
    ]

    # Run BLAST searches and display results
    flat_results = run_blast_parallel(sequences_to_search, num_processors = int(input("Enter the number of processors: ")))
    for i, hit in enumerate(flat_results, start=1):
        print(f"Results for sequence {i}:")
        print(f"Hit ID: {hit['Hit ID']}, Title: {hit['Title']}, Score: {hit['Score']}, E-value: {hit['E-value']}")
