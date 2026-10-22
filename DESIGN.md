# 個人專屬用藥卡 — Design brief for Jessie
**Audience:** family caregivers (60+) · **Format:** A4 portrait printable + phone-readable · **Language:** Traditional Chinese (HK) · **Date on card:** 2026年10月20日  
**Reference:** keep the same section order & colour-block structure as Meta AI share.  
**Screenshots:** `/workspace/med-card-01-*.png` … `03-*.png` and copies under `assets/` if present.

Designer: Celine · Implementer: Jessie · Content must not invent doses — use REFERENCE.md + this brief.

---

## 1. Goals (senior-friendly)
| Do | Don’t |
|---|---|
| Real product photos (pack or blister) | CSS-drawn fake pills |
| Chinese common name **above** Latin brand/generic | Latin-only titles |
| Body ≥18px, titles ≥28px, dose badge ≥22px bold | 12–15px body |
| Dose “**1 粒**” as large dark chip on white | Tiny grey 1 粒 boxes |
| Checkbox row「飯後已服」per meal block | Tiny “記得記錄” only in subtitle |
| Critical rules (空腹 / 禁西柚 / 每日最多) in **bold red** or amber callout | Buried in grey subtext |
| One column on phone; PRN stacks | Dense 2-col PRN on narrow screens |
| Tap targets ≥48×48px if interactive | Tiny chips |

---

## 2. Page chrome
- **Canvas:** `#F7F3EF` full bleed  
- **Card:** white `#FFFFFF`, max-width **840px** (A4 content width ~190mm), `border-radius: 24px`, soft shadow `0 8px 32px rgba(30,42,80,0.08)`, horizontal padding **28–32px**, vertical **32px**  
- **Skip** Meta AI top strip (“A4 列印比例…”). Our build starts at the navy badge.  
- **Font stack:** `"Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif`  
- **Print:** `@page { size: A4; margin: 12mm; }` — card fills printable area; avoid cutting bedtime navy block across pages if possible (`break-inside: avoid` on each time block).

---

## 3. Colour tokens
| Token | Hex | Use |
|---|---|---|
| `navy` | `#1E2A50` | Titles, bedtime block bg, primary text |
| `navy-soft` | `#2A3A6A` | Bedtime inner |
| `text` | `#1A1A1A` | Body (never grey below `#4A4A4A` for readable copy) |
| `muted` | `#5A5A5A` | Secondary only; **not** for doses or warnings |
| `peach` | `#FFF0E6` / border `#F0A070` | Morning block |
| `blue` | `#E8F2FC` / border `#5B9BD5` | Evening block |
| `navy-block` | `#1E2A50` | Bedtime wrapper (white cards inside) |
| `green` | `#E8F6EE` / accent `#2E8B57` | PRN oral |
| `pink` | `#FCEEF2` / accent `#C45B7A` | Topical |
| `amber` | `#FFF8E6` / border `#E8B84A` | Warnings section |
| `danger` | `#C62828` | 空腹必須、禁西柚、每日最多 |
| `course` | `#D32F2F` | 「療程藥」「完成療程」pills |
| `dose-chip-bg` | `#1E2A50` | Dose badge bg |
| `dose-chip-fg` | `#FFFFFF` | Dose badge text |
| `checkbox` | `#1E2A50` border 2px | 「已服」boxes |

---

## 4. Type scale (CSS rem base 16px)
| Role | Size | Weight | Colour |
|---|---|---|---|
| H1 全天服用與使用時間表 | **32–36px** | 700 | navy |
| H2 完整服藥卡 | **22px** | 600 | navy |
| Section time label (早上／晚餐後／睡前) | **24px** | 700 | matching section |
| Time chip (08:00–09:00) | **18px** | 700 | white on accent |
| Med Chinese name | **22px** | 700 | text |
| Med Latin / strength | **16px** | 500 | muted OK |
| Purpose line (護胃藥 · …) | **18px** | 400 | text |
| Dose chip「1 粒 口服」 | **22px** | 700 | white on navy |
| Warning card title | **20px** | 700 | navy |
| Warning body | **18px** | 400 | text; key phrases **danger** |
| Footer | **14px** | 400 | muted (ok for legal) |
| Checkbox label「飯後已服」 | **18px** | 600 | text |

Line-height: titles 1.25 · body 1.45 · never cramped.

---

## 5. Section layout (same order as reference)

### 5.1 Header
```
[ navy pill badge: shield + 個人專屬用藥卡 ]

全天服用與使用時間表          [ white tile ]
完整服藥卡                      🕐 每日準時
請按時服用，完成療程            2026年10月20日
```
- Badge: navy fill, white 14–15px (exception: badge can be smaller).  
- Subtitle instruction stays, but **primary logging** moves to checkboxes in each meal block.  
- Date tile: min 88×88px, clock icon orange `#E67E22`, label 16px bold, date 15px.

### 5.2 Timeline blocks (morning → evening → bedtime)
Each block:
1. **Header row:** icon + time name + time chip (+ bedtime amber chip「晚餐後至少2小時」)  
2. **Checkbox row:** □ 飯後已服（今日） — 48px box, label 18px (bedtime: □ 睡前已服（空腹）)  
3. **Med rows** stacked full-width

**Med row (desktop/print ≥640px):**
```
┌─────────────────────────────────────────────────────────┐
│ [PHOTO 96×96]  中文俗名                    [1 粒 口服] │
│                Brand 40mg · 用途短句                      │
│                [optional tag: 療程藥]                     │
└─────────────────────────────────────────────────────────┘
```
- Photo: **96×96px** (print) / **80×80** phone; `object-fit: contain`; white bg; 12px radius; 1px `#E0E0E0` border.  
- Row min-height **112px**; padding 16px; gap 16px.  
- Tags「療程藥」「完成療程」: red filled pill, white 14px bold, left of dose or under name.

**Phone (<640px):** photo left 72×72; dose chip full-width under purpose line (still ≥44px tall).

### 5.3 Morning (peach)
5 meds — see photo slot table.

### 5.4 Evening (blue)
2 meds — Augmentin + DAFLON.

### 5.5 Bedtime (navy wrapper, white inner cards)
- Outer navy padding 20px; white med cards inside.  
- Entecavir purpose line: keep「必須空腹」in **danger** bold.  
- Simvastatin:「禁西柚」in **danger** bold.  
- Footnote bar (amber on navy or light amber strip):  
  **空腹定義：飯後 2 小時以上，服藥後 1 小時內勿進食** — 18px, high contrast.

### 5.6 PRN + topical
- Section title 22px bold.  
- **Mobile:** stack — 口服 first, then 外用 (not side-by-side).  
- **Print / wide:** 2 columns OK if each column has ≥18px type and photos ≥72px; increase row padding to 14px.  
- Each PRN row: photo + **trigger** in bold (疼痛時 / 頭暈時 / …) + max dose in **danger** + secondary instruction.  
- Extra Amlodipine: show **SBP ≥ 140** as large chip (not tiny).

### 5.7 Warnings (3 amber cards)
Keep 3 cards. Make red emphasis phrases larger (18–20px). Icons OK (moon / grapefruit / shield) but text must stand alone without colour-only meaning.

### 5.8 Footer
Disclaimer +「建議貼於雪櫃門或藥箱旁」+ small「長者大字版 · 高對比設計」. Not critical for seniors’ reading of doses.

---

## 6. Medicine copy + photo slots
**Path convention:** `assets/meds/<slug>.jpg` (or `.png`). Jessie ships with placeholder grey frames + slug filename; Justin/Celine drop real pack photos later.

| Slot | Slug | Chinese (display first) | Latin / product | Dose chip | Notes |
|---|---|---|---|---|---|
| AM1 | `pantoprazole-40` | 護胃藥（泮托拉唑） | Pantoprazole 40mg | 1 粒 口服 | 保護胃黏膜 |
| AM2 | `augmentin-1g` | 安滅菌（抗生素） | Augmentin 1g | 1 粒 口服 | tag 療程藥 · 服至第4天完結 |
| AM3 | `daflon-500` | 達芙琳 | DAFLON 500mg | 1 粒 口服 | 改善下肢循環 |
| AM4 | `osimertinib-80` | 標靶藥（奧希替尼） | Osimertinib 80mg | 1 粒 口服 | 每日固定時間 |
| AM5 | `amlodipine-2-5` | 降血壓藥（氨氯地平） | Amlodipine 2.5mg | 1 粒 口服 | |
| PM1 | `augmentin-1g` | 安滅菌（抗生素） | Augmentin 1g | 1 粒 | tag 完成療程 · 每天第2次 — **reuse same photo** |
| PM2 | `daflon-500` | 達芙琳 | DAFLON 500mg | 1 粒 | 每天第2次 — reuse photo |
| NT1 | `entecavir-0-5` | 抗乙肝藥（恩替卡韋） | Entecavir 0.5mg | 1 粒 | **必須空腹** |
| NT2 | `simvastatin-5` | 降膽固醇（辛伐他汀） | Simvastatin 5mg | 1 粒 | **禁西柚** |
| PRN1 | `diclofenac-100` | 止痛藥（服他寧） | Diclofenac / Voltaren 100mg | 疼痛時 · 每日最多1粒 | 必須飯後 |
| PRN2 | `betahistine-6` | 止暈藥（倍他司汀） | Betahistine 6mg | 頭暈時 · 每日最多3次 | 飯後 |
| PRN3 | `loperamide-2` | 止瀉藥 | Loperamide 2mg | 腹瀉時 · 每日最多3次 | |
| PRN4 | `amlodipine-2-5` | 降血壓藥（加服） | Amlodipine 2.5mg | SBP≥140 · 當日最多多1粒 | reuse photo；總共5mg |
| TOP1 | `difflam-mouthwash` | 特快靈漱口水 | DIFFLAM | 每日4次 · 每次15ml | 含漱後吐出 |
| TOP2 | `kenalog-paste` | 康寧樂口腔膏 | KENALOG Dental Paste | 每日3次 按需要 | 飯後及睡前 |
| TOP3 | `urea-10` | 尿素霜 10% | Urea cream 10% | 每日2次 | 塗小腿 |

Photo guidance for whoever shoots/finds images:
- Prefer **clear HK pack front** or blister strip; white/neutral background; crop square; no other meds in frame.  
- Same product reused in AM/PM/PRN → **one file**, referenced twice.

---

## 7. Component specs (quick CSS mental model)
- `.med-row` flex; gap 16px; align center  
- `.med-photo` 96×96; flex-shrink 0  
- `.dose-chip` padding 8px 14px; border-radius 10px; bg navy; color white; font 22px/700  
- `.tag-course` bg `#D32F2F`; color white; padding 4px 10px; border-radius 999px  
- `.check-row` margin-bottom 12px; display flex; align center; gap 12px  
- `.check-box` width/height 48px; border 2.5px solid navy; border-radius 8px  
- Time blocks: `break-inside: avoid` for print  

Interactive (optional for screen): checkbox can be real `<input type="checkbox">` — print CSS can hide checked state or show empty boxes for pen.

---

## 8. Out of scope for Jessie
- Do not change doses, times, or medical wording beyond layout/emphasis and the Chinese display names in the table (Justin can correct names).  
- Do not add new medicines.  
- Design approval: Justin via Sua; Celine can tweak tokens if screenshots of the build look off.

---

## 9. Acceptance checklist
- [ ] Same section order as reference  
- [ ] All 16 slots use `<img>` (placeholder OK until real files)  
- [ ] Chinese name first on every med row  
- [ ] Type scale meets §4  
- [ ] Dose chips navy-on-white, ≥22px  
- [ ] Meal checkboxes present  
- [ ] 空腹 / 禁西柚 / 每日最多 visually loud  
- [ ] PRN stacks on mobile  
- [ ] Prints cleanly on A4  
