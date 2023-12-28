# tallies = {           # 26 : XXVI
#     'I' : 1,
#     'V' : 5,
#     'X' : 10,
#     'L' : 50,
#     'C' : 100,
#     'D' : 500,
#     'M' : 1000,
#     # Specify more numerals if you wish
# }
#
# def roman_num_deciaml(roman_num):      # XXVI
#     sum = 0
#     for i in range(len(roman_num) - 1):     #it will run i = 0 , 1, 2
#         left = roman_num[i]          # X
#         right = roman_num[i + 1]     # X ,     (ie. X is 1 index)
#         if tallies[left] < tallies[right]:
#             sum -= tallies[left]
#         else:
#             sum += tallies[left]           # 10 + 10 + 5 + 1 =26
#     sum += tallies[roman_num[-1]]          # 25 + 1 = 26
#     return sum
#
# print(roman_num_deciaml('XXVI'))
# print(roman_num_deciaml('LXI'))
# print(roman_num_deciaml('M'))
# print(roman_num_deciaml('MCMXCIX'))

# Mini Project  alarm cock

from datetime import datetime

from playsound import playsound

alarm_time = input('Enter the time of alarm to be set:HH:MM:SS\n')
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print(alarm_period)
print(f"Setting up alarm..at{alarm_hour}hr, {alarm_minute}min, {alarm_seconds}sec")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%H")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    # print(current_hour)
    if alarm_period == current_period:
         # print('inside if')
        if alarm_hour == current_hour:
            # print(current_hour)
            if alarm_minute == current_minute:
                if alarm_seconds == current_seconds:
                    print("Wake Up!")
                    playsound('alarm.mp3')
                    break








