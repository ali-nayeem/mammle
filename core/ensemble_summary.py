from multiprocessing import Pool
import numpy as np
import os
import subprocess
from util.read_aln import EncodeAlignment

consensus_bin = "bin/run_paup_consensus.pl"
consensus_strip_bin = "bin/strip_edge_support.pl"
combine_bin = "bin/strip_edge_support_all.pl"


class GREEDY_CONSENSUS:
    
    def __init__(self, root_dir, tmp_dir, no_msa, data, out_dir, in_labels):
        self.tmp_dir = tmp_dir
        self.no_msa = no_msa
        self.data = data
        self.root_path = root_dir
        self.out_dir = out_dir
        self.in_labels = in_labels

    def combine_tree(self, num, data):
        cmd = ["perl", self.root_path + '/' + combine_bin, "-i", self.tmp_dir, "-o", self.tmp_dir + '/' + data + '-combined.tre', "-n", str(num)]
        subprocess.run(cmd, stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)
        return self.tmp_dir + '/' + data + '-combined.tre'

    def get_unique_id(self):
        uniq_align = {} #{[(0,0)]: -1}
        uniq_id = []
        for i in range(self.no_msa):
            encoded = EncodeAlignment(self.tmp_dir + '/' + str(i) + '.aln', self.in_labels)
            if uniq_align.get(encoded) == None:
                uniq_align[encoded] = i
                uniq_id.append(i)
        return uniq_id

    def save_selected(self, combined_tree_path, selected):
        in_file = open(combined_tree_path)
        selected_tree_path = self.tmp_dir + '/' + self.data + '-unique.tre'
        out_file = open(selected_tree_path, 'w')
        for position, line in enumerate(in_file):
            if position in selected:
                out_file.write(line)
        in_file.close()
        out_file.close()
        return selected_tree_path

    def consensus_tree(self, inpath, data, consensus_type):
        cmd = ["perl", self.root_path + '/' + consensus_bin, "-i", inpath, "-o", self.tmp_dir + '/' + data]
        subprocess.run(cmd, stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)
        cmd = ["perl", self.root_path + '/' + consensus_strip_bin, "-i", self.tmp_dir + '/' + data + "." + consensus_type + ".tree", "-o", self.out_dir +'/' + data + '-output' + '.tree']
        subprocess.run(cmd, stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT)   
    
   
           
    def execute(self):
        
        combined_tree_path = self.combine_tree(self.no_msa, self.data)
        uniq_id = self.get_unique_id()
        uniq_tree_path = self.save_selected(combined_tree_path, uniq_id)
        self.consensus_tree(uniq_tree_path, self.data, 'greedy')
        print("Saved output greedy consensus tree at %s" % (self.tmp_dir))