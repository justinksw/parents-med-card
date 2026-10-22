# Medicine card — reference capture
Source: https://www.meta.ai/share/a/f40a6af6-e944-4bae-b57c-a5becc38f8d9
Captured: 2026-10-20 (Asia/Hong_Kong)
Status: first draft ready — open index.html (see README.md)

## Goal
Static printable A4 medicine schedule for family caregivers (60+).
Same structure/layout as Meta AI poster. Replace CSS fake pills with REAL medicine photos.
Large text, high contrast, big tap targets. Traditional Chinese labels (match reference).

## Layout (top → bottom)
1. Meta strip (skip in our build): A4 列印比例 · 長者友善大字版 · 高對比 | 可直接截圖保存
2. Hero: badge 個人專屬用藥卡; H1 全天服用與使用時間表 / 完整服藥卡; 請按時服用，完成療程 · 飯後記得記錄; date card 每日準時 + date
3. Morning block 早上 早餐後 08:00-09:00 (peach) — 5 meds
4. Dinner block 晚餐後 18:30-19:30 (pale blue) — 2 meds
5. Bedtime block 睡前 空腹 22:30 (dark navy) — 2 meds + footnote
6. PRN section 按需要（PRN）及外用藥物時間表 — 2 cols: 口服 按需要 | 外用 每日固定
7. Warnings 重要注意事項 · 藥物相互作用 — 3 amber cards
8. Footer disclaimer

## Medicine slots (16) — need real photos
### 早上 早餐後
- Pantoprazole 40mg · 1 粒 口服 · 護胃藥 · 保護胃黏膜
- Augmentin 1g · 1 粒 口服 · 療程藥 · 抗生素 · 只需服至第4天療程完結
- DAFLON 500mg · 1 粒 口服 · 靜脈活性 · 改善下肢血液循環
- Osimertinib 80mg · 1 粒 口服 · 標靶藥 · 每日固定時間服
- Amlodipine 2.5mg · 1 粒 口服 · 降血壓 · 常規降血壓藥

### 晚餐後
- Augmentin 1g · 1 粒 · 完成療程 · 抗生素 · 每天第2次
- DAFLON 500mg · 1 粒 · 靜脈活性 · 每天第2次

### 睡前 空腹 (晚餐後至少2小時)
- Entecavir 0.5mg · 1 粒 · 抗乙肝藥 · 必須空腹
- Simvastatin 5mg · 1 粒 · 降膽固醇 · 晚間服效佳，禁西柚
- Footnote: 空腹定義：飯後2小時以上，服藥後1小時內勿進食

### PRN 口服
- Diclofenac (Voltaren) 100mg · 疼痛時，每日最多1粒 · 必須飯後立即服
- Betahistine 6mg · 頭暈時，每日最多3次 · 止暈藥，飯後服
- Loperamide 2mg · 腹瀉時，每日最多3次 · 止瀉藥
- Amlodipine 2.5mg（加服） · SBP ≥140時 · 當天可多服1粒，總共5mg

### 外用
- DIFFLAM Mouthwash · 每日4次 QID · 每次15ml · 含漱後吐出
- KENALOG Dental Paste · 每日3次 TDS 按需要 · 飯後及睡前抹乾患處
- Urea cream 10% · 每日2次 BD · 塗抹於小腿皮膚

## Warnings (3)
1. Entecavir 空腹嚴格要求
2. Simvastatin 禁西柚
3. 護胃與抗生素 (Diclofenac + Pantoprazole; Augmentin 完成療程)

## Image plan
Reference used CSS shapes only (0 photos). Our build: `/assets/meds/<slug>.jpg` placeholders; Celine/Justin swap real photos.
Screenshots of reference:
- top: assets/7073a271009d8f53f68484069ad792cada0788383e4eda547f07564b17115cc2.png
- dinner/bed/prn: assets/23a67363597d0fc70209bf34560dd96092a9696a4a5d91bbbaa8582b465e99df.png
- warnings: assets/b891c8e61086d5d4e936a3425389d3a0617f5f4df45fb161b6ccdb53153d5064.png
