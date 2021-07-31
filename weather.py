import csv
import datetime


DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


# def format_temperature(temp):
#     with open("tests/data/example_one.csv") as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=",")
#         next(csv_reader)
#         for temp in csv_reader:
# print(
#     f"The min temperature on {temp[0]} was {temp[1]}{DEGREE_SYBMOL} Celsius, while the max was {temp[2]}{DEGREE_SYBMOL} Celsius.")
# return f"{temp}{DEGREE_SYBMOL}"

# format_temperature(30)

"""Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
# return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    #iso_string = "2021-07-02T07:00:00+08:00"
    # print(str(iso_string))
    weekday = datetime.datetime.strptime(
        str(iso_string), "%Y-%m-%dT%H:%M:%S%z").strftime("%A")
    month = datetime.datetime.strptime(
        iso_string, "%Y-%m-%dT%H:%M:%S%z").strftime("%B")
    day = datetime.datetime.strptime(
        iso_string, "%Y-%m-%dT%H:%M:%S%z").strftime("%d")
    year = datetime.datetime.strptime(
        iso_string, "%Y-%m-%dT%H:%M:%S%z").strftime("%Y")
    #print(f"{weekday} {day} {month} {year}")

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
    with open("tests/data/example_one.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for temp_in_farenheit in csv_reader:
            min_celcius = (float(temp_in_farenheit[1]) - 32) * 5.0/9.0
            max_celcius = (float(temp_in_farenheit[2]) - 32) * 5.0/9.0
            print(
                f"The minimum Celcius was {float(temp_in_farenheit[1])}. The max Celcius was {float(temp_in_farenheit[2])}.")
        return min_celcius, max_celcius


convert_f_to_c(30.0)
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
        for weather_data in csv_reader:
            # print(weather_data[1])
            nums_list = []
            for data in csv_reader:
                nums_list.append(float(data[1]))
                nums_list.append(float(data[2]))
        mean_num = sum(nums_list) / len(nums_list)
        print(f"The mean temperature was {mean_num}.")

    return mean_num


calculate_mean(1)

"""Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
pass


def load_data_from_csv(csv_file):
    with open("tests/data/example_one.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        data_list = []
        for row in csv_reader:
            if row != 0:
                data_list.append(row)
    print(data_list)
    return data_list


load_data_from_csv(5)

"""Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
pass


def find_min(weather_data):
    # if (weather_data == []):
    #     return ()
    # min_value = weather_data[0]
    # min_index = 0
    # if (weather_data.count(min_value) > 1):
    #     min_value_index = [i for i, value in enumerate(
    #         weather_data) if value == min_value]
    #     min_index = min_value_index[-1]
    # else:
    #     min_index == weather_data.index(min_value)

    # return float(min_value), min_index

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


# find_min(1)
"""Calculates the minimum value in a list of numbers.
    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
pass


def find_max(weather_data):
    with open("tests/data/example_one.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        max_list = []
        for weather_data in csv_reader:
            max_list.append(weather_data[1])
            max_list.append(weather_data[2])
            # print(f"FIND MAX LIST {max_list}")
            max_value = max(max_list)
            max_index = max_list.index(max_value)
    # print(
    #     f"The maximum number in the list is: {max_value}. And it has an index of {max_index}.")

    return max_value, max_index


find_max(1)
"""Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
pass


# def generate_summary(weather_data):
#     with open("tests/data/example_one.csv") as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=",")
#         next(csv_reader)
#         summary_list = []
#         output_string = ""
#         for weather_data in csv_reader:
#             summary_list.append(weather_data[1])
#             summary_list.append(weather_data[2])
#     print(f"This is SUMARU SUMARY LIST {summary_list}")
#     output_string += f"!---{convert_date(weather_data[0])}----!\n {find_min(summary_list)}\n {find_max(summary_list)}\n {calculate_mean(summary_list)}\n"
#     # print(output_string)

#     # output_string = ""
#     # test = []
#     # for weather_data in csv_reader:
#     # outpu = print(f"GENERATE DATA SUMMARY {weather_data}")

#     #    test.append(weather_data[1])
#     # print(weather_data)
#     # list_test.append(weather_data[2])
#     #    print(f"TEST LIST: {test}")
#     # return outpu
#     return output_string


# generate_summary(2)
# summary_list = [weather_data[1], weather_data[2]]

# print(f"SUMMARY LIST: {summary_list}")  # SUMMARY LIST: ['0', '2']
# output_string += f"!---{convert_date(weather_data[0])}----!\nMinimum temperature was {convert_f_to_c(find_min(summary_list)[0])}\n Maximum temparature was {convert_f_to_c(find_max(summary_list)[0])}\n"
# The mean temperature {convert_f_to_c(calculate_mean(summary_list)[0])}\n Minimum temperature was {convert_f_to_c(find_min(summary_list)[0])}"
# print(output_string)
# return output_string

"""Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
pass


# def generate_daily_summary(weather_data):
#     with open("tests/data/example_one.csv") as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=",")
#         next(csv_reader)

#         results = ""
#         new_list = []
#         for weather_data in csv_reader:
#             new_list.append(weather_data[1])
#             new_list.append(weather_data[2])
#     # print(f"!!!!!!!!!{new_list}")
#     results += f"Results are: ---{convert_date(weather_data[0])}----\n Minimum temperature: {convert_f_to_c(find_min(new_list)[0])}\n Maximum temperature: {convert_f_to_c(find_max(new_list)[0])}\n"

#     return results


# generate_daily_summary(1)
"""Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
pass
