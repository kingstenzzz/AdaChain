# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blockchain.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x62lockchain.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\";\n\rAppendRequest\x12\x15\n\rleader_commit\x18\x01 \x01(\x04\x12\x13\n\x0blog_entries\x18\x02 \x03(\x0c\"\x10\n\x0e\x41ppendResponse\"\'\n\x13PrepopulateResponse\x12\x10\n\x08num_keys\x18\x01 \x01(\x04\"J\n\x08ReadItem\x12\x10\n\x08read_key\x18\x01 \x01(\x0c\x12\x15\n\rblock_seq_num\x18\x02 \x01(\x04\x12\x15\n\rtrans_seq_num\x18\x03 \x01(\x04\"3\n\tWriteItem\x12\x11\n\twrite_key\x18\x01 \x01(\x0c\x12\x13\n\x0bwrite_value\x18\x02 \x01(\x0c\"\xc2\x02\n\x0b\x45ndorsement\x12\x1b\n\x08read_set\x18\x01 \x03(\x0b\x32\t.ReadItem\x12\x1d\n\twrite_set\x18\x02 \x03(\x0b\x32\n.WriteItem\x12\x16\n\x0etransaction_id\x18\x03 \x01(\x0c\x12\x13\n\x0b\x65ndorser_id\x18\x04 \x01(\x04\x12\x1a\n\x12\x65ndorser_signature\x18\x05 \x01(\x0c\x12\x0f\n\x07\x61\x62orted\x18\x06 \x01(\x08\x12/\n\x0breceived_ts\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x12\x65xecution_start_ts\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10\x65xecution_end_ts\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xb2\x02\n\x13TransactionProposal\x12\'\n\x04type\x18\x01 \x01(\x0e\x32\x19.TransactionProposal.Type\x12\x0c\n\x04keys\x18\x02 \x03(\t\x12\x0e\n\x06values\x18\x03 \x03(\x0c\x12\x17\n\x0f\x65xecution_delay\x18\x04 \x01(\x04\x12/\n\x0breceived_ts\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\n\n\x02id\x18\x06 \x01(\x04\"~\n\x04Type\x12\x07\n\x03Get\x10\x00\x12\x07\n\x03Put\x10\x01\x12\x13\n\x0fTransactSavings\x10\x02\x12\x13\n\x0f\x44\x65positChecking\x10\x03\x12\x0f\n\x0bSendPayment\x10\x04\x12\x0e\n\nWriteCheck\x10\x05\x12\x0e\n\nAmalgamate\x10\x06\x12\t\n\x05Query\x10\x07\"T\n\x07Request\x12!\n\x0b\x65ndorsement\x18\x01 \x01(\x0b\x32\x0c.Endorsement\x12&\n\x08proposal\x18\x02 \x01(\x0b\x32\x14.TransactionProposal\"V\n\x05\x42lock\x12\"\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x0c.Endorsement\x12\x10\n\x08\x62lock_id\x18\x02 \x01(\x04\x12\x17\n\x0fprev_block_hash\x18\x03 \x01(\t\"E\n\x06\x41\x63tion\x12\x11\n\tblocksize\x18\x01 \x01(\x04\x12\x17\n\x0f\x65\x61rly_execution\x18\x02 \x01(\x08\x12\x0f\n\x07reorder\x18\x03 \x01(\x08\"P\n\x0cWatermarkLow\x12\x12\n\nthroughput\x18\x01 \x01(\x01\x12\x16\n\x0e\x62lock_id_start\x18\x02 \x01(\x04\x12\x14\n\x0c\x62lock_id_now\x18\x03 \x01(\x04\"\x98\x01\n\rAgentExchange\x12\x12\n\noriginator\x18\x01 \x01(\t\x12\x13\n\x0bwrite_ratio\x18\x02 \x01(\x01\x12\x15\n\rhot_key_ratio\x18\x03 \x01(\x01\x12\x1a\n\x12trans_arrival_rate\x18\x04 \x01(\x01\x12\x17\n\x0f\x65xecution_delay\x18\x05 \x01(\x01\x12\x12\n\nthroughput\x18\x06 \x01(\x01\"L\n\x0cPeerExchange\x12\x13\n\x0b\x62lock_index\x18\x01 \x01(\x04\x12\x12\n\nraft_index\x18\x02 \x01(\x04\x12\x13\n\x0bno_progress\x18\x03 \x01(\x08\")\n\x0bTaggedEntry\x12\x0b\n\x03tag\x18\x01 \x01(\x04\x12\r\n\x05\x65ntry\x18\x02 \x01(\x0c\x32\xac\x05\n\x08PeerComm\x12\x33\n\x0e\x61ppend_entries\x12\x0e.AppendRequest\x1a\x0f.AppendResponse\"\x00\x12\x32\n\x0csend_to_peer\x12\x08.Request\x1a\x16.google.protobuf.Empty\"\x00\x12;\n\x13send_to_peer_stream\x12\x08.Request\x1a\x16.google.protobuf.Empty\"\x00(\x01\x12;\n\x0bprepopulate\x12\x14.TransactionProposal\x1a\x14.PrepopulateResponse\"\x00\x12\x46\n\x12start_benchmarking\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12\x44\n\x10\x65nd_benchmarking\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12\x35\n\x10new_episode_info\x12\x07.Action\x1a\x16.google.protobuf.Empty\"\x00\x12;\n\x07timeout\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12?\n\x14\x65xchange_block_index\x12\r.PeerExchange\x1a\x16.google.protobuf.Empty\"\x00\x12\x41\n\x16resume_block_formation\x12\r.PeerExchange\x1a\x16.google.protobuf.Empty\"\x00\x12\x37\n\x15reached_new_watermark\x12\r.PeerExchange\x1a\r.PeerExchange\"\x00\x32\xc4\x01\n\tAgentComm\x12@\n\x15reached_watermark_low\x12\r.WatermarkLow\x1a\x16.google.protobuf.Empty\"\x00\x12;\n\x0fsend_preprepare\x12\x0e.AgentExchange\x1a\x16.google.protobuf.Empty\"\x00\x12\x38\n\x0csend_prepare\x12\x0e.AgentExchange\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')



_APPENDREQUEST = DESCRIPTOR.message_types_by_name['AppendRequest']
_APPENDRESPONSE = DESCRIPTOR.message_types_by_name['AppendResponse']
_PREPOPULATERESPONSE = DESCRIPTOR.message_types_by_name['PrepopulateResponse']
_READITEM = DESCRIPTOR.message_types_by_name['ReadItem']
_WRITEITEM = DESCRIPTOR.message_types_by_name['WriteItem']
_ENDORSEMENT = DESCRIPTOR.message_types_by_name['Endorsement']
_TRANSACTIONPROPOSAL = DESCRIPTOR.message_types_by_name['TransactionProposal']
_REQUEST = DESCRIPTOR.message_types_by_name['Request']
_BLOCK = DESCRIPTOR.message_types_by_name['Block']
_ACTION = DESCRIPTOR.message_types_by_name['Action']
_WATERMARKLOW = DESCRIPTOR.message_types_by_name['WatermarkLow']
_AGENTEXCHANGE = DESCRIPTOR.message_types_by_name['AgentExchange']
_PEEREXCHANGE = DESCRIPTOR.message_types_by_name['PeerExchange']
_TAGGEDENTRY = DESCRIPTOR.message_types_by_name['TaggedEntry']
_TRANSACTIONPROPOSAL_TYPE = _TRANSACTIONPROPOSAL.enum_types_by_name['Type']
AppendRequest = _reflection.GeneratedProtocolMessageType('AppendRequest', (_message.Message,), {
  'DESCRIPTOR' : _APPENDREQUEST,
  '__module__' : 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:AppendRequest)
  })
_sym_db.RegisterMessage(AppendRequest)

AppendResponse = _reflection.GeneratedProtocolMessageType('AppendResponse', (_message.Message,), {
  'DESCRIPTOR' : _APPENDRESPONSE,
  '__module__' : 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:AppendResponse)
  })
_sym_db.RegisterMessage(AppendResponse)

PrepopulateResponse = _reflection.GeneratedProtocolMessageType('PrepopulateResponse', (_message.Message,), {
  'DESCRIPTOR' : _PREPOPULATERESPONSE,
  '__module__' : 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:PrepopulateResponse)
  })
_sym_db.RegisterMessage(PrepopulateResponse)

ReadItem = _reflection.GeneratedProtocolMessageType('ReadItem', (_message.Message,), {
  'DESCRIPTOR' : _READITEM,
  '__module__' : 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:ReadItem)
  })
_sym_db.RegisterMessage(ReadItem)

WriteItem = _reflection.GeneratedProtocolMessageType('WriteItem', (_message.Message,), {
  'DESCRIPTOR' : _WRITEITEM,
  '__module__' : 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:WriteItem)
  })
_sym_db.RegisterMessage(WriteItem)

Endorsement = _reflection.GeneratedProtocolMessageType('Endorsement', (_message.Message,), {
  'DESCRIPTOR' : _ENDORSEMENT,
  '__module__' : 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:Endorsement)
  })
_sym_db.RegisterMessage(Endorsement)

TransactionProposal = _reflection.GeneratedProtocolMessageType('TransactionProposal', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONPROPOSAL,
  '__module__' : 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:TransactionProposal)
  })
_sym_db.RegisterMessage(TransactionProposal)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  })
_sym_db.RegisterMessage(Request)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:Block)
  })
_sym_db.RegisterMessage(Block)

Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), {
  'DESCRIPTOR' : _ACTION,
  '__module__' : 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:Action)
  })
_sym_db.RegisterMessage(Action)

WatermarkLow = _reflection.GeneratedProtocolMessageType('WatermarkLow', (_message.Message,), {
  'DESCRIPTOR' : _WATERMARKLOW,
  '__module__' : 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:WatermarkLow)
  })
_sym_db.RegisterMessage(WatermarkLow)

AgentExchange = _reflection.GeneratedProtocolMessageType('AgentExchange', (_message.Message,), {
  'DESCRIPTOR' : _AGENTEXCHANGE,
  '__module__' : 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:AgentExchange)
  })
_sym_db.RegisterMessage(AgentExchange)

PeerExchange = _reflection.GeneratedProtocolMessageType('PeerExchange', (_message.Message,), {
  'DESCRIPTOR' : _PEEREXCHANGE,
  '__module__' : 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:PeerExchange)
  })
_sym_db.RegisterMessage(PeerExchange)

TaggedEntry = _reflection.GeneratedProtocolMessageType('TaggedEntry', (_message.Message,), {
  'DESCRIPTOR' : _TAGGEDENTRY,
  '__module__' : 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:TaggedEntry)
  })
_sym_db.RegisterMessage(TaggedEntry)

_PEERCOMM = DESCRIPTOR.services_by_name['PeerComm']
_AGENTCOMM = DESCRIPTOR.services_by_name['AgentComm']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _APPENDREQUEST._serialized_start=82
  _APPENDREQUEST._serialized_end=141
  _APPENDRESPONSE._serialized_start=143
  _APPENDRESPONSE._serialized_end=159
  _PREPOPULATERESPONSE._serialized_start=161
  _PREPOPULATERESPONSE._serialized_end=200
  _READITEM._serialized_start=202
  _READITEM._serialized_end=276
  _WRITEITEM._serialized_start=278
  _WRITEITEM._serialized_end=329
  _ENDORSEMENT._serialized_start=332
  _ENDORSEMENT._serialized_end=654
  _TRANSACTIONPROPOSAL._serialized_start=657
  _TRANSACTIONPROPOSAL._serialized_end=963
  _TRANSACTIONPROPOSAL_TYPE._serialized_start=837
  _TRANSACTIONPROPOSAL_TYPE._serialized_end=963
  _REQUEST._serialized_start=965
  _REQUEST._serialized_end=1049
  _BLOCK._serialized_start=1051
  _BLOCK._serialized_end=1137
  _ACTION._serialized_start=1139
  _ACTION._serialized_end=1208
  _WATERMARKLOW._serialized_start=1210
  _WATERMARKLOW._serialized_end=1290
  _AGENTEXCHANGE._serialized_start=1293
  _AGENTEXCHANGE._serialized_end=1445
  _PEEREXCHANGE._serialized_start=1447
  _PEEREXCHANGE._serialized_end=1523
  _TAGGEDENTRY._serialized_start=1525
  _TAGGEDENTRY._serialized_end=1566
  _PEERCOMM._serialized_start=1569
  _PEERCOMM._serialized_end=2253
  _AGENTCOMM._serialized_start=2256
  _AGENTCOMM._serialized_end=2452
# @@protoc_insertion_point(module_scope)
