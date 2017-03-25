def profile_func(func):
    def wrap(*args, **kwargs):
        #import cProfile
        #pr = cProfile.Profile()
        #pr.enable()
        result = func(*args, **kwargs)
        #pr.disable()
        #pr.print_stats(sort="time")
        return result

    return wrap