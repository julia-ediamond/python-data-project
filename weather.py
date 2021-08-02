import csv
import datetime
import math


DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    # temp_string = f" {str(temp)} {DEGREE_SYBMOL}"
    return (f"{temp}{DEGREE_SYBMOL}")


"""Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
# return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    # iso_string = "2021-07-02T07:00:00+08:00"
    # print(str(iso_string))
    weekday = datetime.datetime.strptime(
        str(iso_string), "%Y-%m-%dT%H:%M:%S%z").strftime("%A")
    month = datetime.datetime.strptime(
        iso_string, "%Y-%m-%dT%H:%M:%S%z").strftime("%B")
    day = datetime.datetime.strptime(
        iso_string, "%Y-%m-%dT%H:%M:%S%z").strftime("%d")
    year = datetime.datetime.strptime(
        iso_string, "%Y-%m-%dT%H:%M:%S%z").strftime("%Y")
    # print(f"{weekday} {day} {month} {year}")

    return f"{weekday} {day} {month} {year}"


print(convert_date("2021-07-02T07:00:00+08:00"))

"""Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
pass


def convert_f_to_c(temp_in_farenheit):
    a = float(temp_in_farenheit)
    temp_in_c = (a - 32) / 1.8
    return(float(round(temp_in_c, 1)))
    # print(temp_in_farenheit)
    # celcius = round((temp_in_farenheit - 32) * 5/9, 1)
    # return celcius


"""Converts an temperature from farenheit to celcius.
(°F – 32) x 5/9 = °C
    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
pass


def calculate_mean(weather_data):

    # for number in enumerate(weather_data):

    #     mean_num = sum(map(int, weather_data)) / len(weather_data)
    #     print(f"THIS IS MEAN DATA {mean_num}")
    # return mean_num

    list_of_floats = []
    for item in weather_data:
        list_of_floats.append(float(item))
        avg = sum(list_of_floats) / len(list_of_floats)
    return(round(avg, 5))


"""Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
pass


def load_data_from_csv(csv_file):
    data_list = []
    with open(csv_file, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        for index, line in enumerate(csv_reader):
            if line != [] and index != 0:
                data_list.append([line[0], int(line[1]), int(line[2])])
    return data_list


"""Reads a csv file and stores the data in a list.

    Args:a string representing the file path to a csv file.
        csv_file:
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
pass


def find_min(weather_data):
    if (weather_data == []):
        return ()
    min_value = float(weather_data[0])
    min_index = 0
    if len(weather_data) != 0:
        for index, value in enumerate(weather_data):

            if float(value) <= min_value:
                min_value = float(value)
                min_index = index
    return min_value, min_index


"""Calculates the minimum value in a list of numbers.
    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
pass


def find_max(weather_data):
    if weather_data == []:
        return ()
    max_value = weather_data[0]
    max_index = 0
    if len(weather_data) != 0:
        for index, value in enumerate(weather_data):
            if float(value) >= float(max_value):
                max_value = float(value)
                max_index = index
    return float(max_value), max_index


"""Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
pass


def generate_summary(weather_data):
    count = 0
    min_temp = []
    max_temp = []
    date_time = []
    for index, item in enumerate(weather_data):
        if len(weather_data) == 0:
            return ()
        if index != []:
            count += 1
            date_time.append(item[0])
            min_temp.append(item[1])
            max_temp.append(item[2])
    min_temps, index_date_min = find_min(min_temp)
    max_temps, index_date_max = find_max(max_temp)

    min_temp_c = convert_f_to_c(str(min_temps))
    max_temp_c = convert_f_to_c(str(max_temps))

    mean_min_c = convert_f_to_c(calculate_mean(min_temp))
    mean_max_c = convert_f_to_c(calculate_mean(max_temp))

    date_min = date_time[index_date_min]
    date_max = date_time[index_date_max]

    result = ""
    result += f"{count} Day Overview\n"
    result += f"  The lowest temperature will be {format_temperature(min_temp_c)}, and will occur on {convert_date(date_min)}.\n"
    result += f"  The highest temperature will be {format_temperature(max_temp_c)}, and will occur on {convert_date(date_max)}.\n"
    result += f"  The average low this week is {format_temperature(mean_min_c)}.\n"
    result += f"  The average high this week is {format_temperature(mean_max_c)}.\n"

    return result


"""Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """


def generate_daily_summary(weather_data):
    result = ""

    for item in weather_data:
        result += f"---- {convert_date(item[0])} ----\n"
        result += f"  Minimum Temperature: {format_temperature(convert_f_to_c(item[1]))}\n"
        result += f"  Maximum Temperature: {format_temperature(convert_f_to_c(item[2]))}\n\n"

    return result


"""Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
pass
