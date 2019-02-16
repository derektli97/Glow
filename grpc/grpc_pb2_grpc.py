# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import grpc_pb2 as grpc__pb2


class GlowStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.TestPointReceiving = channel.unary_unary(
        '/glow.Glow/TestPointReceiving',
        request_serializer=grpc__pb2.PointRequest.SerializeToString,
        response_deserializer=grpc__pb2.GlowReply.FromString,
        )


class GlowServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def TestPointReceiving(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GlowServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'TestPointReceiving': grpc.unary_unary_rpc_method_handler(
          servicer.TestPointReceiving,
          request_deserializer=grpc__pb2.PointRequest.FromString,
          response_serializer=grpc__pb2.GlowReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'glow.Glow', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
