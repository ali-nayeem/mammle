from multiprocessing import Pool
import numpy as np
import os
import subprocess

fasttree_bin = 'bin/fasttreemp'


def run(command):
    p1 = os.popen(command)
    temp = p1.readline()
    p1.close()
    return temp.rstrip()

class ML_TREE_FASTTREE:
    
    def __init__(self, root_dir, tmp_dir, no_msa, no_thread):
        self.tmp_dir = tmp_dir
        self.no_msa = no_msa
        self.no_thread = no_thread
        self.root_path = root_dir
    
    def run(self, id):
    #      $muscle_ext -simg $w1 -simng $w2 -osp $w3 -gap $w4 -objscore sp -maxiters 20 -in $input_seq -out 
        if id < self.no_msa:
            #print("Computing %d-th MSA" % id)
            cmd = [self.root_path + '/' + fasttree_bin, '-wag', '-gamma', '-fastest', '-quiet']
            cmd.extend(['-log', self.tmp_dir + '/' + str(id) + "-tre.log",
               self.tmp_dir + '/' + str(id) + ".aln"])#[self.root_path + '/' + mo_aw_muscle_bin] #,  input_file, "-o", '../out/tmp/' + data + '-combined-original.tree', "-n", str(num)]
            with open(self.tmp_dir + '/' + str(id) + ".tre", 'w') as output:
                subprocess.run(cmd, stdout=output)
                # line = run("grep Gamma20LogLk  ../out/" + data + "-tre.log")
                # ml = line.split()[1]
           
    def execute(self):
        # out_dir = output_file.split('/')[:-1]
        # if len(out_dir) == 0:
        #     out_dir = ''
        print("Start computing %d ML trees using %d threads" % (self.no_msa, self.no_thread))
        with Pool(self.no_thread) as p:
            p.map(self.run, list(range(self.no_msa)))
        print("Saved %d ML trees at %s" % (self.no_msa, self.tmp_dir))
        return self.tmp_dir