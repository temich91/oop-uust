#include <iostream>
#include <windows.h>

class CelestialBody{
  // Базовый класс небесного тела

  private:
    std::string name;
    int mass;
    int radius;

  public:
      CelestialBody() = delete;

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

int main() {
  SetConsoleCP(65001);
  SetConsoleOutputCP(65001);
  CelestialBody* cb1 = new CelestialBody("Earth", 100, 6378);
  CelestialBody cb2 = *cb1;
  cb1->print_info();
  printf(" ");
  cb2.print_info();

  delete cb1;
  return 0;
}
