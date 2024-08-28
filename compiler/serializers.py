from rest_framework import serializers

class CodeExecutionSerializer(serializers.Serializer):
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    language = serializers.ChoiceField(choices=[('python', 'Python')])
