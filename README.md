# Affine Encryption
- Bu şifreleme algoritması hangi karakterin yerine hangi karakterin konulacağı ile ilgilidir.
- Şifleme yapıldıktan sonra aynı anahtar değeri ile deşifreleme yapılmaktadır.
- Anahtar değeri (a,b) şeklinde verilir.
- Bu şifreleme yöntemi y = ax+b olarak doğrunun denklemini baz alır.
- Algoritmanın çalışabilmesi için "a" ile "n" değeri mutlaka aralarında asal olarak seçilmelidir.
- Şifreleme için E(x) = (ax+b) mod n işlemi uygulanır.
- Deşifreleme için D(x) = z(y-b) mod n işlemi uygulanır.
- z değeri a'nın mod n ye göre tersidir. Yani a*z mod 29 = 1 denklemi ile z değeri bulunur.

# Uygulanması

## Şifreleme
- Girilen metin tek tek karakterlerine ayrılır.
- Her karakterin alfabedeki konumunun sayısal değeri alınır.(Örneğin Türkçe alfabe için 0-28 aralığı)
- Her değer için E(x) = (ax+b) mod n işlemi uygulanır ve sonuç diziye alınır.
- Sonuçların alfabedeki karşılıkları bulunarak şifreli metin oluşturulur.

## Deşifreleme
- Şifreli metin tek tek karakterlerine ayrılırç
- Her karakterin alfabedeki konumunun sayısal değeri alınır.
- a.z mod 29 = 1 değeri için uygun z değeri bulunur.
- Her değer için D(x) = z(y-b) mod n işlemi uygulanır ve sonuçlar diziye alınır.
- Her sonucun alfabedeki karşılıkları bulunarak şifreli metin çözülür.


