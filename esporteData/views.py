from esporteData.models import Aluno, Turma, Inscricao, Atestado
from esporteData.serializers import AlunoSerializer, TurmaSerializer, ListaInscricaoPorAlunoSerializer, ListaInscricaoPorTurmaSerializer, InscricaoSerializer, AtestadoSerializer
from rest_framework import viewsets, generics

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

    
class InscricoesViewSet(viewsets.ModelViewSet):
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer

class AtestadosViewSet(viewsets.ModelViewSet):
    queryset = Atestado.objects.all()
    serializer_class = AtestadoSerializer

class ListaMatriculasDoAluno(generics.ListAPIView):
    def get_queryset(self):
        queryset = Inscricao.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaInscricaoPorAlunoSerializer

class ListaMatriculasDaTurma(generics.ListAPIView):
    def get_queryset(self):
        queryset = Inscricao.objects.filter(turma_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaInscricaoPorTurmaSerializer