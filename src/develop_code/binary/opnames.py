#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: opnames.py
@time: 2020/8/19 15:51
@project: wasm-python-book
@desc:
"""
from binary.opcodes import *

opnames = [""] * 256
opnames[Unreachable] = "unreachable"
opnames[Nop] = "nop"
opnames[Block] = "block"
opnames[Loop] = "loop"
opnames[If] = "if"
opnames[Else_] = "else"
opnames[End_] = "end"
opnames[Br] = "br"
opnames[BrIf] = "br_if"
opnames[BrTable] = "br_table"
opnames[Return] = "return"
opnames[Call] = "call"
opnames[CallIndirect] = "call_indirect"
opnames[Drop] = "drop"
opnames[Select] = "select"
opnames[LocalGet] = "local.get"
opnames[LocalSet] = "local.set"
opnames[LocalTee] = "local.tee"
opnames[GlobalGet] = "global.get"
opnames[GlobalSet] = "global.set"
opnames[I32Load] = "i32.load"
opnames[I64Load] = "i64.load"
opnames[F32Load] = "f32.load"
opnames[F64Load] = "f64.load"
opnames[I32Load8S] = "i32.load8_s"
opnames[I32Load8U] = "i32.load8_u"
opnames[I32Load16S] = "i32.load16_s"
opnames[I32Load16U] = "i32.load16_u"
opnames[I64Load8S] = "i64.load8_s"
opnames[I64Load8U] = "i64.load8_u"
opnames[I64Load16S] = "i64.load16_s"
opnames[I64Load16U] = "i64.load16_u"
opnames[I64Load32S] = "i64.load32_s"
opnames[I64Load32U] = "i64.load32_u"
opnames[I32Store] = "i32.store"
opnames[I64Store] = "i64.store"
opnames[F32Store] = "f32.store"
opnames[F64Store] = "f64.store"
opnames[I32Store8] = "i32.store8"
opnames[I32Store16] = "i32.store16"
opnames[I64Store8] = "i64.store8"
opnames[I64Store16] = "i64.store16"
opnames[I64Store32] = "i64.store32"
opnames[MemorySize] = "memory.size"
opnames[MemoryGrow] = "memory.grow"
opnames[I32Const] = "i32.const"
opnames[I64Const] = "i64.const"
opnames[F32Const] = "f32.const"
opnames[F64Const] = "f64.const"
opnames[I32Eqz] = "i32.eqz"
opnames[I32Eq] = "i32.eq"
opnames[I32Ne] = "i32.ne"
opnames[I32LtS] = "i32.lt_s"
opnames[I32LtU] = "i32.lt_u"
opnames[I32GtS] = "i32.gt_s"
opnames[I32GtU] = "i32.gt_u"
opnames[I32LeS] = "i32.le_s"
opnames[I32LeU] = "i32.le_u"
opnames[I32GeS] = "i32.ge_s"
opnames[I32GeU] = "i32.ge_u"
opnames[I64Eqz] = "i64.eqz"
opnames[I64Eq] = "i64.eq"
opnames[I64Ne] = "i64.ne"
opnames[I64LtS] = "i64.lt_s"
opnames[I64LtU] = "i64.lt_u"
opnames[I64GtS] = "i64.gt_s"
opnames[I64GtU] = "i64.gt_u"
opnames[I64LeS] = "i64.le_s"
opnames[I64LeU] = "i64.le_u"
opnames[I64GeS] = "i64.ge_s"
opnames[I64GeU] = "i64.ge_u"
opnames[F32Eq] = "f32.eq"
opnames[F32Ne] = "f32.ne"
opnames[F32Lt] = "f32.lt"
opnames[F32Gt] = "f32.gt"
opnames[F32Le] = "f32.le"
opnames[F32Ge] = "f32.ge"
opnames[F64Eq] = "f64.eq"
opnames[F64Ne] = "f64.ne"
opnames[F64Lt] = "f64.lt"
opnames[F64Gt] = "f64.gt"
opnames[F64Le] = "f64.le"
opnames[F64Ge] = "f64.ge"
opnames[I32Clz] = "i32.clz"
opnames[I32Ctz] = "i32.ctz"
opnames[I32PopCnt] = "i32.popcnt"
opnames[I32Add] = "i32.add"
opnames[I32Sub] = "i32.sub"
opnames[I32Mul] = "i32.mul"
opnames[I32DivS] = "i32.div_s"
opnames[I32DivU] = "i32.div_u"
opnames[I32RemS] = "i32.rem_s"
opnames[I32RemU] = "i32.rem_u"
opnames[I32And] = "i32.and"
opnames[I32Or] = "i32.or"
opnames[I32Xor] = "i32.xor"
opnames[I32Shl] = "i32.shl"
opnames[I32ShrS] = "i32.shr_s"
opnames[I32ShrU] = "i32.shr_u"
opnames[I32Rotl] = "i32.rotl"
opnames[I32Rotr] = "i32.rotr"
opnames[I64Clz] = "i64.clz"
opnames[I64Ctz] = "i64.ctz"
opnames[I64PopCnt] = "i64.popcnt"
opnames[I64Add] = "i64.add"
opnames[I64Sub] = "i64.sub"
opnames[I64Mul] = "i64.mul"
opnames[I64DivS] = "i64.div_s"
opnames[I64DivU] = "i64.div_u"
opnames[I64RemS] = "i64.rem_s"
opnames[I64RemU] = "i64.rem_u"
opnames[I64And] = "i64.and"
opnames[I64Or] = "i64.or"
opnames[I64Xor] = "i64.xor"
opnames[I64Shl] = "i64.shl"
opnames[I64ShrS] = "i64.shr_s"
opnames[I64ShrU] = "i64.shr_u"
opnames[I64Rotl] = "i64.rotl"
opnames[I64Rotr] = "i64.rotr"
opnames[F32Abs] = "f32.abs"
opnames[F32Neg] = "f32.neg"
opnames[F32Ceil] = "f32.ceil"
opnames[F32Floor] = "f32.floor"
opnames[F32Trunc] = "f32.trunc"
opnames[F32Nearest] = "f32.nearest"
opnames[F32Sqrt] = "f32.sqrt"
opnames[F32Add] = "f32.add"
opnames[F32Sub] = "f32.sub"
opnames[F32Mul] = "f32.mul"
opnames[F32Div] = "f32.div"
opnames[F32Min] = "f32.min"
opnames[F32Max] = "f32.max"
opnames[F32CopySign] = "f32.copysign"
opnames[F64Abs] = "f64.abs"
opnames[F64Neg] = "f64.neg"
opnames[F64Ceil] = "f64.ceil"
opnames[F64Floor] = "f64.floor"
opnames[F64Trunc] = "f64.trunc"
opnames[F64Nearest] = "f64.nearest"
opnames[F64Sqrt] = "f64.sqrt"
opnames[F64Add] = "f64.add"
opnames[F64Sub] = "f64.sub"
opnames[F64Mul] = "f64.mul"
opnames[F64Div] = "f64.div"
opnames[F64Min] = "f64.min"
opnames[F64Max] = "f64.max"
opnames[F64CopySign] = "f64.copysign"
opnames[I32WrapI64] = "i32.wrap_i64"
opnames[I32TruncF32S] = "i32.trunc_f32_s"
opnames[I32TruncF32U] = "i32.trunc_f32_u"
opnames[I32TruncF64S] = "i32.trunc_f64_s"
opnames[I32TruncF64U] = "i32.trunc_f64_u"
opnames[I64ExtendI32S] = "i64.extend_i32_s"
opnames[I64ExtendI32U] = "i64.extend_i32_u"
opnames[I64TruncF32S] = "i64.trunc_f32_s"
opnames[I64TruncF32U] = "i64.trunc_f32_u"
opnames[I64TruncF64S] = "i64.trunc_f64_s"
opnames[I64TruncF64U] = "i64.trunc_f64_u"
opnames[F32ConvertI32S] = "f32.convert_i32_s"
opnames[F32ConvertI32U] = "f32.convert_i32_u"
opnames[F32ConvertI64S] = "f32.convert_i64_s"
opnames[F32ConvertI64U] = "f32.convert_i64_u"
opnames[F32DemoteF64] = "f32.demote_f64"
opnames[F64ConvertI32S] = "f64.convert_i32_s"
opnames[F64ConvertI32U] = "f64.convert_i32_u"
opnames[F64ConvertI64S] = "f64.convert_i64_s"
opnames[F64ConvertI64U] = "f64.convert_i64_u"
opnames[F64PromoteF32] = "f64.promote_f32"
opnames[I32ReinterpretF32] = "i32.reinterpret_f32"
opnames[I64ReinterpretF64] = "i64.reinterpret_f64"
opnames[F32ReinterpretI32] = "f32.reinterpret_i32"
opnames[F64ReinterpretI64] = "f64.reinterpret_i64"
opnames[I32Extend8S] = "i32.extend8_s"
opnames[I32Extend16S] = "i32.extend16_s"
opnames[I64Extend8S] = "i64.extend8_s"
opnames[I64Extend16S] = "i64.extend16_s"
opnames[I64Extend32S] = "i64.extend32_s"
opnames[TruncSat] = "trunc_sat"