// single inheritance

#include <iostream>
using namespace std;
class Father
{
    public:
    void father_details() {
        cout << "This is father class"<<endl;
        return;
    }
};

class Child:public Father
{
    public:
    void child_details() {
        cout << "Child class inherited by father class(base class)"<<endl;
        return;
    }
};

int main() {
    Child obj;
    obj.child_details();
    obj.father_details();    
    return 0;
} 
 