## 原文要点（Apple 平台安全指南《自动强密码》）

>
> 生成的密码长度默认为 20 个字符。其中包含一位数字、一个大写字符、两个连字符和 16 个小写字符。这些生成的密码均为包含 71 位熵的强密码。
>
>
> 密码基于一种启发技术生成，这种启发技术可确定密码栏是否用于密码创建。……App 开发者可在其文本栏上设定 `UITextContentType.newPassword`，网页开发者可设定 `autocomplete="new-password"`。
>
>
> 为帮助确保生成的密码与相关服务兼容，App 和网站可提供规则…… 设备随后会生成可以满足这些规则的最强密码。

## 核心代码（描述该行为的 Python 实现）

```python
import secrets, string

LOWERCASE, UPPERCASE, DIGITS, HYPHEN = string.ascii_lowercase, string.ascii_uppercase, string.digits, "-"
ALPHANUM = LOWERCASE + UPPERCASE + DIGITS
COMPOSITION = {"digit": 1, "uppercase": 1, "hyphen": 2, "lowercase": 16}   # 合计 20 字符

def generate_default_password():          # 对应"默认强密码"
    pool = [secrets.choice(LOWERCASE) for _ in range(COMPOSITION["lowercase"])]
    pool += [secrets.choice(DIGITS), secrets.choice(UPPERCASE), HYPHEN, HYPHEN]
    secrets.SystemRandom().shuffle(pool)  # 随机排列 20 个位置
    return "".join(pool)

def generate_no_special_password():       # 对应"其他选项 → 无特殊字符"
    pool = [secrets.choice(ALPHANUM) for _ in range(18)]
    pool += [secrets.choice(DIGITS), secrets.choice(UPPERCASE)]
    secrets.SystemRandom().shuffle(pool)
    return "".join(pool)

def generate_with_rules(rules):           # 对应 passwordrules / UITextInputPasswordRules
    min_len, max_len = rules.get("min_length", 8), rules.get("max_length", 20)
    charset, required = LOWERCASE, [secrets.choice(LOWERCASE)]
    if rules.get("require_upper", True):
        charset += UPPERCASE; required.append(secrets.choice(UPPERCASE))
    if rules.get("require_digit", True):
        charset += DIGITS;  required.append(secrets.choice(DIGITS))
    if rules.get("allow_special", True):
        charset += HYPHEN
    rest = [secrets.choice(charset) for _ in range(max(min_len, max_len) - len(required))]
    secrets.SystemRandom().shuffle(required + rest)
    return "".join(required + rest)

```

## 71 位熵的含义