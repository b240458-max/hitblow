"""スコア計算機能。"""

MULTIPLIERS = {
    "Easy": 1,
    "Normal": 2,
    "Hard": 3,
}


def calculate_score(difficulty, tries, hint_count=0):
    """難易度・挑戦回数・ヒント使用回数からスコアを計算する。"""
    base_score = (11 - tries) * 100 * MULTIPLIERS[difficulty]
    hint_penalty = hint_count * 300
    return max(0, base_score - hint_penalty)