import argparse


def run_controller():
    print("start controller")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["controller"])

    args = parser.parse_args()

    if args.mode == "controller":
        run_controller()


if __name__ == "__main__":
    main()
