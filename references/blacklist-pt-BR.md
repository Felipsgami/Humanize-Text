# Lista negra e régua de voz · português do Brasil

Esta é a parte do método que depende da língua. O fluxo de trabalho está em `method.md`; o teste de verdade (estatuto), em `status-check.md`.

## Por que texto de IA soa como IA

Um modelo de linguagem escolhe, palavra a palavra, o que é estatisticamente mais provável. Por isso o texto de IA é, por definição, **o texto mais provável** sobre o tema: fica na média do que já foi escrito. O que é improvável some: a escolha incomum e precisa, o ritmo quebrado, a associação inesperada, o detalhe que só quem viveu tem.

Duas medidas descrevem isso e servem de alvo positivo:
- **Perplexidade:** o quanto a escolha de palavra surpreende. Teste manual: esta é a palavra mais óbvia que eu poderia pôr aqui, ou uma escolha inesperada e ainda assim exata?
- **Burstiness:** a variação de tamanho e de arquitetura das frases. Gente alterna frase de três palavras com frase de trinta; modelo escreve tudo do mesmo tamanho.

**Não se escreve para enganar detector.** Detector erra muito, inclusive contra texto humano (taxas altas de falso positivo, viés contra quem escreve em segunda língua, e paráfrase em cadeia derruba a acurácia). Escreve-se assim porque é o que a prosa humana faz; o detector é um espelho ruim da mesma coisa.

**O que não é slop**, e todo parágrafo precisa de pelo menos um: detalhe específico (nome, data, número com fonte, lugar), experiência vivida, informação nova para o leitor, ponto de vista de que alguém poderia discordar.

**Os cinco tipos de slop** (para diagnosticar quando o texto passa na lista e continua morto):
1. **Genérico:** a foto de banco de imagem em palavras; serviria para qualquer tema.
2. **Pseudo-insight:** soa profundo e não diz nada novo.
3. **Autoridade falsa:** tom de especialista sem fonte mostrada.
4. **Reescrita de enciclopédia:** o primeiro parágrafo do verbete, parafraseado.
5. **Bem-estar:** conselho reconfortante e universal, sem ação concreta; a variante mais traiçoeira é a tese séria que termina em autoajuda.

## A lista negra (28 itens)

Os itens 1 a 17 são a **primeira ordem** (os cacoetes clássicos); os 18 a 28, a **segunda ordem** (os estruturais, que sobrevivem a uma limpeza apressada). O peso de cada um e as exceções vêm logo depois.

**Aberturas**
1. **Moldura de época:** "Em um mundo onde…", "Na era da/de…", "No cenário atual…", "Ao longo da história…", "Desde os primórdios…", "Vivemos em uma época em que…". Comece pelo fato.
2. **Verbo de imersão:** "Vamos explorar…", "Embarque nesta jornada…", "Vamos mergulhar…", "Prepare-se para descobrir…". Anunciar em vez de começar.

**Estrutura e transição**
3. **Conectores em série:** "Além disso", "Por outro lado", "Por fim", "Em suma", "Ou seja", "Portanto" encadeados por reflexo. Prefira a transição que carrega conteúdo (o fato que puxa o próximo).
4. **Travessão em excesso:** um dos marcadores mais reconhecíveis de texto de IA em português. O medidor o trata como sinal quando é denso; em gênero ou casa editorial que o proíbe, use `--dashes zero`. Ao tirar, escolha pelo papel (ver adiante); trocar tudo por vírgula é erro.
5. **"Não é X, é Y"** (e "não se trata de X, mas de Y", "mais do que X, é Y"): a forma mais comum de fingir profundidade. **Exceção:** a negação que corrige uma crença **com dono** dito na frase ("o senso comum diz que…; Fulano diz o contrário"). Sem dono, é espantalho (item 21).
6. **Ponto e vírgula encadeando** o que pedia ponto final.
7. **Lista onde caberia prosa:** argumento vive em prosa; lista só quando a forma-lista é o ponto (ficha, passo a passo, catálogo).
8. **Paralelismo mecânico:** três exemplos sempre que dá três, frases-espelho, simetria perfeita. Quebre de propósito.

**Tom e conteúdo**
9. **Hedging de funcionário:** "É importante notar que…", "Vale ressaltar que…", "Cabe destacar que…", "de certa forma", "por assim dizer". Corte a moldura e diga a coisa. **Não confunda com ressalva:** a marcação que diz de quem é a ideia, de que ano é o dado ou onde a analogia quebra é conteúdo e fica. Se a ressalva acrescenta um fato, fica; se só amortece, sai.
10. **Adjetivo e substantivo de folheto:** "fascinante", "incrível", "revolucionário", "robusto", "transformador", "jornada", "universo de", "essência de", "ecossistema", "paradigma" como enfeite.
11. **"Transformar" sem objeto, direção e escala:** "…transformando a forma como pensamos". Diga o quê, para quem e quanto.
12. **Empatia fabricada:** "Você não está sozinho", "E tudo bem se…", "Respire fundo".
13. **Autoridade anônima:** "Estudos mostram…", "Especialistas concordam…", "Pesquisas indicam…" sem dizer qual. Nomeie a fonte ou corte; marcado por isto **vai para verificação**, não direto para a tesoura (pode haver uma fonte real por trás).
14. **Neutralidade sem risco:** "por um lado…, por outro…" sem tomar posição. Hesitação real é bem-vinda; a covardia do "depende", não.

**Fechamentos**
15. **Gerúndio de fechamento vago:** "…abrindo novas possibilidades", "…redefinindo o futuro".
16. **Recapitulação mecânica:** "Em conclusão…", "Como vimos…", "Recapitulando…".
17. **Chamada de rede social:** "compartilhe com quem precisa", "deixe nos comentários".

**Segunda ordem: estrutura e ritmo**
18. **Fragmento dramático em fila e fecho de uma linha:** "Sem X. Sem Y. Só Z.", três ou mais frases curtíssimas seguidas, todo parágrafo terminando numa frase-soco. A frase curta é técnica legítima; em fila, vira tique. No máximo um fragmento de impacto por seção, e ele carrega informação.
19. **Provérbio que soa profundo:** "No cerne de", "a verdadeira questão é", "o que realmente importa", "ao final do dia".
20. **Andaime antes do ponto:** "Aqui está o que você precisa saber", "e aqui está o ponto", "sinceramente?", "vamos direto ao ponto".
21. **Espantalho:** refutar objeção que ninguém levantou. Se a crença tem dono, nomeie (item 5); se não tem, afirme a tese direto.
22. **Tríade forçada:** três itens porque três soa completo, com o terceiro decorativo. Se forem mesmo três, varie o comprimento.

**Segunda ordem: inflação e autoridade emprestada**
23. **Conexão vaga:** "ligado a", "associado a", "relação entre", "em diálogo com", "ressoa com", sem dizer qual relação. Use o verbo real: citou, contradiz, derivou de, mede, antecipa.
24. **Gerúndio de enfeite:** ", simbolizando", ", refletindo", ", evocando", ", demonstrando". Se o gerúndio afirma **sentido** (o que algo simboliza), é afirmação sem fonte e é também erro de estatuto.
25. **Significância inflada:** "momento crucial", "legado duradouro", "divisor de águas", "continua a prosperar", "desafios e perspectivas", "futuro promissor". Termine no último fato concreto.
26. **Cópula evitada:** "serve como", "constitui", "configura-se como", "representa" onde bastava "é". **Só troque por "é" onde a fonte afirma identidade.** Onde a fonte fala em analogia ou modelo, "funciona como" fica: é marcador de estatuto (ver `status-check.md`).

**Segunda ordem: resíduos e forma**
27. **Resíduo de chatbot e disclaimer de conhecimento:** "Ótima pergunta", "espero ter ajudado", "posso também…?", "até onde sei", "não é amplamente documentado" seguido de palpite. Lacuna se declara, nunca se preenche com o provável.
28. **Formatação por reflexo:** negrito de enfeite, lista em que todo item abre com rótulo em negrito, título repetido na primeira frase, texto que comenta a versão anterior ("agora corrigido", "antes dizia").

## Peso e exceções

| Peso | Regra | Exemplos |
|---|---|---|
| **Forte** | uma ocorrência já pede edição | "não é X, é Y" sem dono, gerúndio interpretativo, "no cerne de", resíduo de chatbot, moldura de época |
| **Fraco** | só pesa em aglomerado (3 tipos no mesmo parágrafo, ou 4 ocorrências), porque é comum na fala | "jornada", "fascinante", "pilar", "além disso", "ligado a" |
| **Observar** | sem evidência de que seja tique; anota e não pontua | "tapeçaria", "delicado equilíbrio", "lançar luz sobre" |

O peso vem de contagem real: cada candidato foi medido em cerca de 11 milhões de palavras de fala humana transcrita em português. Conector e muleta de fala ("ou seja", "além disso", "no fundo", "ligado a") **não são marcador lexical**: o que os condena é o contexto (série, vazio, relação sem nome), e só a leitura decide.

**Quando NÃO agir:**
- dentro de **citação**, em **título de obra**, em **nome próprio**;
- em passagem que **discute** a expressão (este documento, um texto sobre clichês);
- em **termo técnico** no sentido técnico: *paradigma* em Kuhn, *ecossistema* em ecologia, *constitui* em texto jurídico, *representa* em matemática;
- **hesitação real, aparte genuíno, detalhe estranho, sentimento misto, referência datada:** isso é voz, não cacoete, e podar é o erro oposto ao slop;
- a **ressalva que acrescenta fato** (item 9);
- **uma ocorrência fraca isolada**.

**Por gênero:**

| Gênero | Regime | O que mais pesa | O que não se aplica |
|---|---|---|---|
| ensaio, crônica, ficção | pleno | fragmento em fila, "não é X, é Y", gerúndio interpretativo, conexão vaga, ritmo uniforme | nada é isento |
| roteiro, locução, podcast | pleno, só sobre a fala | moldura, andaime, fragmento sem informação, fecho em frase-soco | anáfora escolhida e frase curta são normais na fala |
| vídeo curto, legenda | pleno, frase curta é o gênero | gancho genérico, recapitulação, chamada de rede social | fragmento só reprova se não carrega informação |
| texto técnico, artigo, relatório, pesquisa | **leve**: o rigor vem primeiro | itens 9, 10, 13, gerúndio interpretativo, resíduo de chatbot | ritmo, tríade, fragmento, conector; travessão tolerado |
| post, nota, descrição, e-mail, conversa | pleno | formatação por reflexo, título repetido, chatbot, andaime | |

**No texto técnico, entre "mais preciso" e "menos parecido com IA", vale sempre mais preciso.** Prosa científica é impessoal e densa por natureza, e detector a confunde com IA; isso não é problema a corrigir.

## Travessão: escolha o substituto pelo papel

- aposto ou inciso longo e explicativo → **parênteses**;
- revelação, definição, desfecho, o "isto:" que anuncia → **dois-pontos**;
- pausa dramática, virada → **ponto final** (parta a frase);
- inciso curto → **vírgula**.

Faixa numérica usa hífen ou "a" (de 140 a 187). Trocar tudo por vírgula gera frase longa e frouxa.

## O que pôr no lugar (técnicas positivas)

1. **Burstiness:** uma frase curta, depois uma longa que se desdobra e só então pousa, outra curta. Nenhum parágrafo com todas as frases do mesmo tamanho. A frase curta é **uma** e carrega informação.
2. **Perplexidade:** o específico e improvável-mas-exato no lugar do genérico (o nome técnico da coisa, o número, a palavra da área).
3. **Detalhe verificável:** "um estudo da *Nature* de 2016", nunca "uma pesquisa".
4. **Posição com argumento:** uma tese e a razão dela.
5. **Imagem física para o abstrato**, própria e não de banco.
6. **Quebre o paralelismo** que ninguém escolheu; a anáfora escolhida fica.
7. **Deixe a digressão respirar** quando ela revela a complexidade do tema.

## Prevenir custa menos que corrigir

- **As interdições vão antes da geração**, no topo da instrução, e não só no checklist do fim (moldar pelo que se rejeita funciona melhor que filtrar depois).
- **Nunca peça o texto final de uma vez:** ângulos (não texto) → escolha justificada → rascunho com as interdições → **edição humana** (a etapa insubstituível) → revisão que **aponta sem reescrever** → repetir até não sobrar apontamento.
- **Exemplo vale mais que adjetivo:** dois ou três trechos escritos à mão pelo autor ensinam o tom melhor que qualquer descrição. Amostra instala voz, não substância.
- **Parafrasear não humaniza.** Trocar palavras engana detector e não acrescenta nada. Humanizar é acrescentar o que a IA não tem: o fato, a posição, a imagem própria, a experiência.

## Gate de voz (antes de fechar qualquer texto)

**Texto curto (duas linhas, um post): os cinco sobreviventes.** (1) "não é X, é Y" sem dono; (2) fecho de uma linha ou fragmento em fila; (3) travessão; (4) tríade de enfeite; (5) gerúndio pendurado. Se os cinco passam, o resto costuma passar.

**Texto longo:**
- [ ] lista negra varrida (no técnico, só os itens do regime leve);
- [ ] travessão dentro da política do gênero;
- [ ] burstiness: nenhum parágrafo com frases todas do mesmo tamanho;
- [ ] substância por parágrafo (detalhe, posição, informação nova ou imagem própria);
- [ ] diagnóstico dos cinco tipos de slop;
- [ ] abertura no fato, sem moldura; fechamento concreto, sem gerúndio vago, sem recapitulação, sem virar conselho;
- [ ] nenhuma autoridade anônima;
- [ ] a revisão acrescentou algo além de trocar palavras;
- [ ] roteiro e locução: lido em voz alta, sem tropeço;
- [ ] **gate de estatuto junto** (`status-check.md`): nenhum texto fecha só com o de voz.

## O teste de humanwashing (o mais importante)

Toda técnica positiva acima é, vista de fora, **sinal** de humanidade, e um modelo instruído produz sinal. Instalar sinal sobre um conteúdo que continua sendo a média do que existe é **humanwashing**, e é pior que o slop declarado, porque mente sobre o que é.

> **Sinal** é o que parece humano. **Substância** é o que só um autor específico poderia ter escrito. Primeiro a substância, depois o sinal.

- [ ] Apagados todos os marcadores de estilo do parágrafo, sobra algo que não está em qualquer resumo do tema? Se não sobra, o estilo está fazendo o trabalho que o conteúdo não fez.
- [ ] A imperfeição do texto vem de um pensamento real hesitando, ou foi instalada porque imperfeição sinaliza autoria?
- [ ] O que aqui é irredutivelmente do autor: uma leitura própria, uma memória vivida, uma conexão entre áreas que só a formação dele produz? "A voz" não basta, porque voz se imita.

Quando um parágrafo está genérico, a correção quase nunca é de estilo: é trazer o fato, a experiência ou a conexão que faltava.
