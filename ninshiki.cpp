#include<iostream>
#include<string>
#include<sstream>
#include<iomanip>
#include<fstream>
#include<vector>
#include<math.h>

using namespace std;
const int frame_max = 15;

string makepath(string file_path, int file_num)
{   
    string path_str;
    std::stringstream path;
    path << file_path << "/" << file_path << "_" << std::setw(3) << std::setfill('0') << file_num  << ".txt";
    
    return path_str = path.str();
}

vector<string> split(string str, string separator)//文字列を分割しvectorに格納する関数
{
    vector<string> result;
    string tstr = str + separator;
    long l = tstr.length(), sl = separator.length();
    string::size_type pos = 0, prev = 0;

    for (;pos < l && (pos = tstr.find(separator, pos)) != string::npos; prev = (pos += sl)) 
    {
        result.emplace_back(tstr, prev, pos - prev);
    }
    
    return result;
}


double local_distance(string f1_path, string f2_path)
{   
    vector< vector< string>> f1_vec(160), f2_vec(160);
    vector<string> f_line;
    ifstream f1(f1_path), f2(f2_path);
    string f1_data, f2_data;
    int f1_size = 0, f2_size = 0, i = 0, j, k;
    double ans, cum_up, cum_diag, cum_left;
    while( getline( f1, f1_data))
    {   
        if(i > 2)
        {
            f_line = split(f1_data, " ");
            
            for( j = 0; j < 15; j++)
            {
                f1_vec[i-3].emplace_back(f_line[j]);
            }
        }
    i++;
    }
    f1_size = i-3;
    i = 0;
    while( getline( f2, f2_data))
    {   
        if(i > 2)
        {
            f_line = split(f2_data, " ");
            
            for( j = 0; j < 15; j++)
            {
                f2_vec[i-3].emplace_back(f_line[j]);       
            }
        }
    i++;
    }
    f2_size = i-3;
    
    f1.close();
    f2.close();
    vector< vector< double>> ld_vec(f1_size, vector<double>(f2_size)), cum_dis_vec(f1_size, vector<double>(f2_size));
    //局所距離を求める
    for(i = 0; i < f1_size; i++)
    {
        for(j = 0; j < f2_size; j++)
        {
            for(k = 0; k < 15; k++)
            {
                ans += pow( stod(f1_vec[i][k]) - stod(f2_vec[j][k]),2);
            }
            ld_vec[i][j] = sqrt(ans);
            ans = 0;
        }
    }
    //初期条件
    cum_dis_vec[0][0] = ld_vec[0][0];
    //境界条件
    for( i = 1; i < f1_size; i++)
    {
        cum_dis_vec[i][0] = cum_dis_vec[i-1][0] + ld_vec[i][0];
    }
    for( j = 1; j < f2_size; j++)
    {
        cum_dis_vec[0][j] = cum_dis_vec[0][j-1] + ld_vec[0][j];
    }
    //累積距離
    for(i = 1; i < f1_size; i++)
    {
        for(j = 1; j < f2_size; j++)
        {
            cum_up = cum_dis_vec[i-1][j] +  ld_vec[i][j];
            cum_diag = cum_dis_vec[i-1][j-1] + 2 * ld_vec[i][j];//斜め遷移の計算
            cum_left = cum_dis_vec[i][j-1] +  ld_vec[i][j];
            if(cum_up <= cum_diag && cum_up <= cum_left)
            {
                cum_dis_vec[i][j] = cum_up;
            }
            else if(cum_diag <= cum_up && cum_diag <= cum_left)
            {
                cum_dis_vec[i][j] = cum_diag;
            }
            else if(cum_left <= cum_diag && cum_left <= cum_up)
            {
                cum_dis_vec[i][j] = cum_left;
            }
        }
    }
    return ( cum_dis_vec[ f1_size - 1][ f2_size - 1]/ ( f1_size + f2_size));
}

int main()
{
    vector<string> f_line;
    vector< vector< double>> ld;
    double total, total_min=-1, percent;
    std::ifstream ifs;
    int  i, j, k, l, score = 0 ,min_num, count=0;
    string file_path[] = { "city011", "city012", "city021", "city022"};
    string f1_path, f2_path, f1_data, f2_data, data;
    for(i = 0; i < 4; i++)
    {    
        for(j =0; j < 4; j++)
        {
            if(i != j)
            {
                cout << "=====" << file_path[i] <<"と"<<file_path[j]<<"のマッチング結果====="<<endl;
                for( k = 1; k < 101; k++)
                {
                    for( l = 1; l < 101; l++)
                    {
                        //pathを作成
                        f1_path = makepath(file_path[i], k);
                        f2_path = makepath(file_path[j], l);
                        //マッチング
                        total = local_distance( f1_path, f2_path);
                        //最終の累積距離を比較
                        if(total_min == -1 || total_min >= total)
                        {
                            total_min = total;
                            min_num = l;
                        }
                    }

                    //正答率を計算
                    if(min_num == k)
                    {
                        count++;
                    }else
                    {
                        cout << "ERROR:  " << f1_path  <<",   "<< makepath(file_path[j], min_num) << endl;
                    }
                    total_min = -1;
                }
                //結果を出力
                cout<<"正答率:"<< count << "%"<< endl;
                count = 0;
            }
        }
    }
}
