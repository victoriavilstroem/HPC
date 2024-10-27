# Welcome to the Bioinformatics HPC Simulation Repository!

Hi! 
Are you a bioinformatintian that has never used HPC before? You are in the right place. 
During the time of writing this repository we were in the exact same spot :)

This repository is designed as a hands-on resource for bioinformatics students to explore the exciting world of HPC and its applications in biological data analysis. Through engaging mini simulations in Python, you will have the opportunity to understand the power of multiple processors in optimizing tasks such as sequence filtering.

## What You’ll Find Here
* Interactive Simulations: Experience the impact of parallel processing on bioinformatics tasks.
* (*Soon*) Educational Resources: Access guides and documentation to enhance your understanding of HPC concepts.
* (*Soon*) Collaborative Learning: Join a community of learners and share your insights, improvements, and questions.

## What will happen
1. You will connect to a Supercomputer from DeiC.
2. See, run and alter the code that allows you to do some bioinformatic tasks like DNA sequence or Protein structure analysis. There are 3 .py files for you to try out!
3. Experience how HPC handles massive data in minutes, not hours.

## Using the multiple_processing script (multi_processing.py)
This script generates random DNA sequences and filters them based on their GC content above a specified threshold (e.g., 50%). The filtering process is executed in parallel using multiple processors, which can significantly speed up the computation time, especially with a large number of sequences. The advantages of using multiple processors is that you can use a cluster, which allows you to use more cores than what is found on your computer. This means that tasks such as filtering DNA sequences based on their GC content can become much faster, since it is a CPU bound task. The filtering function can be computationally intensive, especially when processing many sequences simultaneously. Each sequence needs to be evaluated individually, making it a CPU-bound task.

## Using the multithreading script (multithreading.py)
This script simulates gene coverage for two categories of GC content using a multi-threaded approach. It simulates sequencing coverage for a specified number of genes, where the genes are categorized into two groups based on GC content (intermediate and low). The coverage for each gene is modeled using a Poisson distribution, simulating the randomness typically seen in sequencing experiments. The script utilizes multithreading to perform the coverage simulation concurrently, improving the performance when handling a large number of genes. This approach is used for I/O bound tasks (that is tasks that require a lot of waiting time for input/output operations). The simulation involves generating coverage data, which is a relatively lightweight computational task. Although the Poisson distribution calculations do require some CPU time, the main workload often involves reading from or writing to files, or waiting for data to be ready (that is I/O bound tasks).

## Using the BLAST comparison script (blast.py)
This script takes a set of DNA sequences and runs BLAST searches for each one in parallel using multiple processors. By distributing the BLAST jobs, this method speeds up the process of finding similar sequences in the NCBI nucleotide database. This approach is particularly effective when analyzing multiple sequences at once since each sequence comparison is independent and can be processed simultaneously. This one you can just run on your own computer. Input some DNA sequences and change num_processors (the one at the buttom of the script, line 60) to your desired amount (remember to check how many cores your computer has). It will probably not make sense to run it on the cluster since, the NCBI database can't handle more than 8 DNA sequences at a time. Therefore, 8 cores, which your computer probably has, should be enough. But if you had a big enough cluster, you could download a local version of the NCBI database and this script could run in true parallel. Then the cluster would be really useful for multiple DNA sequences at a time. 

## Confused about multiple processing vs multithreading?
Fear not! We were too. Think about it in this way:

### Multiprocessing
Think of it like having multiple chefs in a kitchen.

What It Does: Each chef (process) works in their own separate kitchen (memory space). They can cook (perform tasks) at the same time without getting in each other's way.

How It Works: If you have a big meal to prepare (a heavy task), you can assign different parts of the meal to different chefs. One chef can chop vegetables, another can boil pasta, and a third can bake bread—all happening at once!

When to Use It: Use this method when the tasks are complex and take a lot of effort (like preparing a multi-course dinner). It works best for tasks that need a lot of brainpower (CPU) and space (memory).

### Multithreading
Think of it like having a single chef who can juggle multiple pots on the stove.

What It Does: The chef (thread) works in one kitchen (memory space) but can switch between pots (tasks) quickly. When one pot is cooking and needs some time, the chef can stir another pot or chop ingredients while waiting.

How It Works: If the chef is waiting for water to boil (I/O operation), they can use that time to prepare a salad or set the table, keeping busy and making good use of time.

When to Use It: Use this method for tasks that aren’t too complicated but involve a lot of waiting (like boiling water or baking something). It’s great for keeping things moving without wasting time.

## Using a cluster
Go to: interactivehpc.dk   
Scroll down and click on ucloud. Log in using wayf.   
Once, you are logged in, go to files and press create drive. There should only be one product you can use, so pick this one and give your drive a name like e.g. "HPC".   
Then you upload the .py files from this git repository.
If you press a file, you can click "launch with", pick "Coder Python". Pick a machine (you don't necessarily need a very large one for these scripts, but the bigger the machine, the bigger you can set the cores in the scripts). There are up to 64 core machines on the cluster. 
Press launch and wait for a while till the machine is ready. Then you can press "Open Interface" and it will open an online version of VS code that you can use. 
Remember to install all the correct packages, since they are no longer installed. Ask chatGPT for help :-)


We encourage you to contribute, provide feedback, and collaborate with others to make this a valuable learning experience for everyone involved.

Happy coding! 🚀
