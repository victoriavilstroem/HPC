# Welcome to the Bioinformatics HPC Simulation Repository!

Hi! 
Are you a bioinformatintian that has never used HPC before? You are in the right place. 
During the time of writing this repository we were in the exact same spot :)

This repository is designed as a hands-on resource for bioinformatics students to explore the exciting world of HPC and its applications in biological data analysis. Through engaging mini simulations in Python, you will have the opportunity to understand the power of multiple processors in optimizing tasks such as sequence filtering.

## What You’ll Find Here
* Interactive Simulations: Experience the impact of parallel processing on bioinformatics tasks.
* Educational Resources: Access guides and documentation to enhance your understanding of HPC concepts.
* Collaborative Learning: Join a community of learners and share your insights, improvements, and questions.

## What will happen
1. You will connect to a Supercomputer from DeiC.
2. See, run and alter the code that allows you to do some bioinformatic tasks like DNA sequence or Protein structure analysis.
3. Experience how HPC allows us to work with huge amounts of data very fast, what would take a lot of time when using just your own laptop. 

## **Using the multiple_processing script**
This script generates random DNA sequences and filters them based on their GC content above a specified threshold (e.g., 50%). The filtering process is executed in parallel using multiple processors, which can significantly speed up the computation time, especially with a large number of sequences. The advantages of using multiple processors is that you can use a cluster, which allows you to use more cores than what is found on your computer. This means that tasks such as filtering DNA sequences based on their GC content can become much faster, since it is a CPU bound task. The filtering function can be computationally intensive, especially when processing many sequences simultaneously. Each sequence needs to be evaluated individually, making it a CPU-bound task.

## **Using the multithreading script**
This script simulates gene coverage for two categories of GC content using a multi-threaded approach. It simulates sequencing coverage for a specified number of genes, where the genes are categorized into two groups based on GC content (intermediate and low). The coverage for each gene is modeled using a Poisson distribution, simulating the randomness typically seen in sequencing experiments. The script utilizes multithreading to perform the coverage simulation concurrently, improving the performance when handling a large number of genes. This approach is used for I/O bound tasks (that is tasks that require a lot of waiting time for input/output operations). The simulation involves generating coverage data, which is a relatively lightweight computational task. Although the Poisson distribution calculations do require some CPU time, the main workload often involves reading from or writing to files, or waiting for data to be ready (that is I/O bound tasks).

## **Confused about multiple processing vs multithreading?**
Fear not! We were too. Think about it in this way:

Multiprocessing
Think of it like having multiple chefs in a kitchen.

What It Does: Each chef (process) works in their own separate kitchen (memory space). They can cook (perform tasks) at the same time without getting in each other's way.

How It Works: If you have a big meal to prepare (a heavy task), you can assign different parts of the meal to different chefs. One chef can chop vegetables, another can boil pasta, and a third can bake bread—all happening at once!

When to Use It: Use this method when the tasks are complex and take a lot of effort (like preparing a multi-course dinner). It works best for tasks that need a lot of brainpower (CPU) and space (memory).

Multithreading
Think of it like having a single chef who can juggle multiple pots on the stove.

What It Does: The chef (thread) works in one kitchen (memory space) but can switch between pots (tasks) quickly. When one pot is cooking and needs some time, the chef can stir another pot or chop ingredients while waiting.

How It Works: If the chef is waiting for water to boil (I/O operation), they can use that time to prepare a salad or set the table, keeping busy and making good use of time.

When to Use It: Use this method for tasks that aren’t too complicated but involve a lot of waiting (like boiling water or baking something). It’s great for keeping things moving without wasting time.

## **Using a cluster**
Go to: interactivehpc.dk
Scroll down and click on ucloud. Log in using wayf. 
Once, you are logged in, go to files and press create drive. There should only be one product you can use, so pick this one and give your drive a name like e.g. "HPC".
Then you upload the data files from this git repository. 


We encourage you to contribute, provide feedback, and collaborate with others to make this a valuable learning experience for everyone involved.

Happy coding! 🚀
