import pytest
import TamanhoNomes

class TestNomes2:

    @pytest.fixture
    def t(self):
        return TamanhoNomes.TamanhoNomes()

    @pytest.mark.parametrize("entrada, esperado", [
        (['mateus', 'ana', 'joao', 'du   ', 'roberto   ', 'an'], 'Du'),
        (['mateus', 'ana pasquim', '  joao', '  duarte', 'roberto', 'jose'],'Joao'),
        (['mateus', 'ana jerusalem  ', '  jo', 'du, dudu e edu', 'roberto', 'ana de amsterda'],'Jo')
    ])

    def testa_menor(entrada, esperado):
        assert t.menor_nome(entrada) == esperado
