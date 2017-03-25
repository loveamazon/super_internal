#!/usr/bin/python2.7

import cProfile
import pstats
import StringIO
import logging
import os
#import time

PROFILE_LIMIT = int(os.environ.get("PROFILE_LIMIT", 30))
PROFILER = bool(int(os.environ.get("PROFILER", 1)))

print """
# ** USAGE:
$ PROFILE_LIMIT=100 gunicorn -c ./wsgi_profiler_conf.py wsgi
# ** TIME MEASUREMENTS ONLY:
$ PROFILER=0 gunicorn -c ./wsgi_profiler_conf.py wsgi
"""



global_profile = cProfile.Profile()
def profiler_enable(worker, req):
    #worker.profile = cProfile.Profile()
    #worker.profile.enable()
    global global_profile
    global_profile.enable()
    worker.log.info("PROFILING %d: %s" % (worker.pid, req.uri))


def profiler_summary(worker):
    s = StringIO.StringIO()
    #worker.profile.disable()
    global global_profile
    global_profile.disable()
    global_profile.print_stats(sort="time")
    ps = pstats.Stats(global_profile, stream=s).sort_stats('time', 'cumulative')
    ps.print_stats(PROFILE_LIMIT)
    worker.log.info("Fucking")


import signal
bak_worker = None

global_count = 0
def graceful_reload(signum, traceback):
    """Explicitly close some global MongoClient object."""
    profiler_summary(bak_worker)

signal.signal(signal.SIGHUP, graceful_reload)


def pre_request(worker, req):
    #worker.start_time = time.time()
    global bak_worker
    if bak_worker is None:
        bak_worker = worker
        profiler_enable(worker, req)


def post_request(worker, req, *args):
    #total_time = time.time() - worker.start_time
    #logging.error("\n[%d] [INFO] [%s] Load Time: %.3fs\n" % (
    #    worker.pid, req.method, total_time))
    global global_count 
    global_count += 1
    #logging.error("\n[%d]", global_count)
    if global_count == 500:
        #global_count = 0
        profiler_summary(worker)
        #profiler_enable(worker,req)
