#main.py
#By Kshitij Pingle
#main.py and weather.py are a part of Lab 5 of CPSC 223P

from weather import *
import json

#Default value for filename
filename = 'w.dat'

#Default value for data
weather_data = read_data(filename = filename)

choice = 0

#Main Loop
while True:

    x = ''
    #Print options
    print(f'{x: <6}*** TUFFY TITAN WEATHER LOGGER MAIN MENU\n')
    print('1. Set data filename')
    print('2. Add weather data')
    print('3. Print daily report')
    print('4. Print historical report')
    print('9. Exit the program\n')

    #Get user choice
    while True:
        try:
            choice = int(input("Enter menu choice: "))
            print()
            if ((choice < 1) or (choice > 9) or ((choice > 4) and (choice < 9))):
                print("Invalid number index. Please enter a number from 1 to 4 or a 9.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4 or a 9.")
            continue

    match choice:
        case 1:
            #Set the filename and the data
            filename = str(input("Enter data filename: "))
            weather_data = read_data(filename = filename)


        case 2:
            weather_entry = {}
            
            #Get weather data from user and check for validity of data
            #Get date
            while True:
                date1 = str(input("Enter date (YYYYMMDD): "))

                #Check to see if date1 is a number
                try:
                    int_date = int(date1)
                except ValueError:
                    print("Invalid Input. Please only enter numbers for date\n")
                    continue
                
                if (len(date1) != 8):
                    print("Invalid input. Date needs to be 8 characters long. Follow the YYYYMMDD format\n")
                    continue
                mon = int(date1[4:6])
                if ((mon < 1) or (mon > 12)):
                    print("Invalid input. Month needs to be from 01 to 12. Follow the YYYYMMDD format\n")
                    continue
                date2 = int(date1[6:])
                if((date2 < 1) or (date2 > 31) or ((date2 > 29) and (mon == 2))):
                    print("Invlid input. Date needs to be from 01 to 31 or till 29 for February. Follow the YYYYMMDD format\n")
                    continue
                
                break
            #Get time
            while True:    
                time = str(input("Enter time (hhmmss): "))

                #Check if time is a number
                try:
                    int_time = int(time)
                except ValueError:
                    print("Invalid input. Please only enter numbers for time\n")
                    continue
                
                if (len(time) != 6):
                    print("Invalid input. Time needs to be 6 characters long. Follow the hhmmss format\n")
                    continue
                hour = int(time[:2])
                if ((hour < 0) or (hour > 23)):
                    print("Invlid input. Hour in time needs to be from 00 to 23. Follow the hhmmss format\n")
                    contSinue
                mins = int(time[2:4])
                if ((mins < 0) or (mins > 59)):
                    print("Invalid input. Minutes in time needs to be from 00 to 59. Follow the hhmmss format\n")
                    continue
                sec = int(time[4:])
                if ((sec < 0) or (sec > 59)):
                    print("Invalid input. Seconds in time needs to be from 00 to 59. Follow the hhmmss format\n")
                    continue
                break
                                
            #Get temp, humidity, and rain
            while True:
                try:
                    temp = int(input("Enter temperature: "))
                    hum = int(input("Enter humidity: "))
                    rain = float(input("Enter rainfall: "))
                    break
                except ValueError:
                    print("Invalid inputs. Please enter ints for temperature and humidity and floats for rainfall\n")
                    continue
                    
            final_date = date1 + time

            weather_data[final_date] = {'t':temp, 'h':hum, 'r':rain}
 
            
            #Add entry to datalist
            write_data(data = weather_data, filename = filename)


        case 3:
            #Print daily report
            #Get date while checking for validity of input
            while True:
                try:
                    date1 = str(input("Enter date (YYYYMMDD): "))
                    int_date = int(date1)

                    if(len(date1) != 8):
                        print("Invalid input. Please enter 8 chracters for the date. Follow the YYYYMMDD format\n")
                        continue
                    
                    break           
                except ValueError:
                    print("Invalid input. Please only enter numbers for the date\n")
                    continue
                
            report = report_daily(data = weather_data, date = date1)

            if (len(report) < 193):
                #No record for the given date
                print("\nThere are no records for this date\n")
            else:
                print()
                print(report)


        case 4:
            #Print historical report
            print(historical_report(data = weather_data))

        
        case 9:
            #Quit the program
            print("Quitting the program now. Bye\n")
            break

        case _:
            #Default Case
            print("Congratulations! You have found a bug which I haven't found yet!")
            print("Exiting the program now.")
            break
#End of main.py
