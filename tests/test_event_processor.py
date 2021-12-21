import pytest

from eu2020.common.event_processor import EventProcessor
from eu2020.common.parties import Parties
from eu2020.common.parties_events import PartiesEvents


def test_add_stories_fails_if_party_not_found():
    flags = set()
    parties = Parties({"A": ..., "B": ...})
    parties_events = PartiesEvents([{"party": "A"}], parties, flags)
    processor = EventProcessor(flags)
    processor.add_events(parties_events)
    processor.add_stories([{"party": "A"}])
    processor.add_stories([{"party": "B"}])
    with pytest.raises(ValueError, match="party not found: C"):
        processor.add_stories([{"party": "C"}])
