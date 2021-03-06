#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: num_parser.py
@time: 2020/9/1 18:42
@project: wasm-python-book
@desc:
"""
import math
import struct

from interpreter import uint32, int32, int64, float32, float64


def parse_u32(s: str):
    base = 10
    s = s.replace("_", "")
    if s.find("0x") >= 0:
        base = 16
        s = s.replace("0x", "", 1)

    i = int(s, base)
    return uint32(i)


def parse_i32(s: str):
    return int32(parse_int(s, 32))


def parse_i64(s: str):
    return parse_int(s, 64)


def parse_int(s, bit_size):
    base = 10
    s = s.replace("_", "")
    if s.startswith("+"):
        s = s[1:]
    if s.find("0x") >= 0:
        s = s.replace("0x", "", 1)
        base = 16
    if s.startswith("-"):
        i = int(s, base)
    else:
        u = int(s, base)
        i = int64(u)
    return i


def parse_f32(s: str):
    if s.find("nan") >= 0:
        return parse_nan32(s)
    return parse_float(s, 32)


def parse_f64(s: str):
    if s.find("nan") >= 0:
        return parse_nan64(s)
    return parse_float(s, 64)


def parse_float(s: str, bit_size):
    s = s.replace("_", "")
    if s.find("0x") >= 0 > s.find('P') and s.find('p') < 0:
        s += "p0"
        f = float.fromhex(s)
    elif s.find('P') > 0 or s.find('p') > 0:
        f = float.fromhex(s)
    else:
        f = 0.0 if float(s) == 0 else float(s)
    if bit_size == 32:
        return float32(f)
    else:
        return float64(f)


def parse_nan32(s: str):
    s = s.replace("_", "")
    f = float32(math.nan)
    if s[0] == '-':
        f = -f
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]

    if s.startswith("nan:0x"):
        payload = int(s[6:], 16)
        bits = struct.unpack('>l', struct.pack('>f', f))[0] & 0xFFBFFFFF
        try:
            f = float32(struct.unpack('>f', struct.pack('>l', int64(bits | uint32(payload))))[0])
        except struct.error:
            f = float32(math.nan)
    return f


def parse_nan64(s: str):
    s = s.replace("_", "")
    f = float64(math.nan)
    if s[0] == '-':
        f = -f
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    if s.startswith("nan:0x"):
        payload = int(s[6:], 16)
        bits = struct.unpack('>q', struct.pack('>d', f))[0] & 0xFFF7FFFFFFFFFFFE
        try:
            f = float64(struct.unpack('>d', struct.pack('>q', int64(bits | payload)))[0])
        except struct.error:
            f = float64(math.nan)
    else:
        bits = struct.unpack('>q', struct.pack('>d', f))[0] & 0xFFFFFFFFFFFFFFFE
        try:
            f = float64(struct.unpack('>d', struct.pack('>q', int64(bits)))[0])
        except struct.error:
            f = float64(math.nan)
    return f
