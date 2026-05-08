"""
main.py — Menu chính của Máy Tính Mini
Nhóm trưởng: Việt | Branch: feature-main-menu
"""

from calculator import (
    tinh_toan,
    lich_su_phep_tinh,
)
from history import (
    them_lich_su,
    hien_thi_lich_su,
    tim_kiem_lich_su,
)
from utils import (
    validate_so,
    format_ket_qua,
)


def hien_thi_menu():
    """In ra menu chính của chương trình."""
    print("\n" + "=" * 40)
    print("        🧮  MÁY TÍNH MINI  🧮")
    print("=" * 40)
    print("  1. Thực hiện phép tính")
    print("  2. Xem lịch sử tính toán")
    print("  3. Tìm kiếm trong lịch sử")
    print("  4. Xóa lịch sử")
    print("  0. Thoát")
    print("=" * 40)
    print("Nhập lựa chọn: ", end="")


def menu_phep_tinh():
    """Sub-menu chọn phép tính và nhập số."""
    print("\n--- PHÉP TÍNH ---")
    print("Phép tính hỗ trợ: +  -  *  /  **  %")

    a_str = input("Nhập số thứ nhất: ").strip()
    if not validate_so(a_str):
        print("❌ Số không hợp lệ!")
        return

    phep = input("Nhập phép tính (+, -, *, /, **, %): ").strip()

    b_str = input("Nhập số thứ hai: ").strip()
    if not validate_so(b_str):
        print("❌ Số không hợp lệ!")
        return

    ket_qua = tinh_toan(float(a_str), phep, float(b_str))

    if ket_qua is None:
        print("❌ Phép tính không hợp lệ (vd: chia cho 0).")
        return

    bieu_thuc = f"{a_str} {phep} {b_str}"
    print(f"\n✅ Kết quả: {format_ket_qua(bieu_thuc, ket_qua)}")

    # Lưu vào lịch sử
    them_lich_su(bieu_thuc, ket_qua)


def menu_xem_lich_su():
    """Hiển thị toàn bộ lịch sử tính toán."""
    print("\n--- LỊCH SỬ TÍNH TOÁN ---")
    hien_thi_lich_su()


def menu_tim_kiem():
    """Tìm kiếm lịch sử theo từ khóa."""
    print("\n--- TÌM KIẾM LỊCH SỬ ---")
    tu_khoa = input("Nhập từ khóa (phép tính hoặc kết quả): ").strip()
    tim_kiem_lich_su(tu_khoa)


def menu_xoa_lich_su():
    """Xóa toàn bộ lịch sử."""
    xac_nhan = input("⚠️  Bạn chắc muốn xóa toàn bộ lịch sử? (y/n): ").strip().lower()
    if xac_nhan == "y":
        lich_su_phep_tinh.clear()
        print("✅ Đã xóa lịch sử.")
    else:
        print("Đã hủy.")


def chay_chuong_trinh():
    """Vòng lặp chính của chương trình."""
    print("\nChào mừng đến với Máy Tính Mini! 👋")

    while True:
        hien_thi_menu()
        lua_chon = input().strip()

        if lua_chon == "1":
            menu_phep_tinh()
        elif lua_chon == "2":
            menu_xem_lich_su()
        elif lua_chon == "3":
            menu_tim_kiem()
        elif lua_chon == "4":
            menu_xoa_lich_su()
        elif lua_chon == "0":
            print("\n👋 Tạm biệt! Hẹn gặp lại.\n")
            break
        else:
            print("❌ Lựa chọn không hợp lệ, vui lòng thử lại.")


if __name__ == "__main__":
    chay_chuong_trinh()
