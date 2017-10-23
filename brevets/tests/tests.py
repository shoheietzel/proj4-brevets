"""
Nose tests for flask_brevets.py
"""
import flask_brevets
import acp_times

import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_controles():
  """
  Test a set of controles (0km,25,50,75,100,150,200) for the default starting time(1/1/2017 at 00:00) and default brevet distance(200km)
  """
  assert str(acp_times.open_time(0, 200, '2017-01-01 00:00:00')
             ) == '2017-01-01T00:00:00-08:00'
  assert str(acp_times.close_time(0, 200, '2017-01-01 00:00:00')
             ) == '2017-01-01T01:00:00-08:00'
  assert str(acp_times.open_time(25, 200, '2017-01-01 00:00:00')
             ) == '2017-01-01T00:44:00-08:00'
  assert str(acp_times.close_time(25, 200, '2017-01-01 00:00:00')
             ) == '2017-01-01T01:40:00-08:00'
  assert str(acp_times.open_time(50, 200, '2017-01-01 00:00:00')
             ) == '2017-01-01T01:28:00-08:00'
  assert str(acp_times.close_time(50, 200, '2017-01-01 00:00:00')
             ) == '2017-01-01T03:20:00-08:00'
  assert str(acp_times.open_time(75, 200, '2017-01-01 00:00:00')
             ) == '2017-01-01T02:12:00-08:00'
  assert str(acp_times.close_time(75, 200, '2017-01-01 00:00:00')
             ) == '2017-01-01T05:00:00-08:00'
  assert str(acp_times.open_time(100, 200, '2017-01-01 00:00:00')
             ) == '2017-01-01T02:56:00-08:00'
  assert str(acp_times.close_time(100, 200, '2017-01-01 00:00:00')
             ) == '2017-01-01T06:40:00-08:00'
  assert str(acp_times.open_time(150, 200, '2017-01-01 00:00:00')
             ) == '2017-01-01T04:25:00-08:00'
  assert str(acp_times.close_time(150, 200, '2017-01-01 00:00:00')
             ) == '2017-01-01T10:00:00-08:00'
  assert str(acp_times.open_time(200, 200, '2017-01-01 00:00:00')
             ) == '2017-01-01T05:53:00-08:00'
  assert str(acp_times.close_time(200, 200, '2017-01-01 00:00:00')
             ) == '2017-01-01T13:30:00-08:00'


def test_diff_starting_time():
  """
  Test series of controles(0km,50,100,150,200) for a different starting time
  """
  assert str(acp_times.open_time(0, 200, '2017-10-23 20:00:00')
             ) == '2017-10-23T20:00:00-07:00'
  assert str(acp_times.close_time(0, 200, '2017-10-23 20:00:00')
             ) == '2017-10-23T21:00:00-07:00'
  assert str(acp_times.open_time(50, 200, '2017-10-23 20:00:00')
             ) == '2017-10-23T21:28:00-07:00'
  assert str(acp_times.close_time(50, 200, '2017-10-23 20:00:00')
             ) == '2017-10-23T23:20:00-07:00'
  assert str(acp_times.open_time(100, 200, '2017-10-23 20:00:00')
             ) == '2017-10-23T22:56:00-07:00'
  assert str(acp_times.close_time(100, 200, '2017-10-23 20:00:00')
             ) == '2017-10-24T02:40:00-07:00'
  assert str(acp_times.open_time(150, 200, '2017-10-23 20:00:00')
             ) == '2017-10-24T00:25:00-07:00'
  assert str(acp_times.close_time(150, 200, '2017-10-23 20:00:00')
             ) == '2017-10-24T06:00:00-07:00'
  assert str(acp_times.open_time(200, 200, '2017-10-23 20:00:00')
             ) == '2017-10-24T01:53:00-07:00'
  assert str(acp_times.close_time(200, 200, '2017-10-23 20:00:00')
             ) == '2017-10-24T09:30:00-07:00'


def test_diff_brevet_distance():
  """
  Test series of controles(0km,100,200,500,750,1000) for a different brevet distance
  """
  assert str(acp_times.open_time(0, 1000, '2017-01-01 00:00:00')
             ) == '2017-01-01T00:00:00-08:00'
  assert str(acp_times.close_time(0, 1000, '2017-01-01 00:00:00')
             ) == '2017-01-01T01:00:00-08:00'
  assert str(acp_times.open_time(100, 1000, '2017-01-01 00:00:00')
             ) == '2017-01-01T02:56:00-08:00'
  assert str(acp_times.close_time(100, 1000, '2017-01-01 00:00:00')
             ) == '2017-01-01T06:40:00-08:00'
  assert str(acp_times.open_time(200, 1000, '2017-01-01 00:00:00')
             ) == '2017-01-01T05:53:00-08:00'
  assert str(acp_times.close_time(200, 1000, '2017-01-01 00:00:00')
             ) == '2017-01-01T13:20:00-08:00'
  assert str(acp_times.open_time(500, 1000, '2017-01-01 00:00:00')
             ) == '2017-01-01T15:28:00-08:00'
  assert str(acp_times.close_time(500, 1000, '2017-01-01 00:00:00')
             ) == '2017-01-02T09:20:00-08:00'
  assert str(acp_times.open_time(750, 1000, '2017-01-01 00:00:00')
             ) == '2017-01-02T00:09:00-08:00'
  assert str(acp_times.close_time(750, 1000, '2017-01-01 00:00:00')
             ) == '2017-01-03T05:08:00-08:00'
  assert str(acp_times.open_time(1000, 1000, '2017-01-01 00:00:00')
             ) == '2017-01-02T09:05:00-08:00'
  assert str(acp_times.close_time(1000, 1000, '2017-01-01 00:00:00')
             ) == '2017-01-04T03:00:00-08:00'


def test_over_console():
  """
  Tests a console distance that is over the brevit distance but within 110%.
  """
  assert str(acp_times.open_time(205, 200, '2017-01-01 00:00:00')
             ) == '2017-01-01T05:53:00-08:00'
  assert str(acp_times.close_time(205, 200, '2017-01-01 00:00:00')
             ) == '2017-01-01T13:30:00-08:00'


def test_daylight_savings():
  """
  Tests that the time difference is accounted for within arrow/acp_times.py when a race takes place during the time change.
  """
  assert str(acp_times.open_time(0, 1000, '2017-03-11 12:00:00')
             ) == '2017-03-11T12:00:00-08:00'
  assert str(acp_times.close_time(0, 1000, '2017-03-11 12:00:00')
             ) == '2017-03-11T13:00:00-08:00'
  assert str(acp_times.open_time(1000, 1000, '2017-03-11 12:00:00')
             ) == '2017-03-12T21:05:00-07:00'
  assert str(acp_times.close_time(1000, 1000, '2017-03-11 12:00:00')
             ) == '2017-03-14T15:00:00-07:00'
