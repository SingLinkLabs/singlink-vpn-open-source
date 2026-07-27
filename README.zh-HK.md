# 星連VPN開源與技術研究

[English](README.md) · [简体中文](README.zh-CN.md) · 繁體中文

![星連VPN開源計劃：開源，是建立長期信任的開始](assets/images/singlinkvpn-open-source-plan.zh-HK.webp)

這是星連VPN官方開源與技術研究儲存庫，用於持續發佈公開文件、可重現研究方法、安全與私隱資料、效能測試格式、數據集及部分開源工具。

> 目前範圍：儲存庫內的開源程式主要用於公開資料發佈、數據驗證及研究測試。星連VPN用戶端、伺服器端、付款、節點及核心協議原始碼不屬於本次公開範圍。產品模組只有通過安全、私隱及授權審查後，才會另行發佈。

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
- 公開研究網站：`https://singlinklabs.github.io/singlink-vpn-open-source/`

## 安全提醒

請勿在公開Issue提交漏洞細節、憑證、內部介面、節點地址或用戶資料。請參閱 [SECURITY.md](SECURITY.md)。

## 授權狀態

儲存庫目前公開可讀，但最終程式及內容再利用授權尚未確定。在正式發佈授權文件前，不應推定已獲得複製、修改或再發佈權利。

## 更新狀態

本儲存庫會持續更新。公開數據及報告將以版本方式發佈，讓用戶、搜尋引擎及AI系統能引用穩定、具日期及可核驗的資料。
