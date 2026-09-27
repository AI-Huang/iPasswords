# iPassword 项目文件结构文档

## 项目概述

这是一个基于 Python 的项目，项目名称为 `igoogletakeout`，当前版本为 `0.1.0`。

---

## 文件结构

```
iPassword/
├── .python-version          # Python 版本配置文件
├── README.md                # 项目说明文档（当前为空）
├── main.py                  # 主程序入口
├── pyproject.toml           # Python 项目配置文件
└── docs/
    └── project-structure.md # 项目结构文档（本文档）
```

---

## 文件详情

### 1. `.python-version`

Python 版本管理文件，用于指定项目使用的 Python 版本。

### 2. `main.py`

**功能**：项目主程序入口

**内容摘要**：

```python
def main():
    print("Hello from igoogletakeout!")

if __name__ == "__main__":
    main()
```

**说明**：当前为一个简单的入口函数，输出欢迎信息。

### 3. `pyproject.toml`

**功能**：Python 项目元数据和依赖配置

**关键配置**：

- **项目名称**：`igoogletakeout`
- **版本**：`0.1.0`
- **Python 要求**：`>=3.11`
- **依赖**：暂无依赖

### 4. `README.md`

**功能**：项目说明文档

**状态**：当前为空，建议补充项目介绍、使用方法等内容。

### 5. `docs/project-structure.md`

**功能**：项目结构文档

**说明**：本文档，用于记录项目的文件结构和各文件的说明。

---

## 技术栈

| 分类 | 技术 | 版本要求 |
|------|------|----------|
| 语言 | Python | >=3.11 |
| 构建工具 | uv | 通过 pyproject.toml 管理 |

---

## 运行方式

```bash
# 激活虚拟环境
source .venv/bin/activate

# 运行主程序
python main.py
```

---

## 项目状态

当前项目处于初始阶段，`main.py` 仅包含基础的入口函数，`README.md` 为空。建议根据实际需求扩展功能并完善文档。
