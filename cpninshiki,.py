import math
import copy

def make_path(file_path, file_num):
    num_str = str(file_num)
    num_zero = num_str.zfill(3)
    path = f1_path = "{0}/{1}_{2}.txt".format( file_path, file_path, num_zero)
    return path

def local_distance(f1 ,f2):
    i = 0
    j = 0
    ans = 0
    list_ans = []
    local_d =[]
    dim = f1.readline().split()
    dim = f2.readline().split()
    dim = f1.readline().split()
    dim = f2.readline().split()
    dim = f1.readline().split()
    dim = f2.readline().split()
    dim1 = []
    dim2 = []
    #print(dim1,dim2)
    for line1 in f1:
        dim1.append(line1.split())
        i += 1
    for line2 in f2:
        dim2.append(line2.split())
        j += 1
    for i2 in range(i):
        #print(local_d)     
        list_ans =[]
        for j2 in range(j):
            for k in range (0,15):
                ans += pow( float(dim1[i2][k]) - float(dim2[j2][k]), 2)
            list_ans.append(math.sqrt(ans))
            ans = 0
            #print(i2,j2)
        local_d.append(copy.deepcopy(list_ans))
    #print(i,j)
    #print(local_d)   
    return local_d
  
    
def cumulative_distance(ld):
    cum_dis = []
    cum_up =0
    i = 0
    j = 0
    for l in ld:
        cum_dis_line = []
        for l_i in l:
            if i == 0 and j == 0:
                #print(i)
                cum_dis_line.append(l_i)
            if i != 0:
                cum_up = float(cum_dis[i-1][j]) + float(l_i)
            if j != 0:
                cum_left = float(cum_dis_line[j-1]) + float(l_i)
            if i != 0 and j !=0:
                cum_diag = float(cum_dis[i-1][j-1]) + 2 * float(l_i)
                if cum_up >= cum_left and cum_up >= cum_diag:
                    cum_dis_line.append(cum_up)
                elif cum_diag >= cum_up and cum_diag >= cum_left:
                    cum_dis_line.append(cum_diag)
                else :
                    cum_dis_line.append(cum_left)   
            elif i != 0:
                cum_dis_line.append(cum_up)
            elif j != 0:
                cum_dis_line.append(cum_left)
            j+=1
        cum_dis.append(copy.deepcopy(cum_dis_line))
        i += 1
        j = 0
    #print(cum_dis[59])
    #print(cum_dis[60])
    return(cum_dis[-1][-1])



file_path = ["city011", "city012", "city021", "city022"]
res = 0
for i in range(0,4):
    for j in range(0, 4):
        for k in range(1,101):
            min_cum_dis = 0 
            if j != i:
                for l in range(1,101):
                    f1_path = make_path(file_path[i], k) #テンプレート
                    f1 = open(f1_path)
                    f2_path = make_path(file_path[j], l)
                    f2 = open(f2_path)
                    print(f1_path ,f2_path)
                    #print(f1,f2)
                    #print("i={0},j={1},k={2},l={3},res={4}".formatw(i,j,k,l,res))
                    ld = local_distance(f1,f2) #局所距離を得た
                    print(len(ld[0]))
                    f1.close()
                    f2.close()
                    #print("get_ld")
                    #print(ld)
                    cum_dis = cumulative_distance(ld)
                    if min_cum_dis == 0 or min_cum_dis >= cum_dis:
                        min_cum_dis = cum_dis
                        min_num = l
                    #print(min_num, min_cum_dis, k,l)
                    
                    #print(cum_dis, i, j , k ,l)
                if min_num == k:
                    score += 1
                    #print("scored")
            #print("fin 101")

                    
