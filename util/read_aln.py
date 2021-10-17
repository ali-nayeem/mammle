import sys
import re

def Die(s):
    print(s)
    sys.exit(1)

def ReadSeqs(FileName):
    Seqs = {}
    Id = ""
    File = open(FileName)
    while 1:
        Line = File.readline()
        if len(Line) == 0:
            return Seqs
        if len(Line) == 0:
            continue
        if Line[0] == ">":
            Id = Line[1:][:-1]
            Seqs[Id] = ""
        else:
            if Id == "":
                Die("FASTA file '%s' does not start with '>'" % FileName)
            Seqs[Id] = Seqs[Id] + Line[:-1]

def ReadSeqsAndLabels(FileName):
    Seqs = []
    Labels = []
    File = open(FileName)
    while 1:
        Line = File.readline()
        if len(Line) == 0:
            return Labels, Seqs
        Line = Line.strip()
        if len(Line) == 0:
            continue
        if Line[0] == ">":
            Id = Line[1:]
            Labels.append(Id)
            Seqs.append("")
        else:
            i = len(Seqs)-1
            Seqs[i] = Seqs[i] + Line

def EncodeAlignment(alnPath, labels):
    seqs = ReadSeqs(alnPath)
    index_list = ''
    for label in labels:
        #index_list.extend([(m.start(), m.end()) for m in re.finditer(r'(\-)\1*', seqs[label])])
        for m in re.finditer(r'(\-)\1*', seqs[label]):
            index_list += str((m.start(), m.end()))

    return index_list

# InLabels, InSeqs = ReadSeqs2(InputFileName)
# AlnSeqs = ReadSeqs(AlnFileName)
#
# for Label in InLabels:
#     if Label not in AlnSeqs.keys():
#         Die("Not found in alignment: " + Label)
#     print(">" + Label)
#     print(AlnSeqs[Label])
