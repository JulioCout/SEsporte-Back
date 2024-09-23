from django.db import models

class Aluno(models.Model):
    matricula = models.CharField(max_length=20)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    nascimento = models.DateField(null=True)
    categoria = models.CharField(max_length=30)
    pcg = models.BooleanField(default=0)
    telefone1 = models.CharField(max_length=11)
    telefone2 = models.CharField(max_length=11)
    email = models.EmailField(blank=False, max_length=50)
    nascimento = models.DateField(null=True)
    
    endereco = models.CharField(max_length=150)
    cidade = models.CharField(max_length=70)
    uf = models.CharField(max_length=70)
    bairro = models.CharField(max_length=70)
    status = models.CharField(max_length=70)
    proxima_renovacao = models.DateField(null=True)
    
    responsavel_nome = models.CharField(max_length=150)
    responsavel_cpf = models.CharField(max_length=11)
    
    contato_emergencia_1 = models.CharField(max_length=150)
    contato_emergencia_1_parentesco = models.CharField(max_length=70)
    contato_emergencia_1_telefone = models.CharField(max_length=11)
    contato_emergencia_2 = models.CharField(max_length=150)
    contato_emergencia_2_parentesco = models.CharField(max_length=70)
    contato_emergencia_2_telefone = models.CharField(max_length=11)
    plano_saude = models.CharField(max_length=70)
    grupo_sanguineo = models.CharField(max_length=3)
    vencimento_atestado = models.DateField(null=True)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    unidade = models.CharField(max_length=70)
    modalidade = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    faixa_etaria = models.CharField(max_length=100)
    dias = models.CharField(max_length=70)
    horario = models.CharField(max_length=70)
    status = models.CharField(max_length=70)
    vagas = models.IntegerField()
    cota_pcg = models.IntegerField()
    ocupadas = models.IntegerField()
    ocupadas_pcg = models.IntegerField()
    disponivel = models.IntegerField()
    disponivel_pcg = models.IntegerField()
    local_aula = models.CharField(max_length=70)
    professor = models.CharField(max_length=100)
    data_inicio = models.DateField(null=True)
    tipo = models.CharField(max_length=70)
    gratuidade = models.BooleanField(default=0)

    def __str__(self):
        return self.codigo
    
class Inscricao(models.Model):
    inscricao = models.CharField(max_length=70)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    operador = models.CharField(max_length=70)
    data = models.DateField(null=True)

class Atestado(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    operador = models.CharField(max_length=70)
    data = models.DateField(null=True)
    vencimento = models.DateField(null=True)
 