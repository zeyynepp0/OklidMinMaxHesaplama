import math

# Noktaların tanımlanması ve kullanıcı girişi
points = []
n = int(input("Kaç tane nokta gireceksiniz? "))

for i in range(n):
    x = float(input(f"Nokta {i+1} x koordinatı: "))
    y = float(input(f"Nokta {i+1} y koordinatı: "))
    points.append((x, y))

# Öklid mesafesi için fonksiyon tanımlama
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Mesafelerin hesaplanması ve minimum mesafenin bulunması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

min_distance = min(distances)

# Sonucun yazdırılması
print("Girilen noktalar arasında Öklid mesafesi en küçük olan mesafe:", min_distance)
