Hipótese 2
===========

Motivação
---------

| O desejo de entender em quais horários o número de ligações é maior, parte da pressuposição de que o período noturno\
 é notoriamente mais perigoso que os demais.
| Muito desse senso comum se deve a baixa circulação de pedestres, além da recorrente  defasagem de iluminação pública.
| O estudo desses dados sob tal aspecto pode ser essencial no desenvolvimento de politicas governamentais e na\
 reorganização da rotina de patrulhas policias.

.. warning::
    Os estudos aqui realizados são puramente superficiais, dado a falta de experiência 
    com abordagens estatísticas ou probabilísticas. A analise foi feita com o objetivo de 
    fomentar o interesse do leitor para com às hipóteses comentadas.

Considerações Gerais
--------------------

| Em primeira instância, afim de agilizar a execução do codigo, foi realizada, a filtragem do arquivo.
| Obtendo dessa forma somente as colunas: 'callDateTime', 'priority', 'description'.

Analise Principal
-----------------

| **O número de ligações no período noturno é maior.**

| Para investigar essa hipótese foi necessário primeiramente ter em mãos o horário, em horas, de cada ligação.
| Pois o formato da coluna `callDataTime`, segue o seguinte padrão:

* ano/mês/dia hora:minutos:segundos

Assim sendo, foi implementada a função `get_hour`, onde:

:: 
    Dado um DataFrame:

+-------------------------+
| callDataTime            |
+=========================+
| 2021/01/04 16:33:00+00  |
+-------------------------+
| 2021/01/04 17:34:00+00  |
+-------------------------+

::
    Retorna:

+-------------------------+------+
| callDataTime            | hour |
+=========================+======+
| 2021/01/04 16:33:00+00  | 16   |
+-------------------------+------+
| 2021/01/04 17:34:00+00  | 17   |
+-------------------------+------+

| Depois agrupamos as ligações por horários e contabilizamos o tamanho de cada agrupamento "quantidade de ligações por hora".

.. code-block:: python

    sub_df.groupby('hour').size()

Com todas as informações agrupadas basta plotar o grafico

.. code-block:: python

    plot_graf_bar(sub_groupby_1, 'calls', 'hour', 'calls_per_hour.png')

Clonclusões
-----------

.. image:: images/my_image.png
   :width: 400px
   :height: 200px
   :align: center
    
Adicionais:
^^^^^^^^^^^^^^

A gravidade das ligações é maior no período com mais.
Chamadas sem voz estão entre as principais ocorrências de ligações.


