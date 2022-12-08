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


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    dict_salary = job
    searched_salary = salary

    if dict_salary.get("min_salary") == None or dict_salary.get("max_salary") == None:
        raise ValueError("Chave min_salary ou max_salary inexistente")
    if str(dict_salary["min_salary"]).isdigit() == False:
        raise ValueError("min_salary contém valores não numéricos")
    if str(dict_salary["max_salary"]).isdigit() == False:
        raise ValueError("max_salary contém valores não numéricos")
    if int(dict_salary["min_salary"]) > int(dict_salary["max_salary"]):
        raise ValueError("min_salary não pode ser menor que max_salary")
    if str(searched_salary).lstrip('-').isdigit() == False:
        raise ValueError("salary contém valores não numéricos")
    return int(dict_salary['min_salary']) <= int(searched_salary) <= int(dict_salary['max_salary'])     

def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:

    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
