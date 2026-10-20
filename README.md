# 個人專屬用藥卡 (Parents med card)

Printable / phone-friendly full-day medicine schedule for family caregivers (Traditional Chinese, senior-friendly).

**Live site:** https://justinksw.github.io/parents-med-card/

## Open locally

Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8080 --directory .
```

## Photos (2026-10-20)

Pack + blister / bottle photos are in `assets/meds/`. Sources and licenses: **`IMAGE-SOURCES.md`**.

- **Exact brand now:** DAFLON 500, DIFFLAM mouthwash, Kenalog in Orabase.
- **Strength-correct but brand may differ (on-page「示意」):** pantoprazole (GASPAIN-40), amlodipine (Amlip-2.5), urea (Flexitol 10%).
- **Still prefer household packs:** Tagrisso / 奧希替尼 (box-only web photo), entecavir, simvastatin, plus any brand that differs from the HK shelf pack.

Drop household pack photos into `assets/meds/` using the same slug filenames — `index.html` does not need edits. `augmentin-1g`, `daflon-500`, and `amlodipine-2-5` are each one file referenced twice.

## Privacy note

GitHub Pages sites are **public on the internet**. Do not add patient names or ID numbers to this repo.

## Credits

Design: Celine · Implementation: Jessie · Content from family prescription card (doses must not be changed without clinician guidance).  
Photo sources and licenses: `IMAGE-SOURCES.md`.
