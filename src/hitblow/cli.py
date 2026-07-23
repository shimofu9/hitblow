"""コマンドの入口。第3回で `hitblow` コマンドがここ（main）を呼ぶ。"""

from .decide_digits import get_digits
from .decide_mode import get_game_mode
from .game import play


def main():
    """ゲームモードと桁数を受け取り、ゲームを開始する。"""
    players = get_game_mode()
    digits = get_digits()
    play(digits, players)