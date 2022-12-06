from typing import List, Dict
from .jobs import read

def get_unique_industries(path: str) -> List[str]:
    jobs_reader = read(path)
    jobs_industry = set()
    for job in jobs_reader:
        if len(job["industry"]) > 0:
            jobs_industry.add(job["industry"])
    return jobs_industry


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
