from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from restapi.models import ComputerHardwareModel
from restapi.serializers import ComputerHardwareSerializer

class UpdateByComputerHardwareId(CreateAPIView):
    serializer_class = ComputerHardwareSerializer

    def post(self, request, *args, **kwargs):
        try:
            pk = request.data.get('id')
            hardware = ComputerHardwareModel.objects.get(pk = pk)
            updated_serializer = ComputerHardwareSerializer(data = request.data)
            if updated_serializer.is_valid():
                hardware.price = updated_serializer.validated_data['price'] or hardware.price
                hardware.save()
                return Response({
                    'response_code' : 200,
                    'message' : "Successfully Updated Price",
                    'statusFlag' : True,
                    'status' : "SUCCESS",
                    'errorDetails' : None,
                    'data' : ComputerHardwareSerializer(hardware).data
                })
            else:
                return Response({
                    'response_code': 400,
                    'message': "Validation Error",
                    'statusFlag': False,
                    'status': "FAILED",
                    'errorDetails': updated_serializer.errors,
                    'data': None
                }, status=400)
        except ComputerHardwareModel.DoesNotExist as e:
            return Response({
                'response_code': 404,
                'message': "Not Found Record",
                'statusFlag': False,
                'status': "FAILED",
                'errorDetails': str(e),
                'data': None
            }, status=404)
        except Exception as e:
            return Response({
                'response_code': 500,
                'message': "Internal Error",
                'statusFlag': False,
                'status': "FAILED",
                'errorDetails': str(e),
                'data': None
            })
