import argparse

def far_to_cel(in_temp: float) -> float:
    return (in_temp - 32) * 5.0/9

def cel_to_far(in_temp: float) -> float:
    return (in_temp * 9.0/5) + 32

def parse_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--fahrenheit", type=float, help="Convert Fahrenheit to Celsius")
    group.add_argument('-c', "--celsius", type=float, help="Convert Celsius to Fahrenheit")

    return parser.parse_args()

def main():
    args = parse_args()

    if args.celsius:
        out_temp = cel_to_far(args.celsius)
        print(f"{args.celsius}c is {out_temp:.1f}f")

    if args.fahrenheit:
        out_temp = far_to_cel(args.fahrenheit)
        print(f"{args.fahrenheit}f is {out_temp:.1f}c")

if __name__ == "__main__":
    main()
