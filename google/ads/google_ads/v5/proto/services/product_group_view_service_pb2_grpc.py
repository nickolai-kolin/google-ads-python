# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v5.proto.resources import product_group_view_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_product__group__view__pb2
from google.ads.google_ads.v5.proto.services import product_group_view_service_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_product__group__view__service__pb2


class ProductGroupViewServiceStub(object):
    """Proto file describing the ProductGroup View service.

    Service to manage product group views.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetProductGroupView = channel.unary_unary(
                '/google.ads.googleads.v5.services.ProductGroupViewService/GetProductGroupView',
                request_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_product__group__view__service__pb2.GetProductGroupViewRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_product__group__view__pb2.ProductGroupView.FromString,
                )


class ProductGroupViewServiceServicer(object):
    """Proto file describing the ProductGroup View service.

    Service to manage product group views.
    """

    def GetProductGroupView(self, request, context):
        """Returns the requested product group view in full detail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductGroupViewServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetProductGroupView': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProductGroupView,
                    request_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_product__group__view__service__pb2.GetProductGroupViewRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_product__group__view__pb2.ProductGroupView.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v5.services.ProductGroupViewService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProductGroupViewService(object):
    """Proto file describing the ProductGroup View service.

    Service to manage product group views.
    """

    @staticmethod
    def GetProductGroupView(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v5.services.ProductGroupViewService/GetProductGroupView',
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_product__group__view__service__pb2.GetProductGroupViewRequest.SerializeToString,
            google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_product__group__view__pb2.ProductGroupView.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
