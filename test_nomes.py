#!-*- conding: utf8 -*-
import TamanhoNomes
import pytest

class TestNomes:

    @pytest.fixture
    def t(self):
        return TamanhoNomes.TamanhoNomes()


    def testa_menor(self, t):
        assert t.menor_nome(['mateus', 'ana', 'joao', 'du   ', 'roberto   ', 'an']) == ('Du')

    def testa_menor2(self, t):
        assert t.menor_nome2(['mateus', 'ana pasquim', '  joao', '  duarte', 'roberto', 'jose']) ==('Joao')
    
    def testa_menor3(self, t):
        assert t.menor_nome3(['mateus', 'ana jerusalem  ', '  joao', 'du, dudu e edu', 'roberto', 'ana de amsterda']) == ('Joao')
