# ============================================================
#  utils.py  –  Người D: Validate input & Format output
#  COMMIT 3: Thêm print_header() và print_separator() cho giao diện
# ============================================================


# ── NHÓM 1: Nhập dữ liệu có validate ──────────────────────

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


def get_non_empty_string(prompt: str) -> str:
    """
    Nhập chuỗi không được để trống.
    Dùng cho tìm kiếm từ khoá.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  ⚠  Không được để trống!\n")


# ── NHÓM 2: Định dạng số ──────────────────────────────────

def format_number(n: float) -> str:
    """
    Định dạng số để hiển thị đẹp hơn.
    - Số nguyên: 7.0  →  '7'
    - Số thực:   3.14 →  '3.14'
    """
    if n == int(n):
        return str(int(n))
    return f"{n:.4f}".rstrip("0")


def format_expression(a: float, op: str, b: float, result: float) -> str:
    """
    Tạo chuỗi biểu thức hoàn chỉnh để lưu và hiển thị.
    Ví dụ: 3 + 4 = 7
    """
    return f"{format_number(a)} {op} {format_number(b)} = {format_number(result)}"


# ── NHÓM 3: Giao diện dòng lệnh ───────────────────────────

def print_separator(char: str = "─", length: int = 45) -> None:
    """In một đường kẻ ngang phân cách."""
    print(char * length)


def print_header(title: str) -> None:
    """
    In tiêu đề có viền bao quanh.
    Ví dụ:
    ═════════════════════════════════════════════
      THỰC HIỆN PHÉP TÍNH
    ═════════════════════════════════════════════
    """
    print_separator("═")
    print(f"  {title}")
    print_separator("═")