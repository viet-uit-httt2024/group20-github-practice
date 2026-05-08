# Máy Tính Mini — Nhóm 20

Chương trình máy tính đơn giản chạy trên terminal, có lưu lịch sử các phép tính đã thực hiện.

---

## Thành viên nhóm

| Họ và tên | MSSV | Phân công |
|---|---|---|
| Trương Quang Việt | 24522003 | Menu chính (`main.py`) |
| Hồ Nguyễn Mai Thy | 24521759 | Xử lý tính toán (`calculator.py`) |
| Nguyễn Thành Vinh | 24522021 | Quản lý lịch sử (`history.py`) |
| Tô Đặng Minh Tuấn | 24521942 | Tiện ích & giao diện (`utils.py`) |

---

## Tính năng

### 1. Thực hiện phép tính
Hỗ trợ 4 phép tính cơ bản: cộng (`+`), trừ (`-`), nhân (`*`), chia (`/`).  
Kết quả được lưu tự động vào lịch sử sau mỗi lần tính.

### 2. Xem lịch sử
Hiển thị toàn bộ các phép tính đã thực hiện theo thứ tự thời gian,
bao gồm biểu thức và giờ thực hiện.

### 3. Tìm kiếm lịch sử
Tìm kiếm theo 3 cách:
- Theo **toán tử** (ví dụ: tìm tất cả phép cộng)
- Theo **kết quả** (ví dụ: tìm các phép tính có kết quả bằng 10)
- Theo **từ khoá** (ví dụ: tìm biểu thức có chứa số 5)

### 4. Xoá lịch sử
Xoá toàn bộ lịch sử phép tính, có xác nhận trước khi thực hiện.

---

## Cấu trúc dự án

```
group20-github-practice/
│
├── main.py          # Menu chính, vòng lặp chương trình
├── calculator.py    # Logic xử lý các phép tính
├── history.py       # Thêm, hiển thị, tìm kiếm lịch sử
├── utils.py         # Validate input, định dạng output
└── README.md
```

---

## Cách chạy chương trình

**Yêu cầu:** Python 3.10 trở lên, không cần cài thêm thư viện ngoài.

```bash
# Bước 1: Clone repository
git clone https://github.com/viet-uit-httt2024/group20-github-practice.git

# Bước 2: Di chuyển vào thư mục
cd group20-github-practice

# Bước 3: Chạy chương trình
python main.py
```

---

## Các nhánh trong dự án

| Nhánh | Người phụ trách | Nội dung |
|---|---|---|
| `main` | Cả nhóm | Nhánh chính, chứa code ổn định |
| `feature-main-menu` | Trương Quang Việt | Menu chính và vòng lặp |
| `feature-calculator` |  Hồ Nguyễn Mai Thy | Logic tính toán |
| `feature-history` | Nguyễn Thành Vinh | Quản lý lịch sử |
| `feature-utils` | Tô Đặng Minh Tuấn | Tiện ích và giao diện |

---

## Ghi chú

Dự án được thực hiện trong khuôn khổ bài tập thực hành Git & GitHub,  
môn **Nhập môn Công nghệ Phần mềm** — Trường Đại học Công nghệ Thông tin, VNU-HCM.