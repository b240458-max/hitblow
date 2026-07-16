DIFFICULTIES = {
    "1": "Easy",
    "2": "Normal",
    "3": "Hard",
}

def select_difficulty():
    print("難易度を選択してください")
    print("1: Easy")
    print("2: Normal")
    print("3: Hard")

    while True:
        choice = input("選択 > ").strip()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print("1〜3を入力してください")
