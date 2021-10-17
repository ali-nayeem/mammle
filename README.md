# MAMMLE: Phylogeny estimation based on multiobjective application-aware MUSCLE and maximum likelihood ensemble
**MAMMLE** is a software framework for inferring better phylogenetic trees from unaligned sequences by hybridizing MUSCLE with multiobjective optimization strategy and leveraging multiple Maximum Likelihood hypotheses. MAMMLE may offer a significant improvement (upto 27% in our experiments on BAliBASE 3.0) in tree accuracy over MUSCLE.

<img src="https://github.com/ali-nayeem/mammle/blob/macos/diagram/workflow.png" width="800">

## Multiobjective Application-aware MUSCLE
For MAMMLE, we develop [Multiobjective Application-aware MUSCLE](https://github.com/ali-nayeem/muscle_extesion) by embedding the following four objective functions within the iterattive phase of MUSCLE:
1. Maximize similarity for columns containing gaps (SIMG)
2. Maximize similarity for columns containing no gaps (SIMNG)
3. Maximize sum-of-pairs (SP)
4. Minimize number of gaps (GAP)

<img src="https://github.com/ali-nayeem/mammle/blob/macos/diagram/ma-muscle.png" width="800">



## Installation 
The current version of MAMMLE has been developed and tested entirely on Linux and MAC. 

You need to have:

- [Python](https://www.python.org) (version 3.7 or later) with numpy package
- [Perl](https://www.perl.org/get.html) (version 5.15 or later)

Open a terminal and clone latest MAMMLE from our [github repository](https://github.com/ali-nayeem/mammle). For example you can use: 

```bash
git clone https://github.com/ali-nayeem/mammle.git
```   
## Execution

To run MAMMLE using the command-line:

```bash
python run_mammle.py -i input_fasta -o output_directory
```

MAMMLE by default picks the appropriate configurations automatically for you. 

Run

```bash
python run_mammle.py --help
``` 

to see MAMMLE's various options and descriptions of how they work. For example:

```bash
  --thread THREAD_COUNT, -t THREAD_COUNT
                        Number of threads (default: 1)
  --input INPUT_SEQUENCES, -i INPUT_SEQUENCES
                        Input unaligned sequences in FASTA format
  --out OUTPUT_DIR, -o OUTPUT_DIR
                        Output tree sequences in NEWICK format
  --weight WEIGHT_VECTORS, -w WEIGHT_VECTORS
                        Input weight vectors in CSV format (default: 30 weight
                        vectors in weight/weights4D-30.csv)
``` 

