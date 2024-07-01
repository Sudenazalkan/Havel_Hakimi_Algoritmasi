Bu proje Graf teorisi dersinde yapmış olduğum bir ödevdir. Amacı kullanıcı tarafından girilen derece dizisine ait grafın çizgisel olup olmadığını tespit etmek ve eğer bu derece dizisine ait graf çizgisel ise bu grafı çizdirmektir. Derece dizisinin çizgisel bir graf olup olmadığını havel hakimi algoritmasını kulanarak belirlemektedir.Havel Hakimi Algoritması aşağıdaki gibidir:
* Derece dizisi büyükten küçüğe doğru sıralanır.
* n elemanlı olan bir dizide herhangi bir eleman n-1 den büyükse program bitirilir. (Graf çizgisel değildir)
* Dizideki her terim 0 ise program bitirilir. (Graf çizgiseldir)
* Dizideki her terim negatifse program bitirilir.(Graf çizgisel değildir.)
* Dizideki terimleri her adımda büyükten küçüğe sırala 
* İlk terim olan d'yi sil geriye kalan d tane terimden 1 eksilt ve diğerlerine dokunma ve 3.adıma dön.