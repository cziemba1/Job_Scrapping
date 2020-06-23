from indeed import get_jobs as get_indeed_jobs
from save_file import save_to_file

indeed_jobs = get_indeed_jobs()
save_to_file(indeed_jobs)
