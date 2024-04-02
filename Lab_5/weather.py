#weather.py
#By Kshitij Pingle
#weather.py is a part of Pab 5 for CPSC 223P
#3/8/2024
import json
import calendar

def read_data(*, filename):
    """Reads data from a file and returns a dictionary"""
    try:
        with open(filename, 'r') as f:
            dict1 = json.load(f)
            return dict1
    except FileNotFoundError:
      return {}
    pass
#End of read_data function


def write_data(*, data, filename):
    """Write data onto a file"""
    #Note: data represents the dicitonary
    with open(filename, 'w') as f:
        f.write(json.dumps(data))
#End of write_data function


def max_temperature(*, data, date):
    """Returns the max temp for a given date"""
    max_temp = 0
    for k, v in data.items():
        substring = k[0:8]
        if (date == substring):
            temp = v['t']
            if (max_temp < temp):
                max_temp = temp
    return max_temp
#End of max_temperature function


def min_temperature(*, data, date):
    """Returns the min temp for a given date"""
    min_temp = 1000000
    for k, v in data.items():
        substring = k[0:8]
        if (date == substring):
            temp = v['t']
            if (min_temp > temp):
                min_temp = temp
    return min_temp
#End of min_temperature function


def max_humidity(*, data, date):
    """Returns the max humidity for a given date"""
    max_hum = 0
    for k, v in data.items():
        substring = k[0:8]
        if (date == substring):
            hum = v['h']
            if (max_hum < hum):
                max_hum = hum
    return max_hum
#End of max_humidity function


def min_humidity(*, data, date):
    """Returns the min humidity for a given date"""
    min_hum = 1000000
    for k, v in data.items():
        substring = k[0:8]
        if (date == substring):
            hum = v['h']
            if (min_hum > hum):
                min_hum = hum
    return min_hum
#End of min_humidity function


def tot_rain(*, data, date):
    """Returns the total rainfall for a given date"""
    total_rain = 0.0
    for k, v in data.items():
        substring = k[0:8]
        if (date == substring):
            #print(k, ':', v)
            rain = v['r']
            total_rain += rain
    return total_rain
#End of tot_rain function


def report_daily(*, data, date):
    """Returns the daily report for a given date as a single string"""
    x = ''
    return_str = ''

    #Make the header
    header1 = f'{x:=<25} DAILY REPORT {x:=<24}\nDate'
    header2 = f'{x: <20}Time    Temperature  Humidity  Rainfall'
    header3 = f'\n{x:=<20}  {x:=<8}  {x:=<11}  {x:=<8}  {x:=<8}\n'
    return_str = return_str + header1 + header2 + header3

    #Access results and add them to the string
    for k, v in data.items():
        substring = k[:8]
        
        if (substring == date):
            year = k[:4]
            m = int(k[4:6])
            mon = calendar.month_name[m]
            date1 = k[6:8]

            hour = k[8:10]
            mins = k[10:12]
            sec = k[12:]

            temp = v['t']
            hum = v['h']
            rain = v['r']

            final_date = mon + ' ' + date1 + ', ' + year
            result1 = f'{final_date:<17}'
            result2 = f' {x: <4}{hour}:{mins}:{sec} '
            result3 = f'{temp:>12} {hum:>9} {rain:>9}\n'
            #print(result1, result2, result3)
            return_str = return_str + result1 + result2 + result3
                
    return return_str
#End of report_daily function


def historical_report(*, data):
    """Print out the historical report"""
    #Note: data argument is supposed to recieve a python dict read from
        #the w.dat file

    x = ''
    result_str = ''
    
    #Make the header
    header1 = f'{x:=<30} HISTORICAL REPORT {x:=<27}\n'
    header2 = f'{x: <23}Minimum{x: <6}Maximum     Minumum   Maximum{x: <4}Total\nDate'
    header3 = f'{x: <18}Temperature  Temperature  Humidity  Humidity  Rainfall\n'
    header4 = f'{x:=<20}  {x:=<11}  {x:=<11}  {x:=<8}  {x:=<8}  {x:=<8}\n'
    
    result_str = result_str + header1 + header2 + header3 + header4
    #print(result_str)

    date_list = []
    for k, v in data.items():
        date_substring = k[:8]
        year = k[:4]
        m = int(k[4:6])
        mon = calendar.month_name[m]
        date1 = k[6:8]
        final_date = mon + ' ' + date1 + ', ' + year

        #Check if this date has already been accessed
        if(final_date not in date_list):
            date_list.append(final_date)

            min_temp = min_temperature(data = data, date = date_substring)
            max_temp = max_temperature(data = data, date = date_substring)
            min_hum = min_humidity(data = data, date = date_substring)
            max_hum = max_humidity(data = data, date = date_substring)
            rain = tot_rain(data = data, date = date_substring)

            result1 = f'{final_date:<20}  {min_temp:>11}  {max_temp:>11}  '
            result2 = f'{min_hum:>8}  {max_hum:>8}  {rain:>8}\n'

            result_str = result_str + result1 + result2

    return result_str
#End of historical_report function







