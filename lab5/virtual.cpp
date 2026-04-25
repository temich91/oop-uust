#include <iostream>
#include "Windows.h"

using namespace std;

class Base {
  public:
    Base() {
        printf("Base()\n");
    }

    Base(Base&) {
        printf("Base(Base&)\n");
    }

    virtual ~Base() {
        printf("~Base()\n");
    }

    string classname() {
        return "Base\n";
    }

    bool isA(string classname) {
        return classname == this->classname();
    }

    void method1() {
        printf("Base::method1()\n");
        this->method2();
        this->method3();
    }

    void method2() {
        printf("Base::method2()\n");
    }

    virtual void method3() {
        printf("Base::method3()\n");
    }
};

class Desc : public Base {
  public:
    Desc() {
        printf("Desc()\n");
    }

    Desc(Desc&) {
        printf("Desc(Desc&)\n");
    }

    virtual ~Desc() {
        printf("~Desc()\n");
    }

    string classname() {
        return "Desc\n";
    }

    bool isA(string classname) {
        return (classname == "Desc") || (Base::isA(classname));
    }

    void method2() {
        printf("Desc::method2()\n");
    }

    void method3() {
        printf("Desc::method3()\n");
    }
};

void test_virtual() {
    printf("Обращение через указатель на базовый класс:\n");
    Base* base = new Desc();
    base->method1();
    base->method3();

    printf("\nОбращение через указатель на класс-потомок:\n");
    Desc* desc = new Desc();
    desc->method1();
    desc->method2();
    desc->method3();

    printf("\nПроверка принадлежности:\n");
    string base_name = base->classname();
    string desc_name = desc->classname();
    printf("base - объект класса %s", base_name.c_str());
    printf("desc - объект класса %s", desc_name.c_str());
    printf("Проверка по classname:\n");
    if (base_name == desc_name) {
        printf("base и desc - объекты одного класса\n");
    } else {
        printf("base и desc - объекты разных классов\n");
    }

    printf("Проверки по isA:\n");
    if (base->isA(desc->classname())) {
        printf("base - это объект того же класса, что и desc\n");
    } else {
        printf("base и desc - объекты разных классов\n");
    }

    if (desc->isA(base->classname())) {
        printf("desc - это объект того же класса, что и base\n");
    } else {
        printf("base и desc - объекты разных классов\n");
    }

    // base --> desc
    printf("\nПриведение типов:\n");
    Base* base2 = new Base();
    Desc* dynamic_to_desc = dynamic_cast<Desc*>(base2);
    if (dynamic_to_desc) {
        printf("Успешный dynamic_cast из base в desc\n");
    } else {
        printf("Ошибка в dynamic_cast\n");
    }

    Desc* manual_to_desc = (Desc*)base;    
    printf("Произошло приведение типов вручную\n");
    manual_to_desc->method1();

    // desc --> base
    Base* dynamic_to_base = dynamic_cast<Base*>(desc);
    if (dynamic_to_base) {
        printf("Успешный dynamic_cast из desc в base\n");
    } else {
        printf("Ошибка в dynamic_cast\n");
    }
    
    Base* manual_to_base = (Base*)desc;
    printf("Произошло приведение типов вручную\n");

    delete base;
    delete base2;
    delete desc;
}
