#ifndef CHARITERS_H
#define CHARITERS_H
#include <string>
using namespace std;

class Chariter {   // <--- class has 3 data types.  Public, private, and protected
public:
    Chariter(string n, string j, string r, string h, string a, string no);
    string get_name();
    string get_job();
    string get_race();
    string get_hp_count();
    string get_ac_count();
    string get_notes();
    void set_next_chariter(Chariter *p);
    Chariter *get_next_chariter();

private:
    string name;
    string job;
    string race;
    string hp_count;
    string ac_count;
    string notes;
    Chariter *next;
};

#endif