"""ゲームの進行（入力・表示・ループ）。
★ チームで足す機能は **自分の担当の場所**に書く（1機能=1ファイル）。
下の「ここに足す」場所は3か所（① 開始時 ② 入力コマンド ③ 勝利時）。
ペアごとに**別の場所**を直すので、並行作業でも衝突しない。
import も自分の場所の近くに書くこと（ファイル先頭にまとめない＝衝突回避）。
"""

from .core import judge, make_secret


def play(digits=3):
    secret = make_secret(digits)
    print(f"Hit & Blow（{digits} 桁・重複なし）")

    # ===== ① 開始時に足す（難易度・あいさつ など）: ここに書く =====
    from .difficulty import select_difficulty
    from .limit import get_limit

    difficulty = select_difficulty()
    limit = get_limit(difficulty)

    print(
        f"\n【{difficulty} モード】で開始します！"
        f"（最大挑戦回数: {limit} 回）"
    )
    print("ヒントを使う場合は、予想の代わりに h を入力してください。")
    print("ヒント1回につき300点減点されます。\n")

    tries = 0
    hint_count = 0
    revealed = set()

    while True:
        guess = input("予想 > ").strip()

        # ===== ② 入力コマンドに足す（ヒント など）: ここに書く（import もここに） =====
        from .hint import give_hint, HINT_COST, MAX_HINTS

        if guess.lower() == "h":
            if hint_count >= MAX_HINTS:
                print(f"ヒントは{MAX_HINTS}回までです")
                continue

            confirm = input(
                f"ヒントを使用しますか？ "
                f"{HINT_COST}点減点されます（y/n）> "
            ).strip().lower()

            if confirm != "y":
                print("ヒントの使用をキャンセルしました")
                continue

            digit = give_hint(secret, revealed)

            if digit is None:
                print("これ以上ヒントはありません")
                continue

            hint_count += 1
            print(f"ヒント：答えには「{digit}」が含まれています")
            print(
                f"ヒント使用回数：{hint_count}/{MAX_HINTS}"
                f"（合計-{hint_count * HINT_COST}点）"
            )
            continue

        if len(guess) != digits or not guess.isdigit():
            print(f"{digits} 桁の数字で入力してね")
            continue

        if len(set(guess)) != digits:
            print("同じ数字は複数回使えません")
            continue

        tries += 1
        hit, blow = judge(secret, guess)
        print(f"  Hit={hit}  Blow={blow}")

        if hit == digits:
            # ===== ③ 勝利時に足す（スコア・履歴 など）: ここに書く =====
            from .score import calculate_score

            score = calculate_score(
                difficulty,
                tries,
                hint_count,
            )

            print(
                f"正解！ {tries} 回で当たり"
                f"（答え {secret}）"
            )
            print(f"ヒント使用回数: {hint_count} 回")
            print(f"★ 獲得スコア: {score} 点 ★")
            break

        # 回数制限（limit.py）の機能
        if tries >= limit:
            print(
                f"\nゲームオーバー！"
                f"制限回数（{limit} 回）に達しました。"
                f"（答えは {secret} でした）"
            )
            print("★ 獲得スコア: 0 点 ★")
            break