def get_weather_theme(code):
    if code == 1000:
        return "sunny"

    elif code in [1003, 1006, 1009]:
        return "cloudy"

    elif code in [1030, 1135, 1147]:
        return "fog"

    elif code in [
        1063, 1150, 1153,
        1180, 1183, 1186,
        1189, 1192, 1195,
        1240, 1243, 1246
    ]:
        return "rainy"

    elif code in [
        1066, 1114, 1117,
        1210, 1213, 1216,
        1219, 1222, 1225
    ]:
        return "snow"

    elif code in [
        1087, 1273, 1276,
        1279, 1282
    ]:
        return "storm"

    return "default"