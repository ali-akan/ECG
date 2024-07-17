### Electrocardiogram (ECG) Data Visualization 
#### Overview
This Python script enables interactive visualization of ECG data from CSV files using Plotly.
#### Installation
1.  **Install Dependencies**
    -   Ensure you have Python installed on your system.
    -   Install the required Python libraries using pip:
       `pip install pandas plotly`        
#### How to Use
1.  **Running the Script**
    -   Execute the script by running `ecg_visualizer.py` in your Python environment.
2.  **Selecting Your Data**
    -   A file dialog will open to select your ECG data CSV file.
3.  **Understanding the Plot**  
    -   The plot displays time (ms) on the x-axis and voltage (mV) on the y-axis.
4.  **Interacting with the Plot**    
    -   Use your mouse to zoom in on specific time ranges by dragging a box.
    -   Use the buttons above the plot to adjust the zoom level or reset to view the entire plot.
#### Supported Data Formats
-   Single column (Time vs. Voltage)
-   Multiple columns (Time vs. Multiple Voltages)
#### Troubleshooting Tips
-   Ensure your CSV file contains numeric time and voltage data.
-   Double-check file path and CSV format if the plot doesn't appear.
#### Example Usage
``1. Run `ecg_visualizer.py` in your Python environment.
2. Select your ECG data CSV file.
3. Explore and analyze your ECG data interactively.`` 
#### Conclusion
This script provides a user-friendly way to visualize and analyze ECG data directly from CSV files, helping to interpret cardiac signals effectively.



### Elektrokardiyogram (EKG) Veri Görselleştirme 
#### Genel Bakış
Bu Python script'i, Plotly kullanarak CSV dosyalarından EKG verilerini interaktif olarak görselleştirmenizi sağlar.
#### Kurulum
1.  **Gereksinimler**
    -   Sisteminizde Python'un yüklü olduğundan emin olun.
    -   Gerekli Python kütüphanelerini pip aracılığıyla yükleyin:
        `pip install pandas plotly`         
#### Nasıl Kullanılır
1.  **Script'i Çalıştırma**
    -   `ecg_visualizer.py` dosyasını Python ortamınızda çalıştırarak script'i başlatın.
2.  **Veri Seçimi**
    -   Dosya iletişim kutusu açılacak ve EKG verilerini içeren CSV dosyasını seçebileceksiniz.
3.  **Grafik Anlaması**
    -   Grafikte x-ekseninde zaman (ms) ve y-ekseninde gerilim (mV) değerleri görüntülenir.
4.  **Grafik İle Etkileşim**
    -   Belirli zaman aralıklarını yakınlaşmak için fareyi kullanın.
    -   Grafik üzerindeki düğmelerle zoom seviyesini ayarlayabilir veya tam görünümü görebilirsiniz.
#### Desteklenen Veri Formatları
-   Tek sütunlu (Zaman vs. Voltage)
-   Çoklu sütunlu (Zaman vs. Multiple Voltages)
#### Sorun Giderme İpuçları
-   CSV dosyanızın zaman ve gerilim verilerini içerdiğinden emin olun.
-   Grafik görünmezse, dosya yolunu ve CSV formatını kontrol edin.
#### Kullanım Örneği
``1. Python ortamınızda `ecg_visualizer.py` dosyasını çalıştırın.
2. EKG verilerinizi içeren CSV dosyasını seçin.
3. EKG verilerinizi interaktif olarak keşfedin ve analiz edin.`` 
#### Sonuç
Bu script, CSV dosyalarından EKG verilerini görselleştirme ve analiz etme sürecinizi kolaylaştırarak, kalp sinyallerini etkili bir şekilde anlamanıza yardımcı olur.
