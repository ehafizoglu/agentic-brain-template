# 🧠 Agentic Brain Framework (ABF) - Türkçe Kullanım Kılavuzu

* 🇬🇧 [Click here for English User Guide](README.md)

Yapay Zeka Ajanları (Claude Code, Cursor, ChatGPT, Claude) ile iletişimi optimize etmek, bağlam penceresini (context window) verimli kullanmak ve test odaklı, disiplinli bir mühendislik yapısı kurarak "vibe coding" (rastgele kodlama) sorununu önlemek için tasarlanmış Obsidian uyumlu şablon ve klasör yapısı.

---

## 🚀 Hızlı Başlangıç (Quick Start)

### Adım 1: Klasörü Kopyalayın
Bu şablon deposunu yerel bilgisayarınıza klonlayın:
```bash
git clone https://github.com/ehafizoglu/agentic-brain-template.git yeni-projem
cd yeni-projem
```

### Adım 2: Projeyi Başlatın (Initialize)
Yeni projeyi yapılandırmak, şablonlardaki değişkenleri güncellemek ve eski git geçmişini sıfırlamak için başlatıcı betiği çalıştırın:
```bash
python scripts/init_project.py
```
*Bu betik size **Proje Adı** ve **Geliştirici İsmini** soracak, ilgili şablonlardaki yer tutucuları güncelleyecek, eski git geçmişini temizleyecek ve ilk AI bağlamınızı (context) derleyecektir.*

### Adım 3: Obsidian'da Açın (Open in Obsidian)
**Obsidian** uygulamasını açın, **"Open folder as vault"** seçeneğine tıklayın ve projenizdeki `docs` klasörünü seçin. Bu sayede sadece dokümanları göreceğiniz, kod kalabalığından uzak, temiz bir çalışma alanınız olur.

---

## 🤖 Diğer Yapay Zekalara Bağlam Aktarma (Tek Kalemde)

Eğer ChatGPT, Claude Web veya başka bir yapay zeka arayüzünü kullanıyorsanız ve projeyi tek bir seferde yapay zekaya öğretmek istiyorsanız derleme betiğini çalıştırın:

```bash
python scripts/bundle_ai_context.py
```

Bu komut; global kural setinizi, aktif görevleri, iş analizlerini, veri şemalarını ve test planlarını tarayarak proje kök dizininde tek bir dosya oluşturur: **`ai_context_merged.md`**.
Oluşan bu dosyayı yapay zekanın mesaj kutusuna sürükleyip bırakmanız yeterlidir.

---

## 📁 Klasör Yapısı

```
├── CLAUDE.md                         # Global AI Kuralları ve Komutları (Matt Pocock Stili)
├── .cursorrules                      # Cursor/Windsurf editör yapay zekası kuralları
├── docs/                             # Obsidian Dokümantasyon Kasası (Vault)
│   ├── 00_Core/
│   │   ├── Project_Hub.md            # Ana Bağlantı Haritası (MOC Dashboard)
│   │   └── ADRs/                     # Mimari Karar Defteri (ADR Ledger)
│   ├── 01_Analyst/
│   │   └── business_requirements.md  # Kapsam, Moscow Öncelikleri, Kullanıcı Hikayeleri
│   ├── 02_Architect/
│   │   ├── system_architecture.md    # Teknoloji Seçimleri, DB (Mermaid), API taslakları
│   │   ├── security_guidelines.md    # OWASP & CWE güvenli kodlama yönergeleri
│   │   ├── design_principles.md      # SOLID, DRY/KISS, temiz kod standartları
│   │   └── engineering_principles.md # Hata middleware'i, trace-id loglama, önbellekleme
│   ├── 03_Developer/
│   │   ├── development_guide.md      # Standartlar, Setup, İsimlendirme Kuralları
│   │   └── task_board.md             # Aktif İş Takip Tahtası (Kanban)
│   ├── 04_Tester/
│   │   └── test_plan.md              # Gherkin Testleri, QA Stratejisi, Bug Log
│   ├── 05_Memory/
│   │   ├── lessons_learned.md        # Çözülen zor hatalar, platform ve kütüphane ipuçları
│   │   └── active_context.md         # O anki çalışma odağının özet kartı
│   ├── 06_Product_Manager/
│   │   ├── product_strategy.md       # Pazar uyumu, UVP, rakip analizi
│   │   └── product_roadmap.md        # Miltaşları, yayınlama kontrol listesi, KPI'lar
│   ├── 07_DevOps/
│   │   └── deployment_guide.md       # Docker kurulumu, CI/CD boru hattı ayarları
│   └── 08_UI_UX/
│       └── design_system.md          # Renkler (HSL), tipografi kuralları, CSS tokenları
├── scripts/
│   ├── init_project.py               # Proje kurulum başlatıcısı
│   └── bundle_ai_context.py          # AI bağlam derleme betiği
└── src/                              # Proje kaynak kodları klasörü
```

---

## ❌ Anti-Vibe-Coding Kuralları

Disiplinli yazılım mühendisliğini korumak amacıyla `CLAUDE.md` içerisinde şu bilişsel kurallar zorunlu kılınmıştır:

1.  **Netleştirme Aşaması (Clarification)**: Eğer iş isterlerinde en ufak bir belirsizlik varsa, yapay zeka kod yazmaya başlamadan önce **en az 2 net soru sormak zorundadır**.
2.  **Önce Test (TDD-Lite)**: Yapay zeka, kod değişikliğini yapmadan önce test senaryolarını `test_plan.md` dosyasına işlemelidir.
3.  **Yarım Kod Yazmama**: Kod yapısında `// TODO: sonra yapılacak` şeklinde geçici veya eksik kod blokları bırakılması **kesinlikle yasaktır**. Üretilen tüm kodlar çalışır durumda olmalıdır.
4.  **Hafıza Kaydı (Lessons Learned)**: Keşfedilen kritik buglar, platform uyumsuzlukları ve nedenleri `lessons_learned.md` dosyasına kaydedilmelidir ki yapay zeka tekrar eden hatalara düşmesin.
