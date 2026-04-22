# Analiza Pogodowa – EDA

Eksploracyjna analiza danych pogodowych z wykorzystaniem Pythona.

## Dane

Zbiór danych zawiera **2192 obserwacje** dzienne z okresu od 2020-04-17 do 2026-04-17, bez brakujących wartości. Kolumny:

- `time` – data obserwacji
- `temperature_2m_max` / `temperature_2m_min` – temperatura maksymalna i minimalna (°C)
- `windspeed_10m_max` – prędkość wiatru
- `temp_avg` – średnia temperatura dzienna
- `precipitation_sum` – suma opadów (mm)
- `rainy_day` / `windy_day` / `freeze_day` / `nice_temp` – flagi binarne (dzień deszczowy / wietrzny / mroźny / dobra temperatura)
- `score` – ocena dnia pogodowego (0–3)

## Wyniki analizy

### Temperatura
- Rozkład maksymalnej temperatury jest zbliżony do normalnego z przesunięciem w stronę wyższych wartości.
- **Rekord ciepła:** 35.7°C (2025-07-03)
- **Rekord chłodu:** -21.7°C (2026-02-03)
- Wyraźna sezonowość – najcieplejsze miesiące to czerwiec–sierpień, najchłodniejsze styczeń–luty.

### Rozkład score'ów
- Najczęściej ocena wynosiła **2** (863 dni), następnie **1** (683 dni), **0** (336 dni) i **3** (310 dni).
- Najwyżej oceniane są miesiące letnie (czerwiec–sierpień), najniżej – zimowe.

### Opady i wiatr
- **44.11%** dni było deszczowych.
- **39.28%** dni było wietrznych.
- **24.09%** dni było mroźnych.
- Najbardziej deszczowe miesiące to te z przełomu lata i jesieni (lipiec–październik).
- Najbardziej wietrzne miesiące (grudzień-styczeń).
- Suma opadów i częstość dni deszczowych są ze sobą silnie skorelowane.
- Największa suma opadów wypada w **sierpniu** (~575 mm), a wysoka jest też w czerwcu i lipcu (~450–480 mm). Jednak **% dni deszczowych** jest najwyższy w **styczniu i lipcu** (~52.5%), a najniższy we wrześniu (~35%) — co oznacza, że we wrześniu opady są rzadsze, ale bardziej intensywne.
