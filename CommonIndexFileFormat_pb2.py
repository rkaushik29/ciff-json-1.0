# Protoc compiler code. READ-ONLY
# Definition: CommonIndexFileFormat.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='CommonIndexFileFormat.proto',
  package='io.osirrc.ciff',
  syntax='proto3',
  serialized_pb=_b('\n\x1b\x43ommonIndexFileFormat.proto\x12\x0eio.osirrc.ciff\"\xcc\x01\n\x06Header\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x1a\n\x12num_postings_lists\x18\x02 \x01(\x05\x12\x10\n\x08num_docs\x18\x03 \x01(\x05\x12\x1c\n\x14total_postings_lists\x18\x04 \x01(\x05\x12\x12\n\ntotal_docs\x18\x05 \x01(\x05\x12!\n\x19total_terms_in_collection\x18\x06 \x01(\x03\x12\x19\n\x11\x61verage_doclength\x18\x07 \x01(\x01\x12\x13\n\x0b\x64\x65scription\x18\x08 \x01(\t\"$\n\x07Posting\x12\r\n\x05\x64ocid\x18\x01 \x01(\x05\x12\n\n\x02tf\x18\x02 \x01(\x05\"_\n\x0cPostingsList\x12\x0c\n\x04term\x18\x01 \x01(\t\x12\n\n\x02\x64\x66\x18\x02 \x01(\x03\x12\n\n\x02\x63\x66\x18\x03 \x01(\x03\x12)\n\x08postings\x18\x04 \x03(\x0b\x32\x17.io.osirrc.ciff.Posting\"G\n\tDocRecord\x12\r\n\x05\x64ocid\x18\x01 \x01(\x05\x12\x18\n\x10\x63ollection_docid\x18\x02 \x01(\t\x12\x11\n\tdoclength\x18\x03 \x01(\x05\x62\x06proto3')
)




_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='io.osirrc.ciff.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='io.osirrc.ciff.Header.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_postings_lists', full_name='io.osirrc.ciff.Header.num_postings_lists', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_docs', full_name='io.osirrc.ciff.Header.num_docs', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_postings_lists', full_name='io.osirrc.ciff.Header.total_postings_lists', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_docs', full_name='io.osirrc.ciff.Header.total_docs', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_terms_in_collection', full_name='io.osirrc.ciff.Header.total_terms_in_collection', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='average_doclength', full_name='io.osirrc.ciff.Header.average_doclength', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='io.osirrc.ciff.Header.description', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=252,
)


_POSTING = _descriptor.Descriptor(
  name='Posting',
  full_name='io.osirrc.ciff.Posting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='docid', full_name='io.osirrc.ciff.Posting.docid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tf', full_name='io.osirrc.ciff.Posting.tf', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=254,
  serialized_end=290,
)


_POSTINGSLIST = _descriptor.Descriptor(
  name='PostingsList',
  full_name='io.osirrc.ciff.PostingsList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='term', full_name='io.osirrc.ciff.PostingsList.term', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='df', full_name='io.osirrc.ciff.PostingsList.df', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cf', full_name='io.osirrc.ciff.PostingsList.cf', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='postings', full_name='io.osirrc.ciff.PostingsList.postings', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=292,
  serialized_end=387,
)


_DOCRECORD = _descriptor.Descriptor(
  name='DocRecord',
  full_name='io.osirrc.ciff.DocRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='docid', full_name='io.osirrc.ciff.DocRecord.docid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='collection_docid', full_name='io.osirrc.ciff.DocRecord.collection_docid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doclength', full_name='io.osirrc.ciff.DocRecord.doclength', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=389,
  serialized_end=460,
)

_POSTINGSLIST.fields_by_name['postings'].message_type = _POSTING
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['Posting'] = _POSTING
DESCRIPTOR.message_types_by_name['PostingsList'] = _POSTINGSLIST
DESCRIPTOR.message_types_by_name['DocRecord'] = _DOCRECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
  DESCRIPTOR = _HEADER,
  __module__ = 'CommonIndexFileFormat_pb2'
  # @@protoc_insertion_point(class_scope:io.osirrc.ciff.Header)
  ))
_sym_db.RegisterMessage(Header)

Posting = _reflection.GeneratedProtocolMessageType('Posting', (_message.Message,), dict(
  DESCRIPTOR = _POSTING,
  __module__ = 'CommonIndexFileFormat_pb2'
  # @@protoc_insertion_point(class_scope:io.osirrc.ciff.Posting)
  ))
_sym_db.RegisterMessage(Posting)

PostingsList = _reflection.GeneratedProtocolMessageType('PostingsList', (_message.Message,), dict(
  DESCRIPTOR = _POSTINGSLIST,
  __module__ = 'CommonIndexFileFormat_pb2'
  # @@protoc_insertion_point(class_scope:io.osirrc.ciff.PostingsList)
  ))
_sym_db.RegisterMessage(PostingsList)

DocRecord = _reflection.GeneratedProtocolMessageType('DocRecord', (_message.Message,), dict(
  DESCRIPTOR = _DOCRECORD,
  __module__ = 'CommonIndexFileFormat_pb2'
  # @@protoc_insertion_point(class_scope:io.osirrc.ciff.DocRecord)
  ))
_sym_db.RegisterMessage(DocRecord)


# @@protoc_insertion_point(module_scope)