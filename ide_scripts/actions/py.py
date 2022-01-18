import sys


def main():
    code = sys.stdin.read()
    sys.stdout.write(code)
    sys.stderr.write(code)


if __name__ == '__main__':
    main()
