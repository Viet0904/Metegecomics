import pandas as pd

# Đọc file Gốc
file_goc_path = "data/wt2dphy_x.csv"  # Đường dẫn tới file Gốc
df_goc = pd.read_csv(file_goc_path)

# Đọc file chứa vị trí dòng các đặc trưng
file_dac_trung_path = (
    "data/lime_output_mean.csv"  # Đường dẫn tới file chứa các dòng đặc trưng
)
df_dac_trung = pd.read_csv(file_dac_trung_path, header=None)

# Lấy cột đầu tiên chứa vị trí các dòng (bỏ qua header nếu có)
feature_rows = df_dac_trung.iloc[:, 0].tolist()

# Lọc các giá trị không phải là số nguyên
feature_rows = [row for row in feature_rows if str(row).isdigit()]

# Tăng vị trí dòng lên 2 như yêu cầu
adjusted_rows = [int(row) + 1 for row in feature_rows]

# Kiểm tra và điều chỉnh header
header = df_goc.columns.tolist()
if header[0] == "Unnamed: 0":
    header[0] = ""

# Lặp qua các mức top 10, 20, 30,..., 100
for top in range(10, 101, 10):
    # Lấy các dòng tương ứng từ file Gốc
    selected_rows = adjusted_rows[:top]
    extracted_features = df_goc.iloc[selected_rows, :]

    # Xuất file CSV với header từ file gốc
    output_path = f"data/top_{top}_features_x.csv"
    extracted_features.to_csv(output_path, index=False, header=header)
    print(f"Tập top {top} đã được lưu vào file: {output_path}")
