def find_time_angle(hour, minutes):
    angle = 0
    try:
        hour = (hour + minutes/60)*30
        m = minutes*6
        angle =abs(hour-m)

    except Exception as e:
        print(str(e))

    return angle

print(find_time_angle(3, 15))