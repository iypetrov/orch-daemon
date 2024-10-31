import logging
import argparse

log = logging.getLogger('orch-daemon')
log.setLevel(logging.INFO)
logging.basicConfig(format='%(asctime)s - %(name)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def run_controller():
    log.info("start controller")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["controller"])

    args = parser.parse_args()

    if args.mode == "controller":
        run_controller()

if __name__ == "__main__":
    main()
