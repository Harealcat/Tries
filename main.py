from classes.triest import Triest
import argparse


def main():
    # flags and arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--memory", type=int,
                        help='memory size')
    parser.add_argument("-c", "--choice", type=int, help='base or improved tries')
    parser.add_argument("filename", help='filename with data')
    args = parser.parse_args()

    # get args
    filename = str(args.filename)
    choice = int(args.choice)
    memory = int(args.memory)

    if choice == 1:
        print('Tries - Base Algorithm ')
        Triest(filename, memory).run_triest_base()
    else:
        print('Tries - Improved Algorithm ')
        Triest(filename, memory).run_triest_improved()


if __name__ == '__main__':
    main()
