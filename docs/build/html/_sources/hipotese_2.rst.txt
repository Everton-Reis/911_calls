Hipótese 2
===========

Motivação
---------

| O desejo de entender em quais horários o número de ligações é maior parte da pressuposição de que o período noturno \
  é notoriamente mais perigoso que os demais.
| Muito desse senso comum se deve a baixa circulação de pedestres, além da recorrente defasagem de iluminação pública.
| O estudo desses dados sob tal aspecto pode ser essencial no desenvolvimento de políticas governamentais e na \
 reorganização da rotina de patrulhas policias.

.. warning::
    Os estudos aqui realizados são puramente superficiais, dado a falta de experiência 
    com abordagens estatísticas e/ou probabilísticas. A análise foi feita com o objetivo de 
    fomentar o interesse do leitor para com às hipóteses comentadas.

Considerações Gerais
--------------------

| Em primeira instância, afim de agilizar a execução do código, foi realizada, a filtragem do arquivo.
| Obtendo dessa forma somente as colunas: 'callDateTime', 'priority', 'description'.

.. code-block:: python

    x.load_datafile(filepath)

| Para investigar essa hipótese foi necessário primeiramente ter em mãos o horário, em horas, de cada ligação.
| Pois o formato da coluna `callDataTime`, segue o seguinte padrão:

* ano/mês/dia hora:minutos:segundos

| Assim sendo, foi implementada a função `get_hour`.

.. code-block:: python

    ax.get_hour(df)

| Onde:

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

Analise Principal
-----------------

| **O número de ligações no período noturno é maior.**

| Depois, agrupamos as ligações por horários e contabilizamos o tamanho de cada agrupamento "quantidade de ligações por hora".

.. code-block:: python

    sub_df.groupby('hour').size()

| Com todas as informações bastou plotar o gráfico

.. code-block:: python

    plot_graf_bar(sub_groupby_1, 'calls', 'hour', 'calls_per_hour.png')

Conclusões
-----------

| Com base no gráfico abaixo, é possível perceber, que o horário de menor incidência de ligações ocorre das 09:00 às 09:59.
| Analogamente, o horário de maiores incidências ocorre das 22:00 às 22:59.
| Ademais, em um contexto geral é notório que às ligações aumenta gradativamente a partir das 09:00, atingindo seu ápice as 22:00 voltando gradativamente a diminuir.

.. image:: ../../data/hipotese_2_images/calls_per_hour.png
   :width: 700px
   :height: 300px
   :align: center

| Confirmando, dessa forma, a hipótese de que o maior número de ligações ocorre no período noturno. 

Adicionais:
^^^^^^^^^^^

| **A gravidade das ligações é maior no período com mais ligações.**

| De maneira ampla, entender a gravidade das ligações é essencial ao distribuir a ação de rondas policias ao longo do dia.
| Com todas as informações agrupadas bastou plotar o gráfico

.. code-block:: python

    visual.plot_graf_pie_by_hour(sub_df_2, "18", 'priority_per_hour.png', 'priority')

conclusões
^^^^^^^^^^

| Com base nos gráficos abaixo, é possível perceber, que por mais que o horário mude, a diferença de gravidade por horário é, de certa forma, irregular.

.. image:: ../../data/hipotese_2_images/priority_per_hour_02.png
   :width: 500px
   :height: 300px
   :align: center

.. image:: ../../data/hipotese_2_images/priority_per_hour_05.png
   :width: 500px
   :height: 300px
   :align: center

.. image:: ../../data/hipotese_2_images/priority_per_hour_09.png
   :width: 500px
   :height: 300px
   :align: center

.. image:: ../../data/hipotese_2_images/priority_per_hour_18.png
   :width: 500px
   :height: 300px
   :align: center

.. image:: ../../data/hipotese_2_images/priority_per_hour_22.png
   :width: 500px
   :height: 300px
   :align: center

| Ainda assim, é possível notar um aumento de ligações de alta gravidade durante a madrugada, 02:00 às 02:59 e 05:00 às 05:59, além da presença maior de ligações de baixa e média gravidade.
| Com base nisso, não é possível determinar se a hipótese foi refutada ou confirmada, sendo necessária uma investigação mais aprofundada.

**Chamadas sem voz estão entre as principais ocorrências de ligações.**

| Podemos ainda citar a importância de se investigar os principais tipos de ocorrências ao longo do dia.
| Portanto, depois agrupamos as ligações por horários e contabilizamos o tamanho de cada agrupamento por descrição "quantidade de ligações por descrição".

.. code-block:: python

    sub_df.groupby('description').size()

| Selecionamos então as 15 ocorrências mais frequentes.

.. code-block:: python

    ax.get_first_15_most_frequency(sub_df, sub_groupby_2)

| Com base nos gráficos abaixo, é possível notar, que às mudanças de horário influenciam nas principais ocorrências.

.. image:: ../../data/hipotese_2_images/description_per_hour_02.png
   :width: 500px
   :height: 300px
   :align: center

.. image:: ../../data/hipotese_2_images/description_per_hour_05.png
   :width: 500px
   :height: 300px
   :align: center

.. image:: ../../data/hipotese_2_images/description_per_hour_09.png
   :width: 500px
   :height: 300px
   :align: center

.. image:: ../../data/hipotese_2_images/description_per_hour_18.png
   :width: 500px
   :height: 300px
   :align: center

.. image:: ../../data/hipotese_2_images/description_per_hour_22.png
   :width: 500px
   :height: 300px
   :align: center

| Por fim, analisando algumas informações essenciais, por mais que 911/ no voice e desordem sejam sempre as mais frequentes

1. Durante o período noturno, 18:00 às 18:59 e 22:00 às 22:59, o número de ocorrências por narcóticos é consideravelmente maior que nos demais
2. Das 02:00 às 02:59 e 05:00 às 05:59, o número de assaltos se destaca.
3. E das 09:00 às 09:59, acidentes de carro são a terceira ocorrência mais frequente.
