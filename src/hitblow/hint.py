int.py

"""ヒント機能。"""

import random

HINT_COST = 300
MAX_HINTS = 2


def give_hint(secret, revealed):
    """まだ公開していない答えの数字を1つ返す。"""
    candidates = [digit for digit in secret if digit not in revealed]

    if not candidates:
        return None

    digit = random.choice(candidates)
    revealed.add(digit)
    return digit