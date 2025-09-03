from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from restapi.models import ComputerHardwareModel
from restapi.serializers import ComputerHardwareSerializer


class PostComputerHardwareView(CreateAPIView):
    serializer_class = ComputerHardwareSerializer

    def post(self, request, *args, **kwargs):
        try:
            hardware_serializer = ComputerHardwareSerializer(data = request.data)
            if hardware_serializer.is_valid():
                hardware = ComputerHardwareModel.objects.create(**hardware_serializer.validated_data)
                hardware.save()
                return Response({
                    'response_code' : 200,
                    'message' : "Successfully Created",
                    'statusFlag' : True,
                    'status' : "SUCCESS",
                    'errorDetails' : None,
                    'data' : ComputerHardwareSerializer(hardware).data
                }, status = 200)
            else:
                return Response({
                    'response_code': 400,
                    'message': "Validation Error",
                    'statusFlag': False,
                    'status': "FAILED",
                    'errorDetails': hardware_serializer.errors,
                    'data': None
                }, status=400)
        except Exception as e:
            return Response({
                'response_code': 500,
                'message': "Internal Error",
                'statusFlag': False,
                'status': "FAILED",
                'errorDetails': str(e),
                'data': None
            }, status=500)