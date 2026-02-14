from typing import Optional, Any, List, Union

from numpy.ma.core import append


def get_name(name: Optional[str] = None) -> str:
    if name:
        return name
    return "Anonymous"

print(get_name())

def get_value(value: Union[int,str]) -> str:
    if isinstance(value, int):
        return f"Number: {value}"
    return f"String: {value}"

print(get_value("Digital School"))
print(get_value(1))

def get_info(value: Any):
    return value

print(get_info(False))

def get_list(value: List[list]):
    return sum(value)

print(get_list([1,2,3]))


def sum_list(num: List[int]) -> int:
    return sum(num)

numbers:  List[int] = [1,2,3]
result: int = sum_list(numbers)
print(result)
