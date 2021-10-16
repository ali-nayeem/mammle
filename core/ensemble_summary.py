from multiprocessing import Pool
import numpy as np
import os
import subprocess

consensus_bin = "bin/run_paup_consensus.pl"
consensus_strip_bin = "bin/strip_edge_support.pl"
combine_bin = "bin/strip_edge_support_all.pl"


class GREEDY_CONSENSUS:
    
    def __init__(self, root_dir, tmp_dir, no_msa, data, out_dir):
        self.tmp_dir = tmp_dir
        self.no_msa = no_msa
        self.data = data
        self.root_path = root_dir
        self.out_dir = out_dir

    def combine_tree(self, num, data):
        cmd = ["perl", self.root_path + '/' + combine_bin, "-i", self.tmp_dir, "-o", self.tmp_dir + '/' + data + '-combined.tre', "-n", str(num)]
        subprocess.run(cmd, stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)
        return self.tmp_dir + '/' + data + '-combined.tre'

    def consensus_tree(self, inpath, data, consensus_type):
        cmd = ["perl", self.root_path + '/' + consensus_bin, "-i", inpath, "-o", self.tmp_dir + '/' + data]
        subprocess.run(cmd, stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)
        cmd = ["perl", self.root_path + '/' + consensus_strip_bin, "-i", self.tmp_dir + '/' + data + "." + consensus_type + ".tree", "-o", self.out_dir +'/' + data + '-output' + '.tree']
        subprocess.run(cmd, stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT)   
    
   
           
    def execute(self):
        # out_dir = output_file.split('/')[:-1]
        # if len(out_dir) == 0:
        #     out_dir = ''
        # print("Start computing %d ML trees using %d threads" % (self.no_msa, self.no_thread))
        # with Pool(self.no_thread) as p:
        #     p.map(self.run, list(range(self.no_msa)))
        # print("Saved %d ML trees at %s" % (self.no_msa, self.tmp_dir))
        # return self.tmp_dir
        combined_tree_path = self.combine_tree(self.no_msa, self.data)
        self.consensus_tree(combined_tree_path, self.data, 'greedy')
        print("Saved output greedy consensus tree at %s" % (self.tmp_dir))