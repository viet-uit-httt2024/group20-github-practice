def get_number(prompt: str) -> float:
    """
    Nhập một số từ bàn phím.
    Lặp lại cho đến khi người dùng nhập đúng định dạng số.
    """
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("  ⚠  Vui lòng nhập một số hợp lệ! (ví dụ: 5, 3.14)\n")
