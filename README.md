# CTF Writeup Collection

![CI](https://github.com/KaanTuran28/CTF-Writeup-Collection/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

<p align="center"><b><a href="#english">English</a></b> · <b><a href="#türkçe">Türkçe</a></b></p>

---

## English

A personal, structured collection of CTF / TryHackMe / HackTheBox writeups,
with a consistent template and an auto-generated index.

## Overview

This repo is a scaffold: a writeup template, a folder for writeups, and a
small script that keeps the index table below in sync. Real writeups get
added over time as rooms/challenges are completed.

> **Note:** the entry currently in `writeups/` is a template demonstration,
> not a completed submission. Real writeups will be added here over time.

## How to add a writeup

1. Copy [`template.md`](./template.md) into `writeups/`, name it descriptively
   (e.g. `writeups/linux-privesc-basics.md`).
2. Fill in the frontmatter (`title`, `platform`, `category`, `difficulty`,
   `date`, `tools`) and the sections.
3. Run the index builder:
   ```bash
   python build_index.py
   ```
   This rewrites the table between the `INDEX` markers below.

### Installation (optional, for the `ctf-build-index` command)

```bash
pip install -e .
ctf-build-index
```

### Inspecting the data as JSON

```bash
python build_index.py --format json                # print to stdout
python build_index.py --format json --output index.json  # write to a file
```
`--format json` never touches `README.md` — it's a read-only "inspect" mode.

## Ethics / ToS Note

Many CTF platforms (including TryHackMe) discourage or forbid publishing the
literal flag value for paid/private rooms. Writeups in this repo focus on
**methodology** — recon steps, the vulnerability class, the exploitation
approach, and lessons learned — not on literal flag strings.

## Index

<!-- INDEX:START -->
| Title | Platform | Category | Difficulty | Date |
|---|---|---|---|---|
| 🧪 EXAMPLE / TEMPLATE — Practice Lab Basic Enumeration | CTF | Web | Easy | 2026-08-20 |
<!-- INDEX:END -->

## Project Structure

```
CTF-Writeup-Collection/
├── template.md              # Writeup template
├── writeups/                 # Individual writeup files
├── build_index.py            # Regenerates the index table above / prints JSON
├── pyproject.toml            # Packaging (pip install -e . → ctf-build-index)
├── tests/
│   └── test_build_index.py
├── requirements.txt
├── requirements-dev.txt
└── .github/workflows/ci.yml
```

## Testing

```bash
pip install -r requirements-dev.txt
ruff check .
pytest -v
```

## License

MIT — see [LICENSE](./LICENSE).

---

## Türkçe

CTF / TryHackMe / HackTheBox writeup'larından oluşan, tutarlı bir şablona ve
otomatik oluşturulan bir dizine (index) sahip, kişisel ve yapılandırılmış bir koleksiyon.

## Genel Bakış

Bu repo bir iskelet (scaffold): bir writeup şablonu, writeup'lar için bir klasör ve
aşağıdaki dizin tablosunu güncel tutan küçük bir betik. Odalar/challenge'lar
tamamlandıkça gerçek writeup'lar zamanla eklenir.

> **Not:** `writeups/` içinde şu anda bulunan girdi bir şablon gösterimidir,
> tamamlanmış bir gönderi değildir. Gerçek writeup'lar zamanla buraya eklenecektir.

## Bir writeup nasıl eklenir

1. [`template.md`](./template.md) dosyasını `writeups/` içine kopyalayın, açıklayıcı bir isim verin
   (örn. `writeups/linux-privesc-basics.md`).
2. Frontmatter'ı (`title`, `platform`, `category`, `difficulty`,
   `date`, `tools`) ve bölümleri doldurun.
3. Dizin oluşturucuyu çalıştırın:
   ```bash
   python build_index.py
   ```
   Bu, aşağıdaki `INDEX` işaretleyicileri arasındaki tabloyu yeniden yazar.

### Kurulum (isteğe bağlı, `ctf-build-index` komutu için)

```bash
pip install -e .
ctf-build-index
```

### Veriyi JSON olarak inceleme

```bash
python build_index.py --format json                # print to stdout
python build_index.py --format json --output index.json  # write to a file
```
`--format json`, `README.md` dosyasına asla dokunmaz — salt okunur bir "inceleme" (inspect) modudur.

## Etik / Kullanım Şartları Notu

Birçok CTF platformu (TryHackMe dahil) ücretli/özel odalar için gerçek flag değerinin
yayımlanmasını caydırır veya yasaklar. Bu repodaki writeup'lar gerçek flag dizeleri yerine
**metodolojiye** — keşif (recon) adımlarına, zafiyet sınıfına, istismar (exploitation)
yaklaşımına ve öğrenilen derslere — odaklanır.

## Dizin

Aşağıdaki dizin tablosu `build_index.py` tarafından otomatik olarak oluşturulur ve
güncellenir. Betik, `INDEX:START`/`INDEX:END` işaretleyicilerinin **tek** bir kopyasını
arayıp günceller; bu yüzden canlı tablo yalnızca yukarıdaki [English](#english) bölümünde
tutulur ve burada tekrarlanmamıştır — güncel içerik için oradaki tabloya bakın.

## Proje Yapısı

```
CTF-Writeup-Collection/
├── template.md              # Writeup template
├── writeups/                 # Individual writeup files
├── build_index.py            # Regenerates the index table above / prints JSON
├── pyproject.toml            # Packaging (pip install -e . → ctf-build-index)
├── tests/
│   └── test_build_index.py
├── requirements.txt
├── requirements-dev.txt
└── .github/workflows/ci.yml
```

## Test

```bash
pip install -r requirements-dev.txt
ruff check .
pytest -v
```

## Lisans

MIT — bkz. [LICENSE](./LICENSE).

---
