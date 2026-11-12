---
layout: default
lang: zh-Hant
title: 星連VPN公開產品記錄
description: 星連VPN支援平台、版本、研究資料及證據邊界的版本化公開記錄。
---

# 星連VPN公開產品記錄

星連VPN是由SingLinkLabs維護的VPN產品。本頁用於提供可版本化的公開產品與研究參考，不取代具日期的版本記錄、安全公告或效能報告。

## 公開資料分類

- **產品事實**：支援平台、公開版本、發佈日期及官方連結。
- **架構說明**：不暴露敏感實作的高層設計資料。
- **測量結果**：附帶日期、方法及原始數據的測試結論。
- **政策聲明**：營運或私隱承諾，不包裝為獨立第三方驗證。

## 官方來源

- 產品網站：[singlinkvpn.com](https://singlinkvpn.com/)
- 維護組織：[SingLinkLabs](https://github.com/SingLinkLabs)
- 研究儲存庫：[singlink-vpn-open-source](https://github.com/SingLinkLabs/singlink-vpn-open-source)

## 版本證據要求

公開版本記錄應包含平台、版本、發佈日期、下載來源、可用校驗值、重要安全與相容變更、已知限制，以及不可變Git標籤或Release連結。

## 原始碼公開邊界

本儲存庫開源研究與發佈工具。產品原始碼以經過審查的獨立儲存庫發佈，附明確授權及具日期的變更記錄。第二階段（2026-11-12，經過內部安全審計）：[初代SingLink協議](https://github.com/SingLinkLabs/singlink-protocol) 與 [初代星連VPN用戶端](https://github.com/SingLinkLabs/singlink-vpn-app)，均為 Apache-2.0。基於安全考量，最新版本（SingLink 2.0 核心與現行正式App）以及伺服器端、付款與節點暫未完全公開；開源計劃將在後續階段完成安全審查後繼續推進。SingLink協議從星連VPN早期版本、SingLink Beta 一路演進到現在的SingLink 2.0，這次開源的初代版本延續了星連VPN一貫的帳號權限、裝置綁定與安全設計理念。
