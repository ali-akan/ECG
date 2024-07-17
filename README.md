# ECG Plotter Application Documentation
## Overview

This application visualizes ECG data from a CSV file, allowing you to explore different time ranges using a double-range slider.

## Prerequisites

Ensure you have the following Python libraries installed:
-   pandas
-   matplotlib
-   tkinter
Install them using pip:
`pip install pandas matplotlib` 

## How to Use
1.  **Run the Script:**
    -   Save the provided code into a file, e.g., `ecg_plotter.py`.
    -   Run the script:
        `python ecg_plotter.py`     
2.  **Select a CSV File:**
    
    -   A file dialog will appear. Select your ECG CSV file.
    -   The CSV should contain time in the first column and voltage data in subsequent columns.
3.  **Explore the Data:**
    
    -   The ECG plot will be displayed.
    -   Use the double-range slider at the bottom to zoom in and out of specific time ranges.

## Example CSV Format

python


`time,lead1,lead2,lead3
0,0.1,0.2,0.3
1,0.2,0.3,0.4
...` 

That's it! You can now visualize and explore ECG data easily with this application.



Turkish Version;


# Elektrokardiyogram (EKG) Veri Görselleştirme
## Genel Bakış

Bu uygulama, bir CSV dosyasından alınan EKG verilerini görselleştirir ve çift aralıklı bir kaydırıcı kullanarak farklı zaman aralıklarını keşfetmenizi sağlar.
## Gereksinimler
Aşağıdaki Python kütüphanelerinin yüklü olduğundan emin olun:
-   pandas
-   matplotlib
-   tkinter
Bu kütüphaneleri yüklemek için şu komutu kullanın:
`pip install pandas matplotlib` 
## Nasıl Kullanılır
1.  **Script'i Çalıştırın:**
    -   Verilen kodu bir dosyaya kaydedin, örneğin `ecg_plotter.py`.
    -   Script'i çalıştırın:
        `python ecg_plotter.py` 
2.  **Bir CSV Dosyası Seçin:**
    -   Bir dosya seçme penceresi açılacaktır. EKG CSV dosyanızı seçin.
    -   CSV dosyası, ilk sütunda zamanı ve sonraki sütunlarda voltaj verilerini içermelidir.
3.  **Verileri Keşfedin:**
    -   EKG grafiği görüntülenecektir.
    -   Alt kısımdaki çift aralıklı kaydırıcıyı kullanarak belirli zaman aralıklarına yakınlaştırabilir veya uzaklaştırabilirsiniz.
## Örnek CSV Formatı
`time,lead1,lead2,lead3
0,0.1,0.2,0.3
1,0.2,0.3,0.4
...` 
Bu uygulama ile artık EKG verilerini kolayca görselleştirebilir ve keşfedebilirsiniz.




