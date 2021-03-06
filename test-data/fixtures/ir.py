# These builtins stubs are used implicitly in AST to IR generation
# test cases.

from typing import (
    TypeVar, Generic, List, Iterator, Iterable, Sized, Dict, Optional, Tuple, Any, Set,
    overload, Mapping, Union, Callable, Sequence,
)

T = TypeVar('T')
T_co = TypeVar('T_co', covariant=True)
S = TypeVar('S')
K = TypeVar('K') # for keys in mapping
V = TypeVar('V') # for values in mapping

class object:
    def __init__(self) -> None: pass
    def __eq__(self, x: object) -> bool: pass
    def __ne__(self, x: object) -> bool: pass

class type:
    def __init__(self, o: object) -> None: ...

class ellipsis: pass

# Primitive types are special in generated code.

class int:
    def __init__(self, x: object, base: int = 10) -> None: pass
    def __add__(self, n: int) -> int: pass
    def __sub__(self, n: int) -> int: pass
    def __mul__(self, n: int) -> int: pass
    def __floordiv__(self, x: int) -> int: pass
    def __mod__(self, x: int) -> int: pass
    def __neg__(self) -> int: pass
    def __pos__(self) -> int: pass
    def __eq__(self, n: object) -> bool: pass
    def __ne__(self, n: object) -> bool: pass
    def __lt__(self, n: int) -> bool: pass
    def __gt__(self, n: int) -> bool: pass
    def __le__(self, n: int) -> bool: pass
    def __ge__(self, n: int) -> bool: pass

class str:
    def __init__(self, x: object) -> None: pass
    def __add__(self, x: str) -> str: pass
    def __eq__(self, x: object) -> bool: pass
    def __ne__(self, x: object) -> bool: pass
    def __lt__(self, x: str) -> bool: ...
    def __le__(self, x: str) -> bool: ...
    def __gt__(self, x: str) -> bool: ...
    def __ge__(self, x: str) -> bool: ...
    def join(self, x: Iterable[str]) -> str: pass

class float:
    def __init__(self, x: object) -> None: pass
    def __add__(self, n: float) -> float: pass
    def __sub__(self, n: float) -> float: pass
    def __mul__(self, n: float) -> float: pass
    def __truediv__(self, n: float) -> float: pass

class bytes:
    def __init__(self, x: object) -> None: pass
    def __add__(self, x: object) -> bytes: pass
    def __eq__(self, x:object) -> bool:pass
    def __ne__(self, x: object) -> bool: pass
    def join(self, x: Iterable[object]) -> bytes: pass

class bool:
    def __init__(self, o: object = ...) -> None: ...


class tuple(Generic[T_co], Sized):
    def __init__(self, i: Iterable[T_co]) -> None: pass
    def __getitem__(self, i: int) -> T_co: pass
    def __len__(self) -> int: pass
    def __iter__(self) -> Iterator[T_co]: ...

class function: pass

class list(Generic[T], Sequence[T], Iterable[T], Sized):
    def __init__(self, i: Optional[Iterable[T]] = None) -> None: pass
    @overload
    def __getitem__(self, i: int) -> T: ...
    @overload
    def __getitem__(self, s: slice) -> List[T]: ...
    def __setitem__(self, i: int, o: T) -> None: pass
    def __delitem__(self, i: int) -> None: pass
    def __mul__(self, i: int) -> List[T]: pass
    def __rmul__(self, i: int) -> List[T]: pass
    def __iter__(self) -> Iterator[T]: pass
    def __len__(self) -> int: pass
    def append(self, x: T) -> None: pass
    def pop(self, i: int = -1) -> T: pass
    def count(self, T) -> int: pass
    def extend(self, l: Iterable[T]) -> None: pass
    def insert(self, i: int, x: T) -> None: pass
    def sort(self) -> None: pass

class dict(Mapping[K, V]):
    def __getitem__(self, key: K) -> V: pass
    def __setitem__(self, k: K, v: V) -> None: pass
    def __delitem__(self, k: K) -> None: pass
    def __contains__(self, item: object) -> bool: pass
    def __iter__(self) -> Iterator[K]: pass
    def __len__(self) -> int: pass
    def update(self, a: Mapping[K, V]) -> None: pass
    def pop(self, x: int) -> K: pass
    def keys(self) -> List[K]: pass

class set(Generic[T]):
    def __init__(self, i: Optional[Iterable[T]] = None) -> None: pass
    def __iter__(self) -> Iterator[T]: pass
    def __len__(self) -> int: pass
    def add(self, x: T) -> None: pass
    def remove(self, x: T) -> None: pass
    def discard(self, x: T) -> None: pass
    def clear(self) -> None: pass
    def pop(self) -> T: pass
    def update(self, x: Iterable[S]) -> None: pass
    def __or__(self, s: Set[S]) -> Set[Union[T, S]]: ...

class slice: pass

class property:
    def __init__(self, fget: Optional[Callable[[Any], Any]] = ...,
                 fset: Optional[Callable[[Any, Any], None]] = ...,
                 fdel: Optional[Callable[[Any], None]] = ...,
                 doc: Optional[str] = ...) -> None: ...
    def getter(self, fget: Callable[[Any], Any]) -> property: ...
    def setter(self, fset: Callable[[Any, Any], None]) -> property: ...
    def deleter(self, fdel: Callable[[Any], None]) -> property: ...
    def __get__(self, obj: Any, type: Optional[type] = ...) -> Any: ...
    def __set__(self, obj: Any, value: Any) -> None: ...
    def __delete__(self, obj: Any) -> None: ...
    def fget(self) -> Any: ...
    def fset(self, value: Any) -> None: ...
    def fdel(self) -> None: ...

class BaseException: pass

class Exception(BaseException):
    def __init__(self, message: Optional[str] = None) -> None: pass

class TypeError(Exception): pass

class AttributeError(Exception): pass

class LookupError(Exception): pass

class KeyError(LookupError): pass

class IndexError(LookupError): pass

class RuntimeError(Exception): pass

class NotImplementedError(RuntimeError): pass


def any(i: Iterable[T]) -> bool: pass
def all(i: Iterable[T]) -> bool: pass
def reversed(object: Sequence[T]) -> Iterator[T]: ...
def id(o: object) -> int: pass
def len(o: Sized) -> int: pass
def print(*object) -> None: pass
def range(x: int, y: int = ..., z: int = ...) -> Iterator[int]: pass
def isinstance(x: object, t: object) -> bool: pass
def next(i: Iterator[T]) -> T: pass
def hash(o: object) -> int: ...
def globals() -> Dict[str, Any]: ...
def setattr(object: Any, name: str, value: Any) -> None: ...
def enumerate(x: Iterable[T]) -> Iterator[Tuple[int, T]]: ...
@overload
def zip(x: Iterable[T], y: Iterable[S]) -> Iterator[Tuple[T, S]]: ...
@overload
def zip(x: Iterable[T], y: Iterable[S], z: Iterable[V]) -> Iterator[Tuple[T, S, V]]: ...

# Dummy definitions.
class classmethod: pass
class staticmethod: pass

NotImplemented = ...  # type: Any
