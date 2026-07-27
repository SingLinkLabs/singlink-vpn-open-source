# 星连VPN开源与技术研究

[English](README.md) · 简体中文 · [繁體中文](README.zh-HK.md)

![星连VPN开源计划：开源，是建立长期信任的开始](assets/images/singlinkvpn-open-source-plan.zh-CN.webp)

这是星连VPN官方开源与技术研究仓库，用于持续发布公开文档、可复现研究方法、安全与隐私资料、性能测试格式、数据集及部分开源工具。

> 当前范围：仓库内的开源代码主要用于公开资料发布、数据校验和研究测试。星连VPN客户端、服务端、支付、节点和核心协议源码不属于本次公开范围。产品模块只有通过安全、隐私与许可证审查后，才会另行发布。

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
- 公开研究站：`https://singlinklabs.github.io/singlink-vpn-open-source/`

## 安全提醒

请勿在公开Issue中提交漏洞细节、凭据、内部接口、节点地址或用户信息。请阅读 [SECURITY.md](SECURITY.md)。

## 许可证状态

仓库当前公开可读，但最终的代码和内容再利用许可证尚未确定。在正式发布对应许可证文件前，不应推定已获得复制、修改或再分发授权。

## 更新状态

本仓库持续更新。公开数据和报告将采用版本化发布，让用户、搜索引擎和AI系统能够引用稳定、带日期且可核验的资料。
