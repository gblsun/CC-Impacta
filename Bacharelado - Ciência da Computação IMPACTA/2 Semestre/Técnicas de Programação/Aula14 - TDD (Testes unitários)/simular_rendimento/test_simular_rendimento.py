from simular_rendimento import simular_rendimento

def test_cenario_1():
    assert simular_rendimento(0.1, 3) == 1331.00

def test_cenario_2():
    assert simular_rendimento(0.2, 5) == 2488.32

def test_cenario_3():
    assert simular_rendimento(0.3, 10) == 13785.85

#  python -m pytest '.\IMPACTA\2SEM\tecnicas-de-programacao\Aula14 - TDD (Testes unitários)\simular_rendimento\test_simular_rendimento.py'
