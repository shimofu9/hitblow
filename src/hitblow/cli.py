"""コマンドの入口。第3回で `hitblow` コマンドがここ（main）を呼ぶ。"""

from .game import play
from .decide_digits import get_digits 

def main():
    d = get_digits()
    play(d)
