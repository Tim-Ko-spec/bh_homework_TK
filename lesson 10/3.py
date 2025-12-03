# Написать функцию которая принимает строку в которой есть 
# круглые скобки и возвращает True или False анализируя все ли скобки 
# являются закрытыми и расставлены в правильном порядке.
# Примеры:
#     (()()) -> True
#     (()()() -> False
#     (hello(2)ver()(33)python) -> True
#     (hello(2()ver(33)python)) -> True
#     (hello(2()ver(33)python) -> False


def check_parentheses(s: str) -> bool:
    """
    Проверяет, правильно ли расставлены круглые скобки в строке.
    Возвращает True, если все скобки закрыты и порядок корректный.
    """
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


print(check_parentheses("(()())"))
print(check_parentheses("(()()()"))
print(check_parentheses("(hello(2)ver()(33)python)"))
print(check_parentheses("(hello(2()ver(33)python))"))
print(check_parentheses("(hello(2()ver(33)python)"))
