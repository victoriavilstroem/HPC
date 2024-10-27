import numpy as np
import concurrent.futures
import time

num_genes = int(input("Enter the number of genes: "))
gc_content_intermediate = 0.5  # Intermediate GC content
gc_content_low = 0.2           # Low GC content
coverage_intermediate = int(input("Enter the coverage of intermediate GC content (e.g. 5X): "))
coverage_low = int(input("Enter the coverage of low GC content (e.g. 1X): "))
num_threads = int(input("Enter the number of threads: "))

# Function to simulate coverage for a single gene
def simulate_gene_coverage(gc_content, coverage):
    return np.random.poisson(coverage)

# Function to simulate coverage for a batch of genes
def simulate_coverage_batch(gc_content, coverage, batch_size):
    return [simulate_gene_coverage(gc_content, coverage) for _ in range(batch_size)]

# Main function to run the simulation without threading
def run_simulation_single_threaded():
    results = []
    for _ in range(int(num_genes * 0.9)):  # 90% intermediate GC content
        results.append(simulate_gene_coverage(gc_content_intermediate, coverage_intermediate))
    for _ in range(int(num_genes * 0.1)):  # 10% low GC content
        results.append(simulate_gene_coverage(gc_content_low, coverage_low))
    return results

# Main function to run the simulation with multi-threading
def run_simulation_multi_threaded():
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # 90% intermediate GC content
        future_intermediate = [
            executor.submit(simulate_coverage_batch, gc_content_intermediate, coverage_intermediate, 100) 
            for _ in range(int(num_genes * 0.9) // 100)
        ]
        # 10% low GC content
        future_low = [
            executor.submit(simulate_coverage_batch, gc_content_low, coverage_low, 100) 
            for _ in range(int(num_genes * 0.1) // 100)
        ]
        
        # Collect results as they complete
        for future in concurrent.futures.as_completed(future_intermediate + future_low):
            results.extend(future.result())
    return results

# Measure time for single-threaded run
start_time = time.time()
single_threaded_results = run_simulation_single_threaded()
single_threaded_time = time.time() - start_time
print(f"Single-threaded time: {single_threaded_time:.2f} seconds")

# Measure time for multi-threaded run
start_time = time.time()
multi_threaded_results = run_simulation_multi_threaded()
multi_threaded_time = time.time() - start_time
print(f"Multi-threaded time: {multi_threaded_time:.2f} seconds")

# Compare results
print(f"Speedup from multi-threading: {single_threaded_time / multi_threaded_time:.2f}x")