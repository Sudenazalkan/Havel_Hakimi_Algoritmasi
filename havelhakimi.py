import matplotlib.pyplot as plt
import networkx as nx
dizi = input("Lütfen elemanları arasında virgül bırakarak derece dizisini giriniz:")
liste = dizi.split(",")
liste = [int(eleman) for eleman in liste]
derece_dizisi = sorted(liste,reverse=True) # Girilen diziyi büyükten küçüğe sıralar.
sıfır_liste = [0]*len(derece_dizisi)
tek_sayi=[]
def havel_hakimi(liste):
    for i in derece_dizisi:
        if i > len(derece_dizisi) - 1:  # n terimli bir derece dizisinde n-1 den büyük eleman olup olmadığını kontrol eder.
            print("Derece dizisinde {}'den büyük eleman olduğu için çizgisel değildir.".format(len(derece_dizisi) - 1))
            return
        if i%2!=0: # derece dizisinde tek sayıların adedinin çift sayı olup olmadığını kontrol eder.
            tek_sayi.append(i)
    if len(tek_sayi)%2!=0:
        print("Derece dizisinde tek sayıların adedi çift olmadığından çizgisel değildir.")
        return
    while True:
        print("Derece Dizisi:", liste)
        if min(liste) < 0 or all(x == 0 for x in liste):  # Negatif eleman veya hepsi 0 ise dur
            break
        ilk_eleman = liste.pop(0)
        yeni_dizi = [i - 1 for i in liste[:ilk_eleman]] + liste[ilk_eleman:]
        liste = sorted(yeni_dizi, reverse=True)

    if min(liste) < 0:
        print("Negatif eleman bulunduğu için çizgisel değildir.")

    elif all(x == 0 for x in liste):
        print("Derece dizisinin tüm elemanları 0 dır. Dolayısıyla çizgiseldir.")


havel_hakimi(derece_dizisi)

G = nx.random_degree_sequence_graph(liste)
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', font_weight='bold')
plt.title('Derece Dizisine Ait Graf')
plt.show()