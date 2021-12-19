from pathlib import Path

import eu2020.data
from eu2020.common.utils import from_yaml_file
from eu2020.data.ev_members_cz import ev_member_country_cz as ev_cz

DATA_PATH = Path(eu2020.data.__path__[0])


def test_events_cz():
    ev_cz_from_yaml = from_yaml_file(DATA_PATH / "ev_members_cz.yml")
    assert ev_cz_from_yaml == ev_cz
