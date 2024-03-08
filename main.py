import pygame 
import random 
pygame.init()
GENİSLİK ,YUKSEKLİK = 700, 800
pencere = pygame.display.set_mode((GENİSLİK, YUKSEKLİK))

puan = 0
HIZ = 5 

FPS = 100
saat = pygame.time.Clock()

ses_efekt3 = pygame.mixer.Sound("C:/Users/symnrr/Desktop/python_pygame_/1/money_sesi.wav")

pygame.mixer.music.load("C:/Users/symnrr/Desktop/python_pygame_/1/arka_plan.mp3")  # dosya adı 
pygame.mixer.music.play(-1,0.0)

canavar = pygame.image.load("C:/Users/symnrr/Desktop/python_pygame_/1/monster.png")
canavar_koordinat = canavar.get_rect()
canavar_koordinat.topleft = (50,50)
para = pygame.image.load("C:/Users/symnrr/Desktop/python_pygame_/1/money.png")
para_koordinat = para.get_rect()
para_koordinat.topleft= (500,500)

durum = True  
while durum: 
    for etkinlik in pygame.event.get():
        if etkinlik.type==pygame.QUIT:
            durum =False 

    tus= pygame.key.get_pressed() # Basılan tüşlari aldik 
    if tus[pygame.K_LEFT] and canavar_koordinat.left> 0:  # basılan tuş left ise ve 
                            # canavarinkoordinatinin sol kismi büyükse   0 dan 
        canavar_koordinat.x -= HIZ

    elif  tus[pygame.K_RIGHT] and canavar_koordinat.right <GENİSLİK:  # sağ kismi : genişlikten küçükse 
        canavar_koordinat.x += HIZ

    elif  tus[pygame.K_UP] and canavar_koordinat.top > 0:   # canavar koordinatin üst kismi : büyükse sıfırdan 
        canavar_koordinat.y -= HIZ

    elif  tus[pygame.K_DOWN] and canavar_koordinat.bottom < YUKSEKLİK: # bottom alt kismi 
        canavar_koordinat.y += HIZ

    # arka plan rengini süreki siyah yapalim 
    pencere.fill((0,0,0))

   
    pygame.draw.circle(pencere, (0, 0, 255),     (2000, 2150), 500, 100)  
    pygame.draw.circle(pencere, (0, 255, 0),     (1000, 950), 400, 3)  
    pygame.draw.circle(pencere, (255, 255, 0),   (500, 550), 300, 100000)  
    pygame.draw.circle(pencere, (255, 0, 0),     (100, 250), 200, 200000)  
    pygame.draw.circle(pencere, (0, 0, 255),     (50, 50), 50, 0) 
    
    # canavar_koordinatimiz. colliderect( diğer temas edeceği koordinat bilgisi )
    # iki koordinat  temas ediyorsa : TRUE olur 
    if canavar_koordinat.colliderect(para_koordinat):
        ses_efekt3.play() 
        pygame.time.delay(1000)  
        print("Parayı kaptin ")  # temas varsa # parayi aldiktan sonra koordinat değişsin
        
        para_koordinat.x = random.randint(0, GENİSLİK- 32)
        para_koordinat.y = random.randint(0, YUKSEKLİK- 32)
        puan += 1 
       
    font = pygame.font.Font(None, 36)
    text = font.render("Puan: {}".format(puan), True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (GENİSLİK / 2, YUKSEKLİK // 2)

    # ressimleri gösterebilmek için blit fonksiyonu 
    # resmin değişken adı ,  resmin koordinat bilgisi
    pencere.blit(canavar, canavar_koordinat)
    pencere.blit(para, para_koordinat)
    pencere.blit(text, text_rect) # değişkenin adı ,değişkenin konumu 
    
    
    pygame.display.update()  # sürekli pencereyi güncelle 
    saat.tick(FPS)           # fps ayarladik 

pygame.quit()




