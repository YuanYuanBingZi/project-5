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
    checkpoints = [
        {"km": 0, "open_time": start_time, "close_time":start_time.shift(hours = 1)},
        {"km": 50, "open_time": start_time.shift(hours = 1, minutes = 28), "close_time":start_time.shift(hours = 3, minutes = 30)},
        {"km": 150, "open_time": start_time.shift(hours = 4, minutes = 25), "close_time":start_time.shift(hours = 10)},
        {"km": 200, "open_time": start_time.shift(hours = 5, minutes = 53), "close_time":start_time.shift(hours = 13, minutes = 30)}
    ]

    for checkpoint in checkpoints:
        checkpoint["open_time"] = checkpoint["open_time"].format('YYYY-MM-DDTHH:mm')
        checkpoint["close_time"] = checkpoint["close_time"].format('YYYY-MM-DDTHH:mm')

    start_time = start_time.format('YYYY-MM-DDTHH:mm')

    id = insert_brevet(dist, start_time, checkpoints)
    new_dist, new_start_time, new_checkpoints = get_brevet()
    assert new_start_time == start_time
    assert new_dist == dist
    assert new_checkpoints == checkpoints


def test_db_get_brevets():
    start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    dist = 400
    checkpoints = [
        {"km": 0, "open_time": start_time, "close_time":start_time.shift(hours = 1)},
        {"km": 50, "open_time": start_time.shift(hours = 1, minutes = 28), "close_time":start_time.shift(hours = 3, minutes = 30)},
        {"km": 320, "open_time": start_time.shift(hours = 9, minutes = 38), "close_time":start_time.shift(hours = 21, minutes = 20)},
        {"km": 400, "open_time": start_time.shift(hours = 12, minutes = 8), "close_time":start_time.shift(hours = 27)}
    ]

    for checkpoint in checkpoints:
        checkpoint["open_time"] = checkpoint["open_time"].format('YYYY-MM-DDTHH:mm')
        checkpoint["close_time"] = checkpoint["close_time"].format('YYYY-MM-DDTHH:mm')

    start_time = start_time.format('YYYY-MM-DDTHH:mm')

    id = insert_brevet(dist, start_time, checkpoints)
    new_dist, new_start_time, new_checkpoints = get_brevet()
    assert new_start_time == start_time
    assert new_dist == dist
    assert new_checkpoints == checkpoints
