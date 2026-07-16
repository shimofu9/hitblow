def get_digits():
    while True:
        digits = input("桁数を入力してください。").strip()

        try:
            digits = int(digits)
            return digits
        except ValueError:
            print("エラー：桁数は数字で入力してください。")