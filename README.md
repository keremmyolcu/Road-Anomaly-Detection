# Road-Anomaly-Detection
Çok Disiplinli Tasarım Projesi dahilinde gerçekleştirdiğim bilgisayarlı görü ile otoyolda oluşabilecek bazı anomalilerin tespitini yapan sistem.
Client tarafında CSI modülüne takılı PiCamera ve ekstra olarak bir adet LCD ekran bağlı bulunan Raspberry Pi 1 Model B; server tarafında ise kişisel bilgisayar yer almaktadır. İki cihaz temel soket programlama protokolleri üzerinden haberleşmektedir. Raspberry Pi'ın temel görevi elde ettiği frame'leri server'a göndermek ve server'dan gelebilecek anomali tespiti mesajını kendisine bağlı bulunan LCD ekrana bastırmaktır.  
  
Server Raspberry'den kendisine gelen frame'leri işleyerek offset değerinden büyük alana sahip konturları tespit eder, konturları dikdörtgen içerisine alır ve merkeze bir adet centroid yerleştirir. Bu centroid noktası yol sınırı olarak belirlenmiş çizgilere bir threshold değerinden daha yakınsa arabanın bu sınırı aştığını ve yoldan çıkma, karşı şeride geçme veya yol dışından yol sınırlarına yabancı bir cisim girişi olduğunu varsayarak client'a mesaj gönderir. Yol sınırları önceden belirlenmiş çizgilerdir. burada mesafe hesaplanması için yola uygun çizgilere ait doğru denklemleri ve centroidlerin yol çizgilerine uzaklığını hesaplamak için noktanın doğruya olan uzaklığı denklemleri kullanılmıştır, tracker.py dosyası üzerinden görülebilir.  
  
  
Proje videosu:
https://www.youtube.com/watch?v=XTt2fyTGs5I
