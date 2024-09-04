from fixtube.utils import is_youtube_id


def test_is_youtube_id_valid():
    assert is_youtube_id("abcABC012_-")
    assert is_youtube_id("abcdefghijk")
    assert is_youtube_id("LMNOPQRSTUV")
    assert is_youtube_id("01234567890")


def test_is_youtube_id_wrong_len():
    assert not is_youtube_id("abcd")
    assert not is_youtube_id("abcdABCD012345")


def test_is_youtube_id_illegal_char():
    assert not is_youtube_id("!@#$%^&*()")
    assert not is_youtube_id("adfjvad!#&")
    assert not is_youtube_id("AJKA178.*,")
