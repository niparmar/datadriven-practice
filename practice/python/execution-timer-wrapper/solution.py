import time


def make_timed(func):
  def wrapper(*args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    return result

  return wrapper
  
@make_timed
def answer():
  return 42


@make_timed
def double(n):
  return n * 2


@make_timed
def add(x, y):
  return x + y


@make_timed
def greet(greeting, name):
  return greeting + name


@make_timed
def pair(a, b):
  return [a, b]


JOBS = {
  "answer": answer,
  "double": double,
  "add": add,
  "greet": greet,
  "pair": pair,
}


def run_timed(job, args=None):
  if args is None:
    args = ()
  job_func = JOBS[job]
  return job_func(*args)
  
