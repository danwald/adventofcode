from functools import reduce
from operator import mul

import sys

def possible(attempt, reqs):
    game, trials = attempt.split(':')
    game = int(game.split(' ')[-1])
    for trial in trials.split(';'):
        #print(f'{game} -> {trial}')
        for pull in trial.strip().split(','):
            count, cube = pull.strip().split(' ')
            #print(f'{count}, {cube}')
            try:
                if reqs[cube][0] < int(count):
                    return 0
                reqs[cube][1] = True
            except KeyError:
                continue
    if all(val[1] for _,val in reqs.items()):
        return game
    return 0


def pow_set(attempt, reqs):
    game, trials = attempt.split(':')
    game = int(game.split(' ')[-1])
    for trial in trials.split(';'):
        #print(f'{game} -> {trial}')
        for pull in trial.strip().split(','):
            count, cube = pull.strip().split(' ')
            #print(f'{count}, {cube}')
            try:
                if reqs[cube][0] < int(count):
                    reqs[cube][0] = int(count)
                reqs[cube][1] = True
            except KeyError:
                continue
    if all(val[1] for val in reqs.values()):
        return reduce(mul, [val[0] for val in reqs.values()])
    return 0

def get_reqs(match, override=None):
    reqs = {}
    for req in match.split(','):
        cube, max_value = req.split(' ')
        reqs[cube] = [int(override or max_value), False]
    return reqs

def main():
    games = []
    while line:=sys.stdin.readline().strip():
        #games.append(possible(line, get_reqs('red 12,green 13,blue 14')))
        games.append(pow_set(line, get_reqs('red 12,green 13,blue 14', override=-1)))
    print(sum(games))

if __name__ == "__main__":
    main()
