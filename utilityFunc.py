import os

KERNEL_TYPE_MAP = {\
    'byte': 'char',\
    'ubyte': 'unsigned char',\
    'short': 'short',\
    'ushort': 'unsigned short',\
    'int': 'int',\
    'uint': 'unsigned int',\
    'float': 'float',\
    'ufloat': 'unsigned float',\
    'string': 'char*'\
}

def splitNameToWords(strName):
    lstSplitWords = []
    idxBegin = -1
    for idx, c in enumerate(strName):
        if c.isupper():
            if idxBegin >= 0:
                w = strName[idxBegin:idx]
                lstSplitWords.append(w)
            idxBegin = idx
        if idx == (len(strName)-1):
            w = strName[idxBegin:]
            lstSplitWords.append(w)
    return lstSplitWords

def getStructFileName(strName, strFolder=None):
    lstSplitWords = splitNameToWords(strName)
    ret = ''
    for w in lstSplitWords:
        ret += w.lower()
        ret += '_'
    ret += 'structs.h'

    if strFolder is not None:
        if not os.path.exists(strFolder):
            os.makedirs(strFolder)
        return os.path.join(strFolder, ret)
    else:
        return ret

def getKernelFileName(strName, strFolder=None):
    lstSplitWords = splitNameToWords(strName)
    ret = ''
    for w in lstSplitWords:
        ret += w.lower()
        if w != lstSplitWords[-1]:
            ret += '_'
    ret += '.c'

    if strFolder is not None:
        if not os.path.exists(strFolder):
            os.makedirs(strFolder)
        return os.path.join(strFolder, ret)
    else:
        return ret

def getKernelType(dataType):
    return KERNEL_TYPE_MAP[dataType] if dataType in KERNEL_TYPE_MAP else None