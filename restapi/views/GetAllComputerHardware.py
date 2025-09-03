from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from restapi.models import ComputerHardwareModel
from restapi.serializers import ComputerHardwareSerializer


class GetAllComputerHardwareView(ListAPIView):
    serializer_class = ComputerHardwareSerializer

    def get(self, request, *args, **kwargs):
        try:
            hardwares = ComputerHardwareModel.objects.all()
            hardware_serializer = ComputerHardwareSerializer(hardwares, many = True)
            return Response({
                'response_code': 200,
                'message': "Successfully Fetched",
                'statusFlag': True,
                'status': "SUCCESS",
                'errorDetails': None,
                'data': hardware_serializer.data
            })
        except Exception as e:
            return Response({
                'response_code': 500,
                'message': "Internal Error",
                'statusFlag': False,
                'status': "FAILED",
                'errorDetails': str(e),
                'data': None
            }, status=500)