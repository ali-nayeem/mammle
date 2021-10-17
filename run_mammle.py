import argparse
import os 
from core.mo_aw_muscle import MO_MSA_MUSCLE
from core.fasttree_ml import ML_TREE_FASTTREE
from core.ensemble_summary import GREEDY_CONSENSUS
from util.read_aln import ReadSeqsAndLabels

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    # parser.add_argument('integers', metavar='N', type=int, nargs='+',
    #                    help='an integer for the accumulator')
    
    parser.add_argument('--thread', '-t', dest='thread_count',type=int, default=1,
                    help='Number of threads (default: 1)')
    parser.add_argument('--input', '-i', dest='input_sequences',type=str, default=1, required=True,
                    help='Input unaligned sequences in FASTA format')      
    parser.add_argument('--out', '-o', dest='output_dir',type=str, default=1, required=True,
                    help='Output tree sequences in NEWICK format')
    parser.add_argument('--weight', '-w', dest='weight_vectors',type=str, default=None,
                    help='Input weight vectors in CSV format (default: 30 weight vectors in weight/weights4D-30.csv)')
                                

    args = parser.parse_args()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    #print(dir_path)
    if args.output_dir[0] != '/' or args.output_dir[0] != '~':
        full_output_dir = dir_path + '/' + args.output_dir
    
    print("Start computing tree on %s" % args.input_sequences)
    input_labels, input_seqs = ReadSeqsAndLabels(args.input_sequences)  
    mo_aw_muscle = MO_MSA_MUSCLE(dir_path, args.input_sequences, full_output_dir, args.weight_vectors, args.thread_count)
    data, tmp_dir, no_msa = mo_aw_muscle.execute()
    ml_fasttree = ML_TREE_FASTTREE(dir_path, tmp_dir, no_msa, args.thread_count)
    ml_fasttree.execute()
    greedy = GREEDY_CONSENSUS(dir_path, tmp_dir, no_msa, data,  full_output_dir, input_labels)
    greedy.execute()

    #TODO
    #Error/exception handling routines
