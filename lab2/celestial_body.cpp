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
