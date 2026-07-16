"""Hit & Blowの時間制限を管理する。"""

import queue
import threading


def get_time_limit(digits):
    """桁数に応じた制限時間を秒単位で返す。"""
    return digits * 30


def timed_input(prompt, timeout):
    """制限時間付きで入力を受け取る。

    時間内に入力された場合は文字列を返し、
    時間切れの場合はNoneを返す。
    """
    answers = queue.Queue(maxsize=1)

    def read_input():
        answer = input(prompt)
        answers.put(answer)

    input_thread = threading.Thread(
        target=read_input,
        daemon=True,
    )
    input_thread.start()

    try:
        return answers.get(timeout=timeout)
    except queue.Empty:
        return None