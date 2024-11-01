import logging
import argparse

log = logging.getLogger('orch-daemon')
log.setLevel(logging.INFO)
logging.basicConfig(format='%(asctime)s - %(name)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def run_orch():
    log.info("start orch")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["orch"])

    args = parser.parse_args()

    if args.mode == "orch":
        run_orch()

if __name__ == "__main__":
    main()
