#ifndef Lister_H
#define Lister_H
#include <string>
#include "Chariters.h"
using namespace std;

class Lister {   // <--- class has 3 data types.  Public, private, and protected
public:
    Lister(void);
    void add_chariter(string n, string j, string r, string h, string a, string no);
    void print_chariter_list();
    ~Lister();

private:
    Chariter *start;

};

#endif




