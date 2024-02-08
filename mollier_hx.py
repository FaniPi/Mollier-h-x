import math


def enthalpie(temp, feucht, druck=1013):
    a = round(math.exp((17.62 * temp) / (243.12 + temp)) * 6.112 * 100)
    b = (feucht / 100) * a
    c = 0.622 * (b / ((druck * 100) - b))
    d = 1.005 * temp + c * (2500 + 1.86 + temp)
    return round(d, 2)


def dew_point(temp, rh):
    a = 17.27
    b = 237.7
    gamma = ((a * temp) / (b + temp)) + math.log(rh/100)
    dew_point = (b * gamma) / (a - gamma)
    return round(dew_point, 2)


def specific_weight(temp, pressure=1013):
    R = 287.05
    specific_weight = pressure / (R * (temp + 273.15))
    return round(specific_weight * 100, 2)


#  Die absolute Luftfeuchtigkeit gibt an, wie viel Gramm Wasser in einem Kubikmeter
#  (theoretisch trockener) Luft zu finden sind.
def absolute_humidity(temp, rh, pressure=1013):
    e_s = 6.112 * math.exp((17.67 * temp) / (temp + 243.5))
    e = rh / 100 * e_s
    absolute_humidity = 0.622 * e / (pressure - e)
    return round(absolute_humidity * 1000, 2)


#  Sättigungsdruck
def vapor_pressure(temp):
    vapor_pressure = 6.112 * math.exp((17.67 * temp) / (temp + 243.5))
    return round(vapor_pressure, 2)


#  Dampfdruck
def actual_vapor(temp, rh):
    sat_vp = 6.112 * math.exp((17.67 * temp) / (temp + 243.5))
    actual_vp = rh / 100 * sat_vp
    return round(actual_vp, 2)


#  Kühlgrenztemperatur
def t_wet_bulb(T, H):
    tw = T * math.atan(0.151977 * math.sqrt(H + 8.313659)) + math.atan(T + H) \
         - math.atan(H - 1.676331) + 0.00391838 * math.pow(H, 3/2) * math.atan(0.023101 * H) - 4.686035
    return round(tw, 2)


if __name__ != '__main__':
    pass
else:
    grad = 20
    rLfeuchtigkeit = 35
    hpa = 1013
    print(absolute_humidity(grad, rLfeuchtigkeit, hpa), "g/kg Absolute Feuchte")
    print(actual_vapor(grad, rLfeuchtigkeit), "hPa Dampfdruck")  # hPa Dampfdruck
    print(vapor_pressure(grad), "hPa Sättigungsdruck 100% r.F.")  # hPa
    print(enthalpie(grad, rLfeuchtigkeit, hpa), "kJ/kg Enthalpie")
    print(dew_point(grad, rLfeuchtigkeit), "°C Taupunkttemperatur")  # Taupunkttemperatur(°C)
    print(t_wet_bulb(grad, rLfeuchtigkeit), "°C Kühlgrenztemperatur")  # °C Kühlgrenztemperatur
    print(specific_weight(grad, hpa), "kg/m3 Spezifisches Gewicht")

