import os
import shutil
import glob

# Đường dẫn thư mục nguồn trên Google Drive
thu_muc_drive = r"G:\My Drive\DANHSACHPHATVIDEO\KET_QUA_JSON"
# Đường dẫn thư mục đích trong dự án của anh
thu_muc_du_an = r"E:\tu-dong-gui-thong-bao-moi"

def dong_bo_json():
    if not os.path.exists(thu_muc_drive):
        print(f"Không tìm thấy đường dẫn Google Drive: {thu_muc_drive}")
        return
    
    # Lọc tất cả các tệp .json trong thư mục Drive
    duong_dan_tim_kiem = os.path.join(thu_muc_drive, "*.json")
    danh_sach_file = glob.glob(duong_dan_tim_kiem)
    
    dem = 0
    for file_path in danh_sach_file:
        try:
            # Copy tệp vào thư mục dự án
            shutil.copy(file_path, thu_muc_du_an)
            dem += 1
        except Exception as e:
            print(f"Lỗi khi copy tệp {file_path}: {e}")
            
    print(f"Đã đồng bộ thành công {dem} tệp JSON từ Google Drive về thư mục dự án!")

if __name__ == "__main__":
    dong_bo_json()