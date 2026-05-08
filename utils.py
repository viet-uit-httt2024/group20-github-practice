# ============================================================
#  utils.py  –  Người D: Validate input & Format output
#  COMMIT 2: Thêm get_operator() và format_number()
# ============================================================


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


def get_operator(prompt: str) -> str:
    """
    Nhập toán tử từ bàn phím.
    Chỉ chấp nhận: +, -, *, /
    Lặp lại nếu nhập sai.
    """
    VALID_OPERATORS = {"+", "-", "*", "/"}
    while True:
        op = input(prompt).strip()
        if op in VALID_OPERATORS:
            return op
        print(f"  ⚠  Toán tử không hợp lệ! Chỉ chấp nhận: +  -  *  /\n")


def format_number(n: float) -> str:
    """
    Định dạng số để hiển thị đẹp hơn.
    - Số nguyên: 7.0  →  '7'
    - Số thực:   3.14 →  '3.14'
    """
    if n == int(n):
        return str(int(n))
    return f"{n:.4f}".rstrip("0")