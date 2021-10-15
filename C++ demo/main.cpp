#include <iostream>   // <---  Looks to instalation to get the desired files
#include <string>
#include "Lister.h"
#include "Chariters.h"
using namespace std;

int main(void)
    {
        string name;
        string job;
        string race;
        string hp_count;
        string ac_count;
        string notes;
        int selecion = 0;
        Lister chariters;

        while (selecion != 3)
        {
            cout << endl;
            cout << "******************"<< endl;
            cout << "Please select an option"<< endl;
            cout << "1. add a chariter"<< endl;
            cout << "2. print chariter list"<< endl;
            cout << "3. end program"<< endl;
            cout << "Selection:  ";
            cin >> selecion;
            cin.ignore();

            switch (selecion)
                {
                    case 1: 
                        cout << endl;
                        cout << "please enter a name:  ";
                        getline(cin,name);
                        cout << "please enter a race:  ";
                        getline(cin,race);
                        cout << "please enter a class:  ";
                        getline(cin,job);
                        cout << "please enter an HP total:  ";
                        getline(cin,hp_count);
                        cout << "please enter an AC:  ";
                        getline(cin,ac_count);
                        cout << "please enter any notes:  ";
                        getline(cin,notes);                        
                        chariters.add_chariter(name,job,race,hp_count,ac_count,notes);
                        break;

                    case 2: 
                        chariters.print_chariter_list();
                        break;

                    case 3: break;

                    default:  cout << "Invalid selection. returning to menu."<< endl; break;     
                               
                }


        }
        return 0;
    }

