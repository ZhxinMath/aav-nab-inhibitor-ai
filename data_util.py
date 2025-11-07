
import encoding_matrix
import numpy as np
import sys
import csv


def load_tcr_data(path):
    data = []  
    labels = []
    tcra = []
    tcrb = []

    with open(path, mode='r', newline='') as file:  
        csv_reader = csv.reader(file)  
        head = 1
        for row in csv_reader: 
            if head:
                head = 0 
                continue
            seq = row[0].split('NNNNNNNNNNNNNNNNNNN')
            labels.append(int(row[1]))
            data.append(seq)
            tcra.append(seq[0])
            tcrb.append(seq[1])

    return tcra,tcrb,labels


def seq_encoding_with_matrix(seq='ARNDCQEGHILKMFPSTWYV',matrix=encoding_matrix.BLOSUM62_MATRIX_20):
    # encode data
    # 数据特征处理
    # 通用编码器，根据给定字典编码氨基酸序列，适用于blosum62，onehot，Aatchley特征编码
    """
    字典结构，以3元onehot举例：
    {
        'A' : [1,0,0]
        'B' : [0,1,0]
        'C' : [0,0,1]
    }
    """
    e_seq=np.zeros((len(seq),len(matrix["A"])))
    count = 0
    for aa in seq:
        if aa in matrix:
            e_seq[count]=matrix[aa]
            count+=1
        else:
            sys.stderr.write("Unknown amino acid in peptides: "+ aa +", encoding aborted!\n")
            sys.exit(2)
    return e_seq


def data_padding(encoding_seqs,padding_type,maxlen=False):
    """
    padding函数, 有三种模式, 分别为末尾padding: end, 两端padding: middle, 开头padding: begin
    输入为已经已经做了特征编码的序列集合
    输出为padding完成的序列集合。
    maxlen为空时，自动取集合中的最长值用于padding
    """
    if not maxlen:
        for seq in encoding_seqs:
            maxlen = seq.shape[0] if seq.shape[0]>=maxlen else maxlen
    n_seqs = len(encoding_seqs)
    n_features = encoding_seqs[0].shape[1]
    # 末尾做padding
    if padding_type == 'end':
        enc_aa_seq = np.zeros((n_seqs, maxlen, n_features))
        for i in range(0,n_seqs):
            try:
                enc_aa_seq[i, :encoding_seqs[i].shape[0], :n_features] = encoding_seqs[i]
            except:
                print(i)

    # 两端做padding
    elif padding_type == 'middle':
        enc_aa_seq = np.zeros((n_seqs, maxlen, n_features))
        
        for i in range(0,n_seqs):
            try:
                gap = maxlen-encoding_seqs[i].shape[0]
                margin_l = gap // 2
                enc_aa_seq[i, margin_l:encoding_seqs[i].shape[0]+margin_l, :n_features] = encoding_seqs[i]
            except:
                print(i)

    # 开头做padding
    elif padding_type == 'begin':
        enc_aa_seq = np.zeros((n_seqs, maxlen, n_features))
        for i in range(0,n_seqs):
            try:
                enc_aa_seq[i, -encoding_seqs[i].shape[0]:, :n_features] = encoding_seqs[i]
            except:
                print(i)

    else :
        sys.stderr.write("Unknown padding type: "+ padding_type +", padding aborted!\n")
        sys.exit(2)
    return enc_aa_seq

