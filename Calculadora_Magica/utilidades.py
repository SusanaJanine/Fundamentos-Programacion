def km_millas(km: float) -> float:
    return km * 0.621371

def fahrenheit_celsius(fahrenheit: float) -> float:
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def lbs_kg(lbs: float) -> float:
    kg = lbs * 0.45359
    return kg

def m_km(m: float) -> float:
    km = m / 1000
    return km

def cm_m(cm: float) -> float:
    m = cm / 100
    return m

def hrs_minutos(hrs: float) -> float:
    minutos = hrs * 60
    return minutos

def pies_cm(pies: float) -> float:
    cm = pies * 30.48
    return cm