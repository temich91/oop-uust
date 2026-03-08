#include <iostream>
#include <windows.h>

class CelestialBody{
  // Базовый класс небесного тела

  public:
    std::string name;
    int mass;
    int radius;

    CelestialBody() {
      this->name = "default";
      this->mass = 0;
      this->radius = 0;
      printf("CelestialBody()\n");
    }

    CelestialBody(const std::string& name, int mass, int radius): name(name), mass(mass), radius(radius) {
      printf("CelestialBody(const std::string& name, int mass, int radius)\n");
    }

    CelestialBody(const CelestialBody& cb) {
      this->name = cb.name;
      this->mass = cb.mass;
      this->radius = cb.radius;
      printf("CelestialBody(const CelestialBody& cb)\n");
    }

    ~CelestialBody() {
      printf("~CelestialBody()\n");
    }

    void print_info() {
      printf("Название объекта: %s\nМасса: %d\nРазмер: %d\nОбъем: %.3lf\n", name.c_str(), mass, radius, count_volume());
    }
  
  protected:
    double count_volume();
};

double CelestialBody::count_volume() {
  return 4/3 * 3.14 * radius * radius * radius;
};

void create_cb_static() {
  // Статическое создание
  CelestialBody cb1; // по умолчанию
  cb1.print_info();
  CelestialBody cb2("Mars", 12400, 3400); // с параметрами
  cb2.print_info();
  CelestialBody cb3(cb2); // копирование
  cb3.print_info();
};

void create_cb_dynamic() {
  // динамическое создание
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
