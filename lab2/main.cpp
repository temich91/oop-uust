#include <iostream>
#include "planets.cpp"

// Шаблонная функция тестирования статического создания объектов
void create_cb_static() {
  CelestialBody cb1; // по умолчанию
  cb1.print_info();
  CelestialBody cb2("Mars", 12400, 3400); // с параметрами
  cb2.print_info();
  CelestialBody cb3(cb2); // копирование
  cb3.print_info();
};

// Шаблонная функция тестирования динамического создания объектов
void create_cb_dynamic() {
  CelestialBody* cb1 = new CelestialBody; // по умолчанию
  cb1->print_info();
  CelestialBody* cb2 = new CelestialBody("Mars", 12400, 3400); // с параметрами
  cb2->print_info();
  CelestialBody* cb3 = new CelestialBody(*cb2); // копирование
  cb3->print_info();

  delete cb1;
  delete cb2;
  delete cb3;
};

int main() {
  SetConsoleCP(65001);
  SetConsoleOutputCP(65001);
  //   create_cb_static();
  // Planet p1;// по умолчанию

  Moon m1("The Moon", 1000, 10);
  Moon* m2 = new Moon("2", 1, 1);
  Planet p2("Mars", 1000, 6378, true, m1, m2); // с параметрами
  // Planet p3 = p2; // копирование
  p2.print_info();
  delete m2;
  return 0;
}
