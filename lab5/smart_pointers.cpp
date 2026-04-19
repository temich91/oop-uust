#include <iostream>
#include "virtual.cpp"
#include "Windows.h"
#include <memory>

using namespace std;

void pass_unique(unique_ptr<Desc> ptr) {
    printf("unique_ptr используется в функции\n");
}

void pass_shared(shared_ptr<Desc> ptr) {
    printf("shared_ptr используется в функции\n");
    printf("Кол-во использований указателя при вызове функции : %d\n", ptr.use_count());
}

int main() {
    SetConsoleCP(65001);
    SetConsoleOutputCP(65001);
    printf("unique_ptr\n");
    
    unique_ptr<Desc> un_desc = make_unique<Desc>();
    // unique_ptr<Desc> second_unique = un_desc; // копирование unique_ptr запрещено
    pass_unique(move(un_desc));
    if (un_desc == nullptr) printf("Исходная переменная-указатель пуста\n");


    printf("shared_ptr\n");
    shared_ptr<Desc> sh_desc = make_shared<Desc>();
    shared_ptr<Desc> second_shared = sh_desc; // копировать можно
    printf("Кол-во использований исходного указателя: %d\n", sh_desc.use_count());
    pass_shared(sh_desc);
    printf("Кол-во использований исходного указателя после вызова функции: %d\n", sh_desc.use_count());
    
    return 0;
}
