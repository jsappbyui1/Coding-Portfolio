#include "Chariters.h"
#include <string>
using namespace std;


Chariter :: Chariter(string n, string j, string r, string h, string a, string no)
    {
        name = n;
        job = j;
        race = r;
        hp_count = h;
        ac_count = a;
        notes = no;
        return;
    }

string Chariter :: get_name(void)
    {
        return name;
    }

string Chariter :: get_job(void)
    {
        return job;
    }

string Chariter :: get_race(void)
    {
        return race;
    }

string Chariter :: get_hp_count(void)
    {
        return hp_count;
    }

string Chariter :: get_ac_count(void)
    {
        return ac_count;
    }

string Chariter :: get_notes(void)
    {
        return notes;
    }

void Chariter :: set_next_chariter(Chariter *p)
    {
        next = p;
        return;
    }

Chariter* Chariter :: get_next_chariter()
    {
        return next;
    }