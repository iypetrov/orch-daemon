import logging
import argparse
import time
import datetime as dt

from concurrent.futures import ThreadPoolExecutor
from scheduler import Scheduler

log = logging.getLogger('orch-daemon')
log.setLevel(logging.INFO)
logging.basicConfig(format='%(asctime)s - %(name)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def foo():
    log.info("foo")

def bar():
    log.info("bar")

def schedule_actions():
    try:
        schedule = Scheduler(tzinfo=dt.timezone.utc)
        schedule.cyclic(dt.timedelta(seconds=3), foo)
        schedule.cyclic(dt.timedelta(seconds=4), bar)
        
        while True:
            schedule.exec_jobs()
            time.sleep(1)
    except Exception as e:
        log.error("An error occurred in schedule_actions: %s", e, exc_info=True)

def listen_events():
    try:
        while True:
            log.info("start listen events")
            time.sleep(5)
    except Exception as e:
        log.error("An error occurred in listen_events: %s", e, exc_info=True)

def run_orch():
    log.info("start orch-daemon")
    with ThreadPoolExecutor() as executor:
        executor.submit(schedule_actions)
        executor.submit(listen_events)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["orch"])

    args = parser.parse_args()

    if args.mode == "orch":
        run_orch()

if __name__ == "__main__":
    main()
