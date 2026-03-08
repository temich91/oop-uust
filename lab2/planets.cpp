#include <iostream>
#include "main.cpp"

class Moon: public CelestialBody {};

class Planet: public CelestialBody {
  // Абстрактный класс планеты    
  public:
    bool is_exoplanet;
    int n_moons;
    Moon** moons;

    Planet() : CelestialBody() {
      this->is_exoplanet = false;
      this->n_moons = 0;
      this->moons = new Moon*[n_moons];
      printf("  Planet %s создана\n", this->name);
    }

    Planet(const std::string name, int mass, int radius,
           const bool is_exoplanet, Moon** moons, int n_moons) : CelestialBody(name, mass, radius) {
      this->is_exoplanet = is_exoplanet;
      this->n_moons = n_moons;
      this->moons = new Moon*[n_moons];
      for (int i = 0; i < n_moons; ++i) {
        this->moons[i] = moons[i];
      }
      printf("  Planet %s создана\n", this->name.c_str());
    }

    Planet(const Planet& planet) : CelestialBody(planet) {
      this->is_exoplanet = planet.is_exoplanet;
      this->n_moons = planet.n_moons;
      this->moons = new Moon*[this->n_moons];
      for (int i = 0; i < this->n_moons; ++i) {
        this->moons[i] = planet.moons[i];
      } 
      printf("  Planet %s создана\n", this->name.c_str());
    }

    ~Planet() {
      for (int i=0; i < this->n_moons; ++i) {
        delete this->moons[i];
      }
      delete this->moons;
      printf("  Planet %s уничтожена\n", this->name.c_str());
    }
};

int main() {
  SetConsoleCP(65001);
  SetConsoleOutputCP(65001);

  Moon* m1 = new Moon;
  Moon* m2 = new Moon;
  Moon** maggr = new Moon*[2];
  maggr[0] = m1;
  maggr[1] = m2;

  CelestialBody cb1 = Planet("Mars", 1000, 6378, false, maggr, 2);
  cb1.print_info();

  delete m1;
  delete m2;
  return 0;
}
