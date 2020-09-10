# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v5.proto.resources import video_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_video__pb2
from google.ads.google_ads.v5.proto.services import video_service_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_video__service__pb2


class VideoServiceStub(object):
    """Proto file describing the Video service.

    Service to manage videos.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetVideo = channel.unary_unary(
                '/google.ads.googleads.v5.services.VideoService/GetVideo',
                request_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_video__service__pb2.GetVideoRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_video__pb2.Video.FromString,
                )


class VideoServiceServicer(object):
    """Proto file describing the Video service.

    Service to manage videos.
    """

    def GetVideo(self, request, context):
        """Returns the requested video in full detail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VideoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetVideo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVideo,
                    request_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_video__service__pb2.GetVideoRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_video__pb2.Video.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v5.services.VideoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VideoService(object):
    """Proto file describing the Video service.

    Service to manage videos.
    """

    @staticmethod
    def GetVideo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v5.services.VideoService/GetVideo',
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_video__service__pb2.GetVideoRequest.SerializeToString,
            google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_video__pb2.Video.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)