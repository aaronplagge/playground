from sys import argv


def far_to_cel(in_temp: float) -> float:
    return (in_temp - 32) * 5.0/9

def cel_to_far(in_temp: float) -> float:
    return (in_temp * 9.0/5) + 32

def is_float(test_num: float) -> bool:
    try:
        float(test_num)
        return True
    except:
        return False

def check_args() -> None:
    if len(argv) != 3:
        print("Incorrect number of arguments")
        exit(1)

    if argv[1].lower() not in ('f','c','farhenheit','celsius'):
        print("First argument has to be one of 'f' 'c' 'fahrenheit' or 'celsius'")
        exit(2)

    if not is_float(argv[2]):
        print("Second argument needs to be a number")
        exit(3)

def main():
    check_args()
    disp_in_temp = argv[2]
    in_temp = float(argv[2])

    if argv[1].lower() in ('f', 'farhenheit'):
        print(f"{disp_in_temp}f is {far_to_cel(in_temp):.1f}c")

    if argv[1].lower() in ('c', 'celsius'):
        print(f"{disp_in_temp}c is {cel_to_far(in_temp):.1f}f")

if __name__ == '__main__':
    main()

