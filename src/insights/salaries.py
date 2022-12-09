from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    jobs_reader = read(path)
    salaries = set()
    for salary in jobs_reader:
        if salary["max_salary"].isdigit():
            salaries.add(int(salary["max_salary"]))
    max_salary = max(salaries)
    return max_salary


def get_min_salary(path: str) -> int:
    jobs_reader = read(path)
    salaries = set()
    for salary in jobs_reader:
        if salary["min_salary"].isdigit():
            salaries.add(int(salary["min_salary"]))
    min_salary = min(salaries)
    return min_salary

# Essa função tem como objetivo fazer validações referente a min_salary e max_salary
def validate_min_salary_and_max_salary(job: Dict) -> ValueError:
    if job.get("min_salary") is None or job.get("max_salary") is None:
        raise ValueError("Chave min_salary ou max_salary inexistente")
    if not str(job["min_salary"]).isdigit():
        raise ValueError("min_salary contém valores não numéricos")
    if not str(job["max_salary"]).isdigit():
        raise ValueError("max_salary contém valores não numéricos")
    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError("min_salary não pode ser menor que max_salary")

# Essa função tem como objetivo fazer validações referente a salary
def validate_salary(salary: Union[int, str]) -> ValueError:
    if not str(salary).lstrip('-').isdigit():
        raise ValueError("salary contém valores não numéricos")


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    validate_min_salary_and_max_salary(job)
    validate_salary(salary)
    return int(job['min_salary']) <= int(salary) <= int(job['max_salary'])


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:

    job_list = list()
    for job in jobs:
        try:
            if matches_salary_range(job, salary) is True:
                job_list.append(job)
        except ValueError:
            print(ValueError)
    return job_list
