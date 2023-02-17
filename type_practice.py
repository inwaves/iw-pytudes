from typing import List, Any, TypeVar, Literal, Final

# Final type hint
T = TypeVar("T")
final_str: Final = "This string cannot be mutated!"    # Strings aren't mutable anyway...
final_str = "I'm attempting..."

# Type aliases
foo = int   # Aliasing int as foo.
foo_var: foo = 35   # Declaring a variable with type foo (implicitly int).

# Q: When you type hint a star-expression,
# should you hint as collection[T] or just T?
# A: You should hint as just T.
def mean(*args: int):
    return sum(args) / len(args)

# mypy complains about this: it says that sum's argument
# should be an Iterable[bool], not a Tuple[str, ...].
# But this argument is not a tuple of strings!
def count_truthy(elements: List[T]) -> int:
    return sum(True for elem in elements if elem)

# Literals.
def foo(x: Literal[13]) -> int:
    return x * x

# Enforced non-keyword arguments (dunder + name).
def quux(__x: int, __y__: int = 5) -> int:
    return __x + __y__

if __name__ == "__main__":
    # li = [7, 1, 3, None, True, False]
    # print(count_truthy(li))
    print(foo(10))
