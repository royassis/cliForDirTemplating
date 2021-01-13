import argparse
from dir_template_cli.functions import init, add, tree, ls, rm


def main():
    my_parser = argparse.ArgumentParser(description='Program description')

    subparsers = my_parser.add_subparsers(help='sub-command help',
                                          title="commands",
                                          dest="command",
                                          required=True,
                                          prog='argi')

    parser_init = subparsers.add_parser('init', help='init help')

    parser_init.add_argument('dir',
                             help='the path to dir',
                             nargs=1)

    parser_init.add_argument('template',
                             help='the path to dir',
                             nargs=1)

    parser_ls = subparsers.add_parser('ls', help='ls help')

    parser_tree = subparsers.add_parser('tree', help='ls help')

    parser_tree.add_argument('template',
                             help='template name',
                             nargs=1)

    parser_add = subparsers.add_parser('add', help='ls help')

    parser_add.add_argument('directory',
                            help='template name',
                            nargs=1)

    parser_rm = subparsers.add_parser('rm', help='ls help')

    parser_rm.add_argument('template',
                           help='template name',
                           nargs=1)

    args = my_parser.parse_args()

    if args.command == 'init':
        init(args.dir[0], args.template[0])

    if args.command == 'tree':
        tree(args.template[0])

    if args.command == 'ls':
        ls()

    if args.command == 'add':
        add(args.directory[0])

    if args.command == 'rm':
        rm(args.template[0])


if __name__ == '__main__':
    main()
