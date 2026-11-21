# humanize-text

**PT-BR** · [English below](#english)

Uma skill para transformar texto com cara de IA em prosa que uma pessoa específica poderia ter escrito, em **português do Brasil** e em **inglês (americano e britânico)**, sem parafrasear e sem perder fatos.

Ela não troca palavras por sinônimos. Mede, diagnostica parágrafo por parágrafo e, quando o texto é ruim de verdade, **reconstrói a partir da lista de fatos** em vez de maquiar. E confere o que quase nenhum humanizador confere: se o texto **diz a verdade sobre o tipo de afirmação que faz** (analogia virando definição, disputa virando consenso, "estudos mostram" sem estudo).

## O que tem de diferente

- **Léxico medido, não chutado.** Cada cacoete foi contado em fala humana transcrita: **11,5 milhões de palavras em português** e **10,8 milhões em inglês**, de vídeos de pessoas falando, com as transcrições ruins excluídas. Expressão que gente usa muito ("at the end of the day", "ou seja") não é tratada como marca de IA; só pesa em aglomerado.
- **Três pesos:** forte (uma ocorrência pede edição), fraco (só em cacho), observar (anota, não pontua).
- **28 cacoetes**, com exemplos nos dois idiomas, peso, exceções e regime por gênero (ensaio, roteiro, post, texto técnico).
- **Gate de estatuto**, o teste de verdade que roda junto do de voz.
- **Guarda de fatos:** nenhum número, nome, data, link ou fórmula entra ou sai sem registro.
- **Teste de humanwashing:** apagado o estilo, sobra conteúdo? Se não, o problema não é de estilo.
- **Americano ou britânico:** o medidor aponta grafia do outro lado e mistura das duas.
- **Não é ferramenta para enganar detector** nem para esconder que se usou IA. É método de edição.

## Instalação

**Claude Code** (e agentes que leem o padrão `SKILL.md`): copie a pasta `humanize-text` para `~/.claude/skills/` (vale para todos os projetos) ou para `.claude/skills/` dentro de um projeto. Peça "humaniza este texto" ou "tira a cara de IA disto".

**Claude.ai (app e web):** compacte a pasta em `.zip` e envie em *Configurações › Capacidades › Skills*.

**ChatGPT, Gemini, DeepSeek, Kimi, Qwen, Mistral e outros:** cole o conteúdo de [`PROMPT.md`](PROMPT.md) nas instruções personalizadas, num GPT personalizado, num Gem, num projeto ou na primeira mensagem da conversa. Funciona sem ferramentas. Onde o assistente roda Python (o ChatGPT roda), envie também `scripts/scan.py` e os dois `lexicon_*.tsv` e peça para usar o medidor.

## O medidor

Python 3, só biblioteca padrão.

```bash
python scripts/scan.py rascunho.md                       # idioma e tipo detectados sozinhos
python scripts/scan.py textos/*.md                        # lote: tabela-resumo
python scripts/scan.py draft.md --lang en --variant uk    # inglês britânico
python scripts/scan.py artigo.md --type technical         # regime leve, só léxico
python scripts/scan.py roteiro.md --dashes zero           # travessão vira regra dura
python scripts/scan.py --facts ANTES.md DEPOIS.md         # diff de fatos
python scripts/scan.py --validate-lexicon pasta/ --lang pt   # recalibrar com o seu corpus
```

Saída: palavras, cacoetes fortes e fracos, sinais de estrutura (fragmento em fila, ritmo uniforme, fecho em frase de efeito, tríades, conectores em série, negrito decorativo, travessão, títulos em Title Case, grafia US/UK), pontos por mil palavras, veredito (LIMPO, RETOQUE, REESCRITA PARCIAL, RECONSTRUÇÃO) e os parágrafos mais carregados, para ler primeiro.

**É ponto de partida, não veredito.** Texto LIMPO pode ser oco; texto com pontuação alta pode ser de uma pessoa com tiques. Se o medidor marca um texto que você considera bom, ajuste o medidor, não o texto.

## Arquivos

```
humanize-text/
├── SKILL.md                    instruções da skill
├── PROMPT.md                   o método inteiro num arquivo, para qualquer IA
├── references/
│   ├── method.md               modos A/B/C, fluxo, leitura do medidor, parecer
│   ├── blacklist-pt-BR.md      os 28 cacoetes em português, pesos, exceções, gates
│   ├── blacklist-en.md         o mesmo em inglês, com US e UK
│   └── status-check.md         o gate de estatuto (verdade)
└── scripts/
    ├── scan.py                 o medidor
    ├── lexicon_pt-BR.tsv
    └── lexicon_en.tsv
```

## Limites

- O léxico foi validado contra **fala**. Palavra de registro escrito ("intrincado", "delve") sempre parece mais rara na fala; por isso frequência sozinha nunca promove uma palavra a forte.
- Parte dos vídeos recentes pode ter narração escrita com ajuda de IA, o que deixa o medidor, se tanto, mais tolerante, nunca mais severo.
- Os limiares de veredito são provisórios. Recalibre com textos do seu gênero.

## Contribuir

Regra nova no léxico entra com a contagem em fala humana (`--validate-lexicon`) e um exemplo real. Forte de segunda ordem só abaixo de 5 ocorrências por milhão de palavras de fala.

Licença: [MIT](LICENSE).

---

<a name="english"></a>
## English

A skill that turns AI-sounding text into prose a specific person could have written, in **Brazilian Portuguese** and **English (US and UK)**, without paraphrasing and without losing facts.

It does not swap words for synonyms. It measures, diagnoses paragraph by paragraph and, when a text is genuinely bad, **rebuilds it from its list of facts** instead of polishing it. It also checks what almost no humanizer checks: whether the text **tells the truth about the kind of claim it makes** (an analogy turned into a definition, a dispute turned into consensus, "studies show" with no study).

### What is different

- **A measured lexicon.** Every tic was counted in transcribed human speech: **11.5 million words of Portuguese** and **10.8 million of English**, from videos of people talking, with poor transcripts excluded. Phrases people say all the time ("at the end of the day", "here's the thing") are not treated as AI markers; they count only in clusters.
- **Three weights:** strong (one hit calls for an edit), weak (clusters only), watch (noted, not scored).
- **28 tics**, with examples in both languages, weights, exceptions and a regime per genre (essay, script, post, technical writing).
- **A status gate**, the truth test that runs with the voice gate.
- **A fact guard:** no number, name, date, link or formula enters or leaves unrecorded.
- **The humanwashing test:** with the style stripped away, is there content left? If not, the problem is not style.
- **US or UK:** the meter reports spellings from the other side and mixed spelling.
- **Not a detector-evasion tool** and not a way to hide AI use. It is an editing method.

### Install

**Claude Code** (and agents that read the `SKILL.md` standard): copy the `humanize-text` folder to `~/.claude/skills/` (all projects) or to `.claude/skills/` inside a project. Ask "humanize this" or "make this sound less like AI".

**Claude.ai (app and web):** zip the folder and upload it under *Settings › Capabilities › Skills*.

**ChatGPT, Gemini, DeepSeek, Kimi, Qwen, Mistral and others:** paste [`PROMPT.md`](PROMPT.md) into custom instructions, a custom GPT, a Gem, a project or the first message of a chat. It works without tools. Where the assistant runs Python (ChatGPT does), also upload `scripts/scan.py` and both `lexicon_*.tsv` files and ask it to use the meter.

### The meter

Python 3, standard library only. Same commands as above: language and type are auto-detected; `--variant us|uk`, `--type technical`, `--dashes zero`, `--facts BEFORE AFTER`, `--validate-lexicon DIR --lang en`.

**A starting point, not a verdict.** A CLEAN text can be hollow; a high score can be a human with tics. If the meter flags a text you consider good, fix the meter, not the text.

### Limits

- The lexicon was validated against **speech**. Written-register words ("delve", "intricate") always look rarer in speech, so frequency alone never promotes a word to strong.
- Some recent videos may have AI-assisted narration, which makes the meter more lenient if anything, never harsher.
- Verdict thresholds are provisional. Recalibrate on texts from your own genre.

### Contributing

A new lexicon rule comes with its count in human speech (`--validate-lexicon`) and a real example. A second-order strong rule must stay under 5 occurrences per million words of speech.

License: [MIT](LICENSE).
