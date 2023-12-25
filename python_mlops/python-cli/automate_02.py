import sys
import click


@click.command()
@click.option("--names", default="boyd", type=str, help="Enter your name or list of names separated by comma")
@click.option("--sorted", is_flag=True, help="Sort the names")
def main(names, sorted):
    
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
    main()