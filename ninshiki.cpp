#include<iostream>
#include<string>
#include<sstream>
#include<iomanip>
#include<fstream>

using namespace std;



string makepath(string file_path, int file_num)
{   
    string path_str;
    std::stringstream path;
    path << file_path << "/" << file_path << "_" << std::setw(3) << std::setfill('0') << file_num  << ".txt";
    
    return path_str = path.str();
}



int main()
{
    std::ifstream ifs;
    int  i, j, k, l, score = 0;
    string file_path[] = { "city011", "city012", "city021", "city022"};
    string f1_path, f2_path, f1_data, f2_data;
    for(i = 0; i < 4; i++)
    {
        if(i != j)
        {
            for(j =0; j < 4; j++)
            {
                for( k = 1; k < 101; k++)
                {
                    f1_path = makepath(file_path[i], k);
                    for( l = 1; l < 101; l++)
                    {
                        //cout << f1_path << endl;
                        f2_path = makepath(file_path[j], l);
                        f2_path = "cpninshiki,.py";
                        ifs.open(f2_path);
                        while(!ifs.eof())
                            getline(ifs, f2_data);
                            cout << f2_data;

                    }
                }
            }
        }
    }
    

}
