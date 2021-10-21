import pytest

from eu2020.app import print_hp_events
from eu2020.common.higher_power_events import HigherPowerEvents


@pytest.mark.parametrize(
    'events, expected_stdout',
    (
        ([], ""),
        (
            [{"name": "Inflace"}],
            "\nMimořádné události: Inflace\n"
        ),
        (
            [{"name": "Pandemie"}, {"name": "Inflace"}],
            "\nMimořádné události: Pandemie, Inflace\n"
        ),
    )
)
def test_print_hp_events(capsys, events, expected_stdout):
    hp_events = HigherPowerEvents(events)
    hp_events.active_events = events
    print_hp_events(hp_events)
    assert capsys.readouterr().out == expected_stdout
