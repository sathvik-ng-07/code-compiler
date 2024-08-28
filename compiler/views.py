# compiler/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CodeExecutionSerializer
import subprocess
import time

def index(request):
    return render(request, 'submit_code.html')

class CodeExecutionView(APIView):
    def post(self, request):
        serializer = CodeExecutionSerializer(data=request.data)
        if serializer.is_valid():
            code = serializer.validated_data['code']
            language = serializer.validated_data['language']

            # Save the code to a file
            with open('temp_code.py', 'w') as f:
                f.write(code)

            # Execute the code
            start_time = time.time()
            try:
                result = subprocess.run(['python', 'temp_code.py'], capture_output=True, text=True, timeout=10)
                output = result.stdout + result.stderr
            except subprocess.TimeoutExpired:
                output = 'Execution timed out'
            end_time = time.time()

            # Return execution details
            response_data = {
                'time_running': end_time - start_time,
                'start_time': start_time,
                'lines_of_code': len(code.splitlines()),
                'output': output
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
