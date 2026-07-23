"""1人用・2人用のゲームモードを選択する。"""


def get_game_mode():
    """遊ぶ人数を1または2で受け取る。"""
    while True:
        mode = input(
            "遊ぶ人数を選んでください（1: 1人 / 2: 2人）> "
        ).strip()

        if mode in {"1", "2"}:
            return int(mode)

        print("エラー：1または2を入力してください。")