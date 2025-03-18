import pandas as pd
import os

def process_rainfall(csv_path):
    # CSV dosyasını oku
    df = pd.read_csv(csv_path)
    
    # "rainfall" sütununu tabana yuvarlayarak 2 ondalık haneye indir
    df["rainfall"] = df["rainfall"].apply(lambda x: round(x, 2))
    
    # Yeni dosya adı oluştur
    base_name = os.path.basename(csv_path)
    dir_name = os.path.dirname(csv_path)
    new_file_name = f"processed_{base_name}"
    new_file_path = os.path.join(dir_name, new_file_name)
    
    # Yeni CSV dosyasını kaydet
    df.to_csv(new_file_path, index=False)
    print(f"Processed file saved as: {new_file_path}")

# Örnek kullanım
csv_path = r"C:\Users\lerha\OneDrive\Masaüstü\kaggle-taban-tavan\v2random-forest-submission.csv"  # Senin dosyanın yolu
process_rainfall(csv_path)
