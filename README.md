# bad-asn-list

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Issues](https://img.shields.io/github/issues/brianhama/bad-asn-list.svg)](https://github.com/brianhama/bad-asn-list/issues)

> An open source list of ASNs known to belong to cloud, managed hosting, and colo facilities.

对抗机器人、垃圾邮件和欺诈者的开源解决方案。通过阻止托管/云服务提供商的 ASN 来过滤恶意流量。

---

## 📖 目录

- [背景故事](#背景故事)
- [问题](#问题)
- [解决方案](#解决方案)
- [使用方法](#使用方法)
- [数据来源](#数据来源)
- [贡献指南](#贡献指南)
- [License](#license)

---

## 📖 背景故事

在运营一个拥有约 50 万月活用户的社交网络时，我们遇到了严重的自动化机器人和垃圾邮件问题。尝试了多种检测方法：

| 方法 | 结果 |
|------|------|
| Facebook 登录验证 | ❌ 无效 |
| Google 登录验证 | ❌ 无效 |
| MaxMind API | ✅ 有效但成本过高 |

最终发现：几乎所有恶意流量都来自托管/托管设施和云服务提供商。

---

## 🛠️ 问题

在达到一定规模后，自动化机器人的涌入变得完全无法管理。传统方法存在以下问题：

- 误报率高
- 漏报率高
- 成本过高

---

## 💡 解决方案

构建了一个已知托管/托管/云提供商的 ASN 列表：

1. 用户创建账户时，获取请求 IP 地址所属的 ASN
2. 检查该 ASN 是否在列表中
3. 如果在列表中，阻止请求或提高欺诈评分

**效果**: 问题减少了约 90%，几乎所有恶意流量都消失了。

---

## 🚀 使用方法

### 步骤 1: 加载列表

将 `bad-asn-list.csv` 加载到数据库或内存中。

### 步骤 2: 获取 ASN 信息

获取请求 IP 地址的 ASN。可使用 MaxMind 的免费数据库：

```
http://dev.maxmind.com/geoip/geoip2/geolite2/
```

### 步骤 3: 检查并阻止

```python
if ip_address_asn in bad_asn_list:
    block_request()
```

---

## 📊 数据来源

数据包含以下类型的 ASN：

- 云服务提供商 (AWS, GCP, Azure 等)
- 托管服务商
- 托管设施 (Colo)
- VPN 提供商 (其 IP 通常来自托管设施)

---

## 🤝 贡献指南

欢迎提交 Pull Request 来更新列表！

### 提交新 ASN

1. Fork 本仓库
2. 编辑 `bad-asn-list.csv` 文件
3. 添加新的 ASN（格式：AS号码,提供商名称）
4. 提交 Pull Request

---

## 📧 联系作者

Brian Hamachek  
Email: brian@brianhama.com

---

## 📄 License

MIT License - 详见 [LICENSE](LICENSE) 文件

---

*README optimized with [Gingiris README Generator](https://gingiris.github.io/github-readme-generator/)*
