---
marp: true
---

# Przykładowy sprzęt

---

# Wyświetlacz matrycowy LED RGB z HUB75

![bg right](images/rgb-matrix-p4-64x32-wyswietlacz-matrycowy-led-rgb-64x32-4mm%20(1).jpg)
![](images/rgb-matrix-p4-64x32-wyswietlacz-matrycowy-led-rgb-64x32-4mm.jpg)

---

# Mikrokontroler Adafruit MatrixPortal M4

![bg 100% right](images/1.PNG)

---

# Czym jest framebuffer

Framebuffer (bufor ramki) - jest to obszar pamięci, który przechowuje dane o tym, co ma być wyświetlone na ekranie lub wyświetlaczu. W przypadku macierzy RGB, framebuffer przechowuje informacje o kolorach każdej diody LED (piksela) na macierzy.

---

# Jak działa framebuffer?

1. **Przechowywanie danych**: Framebuffer to tablica w pamięci, która przechowuje wartości kolorów dla każdego piksela na wyświetlaczu.

2. **Renderowanie**: Gdy program chce coś wyświetlić na ekranie, najpierw aktualizuje framebuffer, zapisując w nim nowe dane (np. kolory pikseli). Następnie dane z framebuffera są przesyłane do wyświetlacza (np. macierzy RGB), który odtwarza je na fizycznych diodach LED.

---

# Framebuffer w kontekście macierzy RGB

W przypadku macierzy RGB, framebuffer jest używany do przechowywania informacji o stanie każdej diody LED. Oto jak to działa:

- Reprezentacja macierzy: Framebuffer to tablica 2D, gdzie każdy element odpowiada jednemu pikselowi na macierzy RGB. Na przykład, dla macierzy 32x32, framebuffer będzie miał rozmiar 32x32, a każdy element będzie przechowywał wartości kolorów (np. RGB).

---

# Moduły CircuitPython przydatne do wyświetlania

---

# rgbmatrix

Niskopoziomowy moduł do połączenia się z naszym wyświetlaczem, sterownik. Transmituje dane do matrycy, czyli zapala lampki. Dokumentacja dostępna [tutaj](https://docs.circuitpython.org/en/latest/shared-bindings/rgbmatrix/).

---

# displayio

Wysokopoziomowy moduł. Pozwala nam definiować co chcemy wyświetlać. Dokumentacja dostępna [tutaj](https://docs.circuitpython.org/en/latest/shared-bindings/displayio/).

---

# framebufferio

Moduł jest pośrednikiem między displayio, a rgbmatrix. Zarządza framebufferem wyświetlacza, synchronizuje kiedy i co ma się pokazywać. Dokumentacja dostępna [tutaj](https://docs.circuitpython.org/en/latest/shared-bindings/framebufferio/index.html).

---

# Prosty przykład

examples/REPLprint