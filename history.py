print("--- Lịch sử tính toán ---")
def save_history(calculation):
    print(f"Đã lưu: {calculation}")

# Danh sách lưu trữ các phép tính
history_data = []

def show_history():
        if not history_data:
            print("Lịch sử trống.")
        else:
            for i, calc in enumerate(history_data, 1):
                print(f"{i}. {calc}")
