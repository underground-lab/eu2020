import pytest

from eu2020.app import print_hp_events
from eu2020.common.higher_power_events import HigherPowerEvents


@pytest.mark.parametrize(
    'events, active, expected_stdout',
    (
        ([], [], ""),
        (
            [{"key": "inflation", "name": "Inflace"}],
            ["inflation"],
            "\nMimořádné události: Inflace\n"
        ),
        (
            [{"key": "pandemic", "name": "Pandemie"}, {"key": "inflation", "name": "Inflace"}],
            ["pandemic", "inflation"],
            "\nMimořádné události: Pandemie, Inflace\n"
        ),
    )
)
def test_print_hp_events(capsys, events, active, expected_stdout):
    active = set(active)
    hp_events = HigherPowerEvents(events, active)
    print_hp_events(hp_events)
    assert capsys.readouterr().out == expected_stdout
