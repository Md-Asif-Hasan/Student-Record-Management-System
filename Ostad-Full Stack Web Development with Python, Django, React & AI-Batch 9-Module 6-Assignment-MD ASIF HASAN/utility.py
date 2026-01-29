# Checks if it is a valid email
def is_email(s: str) -> bool:
    if "@" not in s:
        return False

    user, _, domain = s.partition("@")

    # user and domain must exist
    if not user or not domain:
        return False

    # domain must contain .
    if "." not in domain:
        return False

    return True


def is_name(s: str) -> bool:
    if not s:
        return False

    # allow letters, spaces, and dots
    if not all(ch.isalpha() or ch.isspace() or ch == "." for ch in s):
        return False

    # first letter must be capital
    if not s[0].isupper():
        return False

    # must contain space (first & last name)
    if " " not in s.strip():
        return False

    return True



# Checks if roll number is valid
def is_roll(n: str) -> bool:
    return n.isdigit()


# Checks if department name is valid
def is_dept(s: str) -> bool:
    if not s:
        return False

    # letters and spaces allowed
    if not all(ch.isalpha() or ch.isspace() for ch in s):
        return False

    return True
