from functools import wraps

import elasticapm
from elasticapm.utils import get_name_from_func


def apm_capture_span(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with elasticapm.capture_span(get_name_from_func(func)):
            return func(*args, **kwargs)

    return wrapper
