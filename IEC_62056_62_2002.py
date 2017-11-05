# pyOBIS
# Copyright (C) 2017  Hallabalooza
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not, see
# <http://www.gnu.org/licenses/>.

########################################################################################################################
########################################################################################################################
########################################################################################################################

# no imports

########################################################################################################################
########################################################################################################################
########################################################################################################################

# Units
# - IEC 62056-62:2002; unit ::= enum
_IEC_62056_62_Tab_EU = {
  0x00: ("~",          "reserved"),
  0x01: ("a",          "time"),
  0x02: ("mo",         "time"),
  0x03: ("wk",         "time"),
  0x04: ("d",          "time"),
  0x05: ("h",          "time"),
  0x06: ("min",        "time"),
  0x07: ("s",          "time"),
  0x08: ("°",          "(phase) angle"),
  0x09: ("°C",         "temperature (\u03F4)"),
  0x0A: ("$",          "(local) currency"),
  0x0B: ("m",          "length (l)"),
  0x0C: ("m/s",        "speed (v)"),
  0x0D: ("m³",         "volume (V)"),
  0x0E: ("m³",         "corrected volume"),
  0x0F: ("m³/h",       "volume flux"),
  0x10: ("m³/h",       "corrected volume flux"),
  0x11: ("m³/d",       "volume flux"),
  0x12: ("m³/d",       "corrected volume flux"),
  0x13: ("l",          "volume (V)"),
  0x14: ("kg",         "mass (m)"),
  0x15: ("N",          "force (F)"),
  0x16: ("Nm",         "energy"),
  0x17: ("Pa",         "presure (p)"),
  0x18: ("bar",        "pressure (p)"),
  0x19: ("J",          "energy"),
  0x1A: ("J/h",        "thermal power"),
  0x1B: ("W",          "active power (P)"),
  0x1C: ("VA",         "apparent power (S)"),
  0x1D: ("var",        "reactive power (Q)"),
  0x1E: ("Wh",         "active energy"),
  0x1F: ("VAh",        "apparent energy"),
  0x20: ("varh",       "reactive energy"),
  0x21: ("A",          "current (I)"),
  0x22: ("C",          "electrical charge (Q)"),
  0x23: ("V",          "voltage (U)"),
  0x24: ("V/m",        "electrical field strength (E)"),
  0x25: ("F",          "capacity (C)"),
  0x26: ("\u2126",     "resistance (R)"),
  0x27: ("\u2126m²/m", "resistivity (\u03C1)"),
  0x28: ("Wb",         "magnetic flux (\u03D5)"),
  0x29: ("T",          "induction (T)"),
  0x2A: ("A/m",        "magnetic field strength (H)"),
  0x2B: ("H",          "inductivity (L)"),
  0x2C: ("Hz",         "frequency (f, \u03C9)"),
  0x2D: ("R_ac",       "active energy meter constant"),
  0x2E: ("R_re",       "reactive energy meter constant"),
  0x2F: ("R_ap",       "apparent energy meter constant"),
  0x30: ("V²h",        "voltage square hour"),
  0x31: ("A²h",        "ampere square hour"),
  0x32: ("kg/s",       "mass flux"),
  0x33: ("S mho",      "conductance"),
  0x34: ("~",          "reserved"),
  0x35: ("~",          "reserved"),
  0x36: ("~",          "reserved"),
  0x37: ("~",          "reserved"),
  0x38: ("~",          "reserved"),
  0x39: ("~",          "reserved"),
  0x3A: ("~",          "reserved"),
  0x3B: ("~",          "reserved"),
  0x3C: ("~",          "reserved"),
  0x3D: ("~",          "reserved"),
  0x3E: ("~",          "reserved"),
  0x3F: ("~",          "reserved"),
  0x40: ("~",          "reserved"),
  0x41: ("~",          "reserved"),
  0x42: ("~",          "reserved"),
  0x43: ("~",          "reserved"),
  0x44: ("~",          "reserved"),
  0x45: ("~",          "reserved"),
  0x46: ("~",          "reserved"),
  0x47: ("~",          "reserved"),
  0x48: ("~",          "reserved"),
  0x49: ("~",          "reserved"),
  0x4A: ("~",          "reserved"),
  0x4B: ("~",          "reserved"),
  0x4C: ("~",          "reserved"),
  0x4D: ("~",          "reserved"),
  0x4E: ("~",          "reserved"),
  0x4F: ("~",          "reserved"),
  0x50: ("~",          "reserved"),
  0x51: ("~",          "reserved"),
  0x52: ("~",          "reserved"),
  0x53: ("~",          "reserved"),
  0x54: ("~",          "reserved"),
  0x55: ("~",          "reserved"),
  0x56: ("~",          "reserved"),
  0x57: ("~",          "reserved"),
  0x58: ("~",          "reserved"),
  0x59: ("~",          "reserved"),
  0x5A: ("~",          "reserved"),
  0x5B: ("~",          "reserved"),
  0x5C: ("~",          "reserved"),
  0x5D: ("~",          "reserved"),
  0x5E: ("~",          "reserved"),
  0x5F: ("~",          "reserved"),
  0x60: ("~",          "reserved"),
  0x61: ("~",          "reserved"),
  0x62: ("~",          "reserved"),
  0x63: ("~",          "reserved"),
  0x64: ("~",          "reserved"),
  0x65: ("~",          "reserved"),
  0x66: ("~",          "reserved"),
  0x67: ("~",          "reserved"),
  0x68: ("~",          "reserved"),
  0x69: ("~",          "reserved"),
  0x6A: ("~",          "reserved"),
  0x6B: ("~",          "reserved"),
  0x6C: ("~",          "reserved"),
  0x6D: ("~",          "reserved"),
  0x6E: ("~",          "reserved"),
  0x6F: ("~",          "reserved"),
  0x70: ("~",          "reserved"),
  0x71: ("~",          "reserved"),
  0x72: ("~",          "reserved"),
  0x73: ("~",          "reserved"),
  0x74: ("~",          "reserved"),
  0x75: ("~",          "reserved"),
  0x76: ("~",          "reserved"),
  0x77: ("~",          "reserved"),
  0x78: ("~",          "reserved"),
  0x79: ("~",          "reserved"),
  0x7A: ("~",          "reserved"),
  0x7B: ("~",          "reserved"),
  0x7C: ("~",          "reserved"),
  0x7D: ("~",          "reserved"),
  0x7E: ("~",          "reserved"),
  0x7F: ("~",          "reserved"),
  0x80: ("~",          "reserved"),
  0x81: ("~",          "reserved"),
  0x82: ("~",          "reserved"),
  0x83: ("~",          "reserved"),
  0x84: ("~",          "reserved"),
  0x85: ("~",          "reserved"),
  0x86: ("~",          "reserved"),
  0x87: ("~",          "reserved"),
  0x88: ("~",          "reserved"),
  0x89: ("~",          "reserved"),
  0x8A: ("~",          "reserved"),
  0x8B: ("~",          "reserved"),
  0x8C: ("~",          "reserved"),
  0x8D: ("~",          "reserved"),
  0x8E: ("~",          "reserved"),
  0x8F: ("~",          "reserved"),
  0x90: ("~",          "reserved"),
  0x91: ("~",          "reserved"),
  0x92: ("~",          "reserved"),
  0x93: ("~",          "reserved"),
  0x94: ("~",          "reserved"),
  0x95: ("~",          "reserved"),
  0x96: ("~",          "reserved"),
  0x97: ("~",          "reserved"),
  0x98: ("~",          "reserved"),
  0x99: ("~",          "reserved"),
  0x9A: ("~",          "reserved"),
  0x9B: ("~",          "reserved"),
  0x9C: ("~",          "reserved"),
  0x9D: ("~",          "reserved"),
  0x9E: ("~",          "reserved"),
  0x9F: ("~",          "reserved"),
  0xA0: ("~",          "reserved"),
  0xA1: ("~",          "reserved"),
  0xA2: ("~",          "reserved"),
  0xA3: ("~",          "reserved"),
  0xA4: ("~",          "reserved"),
  0xA5: ("~",          "reserved"),
  0xA6: ("~",          "reserved"),
  0xA7: ("~",          "reserved"),
  0xA8: ("~",          "reserved"),
  0xA9: ("~",          "reserved"),
  0xAA: ("~",          "reserved"),
  0xAB: ("~",          "reserved"),
  0xAC: ("~",          "reserved"),
  0xAD: ("~",          "reserved"),
  0xAE: ("~",          "reserved"),
  0xAF: ("~",          "reserved"),
  0xB0: ("~",          "reserved"),
  0xB1: ("~",          "reserved"),
  0xB2: ("~",          "reserved"),
  0xB3: ("~",          "reserved"),
  0xB4: ("~",          "reserved"),
  0xB5: ("~",          "reserved"),
  0xB6: ("~",          "reserved"),
  0xB7: ("~",          "reserved"),
  0xB8: ("~",          "reserved"),
  0xB9: ("~",          "reserved"),
  0xBA: ("~",          "reserved"),
  0xBB: ("~",          "reserved"),
  0xBC: ("~",          "reserved"),
  0xBD: ("~",          "reserved"),
  0xBE: ("~",          "reserved"),
  0xBF: ("~",          "reserved"),
  0xC0: ("~",          "reserved"),
  0xC1: ("~",          "reserved"),
  0xC2: ("~",          "reserved"),
  0xC3: ("~",          "reserved"),
  0xC4: ("~",          "reserved"),
  0xC5: ("~",          "reserved"),
  0xC6: ("~",          "reserved"),
  0xC7: ("~",          "reserved"),
  0xC8: ("~",          "reserved"),
  0xC9: ("~",          "reserved"),
  0xCA: ("~",          "reserved"),
  0xCB: ("~",          "reserved"),
  0xCC: ("~",          "reserved"),
  0xCD: ("~",          "reserved"),
  0xCE: ("~",          "reserved"),
  0xCF: ("~",          "reserved"),
  0xD0: ("~",          "reserved"),
  0xD1: ("~",          "reserved"),
  0xD2: ("~",          "reserved"),
  0xD3: ("~",          "reserved"),
  0xD4: ("~",          "reserved"),
  0xD5: ("~",          "reserved"),
  0xD6: ("~",          "reserved"),
  0xD7: ("~",          "reserved"),
  0xD8: ("~",          "reserved"),
  0xD9: ("~",          "reserved"),
  0xDA: ("~",          "reserved"),
  0xDB: ("~",          "reserved"),
  0xDC: ("~",          "reserved"),
  0xDD: ("~",          "reserved"),
  0xDE: ("~",          "reserved"),
  0xDF: ("~",          "reserved"),
  0xE0: ("~",          "reserved"),
  0xE1: ("~",          "reserved"),
  0xE2: ("~",          "reserved"),
  0xE3: ("~",          "reserved"),
  0xE4: ("~",          "reserved"),
  0xE5: ("~",          "reserved"),
  0xE6: ("~",          "reserved"),
  0xE7: ("~",          "reserved"),
  0xE8: ("~",          "reserved"),
  0xE9: ("~",          "reserved"),
  0xEA: ("~",          "reserved"),
  0xEB: ("~",          "reserved"),
  0xEC: ("~",          "reserved"),
  0xED: ("~",          "reserved"),
  0xEE: ("~",          "reserved"),
  0xEF: ("~",          "reserved"),
  0xF0: ("~",          "reserved"),
  0xF1: ("~",          "reserved"),
  0xF2: ("~",          "reserved"),
  0xF3: ("~",          "reserved"),
  0xF4: ("~",          "reserved"),
  0xF5: ("~",          "reserved"),
  0xF6: ("~",          "reserved"),
  0xF7: ("~",          "reserved"),
  0xF8: ("~",          "reserved"),
  0xF9: ("~",          "reserved"),
  0xFA: ("~",          "reserved"),
  0xFB: ("~",          "reserved"),
  0xFC: ("~",          "reserved"),
  0xFD: ("~",          "reserved"),
  0xFE: ("other",      "other unit"),
  0xFF: ("count",      "no unit, unitless, count"),
}

########################################################################################################################
########################################################################################################################
########################################################################################################################

if __name__ == '__main__':
  pass
