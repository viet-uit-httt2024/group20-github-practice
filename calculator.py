"""
calculator.py — Logic tính toán của Máy Tính Mini
Thành viên: Thy | Branch: feature-calculator
"""

# Lịch sử phép tính (dùng chung với main.py)
lich_su_phep_tinh = []


# ──────────────────────────────────────────
# CÁC HÀM TÍNH TOÁN CƠ BẢN
# ──────────────────────────────────────────

def add(a, b):
    """Cộng hai số.
    
    Args:
        a (float): Số thứ nhất
        b (float): Số thứ hai
    Returns:
        float: Tổng a + b
    """
    return a + b


def subtract(a, b):
    """Trừ hai số.
    
    Args:
        a (float): Số bị trừ
        b (float): Số trừ
    Returns:
        float: Hiệu a - b
    """
    return a - b


def multiply(a, b):
    """Nhân hai số."""
    return a * b


def divide(a, b):
    """Chia hai số. Trả về None nếu chia cho 0."""
    if b == 0:
        print("❌ Lỗi: Không thể chia cho 0!")
        return None
    return a / b


def power(a, b):
    """Lũy thừa: a ** b."""
    return a ** b


def modulo(a, b):
    """Chia lấy dư. Trả về None nếu b = 0."""
    if b == 0:
        print("❌ Lỗi: Không thể chia lấy dư cho 0!")
        return None
    return a % b


# ──────────────────────────────────────────
# HÀM ĐIỀU PHỐI CHÍNH
# ──────────────────────────────────────────

def tinh_toan(a, phep, b):
    """Thực hiện phép tính dựa trên ký hiệu toán tử.

    Args:
        a (float): Số thứ nhất
        phep (str): Toán tử (+, -, *, /, **, %)
        b (float): Số thứ hai
    Returns:
        float | None: Kết quả, hoặc None nếu lỗi
    """
    bang_phep = {
        "+":  add,
        "-":  subtract,
        "*":  multiply,
        "/":  divide,
        "**": power,
        "%":  modulo,
    }

    ham = bang_phep.get(phep)
    if ham is None:
        print(f"❌ Phép tính '{phep}' không được hỗ trợ.")
        return None

    return ham(a, b)


# ──────────────────────────────────────────
# CHẠY THỬ ĐỘC LẬP
# ──────────────────────────────────────────

if __name__ == "__main__":
    print("=== Test calculator.py ===")
    print(f"add(3, 5)        = {add(3, 5)}")
    print(f"subtract(10, 4)  = {subtract(10, 4)}")
    print(f"multiply(6, 7)   = {multiply(6, 7)}")
    print(f"divide(9, 3)     = {divide(9, 3)}")
    print(f"divide(5, 0)     = {divide(5, 0)}")
    print(f"power(2, 8)      = {power(2, 8)}")
    print(f"modulo(10, 3)    = {modulo(10, 3)}")
    print()
    print(f"tinh_toan(10, '+', 5)  = {tinh_toan(10, '+', 5)}")
    print(f"tinh_toan(10, '-', 5)  = {tinh_toan(10, '-', 5)}")
    print(f"tinh_toan(10, '/', 0)  = {tinh_toan(10, '/', 0)}")
