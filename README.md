# pyOBIS

## Abstract

pyOBIS is a Python 3.5 implementation that converts
* various OBIS code representations and
* numeric unit codes

into textual, native and integer numeric representations.

It is based on http://www.edi-energy.de/files2%5CEDI@Energy-Codeliste-OBIS-Kennzahlen_2_2e_20160401.pdf,
IEC 62056-61:2002 and IEC 62056-62:2002.

## Example

```python
import pyOBIS
obis = pyOBIS.OBIS()

# OBIS code representation into textual representation
print(obis.getDescr("1-0:1.8.0*255")["descr"])
print(obis.getDescr(0x0100010800FF)["descr"])
print(obis.getDescr(tuple([0x01,0x00,0x01,0x08,0x00,0xFF]))["descr"])

# OBIS code representation into native representation
print(obis.getDescr("1-0:1.8.0*255")["native"])
print(obis.getDescr(0x0100010800FF)["native"])
print(obis.getDescr(tuple([0x01,0x00,0x01,0x08,0x00,0xFF]))["native"])

# OBIS code representation into integer numeric representation
print(obis.getDescr("1-0:1.8.0*255")["int"])
print(obis.getDescr(0x0100010800FF)["int"])
print(obis.getDescr(tuple([0x01,0x00,0x01,0x08,0x00,0xFF]))["int"])

# numeric unit code into textual representation
print(obis.getUnit(0x1B)["descr"])

# numeric unit code into native representation
print(obis.getUnit(0x1B)["native"])

# numeric unit code into integer numeric representation
print(obis.getUnit(0x1B)["int"])
```
