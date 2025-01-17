from PIL import Image
import os

def validate_image(file_path, allowed_types=["png"], max_size_mb=3):
    try:
        # Validasi ukuran file
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)  # Konversi ke MB
        if file_size_mb > max_size_mb:
            return False, f"Ukuran file terlalu besar: {file_size_mb:.2f} MB. Maksimum {max_size_mb} MB."
        
        # Validasi format file
        with Image.open(file_path) as img:
            file_format = img.format.lower()
            if file_format not in allowed_types:
                return False, f"Tipe file tidak valid: {file_format}. Hanya diperbolehkan: {', '.join(allowed_types)}."
        
        # Jika validasi berhasil
        return True, "Gambar valid."
    except Exception as e:
        return False, f"Gagal memvalidasi gambar: {e}"