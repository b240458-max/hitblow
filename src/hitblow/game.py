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
    
    # 難易度を選択し、最大挑戦回数を取得する
    difficulty = select_difficulty()
    limit = get_limit(difficulty)
    print(f"\n【{difficulty} モード】で開始します！（最大挑戦回数: {limit} 回）\n")

    tries = 0
    while True:
        guess = input("予想 > ").strip()
        
        # ===== ② 入力コマンドに足す（ヒント など）: ここに書く（import もここに） =====
        # 例:  from .hint import hint
        #      if guess == "h":
        #          print(hint(secret)); continue
        
        if len(guess) != digits or not guess.isdigit():
            print(f"{digits} 桁の数字で入力してね")
            continue
            
        tries += 1
        hit, blow = judge(secret, guess)
        print(f"  Hit={hit}  Blow={blow}")
        
        if hit == digits:
            # ===== ③ 勝利時に足す（スコア・履歴 など）: ここに書く =====
            # ※ score.py の関数名を calculate_score に修正した前提です。
            # もし sore のままにする場合は calculate_sore に書き換えてください。
            from .score import calculate_score
            
            score = calculate_score(difficulty, tries)
            
            print(f"正解！ {tries} 回で当たり（答え {secret}）")
            print(f"★ 獲得スコア: {score} 点 ★")
            break

        # 回数制限（limit.py）の機能：制限回数に達したらゲームオーバー
        if tries >= limit:
            print(f"\nゲームオーバー！制限回数（{limit} 回）に達しました。（答えは {secret} でした）")
            print("★ 獲得スコア: 0 点 ★")  # ゲームオーバー時はスコア0を表示
            break