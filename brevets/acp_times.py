"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import math


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    #open time speed reference
    # 0-200: 34 200-400: 32 400-600: 30 600-1000: 28 1000-1300: 26
    OPEN_TIME_TABLE = [(0, 34), (200, 32), (400, 30), (600, 28), (1000, 26)]
    hour_time_reference = {0: 0, 200: 5, 400: 12, 600: 18, 1000: 33} 
    minute_time_reference = {0: 0, 200:53, 400:8 , 600:48, 1000:5 }
    hours, minutes = 0, 0
    if control_dist_km > brevet_dist_km:
        control_dist_km = brevet_dist_km
    for open_time in OPEN_TIME_TABLE:
            min_km, speed = open_time
            if control_dist_km >= min_km:
               hours = (control_dist_km - min_km)//speed
               pre_minute = ((control_dist_km - min_km) / speed - hours) * 60
               if pre_minute - math.floor(pre_minute) == 0.5:
                   minutes = round(pre_minute) - 1
               else:
                   minutes = round(pre_minute)
               hours += hour_time_reference[min_km]
               minutes += minute_time_reference[min_km]
               if minutes > 60:
                   hours += minutes // 60
                   minutes = minutes % 60

    
    return brevet_start_time.shift(hours=hours, minutes=minutes)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    CLOSE_TIME_TABLE = [(0, 15), (600, 11.428), (1000, 13.333)]
    time_reference = {0: 0, 600: 40, 1000: 75} 
    # close time speed reference
    # 0-600: 15 600-1000: 11.428 1000-1300 13.333
    
    #corner case

    hours, minutes = 0, 0
    if control_dist_km > brevet_dist_km:
        control_dist_km = brevet_dist_km
    if control_dist_km == 0:
        hours = 1
    elif control_dist_km <= 60:
        hours = control_dist_km // 20
        minutes = round((control_dist_km / 20 - hours)*60)
        hours += 1
    elif control_dist_km == brevet_dist_km and control_dist_km == 200:
         hours, minutes = 13, 30
    elif control_dist_km == brevet_dist_km and control_dist_km == 400:  
         hours = 27
    else:
        for close_time in CLOSE_TIME_TABLE:
            min_km, speed = close_time
            if control_dist_km >= min_km:
               hours = (control_dist_km - min_km)//speed
               pre_minute = ((control_dist_km - min_km) / speed - hours) * 60
               if pre_minute - math.floor(pre_minute) == 0.5:
                   minutes = round(pre_minute) - 1
               else:
                   minutes = round(pre_minute)
               hours += time_reference[min_km]


    return brevet_start_time.shift(hours=hours, minutes=minutes)
