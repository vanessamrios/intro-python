from functools import lru_cache
import csv


@lru_cache
def read(path):

    with open(path, encoding="utf8") as file:
        jobs_obj = csv.DictReader(file)
        jobs_list = []
        for job in jobs_obj:
            jobs_list.append(job)

    return jobs_list

# https://linuxhint.com/use-python-csv-dictreader/
