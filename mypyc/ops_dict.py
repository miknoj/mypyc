"""Primitive dict ops."""

from typing import List

from mypyc.ops import (
    EmitterInterface, PrimitiveOp,
    dict_rprimitive, object_rprimitive, bool_rprimitive, int_rprimitive,
    ERR_FALSE, ERR_MAGIC, ERR_NEVER,
)
from mypyc.ops_primitive import (
    name_ref_op, method_op, binary_op, func_op,
    simple_emit, negative_int_emit,
    call_emit, call_negative_bool_emit, call_negative_magic_emit,
)


name_ref_op('builtins.dict',
            result_type=object_rprimitive,
            error_kind=ERR_NEVER,
            emit=simple_emit('{dest} = (PyObject *)&PyDict_Type;'),
            is_borrowed=True)

dict_get_item_op = method_op(
    name='__getitem__',
    arg_types=[dict_rprimitive, object_rprimitive],
    result_type=object_rprimitive,
    error_kind=ERR_MAGIC,
    emit=call_emit('CPyDict_GetItem'))


dict_set_item_op = method_op(
    name='__setitem__',
    arg_types=[dict_rprimitive, object_rprimitive, object_rprimitive],
    result_type=bool_rprimitive,
    error_kind=ERR_FALSE,
    emit=call_negative_bool_emit('CPyDict_SetItem'))


binary_op(op='in',
          arg_types=[object_rprimitive, dict_rprimitive],
          result_type=bool_rprimitive,
          error_kind=ERR_MAGIC,
          format_str='{dest} = {args[0]} in {args[1]} :: dict',
          emit=negative_int_emit('{dest} = PyDict_Contains({args[1]}, {args[0]});'))

dict_update_op = method_op(
    name='update',
    arg_types=[dict_rprimitive, dict_rprimitive],
    result_type=bool_rprimitive,
    error_kind=ERR_FALSE,
    emit=call_negative_bool_emit('CPyDict_Update'),
    priority=2)

method_op(
    name='update',
    arg_types=[dict_rprimitive, object_rprimitive],
    result_type=bool_rprimitive,
    error_kind=ERR_FALSE,
    emit=simple_emit('{dest} = CPyDict_UpdateFromSeq({args[0]}, {args[1]}) != -1;'))

method_op(
    name='get',
    arg_types=[dict_rprimitive, object_rprimitive, object_rprimitive],
    result_type=object_rprimitive,
    error_kind=ERR_MAGIC,
    emit=call_emit('CPyDict_Get'))

method_op(
    name='get',
    arg_types=[dict_rprimitive, object_rprimitive],
    result_type=object_rprimitive,
    error_kind=ERR_MAGIC,
    emit=simple_emit('{dest} = CPyDict_Get({args[0]}, {args[1]}, Py_None);'))

new_dict_op = func_op(
    name='builtins.dict',
    arg_types=[],
    result_type=dict_rprimitive,
    error_kind=ERR_MAGIC,
    format_str='{dest} = {{}}',
    emit=call_emit('PyDict_New'))


def emit_len(emitter: EmitterInterface, args: List[str], dest: str) -> None:
    temp = emitter.temp_name()
    emitter.emit_declaration('long long %s;' % temp)
    emitter.emit_line('%s = PyDict_Size(%s);' % (temp, args[0]))
    emitter.emit_line('%s = CPyTagged_ShortFromLongLong(%s);' % (dest, temp))


func_op(name='builtins.len',
        arg_types=[dict_rprimitive],
        result_type=int_rprimitive,
        error_kind=ERR_NEVER,
        emit=emit_len)
