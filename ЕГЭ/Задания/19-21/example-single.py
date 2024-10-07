from functools import lru_cache


@lru_cache(None)
def action(stones: int) -> int:
    """
    :param stones:
    :return: n - turn number; n > 0, if 1st player wins; n < 0, if the 2nd player wins
    """

    # win condition
    if stones <= 19: return 0

    # all possible actions
    actions = [action(stones - 2), action(stones - 5), action(stones // 3)]
    successful = [a for a in actions if a <= 0]

    if len(successful) > 0:
        return -max(successful) + 1
    return -max(actions)


for stones in range(20, 100):
    print(stones, action(stones))