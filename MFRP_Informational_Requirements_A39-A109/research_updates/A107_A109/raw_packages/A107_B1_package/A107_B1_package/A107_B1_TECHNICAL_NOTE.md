# A107-B1 — Lote pré-registrado gamma-plus (ranks canônicos 2–9)

## Pergunta congelada

Após o A107-MIN, o próximo teste foi congelado como um lote determinístico de oito registros ainda não usados, preservando a ordenação canônica dos 922 registros `legacy_three_band_gamma_plus` do A102 por

\[
(M,\; j,\; \text{witness}).
\]

O rank canônico 1 já havia sido consumido pelo A107-MIN. O A107-B1 usa exatamente os ranks 2–9, sem substituição adaptativa de testemunhos.

O arquivo de pré-registro foi escrito antes da execução do lote e possui SHA-256:

`eb2a7cdba3e490c4acc0a0e113fb398b38fb46524ccacfd66e898a99c52fe501`

Pergunta primária: cada um dos oito testemunhos persiste em uma componente aberta KKT estrita, não nula, contendo o witness, sob a arquitetura A102 congelada?

Hipótese secundária pré-declarada: em todo caso parcial, toda fronteira interna selecionada deve ser gerada por

\[
 p_{j+1}=0,
\]

isto é, pela condição `basic_p_{j+1}`.

## Base verificada

Antes do A107-B1, `tools/verify_results.py` foi executado na árvore original A39–A106 fornecida no ZIP. Resultado:

- 68 resultados de auditoria;
- 1013 gates;
- 110 figuras;
- 0 falhas;
- status `PASS`.

## Método exato

O lote usa a mesma redução simbólica do A107-MIN/A105–A106: somente a linha alpha varia com o probe-fonte `s`; a base finita, suportes e bandas ativas permanecem congelados. A atualização rank-one produz um denominador racional comum e numeradores polinomiais exatos para variáveis básicas, multiplicadores duais ativos, custos reduzidos e slacks inativos.

Para cada registro, a auditoria exige simultaneamente:

1. revalidação exata do witness;
2. contagem de condições igual à origem A102;
3. certificação de positividade no núcleo da componente;
4. certificação de todas as condições não selecionadas no hull da fronteira;
5. raiz selecionada simples/exata e ordenação exata de concorrentes;
6. contraexemplo racional externo negativo em cada fronteira selecionada;
7. regressão independente, por inversão matricial direta exata, contra a fórmula rank-one nos checkpoints racionais.

## Resultado

Veredito primário:

`PASS_BATCH_LOCAL_STABILITY`

Os 8/8 registros passaram todos os critérios congelados.

Censo:

| Rank | M | j | classificação | fronteira interna |
|---:|---:|---:|---|---|
| 2 | 15 | 4 | componente estrita própria | `basic_p_5` à esquerda |
| 3 | 16 | 4 | cobertura integral | nenhuma |
| 4 | 17 | 4 | cobertura integral | nenhuma |
| 5 | 19 | 5 | componente estrita própria | `basic_p_6` à esquerda |
| 6 | 20 | 5 | componente estrita própria | `basic_p_6` à esquerda |
| 7 | 21 | 5 | cobertura integral | nenhuma |
| 8 | 22 | 5 | cobertura integral | nenhuma |
| 9 | 24 | 6 | componente estrita própria | `basic_p_7` à esquerda |

Portanto:

- 4 `full_segment_coverage`;
- 4 `proper_strict_subcomponent`;
- 0 `witness_failure`;
- 0 `internal_failure_or_unresolved`.

Foram reconstruídas 380 condições KKT no total. A regressão independente efetuou 1332 comparações racionais exatas entre avaliação rank-one e inversão matricial direta, com 0 discrepâncias.

Todas as quatro fronteiras internas são à esquerda e, em todos os quatro casos, a condição selecionada é exatamente `basic_p_{j+1}`. Assim, a hipótese secundária pré-declarada recebe o veredito:

`SUPPORT_BATCH`

Isto é suporte finito no lote, não uma lei universal.

## Fronteiras parciais

Os pontos de fronteira foram isolados com brackets racionais exatos de largura aproximadamente `8.27e-28` em `s`.

Valores centrais apenas para leitura numérica:

- M=15, j=4: `s* ≈ 0.1293125771346799`, saída por `p_5 -> 0`;
- M=19, j=5: `s* ≈ 0.1308116430539961`, saída por `p_6 -> 0`;
- M=20, j=5: `s* ≈ 0.1290141459871686`, saída por `p_6 -> 0`;
- M=24, j=6: `s* ≈ 0.1308581059667482`, saída por `p_7 -> 0`.

Em cada caso há um ponto racional explícito além da fronteira em que a massa básica selecionada é estritamente negativa. Logo, a perda da base congelada é real e não apenas uma falha do certificador.

## Relação com A107-MIN

Somando o registro previamente testado no A107-MIN aos oito do A107-B1, os primeiros nove registros canônicos agora dão:

- 9/9 com estabilidade local aberta;
- 5 componentes próprias e 4 coberturas integrais;
- em 5/5 casos parciais, a fronteira selecionada é `basic_p_{j+1}`;
- em 5/5 casos parciais, essa fronteira está no lado esquerdo.

Esse agregado é descritivo. O único teste prospectivo do mecanismo neste arquivo é o lote A107-B1.

## Observação pós-hoc, não promovida a resultado

Nos registros iniciais de fase `unique_b_plus_1` aparece um padrão visual por M: M=14,15 e 19,20 são parciais; M=16,17 e 21,22 são integrais; M=24 volta a ser parcial. Isto sugere uma possível estrutura aritmética/geométrica na localização da fronteira. Como essa regularidade foi percebida depois de ver os resultados, ela não conta como confirmação e deve ser transformada em previsão antes de qualquer próximo lote.

## Escopo

O A107-B1 não prova a propriedade para os 922 registros gamma-plus, não é um teorema para todo M, não estende os intervalos além dos segmentos A95/A102 e não tem interpretação física adicional.

## Hashes de reprodução

- resultado A107-B1: `fc47b6517d354d3c476920c6e8bf67f233625d8e8a95d5e0436b61493f8a3d64`
- script A107-B1: `4e0747b7be593d16662d154a10af0ef89a8163317ad66fc379fe29c72e95d6d5`
- helper A107-MIN: `21cb4361c01877eab97392a44106ec111bf5d9ba1c350fc2bef6ec99538071b3`
- ZIP fonte fornecido: `0aeb7daad66a80d03086e9a29f41f28c34156950822c7b3a13f867a296ffdb65`
