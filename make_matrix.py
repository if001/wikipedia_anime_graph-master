#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
多次元尺度構成法(MDS)に渡す行列を生成する
"""

#-------------------------------------------------------#
def set_vc(fname):
    try :
        #句読点で区切られた名前をlistに格納
        for line in open(fname, 'r'):
            namelist = line[:-1].split(',')
        print(namelist)
    except :
        print("cannot be opend")
        exit(-1)
    return namelist

#-------------------------------------------------------#
def  write_mat(mat):
    f = open('text.txt','w')
    f.write(mat)
    f.close()

#-------------------------------------------------------#
def make_matrix(fname):
    import numpy as np
    from wiki_relevance import wiki_rel_mod

    name=set_vc(fname)

    matlen=len(name)
    rel_mat=np.zeros([matlen,matlen], dtype=float)

    for i in range(matlen-1):
        for j in range(i,matlen-1):
            tmp_rel=wiki_rel_mod(name[i],name[j+1],"")
            print(name[i],name[j+1],tmp_rel)
            if tmp_rel == -1 : #エラーが帰ってきたらスキップ
                print("error name:",name[i],name[j+1])
                i,j=i-1,j-1
            else :
                rel_mat[i][j+1] = tmp_rel
                rel_mat[j+1][i] = rel_mat[i][j+1] #対象行列にする
    # print("matrix:")
    # print(rel_mat)
    # write_mat(rel_mat) #行列をファイルに出力
    return rel_mat
#-------------------------------------------------------#
if __name__ == '__main__' :
    make_matrix(fname)
