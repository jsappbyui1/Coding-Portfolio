#include <iostream> 
#include <string>
#include "Lister.h"
#include "Chariters.h"
using namespace std;

Lister :: Lister(void)  
    {
        start = NULL;
    }


void Lister :: add_chariter(string n, string j, string r, string h, string a, string no)
    {
        Chariter *current,*previous,*new_node;

        current = start;
        new_node = new Chariter(n,j,r,h,a,no);

        if (current == NULL)
            {
                start = new_node;
                new_node->set_next_chariter(NULL);
                return;
            }

        for (current = start, previous = NULL;current != NULL&& new_node -> get_name() > current -> get_name();previous = current, current = current -> get_next_chariter())
            {
                ;
            }   

        new_node->set_next_chariter(current);

        if (previous == NULL)
            {
                start = new_node;
            }
        else
            {
                previous->set_next_chariter(new_node);
            }
    }


void Lister :: print_chariter_list() 
    {

        Chariter *np;
        np = start;
        
        cout << "Here is your Chariter List" << endl;

        while (np != NULL)
        {
            cout << "******************" << endl;
            cout << endl;
            cout << np->get_name() << endl;
            cout << "Class: " << np->get_job() << endl;
            cout << "Race: " << np->get_race() << endl;
            cout << "HP: " << np->get_hp_count() << endl;
            cout << "AC: " << np->get_ac_count() << endl;
            cout << "Notes: " << np->get_notes() << endl;
            cout << endl;
            np = np->get_next_chariter();
        }
        return;
    }

Lister :: ~Lister() 
    {
        Chariter *np;
        np = start;

        while (start->get_next_chariter() != NULL)
        {   
            np = start;
            start = start->get_next_chariter();
            delete np;
        }

        delete start;
        return;
    }
