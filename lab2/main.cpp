#include <iostream>
#include <windows.h>

class CelestialBody{
  // Базовый класс небесного тела

  public:
    std::string name;
    int mass;
    int radius;

    CelestialBody() {
      this->name = "";
      this->mass = 0;
      this->radius = 0;
    }

    CelestialBody(const std::string name, const int mass, const int radius): name(name), mass(mass), radius(radius) {
      printf("CelestialBody %s создан\n", name.c_str());
    }

    CelestialBody(const CelestialBody& cb) {
      this->name = cb.name;
      this->mass = cb.mass;
      this->radius = cb.radius;
      printf("CelestialBody %s создан\n", name.c_str());
    }

    ~CelestialBody() {
      printf("CelestialBody %s уничтожен\n", name.c_str());
    }

    void print_info() {
      printf("Название объекта: %s\nМасса: %d\nРазмер: %d\n\n", name.c_str(), mass, radius);
    }
};
