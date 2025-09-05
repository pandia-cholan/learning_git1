from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from restapi.models import ComputerHardwareModel
from restapi.serializers import ComputerHardwareSerializer

class GetByComputerHardwareId(GenericAPIView):
    serializer_class = ComputerHardwareSerializer

    def post(self, request, *args, **kwargs):
        try:
            print(request.user)
            pk = request.data.get('id')
            hardware = ComputerHardwareModel.objects.filter(pk = pk)









































































































            if hardware:
                return Response({
                    'response_code': 200,
                    'message': "Successfully Fetched",
                    'statusFlag': True,
                    'status': "SUCCESS",
                    'errorDetails': None,
                    'data': ComputerHardwareSerializer(hardware, many=True).data
                })
            return Response({
                'response_code': 404,
                'message': "Not Found Record",
                'statusFlag': False,
                'status': "FAILED",
                'errorDetails': "NOt found REcord",
                'data': None
            })
        except Exception as e:
            return Response({
                'response_code': 500,
                'message': "Internal Error",
                'statusFlag': False,
                'status': "FAILED",
                'errorDetails': str(e),
                'data': None
            })
