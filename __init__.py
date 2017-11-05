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

import pyOBIS.IEC_62056_61_2002
import pyOBIS.IEC_62056_62_2002
import re

########################################################################################################################
########################################################################################################################
########################################################################################################################

class OBISException(Exception):
  """
  @brief   OBIS exception base class.
  """

  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def __init__(self, Mssg=None):
    """
    @brief   Constructor.
    @param   Mssg   The Exception message.
    """
    self._mssg = Mssg

  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def __str__(self):
    """
    @brief   Prints a nicely string representation.
    """
    if   ( None == self._mssg ): return
    else                       : return repr(self._mssg)

########################################################################################################################
########################################################################################################################
########################################################################################################################

class OBIS:
  """
  @brief   OBIS code to textual description class.
  @param   IEC_62056_61  The version of IEC_62056_61
  @param   IEC_62056_62  The version of IEC_62056_62
  """

  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def __init__(self, IEC_62056_61=2002, IEC_62056_62=2002):
    """
    @brief   Constructor.
    """
    self.__iec_62056_61 = IEC_62056_61
    self.__iec_62056_62 = IEC_62056_62
    if ( self.__iec_62056_61 == 2002 ):
      self.__IEC_62056_61_Tab_01 = pyOBIS.IEC_62056_61_2002._IEC_62056_61_Tab_01
      self.__IEC_62056_61_Tab_02 = pyOBIS.IEC_62056_61_2002._IEC_62056_61_Tab_02
      self.__IEC_62056_61_Tab_03 = pyOBIS.IEC_62056_61_2002._IEC_62056_61_Tab_03
      self.__IEC_62056_61_Tab_04 = pyOBIS.IEC_62056_61_2002._IEC_62056_61_Tab_04
      self.__IEC_62056_61_Tab_05 = pyOBIS.IEC_62056_61_2002._IEC_62056_61_Tab_05
      self.__IEC_62056_61_Tab_06 = pyOBIS.IEC_62056_61_2002._IEC_62056_61_Tab_06
      self.__IEC_62056_61_Tab_07 = pyOBIS.IEC_62056_61_2002._IEC_62056_61_Tab_07
      self.__IEC_62056_61_Tab_08 = pyOBIS.IEC_62056_61_2002._IEC_62056_61_Tab_08
      self.__IEC_62056_61_Tab_09 = pyOBIS.IEC_62056_61_2002._IEC_62056_61_Tab_09
      self.__IEC_62056_61_Tab_10 = pyOBIS.IEC_62056_61_2002._IEC_62056_61_Tab_10
      self.__IEC_62056_61_Tab_12 = pyOBIS.IEC_62056_61_2002._IEC_62056_61_Tab_12
      self.__IEC_62056_61_Tab_A1 = pyOBIS.IEC_62056_61_2002._IEC_62056_61_Tab_A1
      self.__IEC_62056_61_Tab_A2 = pyOBIS.IEC_62056_61_2002._IEC_62056_61_Tab_A2
    else:
      raise OBISException("Wrong IEC 62056-61 version.")

    if ( self.__iec_62056_62 == 2002 ):
      self.__IEC_62056_62_Tab_EU = pyOBIS.IEC_62056_62_2002._IEC_62056_62_Tab_EU
    else:
      raise OBISException("Wrong IEC 62056-62 version.")

  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def getUnit(self, Code, encoding="utf-8", errors="strict"):
    """
    @brief   Try to determine a textual description of OBIS unit 'Code'.
    @param   Code      The OBIS unit 'Code' in native, integer or list|tuple of bytes representation
    @param   encoding  encoding of the textual description of OBIS unit 'Code'
    @param   errors    type of error handling during encoding of the textual description of OBIS unit 'Code'
                       (strict, ignore, replace, xmlcharrefreplace, backslashreplace)
    @return  dictionary of integer and native representation and textual description of OBIS unit 'Code'
    """
    if ( not(isinstance(Code, int) and Code >= 0x00 and Code <= 0xFF) ):
      raise OBISException("Could not process OBIS unit '{:X}'.".format(Code))
    if ( self.__iec_62056_62 == 2002 ):
      return {"int"   : Code,
              "native": self.__IEC_62056_62_Tab_EU[Code][0].encode(encoding, errors),
              "descr" : self.__IEC_62056_62_Tab_EU[Code][1].encode(encoding, errors)
             }
    else:
      raise OBISException("Wrong IEC 62056-62 version.")

  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def getDescr(self, Code, encoding="utf-8", errors="strict"):
    """
    @brief   Try to determine a textual description of OBIS identifier 'Code'.
    @param   Code      The OBIS identifier 'Code' in native, integer or list|tuple of bytes representation
    @param   encoding  encoding of the textual description of OBIS identifier 'Code'
    @param   errors    type of error handling during encoding of the textual description of OBIS identifier 'Code'
                       (strict, ignore, replace, xmlcharrefreplace, backslashreplace)
    @return  dictionary of integer and native representation and textual description of OBIS identifier 'Code'
    """
    if   ( self.__iec_62056_61 == 2002 ): return self.__getDescr_2002(Code, encoding, errors)
    else                                : raise OBISException("Wrong IEC 62056-61 version.")

  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def __getDescr_2002(self, Code, encoding="utf-8", errors="strict"):
    """
    @brief   Try to determine a textual description of OBIS identifier 'Code'.
    @param   Code      The OBIS identifier 'Code' in native, integer or list|tuple of bytes representation
    @param   encoding  encoding of the textual description of OBIS identifier 'Code'
    @param   errors    type of error handling during encoding of the textual description of OBIS identifier 'Code'
                       (strict, ignore, replace, xmlcharrefreplace, backslashreplace)
    @return  dictionary of integer and native representation and textual description of OBIS identifier 'Code'
    """
    vObisList = [None, None, None, None, None, None] # OBIS code list representation; value group A ... F
    vObisINum = None                                 # OBIS code integer representation
    vObisNatv = None                                 # OBIS code native representation
    vObisDesc = None                                 # OBIS code description

    # process 'native representation' input
    if ( isinstance(Code, str) ):
      vReOb = re.compile("(?P<A>\d+)-(?P<B>\d+):(?P<C>\d+|C|F|L|P)\.(?P<D>\d+)\.(?P<E>\d+)\*(?P<F>\d+)")
      vReMt = re.match(vReOb, Code)
      if ( None == vReMt ):
        raise OBISException("Could not process OBIS code '{}'.".format(Code))
      else:
        vObisList[0] = int(vReMt.group("A"), 10)
        vObisList[1] = int(vReMt.group("B"), 10)
        try   : vObisList[2] = int(vReMt.group("C"), 10)
        except: vObisList[2] = self.__IEC_62056_61_Tab_A1[vReMt.group("C")]
        vObisList[3] = int(vReMt.group("D"), 10)
        vObisList[4] = int(vReMt.group("E"), 10)
        vObisList[5] = int(vReMt.group("F"), 10)
        try   : bytes(vObisList)
        except: raise OBISException("Could not process OBIS code '{}'.".format(Code))
        vObisINum = (vObisList[0] << 40) + (vObisList[1] << 32) + (vObisList[2] << 24) + (vObisList[3] << 16) + (vObisList[4] << 8) + vObisList[5]
        vObisNatv = "{}-{}:{}.{}.{}*{}".format(vObisList[0], vObisList[1], vObisList[2], vObisList[3], vObisList[4], vObisList[5])
    # process 'integer representation' input
    elif ( isinstance(Code, int) ):
      if ( Code > 0xFFFFFFFFFFFF ):
        raise OBISException("Could not process OBIS code '{:X}'.".format(Code))
      vObisINum = Code
      for i in range(len(vObisList)):
        vObisList[-(i+1)] = Code & 0xFF
        Code              = Code >> 8
      vObisNatv = "{}-{}:{}.{}.{}*{}".format(vObisList[0], vObisList[1], vObisList[2], vObisList[3], vObisList[4], vObisList[5])
    # process 'list/tuple representation' input
    elif ( isinstance(Code, (list,tuple)) and len(Code)==6 ):
      try   : bytes(Code)
      except: raise OBISExceptionOBISException("Could not process OBIS code '{}'.".format(Code))
      vObisList = list(Code[:])
      vObisINum = (vObisList[0] << 40) + (vObisList[1] << 32) + (vObisList[2] << 24) + (vObisList[3] << 16) + (vObisList[4] << 8) + vObisList[5]
      vObisNatv = "{}-{}:{}.{}.{}*{}".format(vObisList[0], vObisList[1], vObisList[2], vObisList[3], vObisList[4], vObisList[5])

    # determine description; abstract codes + General purpose codes (electricity)
    if ( vObisDesc == None ):
      if ( vObisList[0] == 0x00 ):
        for k in self.__IEC_62056_61_Tab_10.keys():
          if True == self.__cmp(k, vObisList):
            vObisDesc = "{} / {} / {}".format(self.__IEC_62056_61_Tab_01[vObisList[0]], self.__IEC_62056_61_Tab_02[vObisList[1]], self.__IEC_62056_61_Tab_10[k])
            break
      elif ( vObisList[0] == 0x01 ):
        for k in self.__IEC_62056_61_Tab_12.keys():
          if ( True == self.__cmp(k, vObisList) ):
            vObisDesc = "{} / {} / {}".format(self.__IEC_62056_61_Tab_01[vObisList[0]], self.__IEC_62056_61_Tab_02[vObisList[1]], self.__IEC_62056_61_Tab_12[k])
            break
    # determine description; general
    if ( vObisDesc == None ):
      vObisDesc = "{} / {}".format(self.__IEC_62056_61_Tab_01[vObisList[0]], self.__IEC_62056_61_Tab_02[vObisList[1]])
      # value group C
      if ( vObisList[0] == 0x00 ):
        vObisDesc = vObisDesc + " / {}".format(self.__IEC_62056_61_Tab_03[vObisList[2]])
      elif ( vObisList[0] == 0x01 ):
        vObisDesc = vObisDesc + " / {}".format(self.__IEC_62056_61_Tab_04[vObisList[2]])
      # value group D
      if ( vObisList[0] == 0x00 and vObisList[2] == 0x5E ):
        vObisDesc = vObisDesc + "/ {}".format(self.__IEC_62056_61_Tab_06[vObisList[3]])
      elif ( vObisList[0] == 0x01 and not (vObisList[2] in [0,96,97,88,99]) ):
        vObisDesc = vObisDesc + " / {}".format(self.__IEC_62056_61_Tab_05[vObisList[3]])
      # value group E
      if ( vObisList[0] == 0x01 and vObisList[2] in [31,51,71,32,52,72] and vObisList[3] == 7 ):
        vObisDesc = vObisDesc + " / {}".format(self.__IEC_62056_61_Tab_08[vObisList[4]])
      elif ( vObisList[0] == 0x01 and vObisList[2] in [81] and vObisList[3] == 7 ):
        vObisDesc = vObisDesc + " / {}".format(self.__IEC_62056_61_Tab_09[vObisList[4]])
      elif ( vObisList[0] == 0x01 ):
        vObisDesc = vObisDesc + " / {}".format(self.__IEC_62056_61_Tab_07[vObisList[4]])
      # value group F
      if ( vObisList[0] == 0x01 and vObisList[2] in range(1,100) and vObisList[3] in [3,6,8,9,10,11,12,13,16,21,22,23,26] and vObisList[5] >= 0 and vObisList[5] < 100 ):
        vObisDesc = vObisDesc + " / {}".format(self.__IEC_62056_61_Tab_A2[vObisList[5]])

    return {"int":vObisINum, "native":vObisNatv, "descr":vObisDesc.encode(encoding, errors)}

  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def __cmp(self, ListA, ListB, Both=False):
    """
    @brief   Compare non-'None' elements of 'ListA' with corresponding elements of 'ListB' or
             compare corresponding elements of both lists only if both elements are non-'None'.
    @param   ListA   list A
    @param   ListB   list B
    @param   Mode    'False' = compare non-'None' elements of 'ListA' with corresponding elements of 'ListB'
                     'True'  = compare corresponding elements of 'ListA' and 'ListB' if both elements are non-'None'
    @return  True if all compared, corresponding elements are equal, False otherwise
    """
    if ( len(ListA) != len(ListB) ):
      return False
    else:
      if ( Both == True ):
        for a,b in zip(ListA, ListB):
          if ( a != None and b != None and a != b ):
            return False
      else:
        for a,b in zip(ListA, ListB):
          if ( a != None and a != b ):
            return False
      return True

########################################################################################################################
########################################################################################################################
########################################################################################################################

if ( __name__ == '__main__' ):
  pass
