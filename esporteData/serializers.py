from rest_framework import serializers
from esporteData.models import Aluno, Turma, Inscricao, Atestado

class AlunoListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['nome', 'matricula', 'telefone', 'email']

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class TurmaListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = ['unidade', 'modalidade', 'codigo', 'disponivel', 'disponivel_pcg', 'status']

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'

class InscricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscricao
        fields = '__all__'

class AtestadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atestado
        fields = '__all__'

class ListaInscricaoPorAlunoSerializer(serializers.ModelSerializer):
    turma = serializers.ReadOnlyField(source='turma.descricao')
    codigo = serializers.SerializerMethodField()
    class Meta:
        model = Turma
        fields = ['modalidade', 'codigo']
    
    def get_codigo(self, obj):
        return obj.get_codigo_display()
    
class ListaInscricaoPorTurmaSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Inscricao
        fields = ['aluno_nome']
