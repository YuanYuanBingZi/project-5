"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""
# how can we run the test when we try to 
from acp_times import open_time, close_time
import arrow
import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

def test_brevet1():
    start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    dist = 200
    checkpoints = {
        0: (start_time, start_time.shift(hours = 1)),
        50: (start_time.shift(hours = 1, minutes = 28), start_time.shift(hours = 3, minutes = 30)),
        150:(start_time.shift(hours = 4, minutes = 25), start_time.shift(hours = 10)),
        200:(start_time.shift(hours = 5, minutes = 53), start_time.shift(hours = 13, minutes = 30))
    }

    for km, time_tuple in checkpoints.items():
        check_open, check_close = time_tuple
        assert open_time(km, dist, start_time) == check_open
        assert close_time(km, dist, start_time) == check_close



def test_brevet2():
    start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    dist = 300
    checkpoints = {
        0: (start_time, start_time.shift(hours = 1)),
        50: (start_time.shift(hours = 1, minutes = 28), start_time.shift(hours = 3, minutes = 30)),
        210:(start_time.shift(hours = 6, minutes = 12), start_time.shift(hours = 14)),
        300:(start_time.shift(hours = 9), start_time.shift(hours = 20))
    }

    for km, time_tuple in checkpoints.items():
        check_open, check_close = time_tuple
        assert open_time(km, dist, start_time) == check_open
        assert close_time(km, dist, start_time) == check_close


def test_brevet3():
    start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    dist = 400
    checkpoints = {
        0: (start_time, start_time.shift(hours = 1)),
        50: (start_time.shift(hours = 1, minutes = 28), start_time.shift(hours = 3, minutes = 30)),
        320:(start_time.shift(hours = 9, minutes = 38), start_time.shift(hours = 21, minutes = 20)),
        400:(start_time.shift(hours = 12, minutes = 8), start_time.shift(hours = 27))
    }

    for km, time_tuple in checkpoints.items():
        check_open, check_close = time_tuple
        assert open_time(km, dist, start_time) == check_open
        assert close_time(km, dist, start_time) == check_close

def test_brevet3():
    start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    dist = 400
    checkpoints = {
        0: (start_time, start_time.shift(hours = 1)),
        50: (start_time.shift(hours = 1, minutes = 28), start_time.shift(hours = 3, minutes = 30)),
        320:(start_time.shift(hours = 9, minutes = 38), start_time.shift(hours = 21, minutes = 20)),
        400:(start_time.shift(hours = 12, minutes = 8), start_time.shift(hours = 27))
    }

    for km, time_tuple in checkpoints.items():
        check_open, check_close = time_tuple
        assert open_time(km, dist, start_time) == check_open
        assert close_time(km, dist, start_time) == check_close


def test_brevet4():
    start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    dist = 600
    checkpoints = {
        0: (start_time, start_time.shift(hours = 1)),
        200: (start_time.shift(hours = 5, minutes = 53), start_time.shift(hours = 13, minutes = 20)),
        450:(start_time.shift(hours = 13, minutes = 48), start_time.shift(hours = 30)),
        550:(start_time.shift(hours = 17, minutes = 8), start_time.shift(hours = 36, minutes = 40)),
        600:(start_time.shift(hours = 18, minutes = 48), start_time.shift(hours = 40))
        
    }

    for km, time_tuple in checkpoints.items():
        check_open, check_close = time_tuple
        assert open_time(km, dist, start_time) == check_open
        assert close_time(km, dist, start_time) == check_close


def test_brevet5():
    start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    dist = 1000
    checkpoints = {
        0: (start_time, start_time.shift(hours = 1)),
        200: (start_time.shift(hours = 5, minutes = 53), start_time.shift(hours = 13, minutes = 20)),
        400:(start_time.shift(hours = 12, minutes = 8), start_time.shift(hours = 26, minutes = 40)),
        600:(start_time.shift(hours = 18, minutes = 48), start_time.shift(hours = 40)),
        800:(start_time.shift(hours = 25, minutes = 57), start_time.shift(hours = 57, minutes = 30)),
        1000:(start_time.shift(hours = 33, minutes = 5), start_time.shift(hours = 75))
        
    }

    for km, time_tuple in checkpoints.items():
        check_open, check_close = time_tuple
        assert open_time(km, dist, start_time) == check_open
        assert close_time(km, dist, start_time) == check_close