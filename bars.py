import json
import sys
import os


def load_data(file_path):
    with open(file_path, 'r') as opened_file:
        json_data = json.load(opened_file)
        return json_data['features']


def get_biggest_bar(json_data):
    return max(json_data,
               key=lambda bar: bar['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(json_data):
    return min(json_data,
               key=lambda bar: bar['properties']['Attributes']['SeatsCount'])


def calculate_distance(latitude_1, latitude_2, longitude_1, longitude_2):
    distance = ((latitude_1 - latitude_2) ** 2 + (longitude_1 - longitude_2) ** 2) ** 0.5
    return distance


def get_closest_bar(json_data, latitude, longitude):
    return min(json_data,
               key=lambda bar: calculate_distance(bar['geometry']['coordinates'][0],
                                                  latitude,
                                                  bar['geometry']['coordinates'][1],
                                                  longitude))


def get_bar_name(bar):
    return bar['properties']['Attributes']['Name']


if __name__ == '__main__':
    file_path = sys.argv[1]
    if os.path.exists(file_path) and os.path.isfile(file_path):
        bar_list = load_data(file_path)
        try:
            latitude = float(input('Введите широту вашего местоположения в формате x.xxxxxxxxxxxx:'))
            longitude = float(input('Введите долготу вашего местоположения в формате x.xxxxxxxxxxxx:'))
        except ValueError:
            print('Вы ввели некорректные данные')
        else:
            print('Самый большой бар:', get_bar_name(get_biggest_bar(bar_list)))
            print('Самый маленький бар:', get_bar_name(get_smallest_bar(bar_list)))
            print('Ближайший бар:', get_bar_name(get_closest_bar(bar_list, latitude, longitude)))
    else:
        print("Такого файла не существует")