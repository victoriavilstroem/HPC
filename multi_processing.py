import random
from multiprocessing import Pool
import time

# Step 1: Generate random DNA sequences
def generate_sequences(num_sequences, seq_length):
    bases = ['A', 'T', 'C', 'G']
    return [''.join(random.choices(bases, k=seq_length)) for _ in range(num_sequences)]

# Step 2: Define a filter function
def filter_gc_content(sequence, threshold=0.5):
    gc_count = sequence.count('G') + sequence.count('C')
    gc_content = gc_count / len(sequence)
    return gc_content >= threshold

# Step 3: Apply the filter function over many sequences
def filter_sequences(sequences, threshold=0.5):
    return [seq for seq in sequences if filter_gc_content(seq, threshold)]

# Step 4: Set up a function to run with multiple processors
def parallel_filter(sequences, threshold=0.5, num_processors=4):
    chunk_size = len(sequences) // num_processors
    sequence_chunks = [sequences[i:i + chunk_size] for i in range(0, len(sequences), chunk_size)]
    
    # Create a pool of workers
    with Pool(num_processors) as pool:
        results = pool.starmap(filter_sequences, [(chunk, threshold) for chunk in sequence_chunks])
    
    # Flatten the list of results
    filtered_sequences = [seq for sublist in results for seq in sublist]
    return filtered_sequences

# Main execution
if __name__ == "__main__":
    # Parameters
    # User input for processors, GC content threshold, total number of sequences, length of each sequence
    try:
        num_processors = int(input("Enter the number of processors: "))
        threshold = float(input("Enter GC content threshold (e.g., 0.5 for 50%): "))
        num_sequences = int(input("Enter the total number of sequences")) # Total number of sequences
        seq_length = int(input("Enter the DNA sequence length")) # Length of each sequence


    except ValueError:
        print("Invalid input. Please enter a valid number for processors and threshold.")
        exit(1)
    
    # Generate the data
    sequences = generate_sequences(num_sequences, seq_length)
    
    # Measure time for single processor
    start_time = time.time()
    filtered_single = filter_sequences(sequences, threshold)
    single_time = time.time() - start_time
    
    # Measure time for multiple processors
    start_time = time.time()
    filtered_parallel = parallel_filter(sequences, threshold, num_processors=num_processors)
    parallel_time = time.time() - start_time
    
    # Display results
    print(f"\nSingle Processor Time: {single_time:.2f} seconds")
    print(f"Parallel Processing Time ({num_processors} processors): {parallel_time:.2f} seconds")
    print(f"Speedup: {single_time / parallel_time:.2f}x")

