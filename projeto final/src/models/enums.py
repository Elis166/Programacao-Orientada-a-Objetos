from enum import Enum

class StatusMissao(Enum):
  DISPONIVEL = 'Disponível'
  EM_ANDAMENTO = 'Em Andamento'
  CONCLUIDA = 'Concluída'


class StatusCampanha(Enum):
  NAO_INICIADA = 'Não Iniciada'
  EM_ANDAMENTO = 'Em Andamento'
  CONCLUIDA = 'Concluída'


class TipoRecompensa(Enum):
  ITEM = 'Item'
  TITULO = 'Título'
  PONTO_EXTRA = 'Ponto Extra'