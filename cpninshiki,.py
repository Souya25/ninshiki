import math
import copy
import numpy as np
import time


def make_path(file_path, file_num):
    num_str = str(file_num)
    num_zero = num_str.zfill(3)
    path = f1_path = "{0}/{1}_{2}.txt".format( file_path, file_path, num_zero)
    return path

def local_distance(f1 ,f2):
    i = 0
    j = 0
    ans = 0
    dim = f1.readline().split()
    dim = f2.readline().split()
    dim = f1.readline().split()
    dim = f2.readline().split()
    dim = f1.readline().split()
    dim = f2.readline().split()
    dim1 = np.empty( (0,15) , str)
    dim2 = np.empty( (0,15) , str)
    #print(dim1,dim2)
    for line1 in f1:
        dim1 = np.append(dim1, np.array([line1.split()]), axis = 0 )
        i += 1
    for line2 in f2:
        dim2 = np.append(dim2, np.array([line2.split()]), axis = 0)
        j += 1
    local_d = np.empty((0,j),float)
    for i2 in range(i):
        #print(local_d)     
        list_ans =np.empty(0,float)
        for j2 in range(j):
            for k in range (0,15):
                ans += pow( float(dim1[i2][k]) - float(dim2[j2][k]), 2)
            list_ans = np.append(list_ans, math.sqrt(ans))
            ans = 0
            #print(i2,j2)
        #print(list_ans.shape)
        local_d = np.append(local_d, [copy.deepcopy(list_ans)], axis = 0) 
    #print(local_d.shape)
    return local_d
  
    
def cumulative_distance(ld):
    #print(ld)
    cum_dis = np.empty((0,len(ld[0])), float)
    cum_up =0
    i = 0
    j = 0
    for l in ld:
        cum_dis_line = np.empty(0,float)
        j = 0
        for l_i in l:
            if i == 0 and j == 0:
                #print(i)
                cum_dis_line = np.append(cum_dis_line, l_i)
            if i != 0:
                cum_up = float(cum_dis[i-1][j]) + float(l_i)
            if j != 0:
                cum_left = float(cum_dis_line[j-1]) + float(l_i)
            if i != 0 and j !=0:
                cum_diag = float(cum_dis[i-1][j-1]) + (2 * float(l_i))
                #print("up  {}, left  {}, diag  {}".format(cum_up, cum_left, cum_diag))
                if cum_up <= cum_left and cum_up <= cum_diag:
                    cum_dis_line = np.append(cum_dis_line, cum_up)
                elif cum_diag <= cum_up and cum_diag <= cum_left:
                    cum_dis_line = np.append(cum_dis_line, cum_diag)
                else :
                    cum_dis_line = np.append(cum_dis_line, cum_left)
            elif i != 0:
                #print("up  {}".format(cum_up))
                cum_dis_line = np.append(cum_dis_line, cum_up)
            elif j != 0:
                #print("left  {}".format(cum_left))
                cum_dis_line = np.append(cum_dis_line, cum_left)
            #print(cum_dis_line[-1])
            j+=1
        cum_dis = np.append(cum_dis, [copy.deepcopy(cum_dis_line)], axis = 0)
        i += 1
    #print(cum_dis.shape)
    #print(cum_dis[59])
    t = cum_dis[-1][-1]/(i+j) #単語間距離 =　最終点までの累積距離 / i+j
    return(t)



file_path = np.array(["city011", "city012", "city021", "city022"])
res = 0
for i in range(0,4):
    for j in range(0, 4):
        score = 0
        for k in range(1,101):
            min_t_dis = 0
            if j != i:
                for l in range(1,101):
                    f1_path = make_path(file_path[i], k) #テンプレート
                    f1 = open(f1_path)
                    f2_path = make_path(file_path[j], l)
                    f2 = open(f2_path)
                    #print(f1_path ,f2_path)
                    #print(f1,f2)
                    #print("i={0},j={1},k={2},l={3},res={4}".formatw(i,j,k,l,res))
                    #start = time.time()
                    ld = local_distance(f1,f2) #局所距離を得た
                    #print(time.time() - start)
                    f1.close()
                    f2.close()
                    #print("get_ld")
                    #print(len(ld), l)
                    #print("do")
                    start = time.time()
                    t_dis = cumulative_distance(ld)
                    print(time.time() - start)
                    #print(t_dis, k, l)
                    if min_t_dis == 0 or min_t_dis >= t_dis:
                        min_t_dis = t_dis
                        min_num = l
                    #print(min_num, min_t_dis ,t_dis, k,l, len(ld[0]))
                if min_num == k:
                    score += 1
                    print("scored")
                #print("fin101")

                    
