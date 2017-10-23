"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import logging

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
  """
  Args:
     control_dist_km:  number, the control distance in kilometers
     brevet_dist_km: number, the nominal distance of the brevet
         in kilometers, which must be one of 200, 300, 400, 600,
         or 1000 (the only official ACP brevet distances)
     brevet_start_time:  An ISO 8601 format date-time string indicating
         the official start time of the brevet
  Returns:
     An ISO 8601 format date string indicating the control open time.
     This will be in the same time zone as the brevet start time.
  """
  # format and adjust start_time to proper timezone
  formatted_start_time = arrow.get(
      brevet_start_time, 'YYYY-MM-DD HH:mm:ss').replace(tzinfo='local')

  if control_dist_km > brevet_dist_km:  # even if controle distance
    control_dist_km = brevet_dist_km  # slightly over brevet distance
    #(if within 110%), don't display
    # times over brevet distance
  shift_amount = 0

  if control_dist_km >= 0 and control_dist_km <= 200:
    shift_amount = ((control_dist_km) / 34)
  elif control_dist_km > 200 and control_dist_km <= 400:
    shift_amount = ((control_dist_km - 200) / 32) + (200 / 34)
  elif control_dist_km > 400 and control_dist_km <= 600:
    shift_amount = ((control_dist_km - 400) / 30) + (200 / 32) + (200 / 34)
  elif control_dist_km > 600 and control_dist_km <= 1000:
    shift_amount = ((control_dist_km - 600) / 28) + \
        (200 / 30) + (200 / 32) + (200 / 34)
  elif control_dist_km > 1000 and control_dist_km <= 1300:
    shift_amount = ((control_dist_km - 1000) / 26) + \
        (400 / 28) + (200 / 30) + (200 / 32) + (200 / 34)

  shift_hours = shift_amount // 1
  shift_minutes = round((shift_amount % 1) * 60)

  formatted_start_time = formatted_start_time.shift(
      hours=shift_hours, minutes=shift_minutes)
  return formatted_start_time.isoformat()


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
  """
  Args:
     control_dist_km:  number, the control distance in kilometers
        brevet_dist_km: number, the nominal distance of the brevet
        in kilometers, which must be one of 200, 300, 400, 600, or 1000
        (the only official ACP brevet distances)
     brevet_start_time:  An ISO 8601 format date-time string indicating
         the official start time of the brevet
  Returns:
     An ISO 8601 format date string indicating the control close time.
     This will be in the same time zone as the brevet start time.
  """
  formatted_start_time = arrow.get(
      brevet_start_time, 'YYYY-MM-DD HH:mm:ss').replace(tzinfo='local')

  if control_dist_km > brevet_dist_km:  # even if controle distance
    control_dist_km = brevet_dist_km  # slightly over brevet distance
    #(if within 110%), don't display
    # times over brevet distance
  shift_amount = 0

# special cases
  if control_dist_km == 0:  # control at 0km stays open for hour
    shift_amount = 1
  elif brevet_dist_km == 200 and control_dist_km == 200:
    shift_amount = 13.5  # 200km brevet limit is 13.5 hours
    # even though algorithm gives 13.333
# normal cases
  elif control_dist_km > 0 and control_dist_km <= 600:
    shift_amount = ((control_dist_km) / 15)
  elif control_dist_km > 600 and control_dist_km <= 1000:
    shift_amount = ((control_dist_km - 600) / 11.428) + (600 / 15)
  elif control_dist_km > 1000 and control_dist_km <= 1300:
    shift_amount = ((control_dist_km - 1000) / 13.333) + \
        (400 / 11.428) + (600 / 15)

  shift_hours = shift_amount // 1
  shift_minutes = round((shift_amount % 1) * 60)

  formatted_start_time = formatted_start_time.shift(
      hours=shift_hours, minutes=shift_minutes)
  return formatted_start_time.isoformat()
