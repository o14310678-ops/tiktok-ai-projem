import time
import random
import os

try:
    from openai import OpenAI
except ImportError:
    print("🤖 Yapay Zeka: İlk kurulum yapılıyor, lütfen bekleyin...")
    os.system('pip install openai')
    from openai import OpenAI

# ⚠️ BURAYA KENDİ CHATGPT API ANAHTARINIZI YAZMALISINIZ
API_KEY = "BURAYA_CHATGPT_API_ANAHTARINIZI_YAZIN"

try:
    client = OpenAI(api_key=API_KEY)
except Exception:
    client = None

print("🤖 Yapay Zeka: Merhaba! Ben ChatGPT destekli kişisel TikTok asistanıyım.")
isim = input("🤖 Yapay Zeka: Başlamadan önce size nasıl hitap etmemi istersiniz?\n👉 Cevabınız: ")
print(f"\n🤖 Yapay Zeka: Hoş geldin {isim}! İstediğini sorabilirsin. Kapatmak için 'çıkış' yazman yeterli.\n")

while True:
    print("-" * 50)
    kullanici_mesaji = input(f"💬 {isim}: ")
    
    if kullanici_mesaji.lower() == 'çıkış':
        print(f"\n🤖 Yapay Zeka: Görüşmek üzere {isim}! Kendine iyi bak.")
        break
        
    if "takipçi" in kullanici_mesaji.lower() or "liste" in kullanici_mesaji.lower():
        print(f"\n🤖 Yapay Zeka: Güvenli takipçi listeleme modunu başlatıyorum {isim}.")
        print("🤖 Yapay Zeka: TikTok bot korumasına yakalanmamak için insansı bekleme devrede.\n")
        
        ornek_takipciler = ["kullanici_1", "kullanici_2", "kullanici_3"]
        for sira, takipci in enumerate(ornek_takipciler, 1):
            print(f"📝 [{sira}/{len(ornek_takipciler)}] Kaydedilen Profil: @{takipci}")
            
            # 5-10 saniyelik kesin güvenlik koruması
            bekleme = random.randint(5, 10)
            print(f"⏱️ Güvenlik Duraklaması: {bekleme} saniye bekleniyor...")
            time.sleep(bekleme)
            print("🔄 Sayfa aşağı kaydırıldı.\n")
            
        print("🤖 Yapay Zeka: Takipçi listeleme işlemi güvenle tamamlandı!")
        continue

    print("\n🤖 Yapay Zeka: Düşünüyorum...")
    
    if API_KEY == "BURAYA_CHATGPT_API_ANAHTARINIZI_YAZIN":
        time.sleep(1)
        print(f"🤖 Yapay Zeka: '{kullanici_mesaji}' mesajını aldım {isim}. Gerçek ChatGPT cevapları için koddaki API anahtarını girmen lazım kanka! Ama TikTok tüyosu: Akşam saatlerinde paylaşım yaparsan daha çok izlenirsin.")
    else:
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Sen samimi, arkadaş canlısı bir TikTok asistanısın. Türkçe cevap ver."},
                    {"role": "user", "content": kullanici_mesaji}
                ]
            )
            print(f"\n🤖 Yapay Zeka: {response.choices.message.content}")
        except Exception as e:
            print(f"\n🤖 Yapay Zeka: ChatGPT bağlanırken bir hata oldu: {e}")
