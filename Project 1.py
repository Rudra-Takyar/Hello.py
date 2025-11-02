
total_rain = 0.0
total_wind = 0.0
count = 0


data = input()
parts = data.split()
rain = float(parts[0])


while rain != -1.0:
    wind = float(parts[1])

    total_rain += rain
    total_wind += wind
    count += 1


    data = input()
    parts = data.split()
    rain = float(parts[0])


if count > 0:
    avg_rain = total_rain / count
    avg_wind = total_wind / count
    weather_severity = avg_rain * 10 + avg_wind


    print(f"The average rain is {avg_rain:.1f} inches")
    print(f"The average wind is {avg_wind:.1f} mph")
    print(f"The weather severity for these {count} readings is: {weather_severity}")

