from multiprocessing import Pool
import numpy as np
import sys
import subprocess
from pathlib import Path
obj_id = {'simg': 0, 'simng': 1, 'osp': 2, 'gap': 3}
mo_aw_muscle_bin = 'bin/mo-aw-muscle'


class MO_MSA_MUSCLE:
    
    def __init__(self, root_path, input_file, output_dir, weight_file, no_thread):
        self.input_file = input_file
        self.root_path = root_path
        self.data_name = input_file.split('/')[-1]
        self.tmp_dir = output_dir + '/tmp-' + self.data_name
        Path(self.tmp_dir).mkdir(parents=True, exist_ok=True)
        self.no_thread = no_thread
        if weight_file is None:
            weight_file = root_path + '/weight/weights4D-30.csv'
        try:    
            self.weight_matrix = np.loadtxt(weight_file, delimiter=',',ndmin=1)
        except OSError:
            print ("Could not open/read file: " + weight_file)
            sys.exit()
        if len(self.weight_matrix[0]) < 4:
            print ("Weight vector dimension is less than 4")
            sys.exit()
        self.no_weight = len(self.weight_matrix)
    
    def run(self, id):
    #      $muscle_ext -simg $w1 -simng $w2 -osp $w3 -gap $w4 -objscore sp -maxiters 20 -in $input_seq -out 
        if id < len(self.weight_matrix):
            #print("Computing %d-th MSA" % id)
            weight = self.weight_matrix[id]
            cmd = [self.root_path + '/' + mo_aw_muscle_bin] #,  input_file, "-o", '../out/tmp/' + data + '-combined-original.tree', "-n", str(num)]
            for k,v in obj_id.items():
                cmd.extend(['-'+k, str(weight[v])])
            cmd.extend(['-in', self.input_file, '-out', self.tmp_dir + '/' + str(id) + '.aln' ])
            cmd.extend(['-objscore', 'sp', '-maxiters', '20'])
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)     

    def execute(self):
        # out_dir = output_file.split('/')[:-1]
        # if len(out_dir) == 0:
        #     out_dir = ''
        print("Start computing %d MSAs using %d threads" % (self.no_weight, self.no_thread))
        with Pool(self.no_thread) as p:
            p.map(self.run, list(range(len(self.weight_matrix))))
        print("Saved %d MSAs at %s" % (self.no_weight, self.tmp_dir))
        return self.data_name, self.tmp_dir, self.no_weight