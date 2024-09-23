from django.contrib import admin
from django.urls import path, include
from esporteData.views import AlunoViewSet, TurmaViewSet, InscricoesViewSet, AtestadosViewSet, ListaMatriculasDoAluno, ListaMatriculasDaTurma
from rest_framework import routers




router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename='Alunos')
router.register('turmas', TurmaViewSet, basename='Turmas')
router.register('incricoes', InscricoesViewSet, basename='Incrições')
router.register('atestados', AtestadosViewSet, basename='Atestados')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('alunos/<int:pk>/inscricoes', ListaMatriculasDoAluno.as_view()),
    path('turmas/<int:pk>/inscricoes', ListaMatriculasDaTurma.as_view()),
]