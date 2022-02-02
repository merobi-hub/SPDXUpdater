<!-- SPDX-License-Identifier: Apache-2.0 -->

# A Simple Script to Update License Text 

The lengthy block text often used by open source developers to include a license
in their projects has been superceded by the SPDX License standard, which 
reduces the length of the license text to a single, machine-readable line.

This project automates the process of replacing block license text with 
SPDX-compliant text or adding the same where no license text is present.

## Requisites

Python 3

## Supported License Types

Apache 2.0

## Supported File Types

The files types currently supported:
.java
.py
.md
.txt

## How to Use

Copy the spdx-convert.py file to the root directory of your project. Then,
open a terminal window, cd into the root directory, and execute the script 
with Python 3.

## Contributors

[merobi-hub](https://github.com/merobi-hub)

## More Info

[SPDX License List](https://spdx.org/licenses/)