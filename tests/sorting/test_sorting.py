from src.pre_built.sorting import sort_by

job_1 = {"min_salary": 100, "max_salary": 1000, "date_posted": '2001-02-01'}
job_2 = {"min_salary": 50, "max_salary": 2000, "date_posted": ''}
job_3 = {"min_salary": '', "max_salary": 3000, "date_posted":  '2021-02-01'}
job_4 = {"min_salary": 200, "max_salary": '', "date_posted": '2011-02-01'}

MOCK_MAX = [job_1, job_2, job_3, job_4]
MOCK_MIN = [job_1, job_2, job_3, job_4]
MOCK_DATE = [job_1, job_2, job_3, job_4]


def test_sort_by_criteria():
    sort_by(MOCK_MAX, "max_salary")
    assert MOCK_MAX == [job_3, job_2, job_1, job_4]
    sort_by(MOCK_MIN, "min_salary")
    assert MOCK_MIN == [job_2, job_1, job_4, job_3]
    sort_by(MOCK_DATE, "date_posted")
    assert MOCK_DATE == [job_3, job_4, job_1, job_2]
