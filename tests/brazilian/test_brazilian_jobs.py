from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    read_file = read_brazilian_file("tests/mocks/brazilians_jobs.csv")

    for translated_job in read_file:
        assert translated_job.get("title") is not None
        assert translated_job.get("salary") is not None
        assert translated_job.get("type") is not None
        assert translated_job.get("titulo") is None
        assert translated_job.get("salario") is None
        assert translated_job.get("tipo") is None
