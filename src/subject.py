import re


def get_result(x: str) -> int:
    r = re.search(r"^\d{2}\:\d{2}$", x)
    base = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
    if not r:
        raise ValueError(f"entry should have this format XX:XX")
    str_hour, str_minute = r.group().split(":")
    if not str_hour in base + [str(item) for item in range(10, 24)]:
        raise ValueError(f"Hour must be in 0:23 not {str_hour}.")
    if not str_minute in base + [str(item) for item in range(10, 60)]:
        raise ValueError(f"Minute must be in 0:59 not {str_minute}.")
    int_hour, int_minute = int(str_hour), int(str_minute)
    if int_hour > 12:
        int_hour = int_hour - 12
    angle_one_hour = 360 / 12
    angle_one_minute = 360 / 60
    hour_angle = angle_one_hour * int_hour
    minute_angle = angle_one_minute * int_minute
    return min([abs(hour_angle - minute_angle), abs(minute_angle - hour_angle)])
