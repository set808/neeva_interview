import click
import os
from re import findall
from statistics import fmean
from subprocess import check_output

cwd = os.path.dirname(os.path.realpath(__file__))
regex = b'([a-z0-9]+)\s+([A-z0-9/.]+)\s+\(<([^>]+)>'


@click.command()
@click.argument('path')
@click.argument('email')
def main(path, email):
    counts = []
    for root, dir, files in os.walk('go/' + path):
        file_root = root.split('/', 1)[1]
        for file in files:
            counts.append(calculate_blame_score(file_root, email, file))
    print(format(fmean(counts), '.1f'))


def calculate_blame_score(file_root: str, email: str, file: str):
    blame = check_output(
        ['git', '-C', cwd + '/go', 'blame', '-fe', file_root + '/' + file])
    records = findall(regex, blame)
    user_count = 0
    line_count = len(records)
    for commit, fp, user in records:
        if email == user.decode('utf-8'):
            user_count += 1
    return user_count / line_count


if __name__ == '__main__':
    main()
