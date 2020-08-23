#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Main.py
@time: 2020/8/18 16:23
@desc: 主函数
"""
import os
from optparse import OptionParser

from ch08 import binary
from ch08.cmd.dumper import dump
from ch08.interpreter.vm import exec_main_func


def main(input_args):
    # 设置传入参数
    parser = OptionParser(usage="usage:%prog [-d] filename")

    parser.add_option("-d", "--dump", action="store_true", default=False, dest="dump_flag",
                      help="print version and exit.")
    parser.add_option("--verbose", action="store_true", default=False, dest="verbose_flag",
                      help="enable verbose output")
    # 解析参数
    (options, args) = parser.parse_args(input_args)
    module, err = binary.decode_file(args[0])

    if err is not None:
        raise err

    if options.dump_flag:
        dump(module)
    else:
        exec_main_func(module, options.verbose_flag)


if __name__ == '__main__':
    # 打印帮助
    # fake_args = ['-h']
    # main(fake_args)

    # 使用输入参数测试
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    file_name = os.path.join(os.path.dirname(root_path), "../wat", "ch08_fac.wasm")
    fake_args = ["--verbose", file_name]
    main(fake_args)
