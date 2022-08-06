from src.counter import count_ocurrences


def test_counter():
    path = "src/jobs.csv"
    word = "java"
    report = count_ocurrences(path, word)
    assert report == 676
    assert type(report) is int
    assert type(path) is str
    assert type(word) is str
