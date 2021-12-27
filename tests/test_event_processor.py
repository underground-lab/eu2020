import pytest

from eu2020.common.event_processor import EventProcessor
from eu2020.common.parties import Parties


def test_add_stories_fails_if_party_not_found():
    flags = set()
    parties = Parties({"A": ..., "B": ...}, "TEST")
    processor = EventProcessor(flags)
    processor.add_parties(parties)
    processor.add_events([{"party": "A"}])
    processor.add_events([{"party": "B"}])
    with pytest.raises(ValueError, match="party not found: C"):
        processor.add_events([{"party": "C"}])
