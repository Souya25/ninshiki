def make_path(file_path, file_num):
    num_str = str(file_num)
    num_zero = num_str.zfill(3)
    path = f1_path = "{0}/{1}_{2}.txt".format( file_path, file_path, num_zero)
    return path

file_path = ["city011", "city012", "city021", "city022"]
res=0
for i in range(0,4):
    for j in range(0, 4):
        if j != i:
            for k in range(1,10):
                #f1_path = make_path(file_path[i], k) #テンプレート
                #f1 = open(f1_path)
                res+=1
                for l in range(1,10):
                    #f2_path = make_path(file_path[j], l)
                    #f2 = open(f2_path)
                    #print(type(f1),type(f2))
                    
                    print("i={0},j={1},k={2},l={3},res={4}".format(i,j,k,l,res))