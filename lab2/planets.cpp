#include <iostream>
#include "main.cpp"

class Moon: public CelestialBody {
  public:
    double density;
    Moon() : CelestialBody() {
      density = 0.0;
      printf("  Moon()\n");
    }

    Moon(const std::string& name, int mass, int radius) : CelestialBody(name, mass, radius) {
      this->density = count_density();
      printf("  Moon(const std::string& name, int mass, int radius, double density)\n");
    }

    Moon(const Moon& moon) : CelestialBody(moon) {
      density = moon.density;
      printf("  Moon(const Moon& moon)\n");
    }

    ~Moon() {
      printf("  ~Moon()\n");
    }

    void print_info() {
      // вызов родительского метода
      CelestialBody::print_info();
      // дополнение
      printf("Средняя плотность: %lf\n", density);
    }

  private:
    double count_density() {
      return static_cast<double>(mass) / CelestialBody::count_volume();
    }
};

class Planet: public CelestialBody {
  public:
    bool is_exoplanet;
    int n_extra_moons;
    Moon main_moon;
    Moon* extra_moons;

    Planet() : CelestialBody() {
      this->is_exoplanet = false;
      this->n_extra_moons = 0;
      this->extra_moons = nullptr;
      printf("  Planet()\n");
    }

    Planet(const std::string& name, int mass, int radius,
           bool is_exoplanet, const Moon& main_moon, const Moon* extra_moons, int n_extra_moons) : CelestialBody(name, mass, radius), main_moon(main_moon) {
      this->is_exoplanet = is_exoplanet;
      this->n_extra_moons = n_extra_moons;
      this->extra_moons = new Moon[n_extra_moons];
      for (int i = 0; i < n_extra_moons; ++i) {
        this->extra_moons[i] = extra_moons[i];
      }
      printf("  Planet(const std::string& name, int mass, int radius, bool is_exoplanet, Moon** moons, int n_moons)\n");
    }

    Planet(const Planet& planet) : CelestialBody(planet) {
      this->is_exoplanet = planet.is_exoplanet;
      this->n_extra_moons = planet.n_extra_moons;
      this->main_moon = planet.main_moon;
      this->extra_moons = new Moon[this->n_extra_moons];
      for (int i = 0; i < this->n_extra_moons; ++i) {
        this->extra_moons[i] = planet.extra_moons[i];
      } 
      printf("  Planet(const Planet& planet)\n");
    }

    ~Planet() {
      delete[] this->extra_moons;
      printf("  ~Planet\n");
    }

    void print_info() {
      // вызов родительского метода
      CelestialBody::print_info();
      // дополнение
      if (this->is_exoplanet) {
        printf("Является экзопланетой\n");
      } else {
        printf("Не является экзопланетой\n");
      }
    }
};

int main() {
  SetConsoleCP(65001);
  SetConsoleOutputCP(65001);

  Moon m1("wasd", 1000, 10);
  Moon* m2 = new Moon;
  Moon* maggr = new Moon[1];
  maggr[0] = *m2;

  Planet cb1("Mars", 1000, 6378, true, m1, maggr, 1);
  cb1.print_info();
  delete m2;
  delete[] maggr;
  return 0;
}
