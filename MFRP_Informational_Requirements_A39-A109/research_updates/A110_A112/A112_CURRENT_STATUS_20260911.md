# A112 — onde estamos agora

**Data do registro:** 2026-09-11  
**Repositório-base auditado:** `d1b1a951618d3778b43f04698111db5643ed5414`

Este arquivo é a porta de entrada humana para o trabalho A110–A112. A ideia é simples: alguém que chegue aqui depois de semanas ou meses deve conseguir entender o que já foi demonstrado, o que foi apenas testado, o que falhou no caminho e qual é a próxima pergunta aberta — sem precisar reconstruir a história a partir de scripts soltos.

## Em uma frase

O mecanismo local de duas fronteiras da família gamma-plus — `p_(j+1)=0` pela esquerda e `p_j=0` pela direita — agora tem um fechamento analítico uniforme no tail `M>=521`, sob o mesmo contrato congelado de fonte e dentro de uma fase de máximo comprimido estrito.

Isso completa, no tail, a peça estrutural que o A110 havia fechado apenas para `14<=M<=520`.

## O teorema que podemos afirmar

Para

- `M >= 521`;
- `129/1000 <= s <= 133/1000`;
- arquitetura gamma-plus congelada
  `P={0,j,j+1,M}`, `Q={1,h,h+1}`, `h=floor(M/2)`;
- sinais ativos `alpha+`, `beta-`, `gamma+`;
- contato `j` dentro de uma fase de máximo comprimido estrito;

as condições KKT estritas dessa base são satisfeitas **exatamente** onde

`p_j > 0` e `p_(j+1) > 0`.

Esse conjunto é um único intervalo, possivelmente vazio. Suas únicas fronteiras KKT internas possíveis são:

- esquerda: `p_(j+1)=0`;
- direita: `p_j=0`.

## O que isso NÃO diz

Este resultado não prova que a arquitetura gamma-plus acima é a arquitetura globalmente selecionada entre todas as arquiteturas possíveis para todo `(M,s)`.

Também não prova nada fora da janela `s in [0.129,0.133]`, não cobre outros padrões de suporte/bandas e não fornece interpretação física, gravitacional, quântica ou experimental.

Em outras palavras: o teorema é forte, mas local à família e ao contrato que realmente foram demonstrados.

## Como chegamos aqui

A cadeia ficou dividida em peças independentes e auditáveis:

1. **A112-A — localização.** Se `p_j` e `p_(j+1)` são positivos, então o contato só pode ser `b+1` ou `b+2`, com `b=ceil(M c(s))`.
2. **A112-B — pivô q2.** Dentro desses dois offsets, `p_j,p_(j+1)>0 => RQ(2)>0`.
3. **A112-C — reduced costs.** `RQ(2)>0` força todos os outros reduced costs P/Q não básicos a serem positivos.
4. **A112-D — duais ativos.** Uma identidade exata liga o multiplicador gamma ao fator de máximo comprimido: `N_gamma = -(detB/D_G) E_j`. Assim uma fase comprimida estrita força `y_alpha,y_beta,y_gamma>0`.
5. **A112-E — massa central Q.** `p_(j+1)>0 => q_h>0`.
6. **A112-F — monotonicidade.** As massas adjacentes têm slopes opostos na coordenada `t`, e o numerador da derivada `t'(s)` tem sinal correto.
7. **A112-G — regularidade e q1.** `A<0<B` elimina polos e fecha `t'(s)>0`; além disso `p_j>0 => q_1>0` diretamente, sem depender de witness histórico.
8. **Auditoria de composição.** As peças A–G foram encadeadas procurando dependências circulares, mudanças de quantificador e uso indevido de hipóteses. Duas lacunas reais foram encontradas e fechadas antes do PASS final.

## Correções que fazem parte da história

Nem tudo que tentamos sobreviveu.

- A afirmação mais forte `j in {b+1,b+2} => RQ(2)>0` é falsa. Há contraexemplo exato em `M=600, s=133/1000, j=106`, onde `p_(j+1)<0` e `RQ(2)<0`. A positividade primal é essencial.
- Duas fórmulas intermediárias para a correção de tail em `T` foram descartadas porque omitiam contribuições gamma-contact. A fórmula final correta foi derivada novamente com essas contribuições presentes.
- A primeira versão da prova de monotonicidade ainda não certificava `A(s) != 0`. A auditoria detectou isso; A112-G provou `A<0<B` no strip inteiro.
- As antigas exclusões por Descartes de `q_1,p_0,p_M` eram do tipo “não pode ser o primeiro zero partindo de um witness estrito”. Para o tail, isso foi fortalecido para uma prova ponto-a-ponto: `p_j>0 => q_1>0`, e então Descartes força `p_0,p_M>0` diretamente.

Essas correções não são notas laterais: elas explicam por que o resultado atual é mais confiável que uma simples continuação numérica do A110.

## Relação com o estado antigo do repositório

O arquivo histórico `session_artifacts/A112_PIVOT_SQUARE_STATUS_NOTE.md` dizia `OPEN / INCONCLUSIVE`. Ele deve permanecer no repositório como registro histórico do estado anterior.

Ele está agora **superado**, não apagado. O estado corrente é dado por:

- `session_artifacts/A112_ANALYTIC_TAIL_STRUCTURAL_THEOREM_20260911.md`;
- `session_artifacts/A112_LOGICAL_COMPOSITION_AUDIT_20260911.md`;
- os certificados A112-B ... A112-G e seus JSONs.

## O que falta agora

A próxima pergunta não é mais uma desigualdade local do A112.

O próximo nível é a **seleção global de arquitetura**: demonstrar, se for verdadeiro, quando e por que esta arquitetura gamma-plus é a arquitetura relevante/global entre todas as possibilidades. Até isso ser feito, devemos chamar o resultado atual de **teorema estrutural local da família gamma-plus**, e não de teorema global irrestrito do LP.

## Regra de trabalho daqui para frente

Tratar este repositório como um caderno de campo:

- preservar resultados antigos mesmo quando forem superados;
- registrar contraexemplos e tentativas falhas;
- separar evidência finita de prova uniforme;
- guardar scripts e resultados juntos;
- escrever uma nota humana sempre que o estado científico mudar;
- declarar explicitamente o que ainda não foi provado.

A meta é que a trilha de raciocínio continue auditável mesmo quando a memória humana falhar.
