import secrets, string

LOWERCASE, UPPERCASE, DIGITS, HYPHEN = (
    string.ascii_lowercase,
    string.ascii_uppercase,
    string.digits,
    "-",
)
ALPHANUM = LOWERCASE + UPPERCASE + DIGITS
COMPOSITION = {"digit": 1, "uppercase": 1, "hyphen": 2, "lowercase": 16}  # 合计 20 字符


def generate_default_password():  # 对应"默认强密码"
    pool = [secrets.choice(LOWERCASE) for _ in range(COMPOSITION["lowercase"])]
    pool += [secrets.choice(DIGITS), secrets.choice(UPPERCASE), HYPHEN, HYPHEN]
    secrets.SystemRandom().shuffle(pool)  # 随机排列 20 个位置
    return "".join(pool)


def generate_no_special_password():  # 对应"其他选项 → 无特殊字符"
    pool = [secrets.choice(ALPHANUM) for _ in range(18)]
    pool += [secrets.choice(DIGITS), secrets.choice(UPPERCASE)]
    secrets.SystemRandom().shuffle(pool)
    return "".join(pool)


def generate_with_rules(rules):  # 对应 passwordrules / UITextInputPasswordRules
    min_len, max_len = rules.get("min_length", 8), rules.get("max_length", 20)
    charset, required = LOWERCASE, [secrets.choice(LOWERCASE)]
    if rules.get("require_upper", True):
        charset += UPPERCASE
        required.append(secrets.choice(UPPERCASE))
    if rules.get("require_digit", True):
        charset += DIGITS
        required.append(secrets.choice(DIGITS))
    if rules.get("allow_special", True):
        charset += HYPHEN
    rest = [
        secrets.choice(charset) for _ in range(max(min_len, max_len) - len(required))
    ]
    secrets.SystemRandom().shuffle(required + rest)
    return "".join(required + rest)
