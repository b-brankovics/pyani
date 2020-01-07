#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) University of Strathclyde 2020
# Author: Leighton Pritchard
#
# Contact:
# leighton.pritchard@strath.ac.uk
#
# Leighton Pritchard,
# Strathclyde Institute for Pharmacy and Biomedical Sciences,
# Cathedral Street,
# Glasgow,
# G1 1XQ
# Scotland,
# UK
#
# The MIT License
#
# Copyright (c) 2020 University of Strathclyde
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""Provides the listdeps subcommand for pyani."""

from argparse import Namespace
from logging import Logger

from pyani.dependencies import (
    get_requirements,
    get_dev_requirements,
    get_pip_requirements,
    get_tool_versions,
)


def subcmd_listdeps(args: Namespace, logger: Logger) -> int:
    """Reports dependency versions to logger.

    :param args:  Namespace, received command-line arguments
    :param logger:  logging object
    """
    logger.info("Listing pyani Python dependendencies...")
    for package, version in get_requirements():
        logger.info("\t%s==%s", package, version)
    logger.info("Listing pyani development dependendencies...")
    for package, version in get_dev_requirements():
        logger.info("\t%s==%s", package, version)
    logger.info("Listing pyani pip-install dependendencies...")
    for package, version in get_pip_requirements():
        logger.info("\t%s==%s", package, version)
    logger.info("Listing third-party tool versions...")
    for tool, version in get_tool_versions():
        logger.info("\t%s==%s", tool, version)
    return 0
