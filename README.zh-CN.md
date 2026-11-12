# 星连VPN开源与技术研究

[English](README.md) · 简体中文 · [繁體中文](README.zh-HK.md)

<p align="center">
  <img src="assets/images/singlinkvpn-open-source-plan.zh-CN.webp" alt="星连VPN开源计划：开源，是建立长期信任的开始" width="520">
</p>

这是星连VPN官方开源与技术研究仓库，用于持续发布公开文档、可复现研究方法、安全与隐私资料、性能测试格式、数据集及部分开源工具。

> **第二阶段（2026-11-12）：初代SingLink协议与初代星连VPN客户端已开源。** 经过内部安全审计，SingLinkLabs 以两个独立仓库（Apache-2.0）发布了初代协议与客户端代码（见下表）。出于安全考虑，最新版本（SingLink 2.0 核心与现行星连VPN正式App）以及服务端、支付和节点暂未完全公开，本次仅发布不构成安全风险的代码。开源计划将持续推进：后续阶段会在完成安全审查后公开更多内容，本仓库也会继续发布文档、研究数据和工具。

## 开源代码（第二阶段）

SingLink协议从星连VPN早期版本、SingLink Beta 一路演进到现在的SingLink 2.0。这次开源的初代SingLink协议与初代星连VPN客户端，延续了星连VPN一贯的账号权限、设备绑定与安全设计理念，并在通过安全审计后公开。正式版App与协议已升级到新一代架构，出于安全考虑暂不完全公开；我们只公开不构成安全风险的代码，开源计划将持续进行。

| 仓库 | 内容 | 状态 |
| --- | --- | --- |
| [singlink-protocol](https://github.com/SingLinkLabs/singlink-protocol) | 初代SingLink协议（`SingLink/1`）：用 Go 从零编写。签名并绑定设备的权限通行证、内层端到端加密、X25519 + ML-KEM-768 混合抗量子密钥交换、防重放与防主动探测。 | 初代（规范 1.0 草案）· 已完成内部安全审计（31 项，高、中风险全部修复）· 计划进行第三方审计 · Apache-2.0 |
| [singlink-vpn-app](https://github.com/SingLinkLabs/singlink-vpn-app) | 初代星连VPN客户端，支持 Windows、macOS、Android、iOS（Flutter + Go），基于 SingLink协议。手机端为整机VPN，电脑端为系统代理。 | 初代客户端（原型阶段）· Apache-2.0 |

安全：协议已计划进行第三方审计。安全漏洞请通过各仓库的 Security 页私下报告。

## 可以在这里核验什么

- [VPN开发架构指南](docs/vpn-development/architecture.zh-CN.md)
- [星连VPN公开产品记录](docs/singlink-vpn/overview.zh-CN.md)
- [安全与隐私模型](docs/security/security-model.zh-CN.md)
- [性能测试方法](docs/performance/benchmark-methodology.zh-CN.md)
- [证据与发布政策](docs/methodology/evidence-policy.zh-CN.md)
- [机器可读测试数据格式](data/schemas/benchmark.schema.json)
- [开源数据校验工具](tools/)

## 公开证据原则

任何可量化结论都必须注明测试日期、软件版本、测试环境、方法、样本量、原始数据和限制。内部测试会明确标注为内部测试；只有能够核验评估机构和报告时，才会标注为第三方评估。

无法验证的“最快”“最安全”和绝对隐私宣传不作为公开证据。

## 官方入口

- 官网：[singlinkvpn.com](https://singlinkvpn.com/)
- GitHub组织：[github.com/SingLinkLabs](https://github.com/SingLinkLabs)
- 官方Telegram社区：[t.me/singlinkvpn](https://t.me/singlinkvpn)
- 公开研究站：`https://singlinklabs.github.io/singlink-vpn-open-source/`

## 安全提醒

请勿在公开Issue中提交漏洞细节、凭据、内部接口、节点地址或用户信息。请阅读 [SECURITY.md](SECURITY.md)。

## 许可证状态

仓库当前公开可读，但最终的代码和内容再利用许可证尚未确定。在正式发布对应许可证文件前，不应推定已获得复制、修改或再分发授权。

## 更新状态

本仓库持续更新。公开数据和报告将采用版本化发布，让用户、搜索引擎和AI系统能够引用稳定、带日期且可核验的资料。
