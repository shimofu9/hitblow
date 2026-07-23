"""ゲームの進行（入力・表示・ループ）。

★ チームで足す機能は **自分の担当の場所**に書く（1機能=1ファイル）。
   下の「ここに足す」場所は3か所（① 開始時 ② 入力コマンド ③ 勝利時）。
   ペアごとに**別の場所**を直すので、並行作業でも衝突しない。
   import も自分の場所の近くに書くこと（ファイル先頭にまとめない＝衝突回避）。
"""

"""ゲームの進行（入力・表示・ループ）。"""

from .core import judge, make_secret

def play(digits, players=1):
    """人数に応じて1人用または2人用ゲームを開始する。"""
    if players == 1:
        play_single(digits)
    #elif players == 2:
        # play_two_players(digits)
    # else:
        # raise ValueError("playersには1または2を指定してください。")

def play_single(digits):
    secret = make_secret(digits)
    print(f"Hit & Blow（{digits}桁・重複あり）")

    # ===== ① 開始時に足す =====
    import math
    import time

    from .time_limit import get_time_limit, timed_input

    time_limit = get_time_limit(digits)
    start_time = time.monotonic()

    print(f"制限時間は{time_limit}秒です。")

    tries = 0

    while True:
        elapsed_time = time.monotonic() - start_time
        remaining_time = time_limit - elapsed_time

        if remaining_time <= 0:
            print()
            print(f"時間切れです。答えは {secret} でした。")
            return

        remaining_seconds = math.ceil(remaining_time)

        guess = timed_input(
            f"予想（残り{remaining_seconds}秒）> ",
            remaining_time,
        )

        if guess is None:
            print()
            print(f"時間切れです。答えは {secret} でした。")
            return

        guess = guess.strip()

        # ===== ② 入力コマンドに足す =====

        if len(guess) != digits or not guess.isdigit():
            print(f"{digits}桁の数字で入力してください。")
            continue

        tries += 1

        hit, blow = judge(secret, guess)
        print(f"  Hit={hit}  Blow={blow}")

        if hit == digits:
            # ===== ③ 勝利時に足す =====

            elapsed_time = time.monotonic() - start_time

            print(
                f"正解！ {tries}回で当たり"
                f"（答え {secret}・時間 {elapsed_time:.1f}秒）"
            )
            return