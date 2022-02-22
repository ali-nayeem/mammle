# MAMMLE: A framework for phylogeny estimation based on multiobjective application-aware MSA and maximum likelihood ensemble
**MAMMLE** is a software framework for inferring better phylogenetic trees from unaligned sequences by hybridizing MUSCLE with multiobjective optimization strategy and leveraging multiple Maximum Likelihood hypotheses. MAMMLE may offer a significant improvement (upto 27% in our experiments on BAliBASE 3.0) in tree accuracy over MUSCLE.

<figure>
  <img src="https://github.com/ali-nayeem/mammle/blob/linux/diagram/workflow-v2.png" alt="Trulli" style="width:80%">
  <figcaption>Fig.1: Simplified phylogenetic reconstruction pipeline of MAMMLE framework. The components open to modification are marked with a blue shade.</figcaption>
</figure>

## Multiobjective Application-aware MUSCLE
For MAMMLE, we develop [Multiobjective Application-aware MUSCLE](https://github.com/ali-nayeem/muscle_extesion) by embedding the following four objective functions, identified based on their better correlation to the tree accuracy, within the iterative phase of MUSCLE:
1. Maximize similarity for columns containing gaps (SIMG)
2. Maximize similarity for columns containing no gaps (SIMNG)
3. Maximize sum-of-pairs (SP)
4. Minimize number of gaps (GAP)

<figure>
  <img src="https://github.com/ali-nayeem/mammle/blob/macos/diagram/ma-muscle.png" alt="Trulli" style="width:80%">
  <figcaption>Fig.2: High-level workflow of multiobjective application-aware MUSCLE for a single weight vector. Steps (3.4 to 3.6) added/modified on the original MUSCLE are marked with red color. This figure is modification of the original image taken from https://doi.org/10.1093/nar/gkh340.</figcaption>
</figure>

## Software Commands
Below we provide the software commands used for out experimentation. Please note the provided commands of MUSCLE and RAxML only represent the current components of MAMMLE framework. One can easily replace these components with other appropriate tools/commands which is the main strength of this framework.

- MUSCLE (version 3.8.1551) command
```
muscle -in [unaligned_sequences] -out  [output_name] -maxiters 20
```
- RAxML (version 8.2.11) command for reference tree
```
raxml -f a -m PROTGAMMAAUTO -s [reference_msa]  -n [output_name]  -p 1234 -x 1234 -#100 -T [thread_count]
```
- RAxML (version 8.2.11) command for ML tree
```
raxml -m PROTCATWAGF -n [output_name]  -s [estimated_msa]   -p 123456789 -T [thread_count] 	
```
- MAFFT (version 7.490) command
```
linsi --auto --amino  --thread [thread_count]  [unaligned_fasta] > [output_name]
```
- M2Align (version 4.13.1) command
```
java -cp [path_to_jar] org.uma.khaos.m2align.runner.M2AlignBALIBASERunner [balibase_instance] [path_to_balibase_data] [number_of_evaluations:15000] [population_size:30] [thread_count]
```

## Installation 
The current version of MAMMLE has been developed and tested entirely on Linux and MAC. 

You need to have:

- [Python](https://www.python.org) (version 3.7 or later) with numpy package
- libpython2.7 (install via ```sudo apt-get install libpython2.7```)
- [Perl](https://www.perl.org/get.html) (version 5.15 or later)

Open a terminal and clone latest MAMMLE from our [github repository](https://github.com/ali-nayeem/mammle). For example you can use: 

```bash
git clone https://github.com/ali-nayeem/mammle.git
cd mammle
```  
Give executive permission to the binaries 

```bash
chmod +x bin/*
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

