import sys
import arguments
from Instance import Instance

def main(args):
    # Reading file
    kwargs = {"maxiters": args.maxiters, "pop_size": args.size}
    file = "./data/" + args.file
    instance = Instance.from_file(file, **kwargs)

    print(instance.items)

main(arguments.defineArgs())
