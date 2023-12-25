import sys
import argparse


def main(names, sorted=False):
    
    name_ls = names.split(",")
    print(name_ls)
    if sorted:
        names = name_ls.sort()
        for name in name_ls:
            print(f"Hello World to: {name}")
    
    else:
        for name in name_ls:
            print(f"Hello World to: {name}")


if __name__ == '__main__':
    
    parse = argparse.ArgumentParser(description="This is an automated test program")
    parse.add_argument("--name", type=str, help="Enter your name")
    parse.add_argument("--sort", action="store_true", help="Sort the names")
    
    arg_name = vars(parse.parse_args())["name"]
    arg_sort = vars(parse.parse_args())["sort"]
    
    main(arg_name, arg_sort)