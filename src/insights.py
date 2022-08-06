from src.jobs import read


def get_unique_job_types(path):

    jobs = read(path)
    unique_jobs = set()
    for job in jobs:
        unique_jobs.add(job["job_type"])

    return unique_jobs


def filter_by_job_type(jobs, job_type):

    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs


def get_unique_industries(path):

    jobs = read(path)
    unique_industries = set()
    for job in jobs:
        if job["industry"]:  # verifica se tem conteúdo
            unique_industries.add(job["industry"])

    return unique_industries


def filter_by_industry(jobs, industry):

    filtered_jobs = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_jobs.append(job)

    return filtered_jobs


def get_max_salary(path):

    jobs = read(path)
    max_salary = 0
    for job in jobs:
        if job["max_salary"]:  # verifica se tem conteúdo
            if job["max_salary"].isdigit():  # verifica se é numero
                if int(job["max_salary"]) > max_salary:  # faz a comparação
                    max_salary = int(job["max_salary"])
    return max_salary


def get_min_salary(path):

    jobs = read(path)
    salaries = []
    for job in jobs:
        if job["min_salary"]:  # verifica se tem conteúdo
            if job["min_salary"].isdigit():  # verifica se é numero
                salaries.append(int(job["min_salary"]))
    return min(salaries)  # faz a comparação

# https://www.w3schools.com/python/python_ref_functions.asp


def matches_salary_range(job, salary):

    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError("valor minimo ou máximo não encontrado")

    if type(salary) != int:
        raise ValueError("valor de salary não numérico")

    min_salary = job["min_salary"]
    max_salary = job["max_salary"]

    if type(max_salary) != int or type(min_salary) != int:
        raise ValueError("valor mínimo ou máximo não numérico")

    if max_salary < min_salary:
        raise ValueError("valor máximo maior que valor mínimo")

    return max_salary >= salary >= min_salary


def filter_by_salary_range(jobs, salary):
    salaries = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salaries.append(job)
        except ValueError as error:
            print(error)

    return salaries

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
