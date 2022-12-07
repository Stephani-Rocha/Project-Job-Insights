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
    all_jobs = jobs
    searched_industry = industry

    filter_industry = list()

    for industry_2 in all_jobs:
        if searched_industry == industry_2["industry"]:
            filter_industry.append(industry_2)
    return filter_industry
