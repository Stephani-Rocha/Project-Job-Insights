from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        return list(jobs_reader)


def get_unique_job_types(path: str) -> List[str]:
    jobs_reader = read(path)
    jobs = set()

    for job in jobs_reader:
        jobs.add(job["job_type"])
    return jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    all_jobs = jobs
    searched_job = job_type

    jobs_type = list()

    for job in all_jobs:
        if searched_job == job["job_type"]:
            jobs_type.append(job)
    return jobs_type
