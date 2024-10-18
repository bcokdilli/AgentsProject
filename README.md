# AI Sohbet Ajanı

Bu proje, Langgraph ve LangChain kütüphanelerini kullanarak interaktif bir AI sohbet ajanı oluşturur. Ajan, kullanıcı girişlerine yanıt verebilir ve gerektiğinde web araması yapabilir.

## Özellikler

- GPT-4 tabanlı dil modeli
- Tavily arama aracı entegrasyonu
- Bellek yönetimi için MemorySaver kullanımı
- Interaktif komut satırı arayüzü

## Gereksinimler

- Python 3.12+
- pip

## Kurulum

1. Repoyu klonlayın:

    ```bash
    git clone https://github.com/bcokdilli/AgentsProject.git
    cd agentsproject
    ```

2. Gerekli kütüphaneleri yükleyin:

    ```bash
    pip install -r requirements.txt
    ```

3. `.env` dosyasını oluşturun ve gerekli API anahtarlarını ekleyin:

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    TAVILY_API_KEY=your_tavily_api_key
    ```

## Kullanım

Projeyi çalıştırmak için:

```bash
python main.py
```

Ardından, komut isteminde mesajlarınızı girin. AI ajanı yanıt verecektir.

## Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.

## Katkıda Bulunma

Katkılarınızı memnuniyetle karşılıyoruz! Lütfen bir pull request göndermeden önce değişikliklerinizi tartışmak için bir konu açın.

## İletişim

Sorularınız için [e-posta adresiniz] adresinden bana ulaşabilirsiniz.
