#include <iostream>
#include "virtual.cpp"
#include "Windows.h"

using namespace std;

// Создание статических объектов
Base func1() {
    static Base x;
    return x;
}

Base* func2() {
    static Base x;
    return &x;
}

Base& func3() {
    static Base x;
    return x;
    // return Base();
}

// Создание динамических объектов
Base func4() {
    Base* x = new Base();
    return *x;
}

Base* func5() {
    return new Base();
}

Base& func6() {
    return *(new Base());
}

int main() {
    SetConsoleCP(65001);
    SetConsoleOutputCP(65001);

    printf("Вызовы для Base:\n");
    Base b1 = func1();
    Base* b2 = func2();
    Base b3 = func3();
    Base b4 = func4();
    Base* b5 = func5();
    Base b6 = func6();

    delete b5;
    return 0;
}
