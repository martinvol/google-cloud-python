# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grafeas_v1/proto/cvss.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="grafeas_v1/proto/cvss.proto",
    package="grafeas.v1",
    syntax="proto3",
    serialized_options=_b(
        "\n\rio.grafeas.v1P\001Z8google.golang.org/genproto/googleapis/grafeas/v1;grafeas\242\002\003GRA"
    ),
    serialized_pb=_b(
        '\n\x1bgrafeas_v1/proto/cvss.proto\x12\ngrafeas.v1"\xc5\t\n\x06\x43VSSv3\x12\x12\n\nbase_score\x18\x01 \x01(\x02\x12\x1c\n\x14\x65xploitability_score\x18\x02 \x01(\x02\x12\x14\n\x0cimpact_score\x18\x03 \x01(\x02\x12\x36\n\rattack_vector\x18\x05 \x01(\x0e\x32\x1f.grafeas.v1.CVSSv3.AttackVector\x12>\n\x11\x61ttack_complexity\x18\x06 \x01(\x0e\x32#.grafeas.v1.CVSSv3.AttackComplexity\x12\x42\n\x13privileges_required\x18\x07 \x01(\x0e\x32%.grafeas.v1.CVSSv3.PrivilegesRequired\x12<\n\x10user_interaction\x18\x08 \x01(\x0e\x32".grafeas.v1.CVSSv3.UserInteraction\x12\'\n\x05scope\x18\t \x01(\x0e\x32\x18.grafeas.v1.CVSSv3.Scope\x12\x39\n\x16\x63onfidentiality_impact\x18\n \x01(\x0e\x32\x19.grafeas.v1.CVSSv3.Impact\x12\x33\n\x10integrity_impact\x18\x0b \x01(\x0e\x32\x19.grafeas.v1.CVSSv3.Impact\x12\x36\n\x13\x61vailability_impact\x18\x0c \x01(\x0e\x32\x19.grafeas.v1.CVSSv3.Impact"\x99\x01\n\x0c\x41ttackVector\x12\x1d\n\x19\x41TTACK_VECTOR_UNSPECIFIED\x10\x00\x12\x19\n\x15\x41TTACK_VECTOR_NETWORK\x10\x01\x12\x1a\n\x16\x41TTACK_VECTOR_ADJACENT\x10\x02\x12\x17\n\x13\x41TTACK_VECTOR_LOCAL\x10\x03\x12\x1a\n\x16\x41TTACK_VECTOR_PHYSICAL\x10\x04"l\n\x10\x41ttackComplexity\x12!\n\x1d\x41TTACK_COMPLEXITY_UNSPECIFIED\x10\x00\x12\x19\n\x15\x41TTACK_COMPLEXITY_LOW\x10\x01\x12\x1a\n\x16\x41TTACK_COMPLEXITY_HIGH\x10\x02"\x92\x01\n\x12PrivilegesRequired\x12#\n\x1fPRIVILEGES_REQUIRED_UNSPECIFIED\x10\x00\x12\x1c\n\x18PRIVILEGES_REQUIRED_NONE\x10\x01\x12\x1b\n\x17PRIVILEGES_REQUIRED_LOW\x10\x02\x12\x1c\n\x18PRIVILEGES_REQUIRED_HIGH\x10\x03"m\n\x0fUserInteraction\x12 \n\x1cUSER_INTERACTION_UNSPECIFIED\x10\x00\x12\x19\n\x15USER_INTERACTION_NONE\x10\x01\x12\x1d\n\x19USER_INTERACTION_REQUIRED\x10\x02"F\n\x05Scope\x12\x15\n\x11SCOPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fSCOPE_UNCHANGED\x10\x01\x12\x11\n\rSCOPE_CHANGED\x10\x02"R\n\x06Impact\x12\x16\n\x12IMPACT_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIMPACT_HIGH\x10\x01\x12\x0e\n\nIMPACT_LOW\x10\x02\x12\x0f\n\x0bIMPACT_NONE\x10\x03\x42Q\n\rio.grafeas.v1P\x01Z8google.golang.org/genproto/googleapis/grafeas/v1;grafeas\xa2\x02\x03GRAb\x06proto3'
    ),
)


_CVSSV3_ATTACKVECTOR = _descriptor.EnumDescriptor(
    name="AttackVector",
    full_name="grafeas.v1.CVSSv3.AttackVector",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="ATTACK_VECTOR_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="ATTACK_VECTOR_NETWORK",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="ATTACK_VECTOR_ADJACENT",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="ATTACK_VECTOR_LOCAL",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="ATTACK_VECTOR_PHYSICAL",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=586,
    serialized_end=739,
)
_sym_db.RegisterEnumDescriptor(_CVSSV3_ATTACKVECTOR)

_CVSSV3_ATTACKCOMPLEXITY = _descriptor.EnumDescriptor(
    name="AttackComplexity",
    full_name="grafeas.v1.CVSSv3.AttackComplexity",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="ATTACK_COMPLEXITY_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="ATTACK_COMPLEXITY_LOW",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="ATTACK_COMPLEXITY_HIGH",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=741,
    serialized_end=849,
)
_sym_db.RegisterEnumDescriptor(_CVSSV3_ATTACKCOMPLEXITY)

_CVSSV3_PRIVILEGESREQUIRED = _descriptor.EnumDescriptor(
    name="PrivilegesRequired",
    full_name="grafeas.v1.CVSSv3.PrivilegesRequired",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="PRIVILEGES_REQUIRED_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIVILEGES_REQUIRED_NONE",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIVILEGES_REQUIRED_LOW",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRIVILEGES_REQUIRED_HIGH",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=852,
    serialized_end=998,
)
_sym_db.RegisterEnumDescriptor(_CVSSV3_PRIVILEGESREQUIRED)

_CVSSV3_USERINTERACTION = _descriptor.EnumDescriptor(
    name="UserInteraction",
    full_name="grafeas.v1.CVSSv3.UserInteraction",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="USER_INTERACTION_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="USER_INTERACTION_NONE",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="USER_INTERACTION_REQUIRED",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1000,
    serialized_end=1109,
)
_sym_db.RegisterEnumDescriptor(_CVSSV3_USERINTERACTION)

_CVSSV3_SCOPE = _descriptor.EnumDescriptor(
    name="Scope",
    full_name="grafeas.v1.CVSSv3.Scope",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="SCOPE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="SCOPE_UNCHANGED",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="SCOPE_CHANGED", index=2, number=2, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1111,
    serialized_end=1181,
)
_sym_db.RegisterEnumDescriptor(_CVSSV3_SCOPE)

_CVSSV3_IMPACT = _descriptor.EnumDescriptor(
    name="Impact",
    full_name="grafeas.v1.CVSSv3.Impact",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="IMPACT_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="IMPACT_HIGH", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="IMPACT_LOW", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="IMPACT_NONE", index=3, number=3, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1183,
    serialized_end=1265,
)
_sym_db.RegisterEnumDescriptor(_CVSSV3_IMPACT)


_CVSSV3 = _descriptor.Descriptor(
    name="CVSSv3",
    full_name="grafeas.v1.CVSSv3",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="base_score",
            full_name="grafeas.v1.CVSSv3.base_score",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="exploitability_score",
            full_name="grafeas.v1.CVSSv3.exploitability_score",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="impact_score",
            full_name="grafeas.v1.CVSSv3.impact_score",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="attack_vector",
            full_name="grafeas.v1.CVSSv3.attack_vector",
            index=3,
            number=5,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="attack_complexity",
            full_name="grafeas.v1.CVSSv3.attack_complexity",
            index=4,
            number=6,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="privileges_required",
            full_name="grafeas.v1.CVSSv3.privileges_required",
            index=5,
            number=7,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="user_interaction",
            full_name="grafeas.v1.CVSSv3.user_interaction",
            index=6,
            number=8,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="scope",
            full_name="grafeas.v1.CVSSv3.scope",
            index=7,
            number=9,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="confidentiality_impact",
            full_name="grafeas.v1.CVSSv3.confidentiality_impact",
            index=8,
            number=10,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="integrity_impact",
            full_name="grafeas.v1.CVSSv3.integrity_impact",
            index=9,
            number=11,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="availability_impact",
            full_name="grafeas.v1.CVSSv3.availability_impact",
            index=10,
            number=12,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[
        _CVSSV3_ATTACKVECTOR,
        _CVSSV3_ATTACKCOMPLEXITY,
        _CVSSV3_PRIVILEGESREQUIRED,
        _CVSSV3_USERINTERACTION,
        _CVSSV3_SCOPE,
        _CVSSV3_IMPACT,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=44,
    serialized_end=1265,
)

_CVSSV3.fields_by_name["attack_vector"].enum_type = _CVSSV3_ATTACKVECTOR
_CVSSV3.fields_by_name["attack_complexity"].enum_type = _CVSSV3_ATTACKCOMPLEXITY
_CVSSV3.fields_by_name["privileges_required"].enum_type = _CVSSV3_PRIVILEGESREQUIRED
_CVSSV3.fields_by_name["user_interaction"].enum_type = _CVSSV3_USERINTERACTION
_CVSSV3.fields_by_name["scope"].enum_type = _CVSSV3_SCOPE
_CVSSV3.fields_by_name["confidentiality_impact"].enum_type = _CVSSV3_IMPACT
_CVSSV3.fields_by_name["integrity_impact"].enum_type = _CVSSV3_IMPACT
_CVSSV3.fields_by_name["availability_impact"].enum_type = _CVSSV3_IMPACT
_CVSSV3_ATTACKVECTOR.containing_type = _CVSSV3
_CVSSV3_ATTACKCOMPLEXITY.containing_type = _CVSSV3
_CVSSV3_PRIVILEGESREQUIRED.containing_type = _CVSSV3
_CVSSV3_USERINTERACTION.containing_type = _CVSSV3
_CVSSV3_SCOPE.containing_type = _CVSSV3
_CVSSV3_IMPACT.containing_type = _CVSSV3
DESCRIPTOR.message_types_by_name["CVSSv3"] = _CVSSV3
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CVSSv3 = _reflection.GeneratedProtocolMessageType(
    "CVSSv3",
    (_message.Message,),
    dict(
        DESCRIPTOR=_CVSSV3,
        __module__="grafeas_v1.proto.cvss_pb2",
        __doc__="""Common Vulnerability Scoring System version 3. For
  details, see https://www.first.org/cvss/specification-document
  
  
  Attributes:
      base_score:
          The base score is a function of the base metric scores.
      attack_vector:
          Base Metrics Represents the intrinsic characteristics of a
          vulnerability that are constant over time and across user
          environments.
  """,
        # @@protoc_insertion_point(class_scope:grafeas.v1.CVSSv3)
    ),
)
_sym_db.RegisterMessage(CVSSv3)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
