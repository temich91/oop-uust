#include <iostream>
#include "virtual.cpp"
#include "Windows.h"
#include <memory>

using namespace std;


void smartPtrDemo() {
    {
        unique_ptr<Base> p1 = make_unique<Desc>();
    } // удаление автоматически

    {
        shared_ptr<Base> p2 = make_shared<Desc>();
        shared_ptr<Base> p3 = p2;

        cout << "use_count = " << p2.use_count() << endl;
    } // удалится когда счетчик = 0
}

int main() {
    SetConsoleCP(65001);
    SetConsoleOutputCP(65001);
    smartPtrDemo();
    return 0;
}
