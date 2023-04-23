numbers = input().split(' ')
num_stations = int(numbers[0])
sit_station = int(numbers[1])
destination_station = int(numbers[2])

half_way = int(num_stations / 2)
real_way = abs(destination_station - sit_station)
if destination_station == num_stations:
    if real_way > half_way:
        print(sit_station - 1)
    else:
        print(abs(destination_station - sit_station) - 1)
elif sit_station == num_stations:
    if real_way > half_way:
        print(destination_station - 1)
    else:
        print(abs(destination_station - sit_station) - 1)
else:
    if real_way > half_way:
        if destination_station > sit_station:
            print(num_stations - destination_station + sit_station - 1)
        else:
            print(num_stations - sit_station + destination_station - 1)
    else:
        print(abs(destination_station - sit_station) - 1)
