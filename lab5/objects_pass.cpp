#include <iostream>
#include "virtual.cpp"
#include "Windows.h"

using namespace std;

void func1(Base obj) {
    printf("func1()\n");
    // Desc* obj2 = dynamic_cast<Desc*>(&obj);
    printf(obj.classname().c_str());
}

void func2(Base* obj) {
    printf("func2()\n");
    printf(obj->classname().c_str());
}

void func3(Base& obj) {
    printf("func3()\n");
    printf(obj.classname().c_str());
}

int main() {
    SetConsoleCP(65001);
    SetConsoleOutputCP(65001);

    Base* base = new Base();
    Desc* desc = new Desc();

    printf("Вызовы для Base:\n");
    func1(*base);
    func2(base);
    func3(*base);

    printf("\nВызовы для Desc:\n");
    func1(*desc);
    func2(desc);
    func3(*desc);

    delete base;
    delete desc;
    return 0;
}
