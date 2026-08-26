# Durum Günlüğü

> En üstteki kayıt en güncelidir. Her çalışma sonrası buraya kısa bir not düşülür.

---

## 2026-08-20 — Paketleme, JSON çıktı ve lint eklendi

- Konu: `pyproject.toml` ile pip kurulabilir hale getirildi (`pip install -e .` → `ctf-build-index` komutu), `--format json` (README'ye dokunmayan inspect modu) eklendi, ruff lint + CI'a ayrı lint job'u eklendi.
- Durum: ✅ 7/7 test geçiyor, `ruff check .` temiz, `pip install -e .` → `ctf-build-index` → `pip uninstall` uçtan uca doğrulandı.

**Sıradaki iş:** GitHub'da `CTF-Writeup-Collection` adıyla repo aç, git init + push. Gerçek writeup eklemeyi unutma.

---

## 2026-08-20 — İlk sürüm oluşturuldu

- Konu: writeup şablon sistemi + otomatik index oluşturucu (`build_index.py`) kuruldu. TEK örnek dosya (`writeups/00-example-template-walkthrough.md`) jenerik bir şablon gösterimi, gerçek bir çözülmüş oda DEĞİL — kullanıcıkendi gerçek writeup'larını `writeups/` altına ekleyip `python build_index.py` çalıştırarak index'i güncelleyebilir.
- Durum: ✅ Çalışıyor, test edildi (5/5 pytest).

**Sıradaki iş:** GitHub'da `CTF-Writeup-Collection` adıyla repo aç, git init + push. Zamanla gerçek TryHackMe/CTF writeup'ları eklenmeli (flag'ler paylaşılmadan, metodoloji odaklı).
