# Análise de Circuito Elétrico com Inversão de Matriz

## 📋 Descrição do Projeto

Este projeto implementa um sistema para análise de correntes em circuitos elétricos utilizando **inversão de matriz 3x3** e a **Lei de Kirchhoff**. O programa resolve sistemas de equações lineares para determinar as correntes em cada malha de um circuito elétrico.

## 🎯 Objetivo

Resolver problemas reais de engenharia elétrica através da aplicação prática de álgebra linear, especificamente:
- Implementar algoritmo de inversão de matriz 3x3
- Aplicar a Lei de Kirchhoff para análise de circuitos
- Calcular correntes em circuitos com múltiplas malhas

## ⚡ Fundamentos Teóricos

### Lei de Kirchhoff das Tensões (LKT)
Em qualquer malha fechada de um circuito, a soma algébrica das tensões é zero:
```
∑ V = 0
```

### Sistema de Equações Lineares
Para um circuito com 3 malhas:
```
R₁₁I₁ + R₁₂I₂ + R₁₃I₃ = V₁
R₂₁I₁ + R₂₂I₂ + R₂₃I₃ = V₂  
R₃₁I₁ + R₃₂I₂ + R₃₃I₃ = V₃
```

Onde:
- **I₁, I₂, I₃**: Correntes nas malhas (A)
- **R**: Resistências (Ω)
- **V**: Tensões aplicadas (V)

### Solução por Inversão de Matriz
```
[I₁]   [R₁₁ R₁₂ R₁₃]⁻¹   [V₁]
[I₂] = [R₂₁ R₂₂ R₂₃]   × [V₂]
[I₃]   [R₃₁ R₃₂ R₃₃]     [V₃]
```

## 🔧 Funcionalidades

- ✅ **Entrada dinâmica**: Usuário define resistências e tensões
- ✅ **Cálculo automático**: Inversão de matriz 3x3 implementada
- ✅ **Validação**: Verificação automática dos resultados
- ✅ **Interpretação física**: Correntes positivas e negativas
- ✅ **Interface intuitiva**: Menu interativo e explicações

## 📁 Estrutura do Projeto

```
MatrizInversa/
├── matriz3.py          # Implementação da inversão de matriz 3x3
├── circuito.py         # Interface e lógica do circuito elétrico
├── main.py            # Arquivo principal para execução
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.6 ou superior

### Execução
```bash
python main.py
```

### Exemplo de Uso
```
=== ANÁLISE DE CIRCUITO ELÉTRICO ===

Malha 1:
Resistência R11 (Ω): 5
Resistência R12 (Ω): 2  
Resistência R13 (Ω): 1
Tensão V1 (V): 12

Malha 2:
Resistência R21 (Ω): 1
Resistência R22 (Ω): 4
Resistência R23 (Ω): 2
Tensão V2 (V): 10

Malha 3:
Resistência R31 (Ω): 2
Resistência R32 (Ω): 1
Resistência R33 (Ω): 6
Tensão V3 (V): 15
```

### Resultado
```
=== RESULTADO ===
Corrente na malha 1 (I₁): 1.556A
Corrente na malha 2 (I₂): 1.222A
Corrente na malha 3 (I₃): 1.778A

Verificação:
Malha 1: 12.000V (esperado: 12.0V) ✓
Malha 2: 10.000V (esperado: 10.0V) ✓
Malha 3: 15.000V (esperado: 15.0V) ✓
```

## 🧮 Algoritmo de Inversão

### Método Implementado
1. **Cálculo do determinante** usando regra de Sarrus
2. **Matriz de cofatores** com sinais alternados
3. **Matriz adjunta** (transposta dos cofatores)
4. **Matriz inversa** = adjunta ÷ determinante

### Validação
- Verificação de determinante não-nulo
- Substituição dos resultados nas equações originais
- Precisão numérica validada externamente (Wolfram Alpha)

## 📊 Interpretação dos Resultados

### Correntes Positivas
Indicam que a corrente flui no sentido assumido inicialmente.

### Correntes Negativas  
Indicam que a corrente flui no sentido **oposto** ao assumido.

### Verificação
O programa substitui automaticamente os resultados nas equações originais para confirmar a precisão dos cálculos.

## 🔬 Validação Externa

Os resultados foram validados usando:
- **Wolfram Alpha**: Sistema de equações lineares (confirmado 100% preciso)
- **Calculadoras online**: Inversão de matriz
- **Verificação automática**: Substituição nas equações originais
- **Testes múltiplos**: Diferentes combinações de resistências e tensões

## 🎓 Aplicações Educacionais

Este projeto demonstra:
- **Álgebra Linear**: Inversão de matriz e sistemas lineares
- **Engenharia Elétrica**: Lei de Kirchhoff e análise de circuitos
- **Programação**: Implementação de algoritmos matemáticos
- **Validação**: Verificação de resultados computacionais

## 📝 Licença

Este projeto é de uso educacional e acadêmico.