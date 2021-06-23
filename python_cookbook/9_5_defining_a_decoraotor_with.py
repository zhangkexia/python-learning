#!/usr/bin/python
# -*- encoding: utf-8 -*-


from functools import wraps, partial
import logging

# Utility decorator to attatch a function as an attribute of obj
def attatch_wrapper(obj, func=None):
    if func is None:
        return partial(attatch_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    '''
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the log
    message. If name and message aren't specified,
    they default to the function's module and name.
    '''
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        # Attatch setter functions
        @attatch_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level 
            level = newlevel

        @attatch_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper
    return decorate


# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y 


add.set_message('Add called.')
