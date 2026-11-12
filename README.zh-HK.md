# 星連VPN開源與技術研究

[English](README.md) · [简体中文](README.zh-CN.md) · 繁體中文

<p align="center">
  <img src="assets/images/singlinkvpn-open-source-plan.zh-HK.webp" alt="星連VPN開源計劃：開源，是建立長期信任的開始" width="520">
</p>

這是星連VPN官方開源與技術研究儲存庫，用於持續發佈公開文件、可重現研究方法、安全與私隱資料、效能測試格式、數據集及部分開源工具。

> **第二階段（2026-11-12）：開放協議與初代原型App已開源。** 經過安全、私隱及授權審查，SingLinkLabs 以兩個獨立儲存庫（Apache-2.0）發佈了第一批產品原始碼（見下表）。本儲存庫繼續發佈文件、研究數據及工具。星連VPN正式App、伺服器端、付款、節點及 SingLink 2.0 核心協議仍不公開。

## 開源程式碼（第二階段）

| 儲存庫 | 內容 | 狀態 |
| --- | --- | --- |
| [singlink-protocol](https://github.com/SingLinkLabs/singlink-protocol) | SingLink開源協議（`SingLink/1`）：以 Go 從零編寫的開放代理／VPN協議。簽章並綁定裝置的權限通行證、內層端對端加密、X25519 + ML-KEM-768 混合抗量子金鑰交換、防重放及防主動探測。 | 1.0 草案 · 已完成內部安全審計（31 項，高、中風險全部修正）· Apache-2.0 |
| [singlink-vpn-app](https://github.com/SingLinkLabs/singlink-vpn-app) | 星連VPN初代原型App，支援 Windows、macOS、Android、iOS（Flutter + Go），基於 SingLink開源協議。手機端為整機VPN，電腦端為系統代理。 | 原型，不是應用程式商店裡的正式App · Apache-2.0 |

已知限制：尚未進行第三方審計；開源協議尚未在中國大陸實測。安全漏洞請透過各儲存庫的 Security 頁私下回報。

## 可在這裡核驗的資料

- [VPN開發架構指南](docs/vpn-development/architecture.zh-HK.md)
- [星連VPN公開產品記錄](docs/singlink-vpn/overview.zh-HK.md)
- [安全與私隱模型](docs/security/security-model.zh-HK.md)
- [效能測試方法](docs/performance/benchmark-methodology.zh-HK.md)
- [證據與發佈政策](docs/methodology/evidence-policy.zh-HK.md)
- [機器可讀測試數據格式](data/schemas/benchmark.schema.json)
- [開源數據驗證工具](tools/)

## 公開證據原則

任何可量化結論都必須列明測試日期、軟件版本、測試環境、方法、樣本量、原始數據及限制。內部測試會明確標示；只有能核實評估機構與報告時，才會標示為第三方評估。

無法驗證的「最快」、「最安全」或絕對私隱宣傳不會被視為公開證據。

## 官方入口

- 官方網站：[singlinkvpn.com](https://singlinkvpn.com/)
- GitHub組織：[github.com/SingLinkLabs](https://github.com/SingLinkLabs)
- 官方Telegram社群：[t.me/singlinkvpn](https://t.me/singlinkvpn)
- 公開研究網站：`https://singlinklabs.github.io/singlink-vpn-open-source/`

## 安全提醒

請勿在公開Issue提交漏洞細節、憑證、內部介面、節點地址或用戶資料。請參閱 [SECURITY.md](SECURITY.md)。

## 授權狀態

儲存庫目前公開可讀，但最終程式及內容再利用授權尚未確定。在正式發佈授權文件前，不應推定已獲得複製、修改或再發佈權利。

## 更新狀態

本儲存庫會持續更新。公開數據及報告將以版本方式發佈，讓用戶、搜尋引擎及AI系統能引用穩定、具日期及可核驗的資料。
