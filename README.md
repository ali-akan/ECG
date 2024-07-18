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
    - Selected lines can be displayed individually or together.
#### Supported Data Formats
-   Single column (Time vs. Voltage)
-   Multiple columns (Time vs. Multiple Voltages)
- Handles data where each row represents a time point and columns represent voltage leads by checking and transposing the data if necessary.
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
Bu Python script'i, CSV dosyalarından alınan EKG verilerini Plotly kullanarak etkileşimli olarak görselleştirmenizi sağlar.
#### Kurulum
1.  **Gereksinimler**
    -   Sisteminizde Python'un yüklü olduğundan emin olun.
    -   Gerekli Python kütüphanelerini pip aracılığıyla yükleyin:
        `pip install pandas plotly`         
#### Nasıl Kullanılır
1.  **Script'i Çalıştırma**
    -   `ecg_visualizer.py` dosyasını Python ortamınızda çalıştırarak script'i başlatın.
2.  **Veri Seçimi**
    -   EKG verilerinizin bulunduğu CSV dosyasını seçmek için bir dosya iletişim kutusu açılacaktır.
3.  **Grafik Anlama**
    -   Grafik, x-ekseninde zaman (ms) ve y-ekseninde voltaj (mV) olarak gösterilir.
4.  **Grafik İle Etkileşim**
    -   Belirli zaman aralıklarını yakınlaşmak için fareyi kullanın.
    -   Grafik üzerindeki düğmelerle zoom seviyesini ayarlayabilir veya tam görünümü görebilirsiniz.
    - Seçilen çizgiler tek tek veya birlikte görüntülenebilir.

#### Desteklenen Veri Formatları
-   Tek sütunlu (Zaman vs. Voltaj)
-   Çoklu sütunlu (Zaman vs. Çeşitli Voltajlar)
#### Sorun Giderme İpuçları
-   CSV dosyanızın zaman ve voltaj  verilerini içerdiğinden emin olun.
-   Grafik görünmezse, dosya yolunu ve CSV formatını kontrol edin.
#### Kullanım Örneği
``1. Python ortamınızda `ecg_visualizer.py` dosyasını çalıştırın.
2. EKG verilerinizi içeren CSV dosyasını seçin.
3. EKG verilerinizi interaktif olarak keşfedin ve analiz edin.`` 
#### Sonuç
Bu script, CSV dosyalarından EKG verilerini görselleştirme ve analiz etme sürecinizi kolaylaştırarak, kalp sinyallerini etkili bir şekilde anlamanıza yardımcı olur.
