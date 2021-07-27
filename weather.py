import csv
from datetime import datetime
import statistics

# with open("tests/data/example_one.csv") as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=",")
#    next(csv_reader)
#    for row in csv_reader:
#        print(row)
DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    with open("tests/data/example_one.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for temp in csv_reader:
            print(
                f"The min temperature on {temp[0]} was {temp[1]}{DEGREE_SYBMOL} Celsius, while the max was {temp[2]}{DEGREE_SYBMOL} Celsius.")
            # return f"{temp}{DEGREE_SYBMOL}"


format_temperature(30)
"""Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
# return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    with open("tests/data/example_one.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for iso_string in csv_reader:
            # date = datetime.datetime(csv_reader)
            # date = datetime(int(year), int(month), 1)
            # date = date.strftime("%m/%d/%Y, %H:%M")
            # date = datetime.datetime(2018, 9, 15)

            # print(date.strftime("%b %d %Y %H:%M:%S"))
            # print(f"{date}")
            # date_object = datetime.strptime(date[0], '%m-%d-%y')
            # date_object = [date[0].strftime('%m-%d-%Y') for date in csv_reader]
            # print(iso_string[0])
            iso_string = str(iso_string[0]).split('-')
            print(iso_string)


convert_date(2021-12-13)


"""Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
pass


def convert_f_to_c(temp_in_farenheit):
    with open("tests/data/example_one.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for temp in csv_reader:
            min_celcius = (float(temp[1]) - 32) * 5.0/9.0
            max_celcius = (float(temp[2]) - 32) * 5.0/9.0
            print(
                f"The minimum Celcius was {float(temp[1])}. The max Celcius was {float(temp[2])}.")


convert_f_to_c(30)
"""Converts an temperature from farenheit to celcius.
(°F – 32) x 5/9 = °C
    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
pass


def calculate_mean(weather_data):

    with open("tests/data/example_one.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            min_result = statistics.mean(int(row[1]))
            max_result = statistics.mean(int(row[2]))
            print(
                f"The avarage min tempreture was {int(min_result)}. the avarage max_result was {int(max_result)}.")
    return min_result, max_result


calculate_mean(1)
"""Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
pass


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    pass


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    pass


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
