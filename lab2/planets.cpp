#include <iostream>
#include "celestial_body.cpp"

class Moon: public CelestialBody {
  public:
    double density;
    Moon() : CelestialBody() {
      density = 0.0;
      printf("  Moon()\n");
    }

    Moon(const std::string& name, int mass, int radius) : CelestialBody(name, mass, radius) {
      this->density = count_density();
      printf("  Moon(const std::string& name, int mass, int radius)\n");
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
    Moon main_moon;
    Moon* secondary_moon;

    Planet() : CelestialBody() {
      this->is_exoplanet = false;
      this->secondary_moon = new Moon();
      printf("  Planet()\n");
    }

    Planet(const std::string& name, int mass, int radius,
           bool is_exoplanet, const Moon& main_moon, const Moon* secondary_moon) : CelestialBody(name, mass, radius), main_moon(main_moon) {
      this->is_exoplanet = is_exoplanet;
      this->secondary_moon = new Moon(*secondary_moon);
      printf("  Planet(const std::string& name, int mass, int radius, bool is_exoplanet, const Moon& main_moon, const Moon* secondary_moon)\n");
    }

    Planet(const Planet& planet) : CelestialBody(planet) {
      this->is_exoplanet = planet.is_exoplanet;
      this->main_moon = planet.main_moon;
      this->secondary_moon = new Moon(*planet.secondary_moon);
      printf("  Planet(const Planet& planet)\n");
    }

    ~Planet() {
      delete this->secondary_moon;
      printf("  ~Planet()\n");
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
