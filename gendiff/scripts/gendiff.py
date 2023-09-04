#!/usr/bin/env python


import argparse


from gendiff.gendiff import generate_diff


def get_args():
    parser = argparse.ArgumentParser(
            usage='gendiff [-h] first_file second_file',
            description='Compares two\
                    configuration files and shows a difference.'
            )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
                        help='set format of output')
    return parser.parse_args()


def main():
    args = get_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
