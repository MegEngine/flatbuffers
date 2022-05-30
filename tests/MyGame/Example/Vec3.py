# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Example

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Vec3(object):
    __slots__ = ['_tab']

    @classmethod
    def SizeOf(cls):
        return 32

    # Vec3
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Vec3
    def X(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # Vec3
    def Y(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(4))
    # Vec3
    def Z(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(8))
    # Vec3
    def Test1(self): return self._tab.Get(flatbuffers.number_types.Float64Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(16))
    # Vec3
    def Test2(self): return self._tab.Get(flatbuffers.number_types.Uint8Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(24))
    # Vec3
    def Test3(self, obj):
        obj.Init(self._tab.Bytes, self._tab.Pos + 26)
        return obj


def CreateVec3(builder, x, y, z, test1, test2, test3_a, test3_b):
    builder.Prep(8, 32)
    builder.Pad(2)
    builder.Prep(2, 4)
    builder.Pad(1)
    builder.PrependInt8(test3_b)
    builder.PrependInt16(test3_a)
    builder.Pad(1)
    builder.PrependUint8(test2)
    builder.PrependFloat64(test1)
    builder.Pad(4)
    builder.PrependFloat32(z)
    builder.PrependFloat32(y)
    builder.PrependFloat32(x)
    return builder.Offset()

import MyGame.Example.Test
try:
    from typing import Optional
except:
    pass

class Vec3T(object):

    # Vec3T
    def __init__(self):
        self.x = 0.0  # type: float
        self.y = 0.0  # type: float
        self.z = 0.0  # type: float
        self.test1 = 0.0  # type: float
        self.test2 = 0  # type: int
        self.test3 = None  # type: Optional[MyGame.Example.Test.TestT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        vec3 = Vec3()
        vec3.Init(buf, pos)
        return cls.InitFromObj(vec3)

    @classmethod
    def InitFromObj(cls, vec3):
        x = Vec3T()
        x._UnPack(vec3)
        return x

    # Vec3T
    def _UnPack(self, vec3):
        if vec3 is None:
            return
        self.x = vec3.X()
        self.y = vec3.Y()
        self.z = vec3.Z()
        self.test1 = vec3.Test1()
        self.test2 = vec3.Test2()
        if vec3.Test3(MyGame.Example.Test.Test()) is not None:
            self.test3 = MyGame.Example.Test.TestT.InitFromObj(vec3.Test3(MyGame.Example.Test.Test()))

    # Vec3T
    def Pack(self, builder):
        return CreateVec3(builder, self.x, self.y, self.z, self.test1, self.test2, self.test3.a, self.test3.b)
