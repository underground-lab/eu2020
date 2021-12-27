# coding: utf-8

from eu2020.common.utils import auto_set_option_keys
from eu2020.data.ev_story_covid19 import ev_story_covid19
from eu2020.data.ev_story_greendeal import ev_story_greendeal
from eu2020.data.ev_story_vrbetice import ev_story_vrbetice

ev_story = [
    *ev_story_covid19,
    *ev_story_greendeal,
    *ev_story_vrbetice,
]

auto_set_option_keys(ev_story)
