// multi-level inheritance

#include <iostream>
using namespace std;

class X
{
    public:
    void xclass() {
        cout <<"base class"<<endl;
        return;
    }
};

class Y:public X
{
    public:
    void yclass() {
        cout << "class Y"<<endl;
        return;
    }
};

class Z:public Y
{
    public:
    void zclass() {
        cout << "class Z" << endl;
        return;
    }
};

int main() {
    Z obj;
    obj.xclass();
    obj.yclass();
    obj.zclass();    
    return 0;
}
