### Sobre

Esse repositório tem como objetivo mostrar a implementação do trabalho 1 da matéria de Otimização 2020 - ERE3 da UFPR

### O problema

**Escalonamento de uso no tempo**  
Uma empresa aluga máquinas(para uso remoto) sob demanda de seus clientes. A única restrição é que as máquinas só podem ser usadas durante um mesmo dia de trabalho (expediente de 8h às 17h). Possivelmente maisde  um  destes  usos  podem  ser  alugados  num  mesmo  dia  para  uma  mesmam ́aquina,  se  a  soma  dos  tempos  for  menor  que  as  9  horas  do  expediente.Cada cliente pede quanto tempo, em minutos, vai usar uma m ́aquina.  Essetempo deve estar entre 0 e 540 minutos.
A  empresa  tem maquinas. Ao receber um conjunto de pedidos, o gerente da empresa precisa escalonar em qual maquina e em qual dia cada uso vai ser feito.
Considere que a demanda (pedidos) ́e dada por um conjunto de *n* pares(ni, ti), onde *ni* ́e o numero de pedidos de tempo ti, com 1 ≤ i ≤ n.
Queremos minimizar o numero de dias necessario para atender aos pedidos da demanda