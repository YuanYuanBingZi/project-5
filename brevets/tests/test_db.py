# nose tests for mymongo.py

import arrow
import nose 
import logging
from mymongo import insert_brevet, get_brevet

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_db_insertion():
    start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    dist = 200
    checkpoints = {
        0: (start_time, start_time.shift(hours = 1)),
        50: (start_time.shift(hours = 1, minutes = 28), start_time.shift(hours = 3, minutes = 30)),
        150:(start_time.shift(hours = 4, minutes = 25), start_time.shift(hours = 10)),
        200:(start_time.shift(hours = 5, minutes = 53), start_time.shift(hours = 13, minutes = 30))
    }

    id = insert_brevet(dist, start_time, checkpoints)
    new_start_time, new_dist, new_checkpoints = get_brevet()
    assert new_start_time == start_time
    assert new_dist == dist
    assert new_checkpoints == checkpoints

    