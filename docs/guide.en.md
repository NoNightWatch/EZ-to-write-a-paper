<p align="center"><img src="../assets/guild/guide.svg" width="960" alt="User guide · PAPER QUEST v3.7.1" /></p>

# English user guide

[Back to the homepage](../README.en.md) · [中文指南](guide.zh-CN.md) · [Download ZIP directly](https://github.com/NoNightWatch/EZ-to-write-a-paper/releases/latest/download/academic-manuscript-polish.zip)

This guide takes you from installation to your first revision with `academic-manuscript-polish`. Start with a sentence or bring a full draft. The author's materials support the technical content; the assistant handles expression, organization, and explanation within the agreed scope.

**Choose the entry you need. You do not need to read this guide in order.**

| What you want now | Go directly to |
| :--- | :--- |
| Find starting a paper difficult | [Say one clear thing](#one-clear-thing) |
| Try the workflow | [File-based trial without installation](#try-without-install) |
| Use it regularly | [Install](#install) or [update an older version](#update) |
| Revise a paragraph | [First session](#first-session) and [editing controls](#controls) |
| Address mechanical or generic prose | [Disciplinary style and author voice](#field-style) |
| Write a review | [Literature reviews](#review) |
| Address reviewer comments | [Revision responses](#reviewer-response) |
| Resume a long draft | [Versions and continuation](#long-drafts) |

## 1. What you are downloading

PAPER QUEST is an academic writing guide for use with an AI assistant or for self-study. It brings together writing workflows, terminology, lessons, journal references, and optional lookup tools. Have a file-reading assistant consult the relevant resources for your draft, or read them directly as Markdown.

Prepare:

- An AI assistant that can read the guide and your writing.
- Some text, notes, an outline, or references you have permission to share. Without materials, you can practice with an explicitly fictional example.
- Your target journal and article type, if decided. You can start without them.

You do not need Python to begin. Scripts are optional lookup and maintenance tools. Accounts, service costs, connectivity, and privacy settings belong to the AI service you choose.

<a id="try-without-install"></a>
### Try without changing a manuscript or settings

Download and extract the complete bundle into a workspace your assistant can read. Open `START-HERE.en.md`, or send:

```text
Read academic-manuscript-polish/SKILL.md and follow its workflow.
Confirm that the entry and required resources are accessible.
Do not install anything or change settings.
Use assets/first-session-demo.md inside that guide folder.
Revise and explain in English. Do not save files.
```

This uses file access without configuring automatic loading. Supply the actual path if your working directory differs. If your chat tool cannot read folders, provide the relevant content or use a local-file assistant. A claim to know the guide does not prove that its files were loaded.

Expect a clean revision and two explanations, with participant numbers and attribution preserved. Then ask to restore the first sentence while keeping the second revision. The [fictional demo](../academic-manuscript-polish/assets/first-session-demo.md) includes a reference output. No private manuscript is needed.

<a id="install"></a>
## 2. Download and install

### Get the complete bundle

[Download `academic-manuscript-polish.zip` directly](https://github.com/NoNightWatch/EZ-to-write-a-paper/releases/latest/download/academic-manuscript-polish.zip) and extract it. This points to the latest release; check its version in the folder's `bundle-manifest.json`. Alternatively, choose **Code → Download ZIP** on the repository homepage and take the `academic-manuscript-polish` folder from that download.

Do not copy only `SKILL.md`. The other resources are loaded through relative paths, so preserve the folder hierarchy. Extract the ZIP before using the local-directory installation method.

### Choose an installation scope

| Assistant | Current project only | Across your personal projects |
| :--- | :--- | :--- |
| Codex | `<project>/.agents/skills/academic-manuscript-polish/` | `~/.agents/skills/academic-manuscript-polish/` |
| Claude Code | `<project>/.claude/skills/academic-manuscript-polish/` | `~/.claude/skills/academic-manuscript-polish/` |

`~` means your home directory. On Windows, entering `%USERPROFILE%` in File Explorer's address bar opens it; on macOS/Linux, use your user's home folder. Replace `<project>` with the working folder you actually open. Usually one installation scope is enough; avoid loading several versions with the same name.

A project installation looks like this:

```text
my-paper/
  draft.md
  .agents/
    skills/
      academic-manuscript-polish/
        SKILL.md
        START-HERE.en.md
        START-HERE.zh-CN.md
        references/
        assets/
        scripts/
        tests/
        agents/
        README.md
        bundle-manifest.json
```

For a Claude Code project, the corresponding directory is `.claude`. Check that `SKILL.md` is directly inside `academic-manuscript-polish/`, without an extra nested folder of the same name.

Paths were checked on 2026-10-18 against the official [OpenAI host documentation](https://learn.chatgpt.com/docs/build-skills) and [Claude Code documentation](https://code.claude.com/docs/en/skills). Organization policies and cloud sessions can differ from local sessions; follow your host's current instructions.

### Check that the assistant can read it

Start a session in the relevant project and try:

- Codex CLI / IDE: `$academic-manuscript-polish`. In desktop hosts, use the supported guide selector or a natural-language request.
- Claude Code: `/academic-manuscript-polish`

You can also say: “Read the installed academic-manuscript-polish guide and use its workflow for the paragraph below.” If the list has not refreshed, check in a new session. Ask the assistant which entry file it actually read; saying it knows the guide is not evidence that it loaded your files.

For another assistant with directory access, point it directly to `SKILL.md`. If it accepts only pasted chat text, provide the entry instructions and relevant resources manually, but automatic access to all relative links is not guaranteed. Ordinary chat uploads and host-managed loading may have different capabilities.

### Want your assistant to copy it for you?

For Codex with local file permissions, you can send the request below. The corresponding Claude Code project directory is `.claude/skills/`.

```text
Install my extracted academic-manuscript-polish folder into this
project's .agents/skills/ directory. Do not change other settings.
Confirm the source and destination. If the destination already
exists, report versions and differences without overwriting,
deleting, or merging. Check the copied files and report the
installed version and entry path.
```

This request authorizes copying to that location; downloading alone does not. Start with project scope unless you specifically want the guide across projects.

<a id="first-session"></a>
## 3. First session: bring one paragraph

Copy this and replace the bracketed parts:

```text
Please use academic-manuscript-polish.
I am new to academic writing.

My material: [paste one paragraph or provide an accessible file].
Target journal: [journal name / undecided].
Scope: this paragraph only.
Draft language: [original language / English / Chinese].
Explanation language: English.

Give me a usable revision first, then explain the two most
important changes. Preserve numbers, citations, and meaning.
Do not add research facts. Ask if a technical meaning is unclear.
```

Expect a revised paragraph, a few important explanations, and questions that genuinely affect the editing. Clear original sentences may remain unchanged. You can reject an edit, restore a term, ask for lighter editing, or request an explanation.

If the output changes your meaning, be specific: “Here, X means […]. Restore that definition and keep the other changes.”

If you prefer less setup, “Polish this paragraph and preserve its meaning” is enough. The default preserves the supplied passage's content and structure, keeps its language, and explains in the conversation's language. Add a journal later if needed.

<a id="one-clear-thing"></a>
### Say one clear thing

If thinking about a whole paper makes it difficult to begin, open the [short English entry](../academic-manuscript-polish/references/one-clear-thing.en.md), or send:

```text
Help me begin with “Say one clear thing.” Teach in English.
Do not show the whole course, glossary, or journal requirements yet.
Ask about one thing in my materials and let me answer in everyday language.
Use my answer, identify what it already communicates, and address one key point.
I may request a demonstration, direct editing, or a pause at any time.
```

Use an existing sentence if you have one; there is no need to start it again. With materials, describe an observation. With only a topic, form a question. Without materials, you may choose a fictional example. Findings must not be invented to complete a task.

A record, a quoted sentence, two notices, or your own notes count as starting material. You do not need to know whether they support a whole paper yet. If you do not know where to look, say: “Point to something in this passage and ask me one specific question.” Answer in everyday language without fitting a fixed sentence frame.

“I think the new version flows better” can begin as a note about your impression. For analysis, look for a change that can be checked in the text, such as how sentences are connected; unobserved reader reactions cannot become results. The assistant should explain the sentence's current use. You can ask: “Does this belong in my notes or in the paper?”

The assistant explains what the sentence can do and retains usable wording. If numbers, units, or sources are missing, it asks about what needs checking now; untidy language can be revised gradually. It does not give a total score, a countdown, or a demand to complete every part of the paper at once.

One sentence is a valid stopping point. If you want to continue, add a source or related sentence, then expand into paragraphs or the course as appropriate. You can request the full course directly without resubmitting confirmed work. This entry helps organize a start to writing; it is not a psychological assessment and has not been tested for emotional or learning outcomes.

<a id="first-paper"></a>
### Learn to write a whole paper from the beginning

You can edit an existing draft directly. For a structured practice route, open the [complete-paper course](../academic-manuscript-polish/references/first-paper-course.en.md); no private manuscript is needed. Six pairs of fictional service cards support one complete descriptive comparison paper. All original card texts and counting rules are included.

```text
Read first-paper-course.en.md in the complete bundle.
I have never written a paper. Use the fictional case and teach in English.
Start with E01 in the English workbook, showing only the current task.
Let me try, then identify a specific passage, its evidence, and one revision.
Give a hint if I am stuck; give the answer when I request it.
Do not transfer teaching data or fictional readings into my real paper.
```

| How you want to start | Open |
|---|---|
| Try first, then receive feedback | [English workbook](../academic-manuscript-polish/references/paper-workbook.en.md), with E01 to E08 and T01 |
| Follow one paper section by section | [Continuous walkthrough](../academic-manuscript-polish/references/paper-case-walkthrough.md), primarily Chinese; request English explanations |
| Read the finished manuscript | [Complete English model](../academic-manuscript-polish/references/paper-case-manuscript.md), including abstract, sections, results table, and references |
| Find what is missing | [Missing-materials guidance](../academic-manuscript-polish/references/missing-materials.md), primarily Chinese; request English explanations |

The eight stages produce an evidence inventory, question and outline, methods, results, introduction, discussion and conclusion, title and abstract, then a full-paper consistency check. Feedback points to your actual wording and evidence, followed by a reattempt and recheck. The [reference answers](../academic-manuscript-polish/references/paper-answer-key.md) are stored separately and available whenever you ask.

The final task uses new event-notice records. Directions differ from the original case, and original texts are unavailable, requiring different conclusions and an honest access statement. Record what you did independently and what needed hints; completing these tasks does not establish general research competence.

For your own manuscript, supply real materials and use the structure appropriate to its genre. This case illustrates one genre; mathematics, history, reviews, and others may need different organization. Fictional data must not be submitted as research. No student learning-outcome study has been conducted. You may leave practice and request direct editing at any point.

<a id="controls"></a>
## 4. Choose how you want to work

| Your time and needs | What to request |
| :--- | :--- |
| In a hurry | “Give me the revised text directly. Ask only questions that affect correctness.” |
| Want to understand the edits | “Revise first, then explain the two or three most important changes.” |
| Want to learn to revise | “Show one example, then offer an optional exercise and a reference answer.” |

Switch at any point. Exercises can be skipped. Choosing mentoring does not automatically authorize restructuring the whole manuscript or adding discussion content.

Specify the editing permission as well:

- **Language editing**: grammar, spelling, wording, references within sentences, and transitions, while preserving content.
- **Structural editing**: allow changes to paragraph or section order and request a mapping to the original.
- **Drafting from supplied material**: organize facts, explanations, and references already provided; list gaps for the author.

With only a topic, request a working outline or a materials checklist. Without data or results, anticipated findings must not be written as completed research.

### Control the output in ordinary language

| What you want to change | What to say |
| :--- | :--- |
| Diagnose first | “Identify the two main obstacles to understanding. Do not edit files yet.” |
| Preserve your voice | “Keep my wording and paragraph order; list optional style suggestions separately.” |
| Compare changes | “Give a clean, copyable version, then the important before/after changes.” |
| Restore a sentence | “Restore this version's second sentence from the original; keep the other changes.” |
| Reduce explanation | “Explain only the most important change and skip the exercise.” |

Restoring text requires the original. If the version is unclear, provide the sentence again. A plain-text comparison differs from native Word tracked changes, which require suitable host capabilities and an actual generated file. See [session controls](../academic-manuscript-polish/references/session-controls.md).

<a id="field-style"></a>
### Write naturally in your field, with your own voice

You can request natural or native-like academic prose. The assistant checks subject continuity, sentence structure, the placement of qualifications, and paragraph rhythm. It keeps clear long sentences, combines repetitive openings, and retains short sentences that mark a contrast or scope boundary. There is no universal sentence-length score, and concision must preserve conditions and citations.

```text
Revise this paragraph in a natural style suited to my field, keeping my voice.
Do not split sentences mechanically. Combine repeated subjects where useful,
while preserving every claim and qualification.
Reference passages: [optional materials or links to comparable sections].
Give one clean version and explain two choices to keep, combine, or split sentences.
```

When examples are available, use actual text from the same field, genre, and section. An abstract-only sample supports abstract-level observations. Editing can start without examples, but field-specific calibration should then be marked as unperformed. Names and affiliations do not establish an author's first language or writing quality. Journal requirements, general advice, and observed usage are handled separately; a clear original sentence can stay unchanged.

For example, `We examined X. We compared Y. We reported Z.` can become `We examined X, compared Y, and reported Z.` when the subject and conditions are shared. Different actors or citation scopes may require explicit separation. The package includes the [decision workflow](../academic-manuscript-polish/references/field-natural-style.md) and [eight sets of examples](../academic-manuscript-polish/references/field-style-examples.md). Explanations can be simple while the manuscript retains the technical information its readers need.

## 5. Match terminology to your manuscript

Provide the research object, main question, and relevant passage. This is usually more informative than a field name alone. Cross-disciplinary work can use a main field and the necessary secondary fields.

```text
This paragraph concerns battery materials. In this manuscript,
SOC means state of charge. Check abbreviations and terminology
for consistency, preserving the author's definition.
Do not apply a different field's definition of the same acronym.
```

The 52 entries provide foundation coverage. For missing terms, specialized definitions, or less-covered fields, provide references you may use and explain whether you want terminology, genre, or organizational guidance. The assistant should record provenance, reading scope, and applicability. Facts from a sample article must not be transferred into your paper as your findings.

Author-supplied references and temporary glossaries are for the current manuscript by default. They are not automatically added to the shared bundle. Working glossary definitions should not be presented as verbatim standards.

### How does this field express the intended action?

The [field-usage resources](../academic-manuscript-polish/references/usage-selection.md) provide 208 contrasts across all 52 entries. Each includes candidates, collocations, selection conditions, an original example, and meaning boundaries. For instance, `rebuild a project` fits a software build task, `restructure an organization` concerns organization, and fisheries also uses `rebuild a stock`. The actual object and action control the choice; a discipline label alone is insufficient.

```text
Check the research verbs and collocations against the objects in this paragraph.
Explain choices among terms such as restructure, rebuild, and reconstruct.
Preserve technical meaning and claim strength. Keep suitable original wording.
You may consult my field-specific references, but do not treat a few examples
as evidence of a universal disciplinary preference.
```

From the bundle root, optionally run `python scripts/search_usage.py "rebuild" --exact --format text`; add `--domain n10` for computing. You can also ask the assistant to read the resources without using commands. The examples illustrate editorial choices; they are not a frequency ranking of native-speaker usage.

<a id="review"></a>
## 6. Use it for a literature review

Identify the task: an introduction paragraph, a thesis chapter, a standalone review, or related work. A short paragraph can start from a few existing materials.

```text
Here are the papers and notes I have read. I need one review
paragraph for an introduction. My organizing question is [question].
Record what you can actually read from each source. Compare
similarities and differences, then draft a traceable paragraph.
List relationships that lack support. Do not describe this
limited collection as a systematic review.
```

A useful sequence is:

1. Define one answerable organizing question.
2. Distinguish full text, partial text, abstracts, and secondary quotations; record actual access.
3. Choose comparison fields for the question, such as objects, periods, definitions, or research tasks.
4. Check which specific claim each source supports. Do not use one citation to cover unrelated claims in a compound sentence.
5. Organize a paragraph that states agreements, differences, and limits.
6. Recheck sources, attribution, and unresolved gaps.

Standalone systematic reviews, scoping reviews, and other review types have corresponding methods requirements. A reporting checklist cannot replace the actual search and screening process. Start with the [worked exercise](../academic-manuscript-polish/references/review-worked-example.md), then explore [history, philosophy, mathematics, and computing/engineering exercises](../academic-manuscript-polish/references/review-transfer-cases.md). Their demonstration materials are fictional and cannot be cited as real literature.

## 7. Supply a target journal

Give the full journal name, article type, and official author-guideline link. You may add a small number of published articles matching your article type, specifying what you want to learn from them.

```text
Target journal: [name]. Article type: [type].
Official guidelines: [link or file].
This session covers only the abstract, title, and keywords.
Separate explicit journal requirements, observations from sample
articles, and unverified items. Preserve the strength of my claims;
do not add novelty claims or promises of acceptance.
```

The 40 reference cards offer a starting point; current official guidance controls the requirements. Distinguish article type, initial submission or revision, requirements or recommendations, and words or characters. If browsing is unavailable, provide the guideline file. Unchecked items remain labelled unverified. Search with public journal information, without sending unpublished text. Adaptation may change structure, audience framing, and length, while preserving the meaning of the research.

<a id="long-drafts"></a>
## 8. Long drafts, files, and continuing later

Handle a long draft in batches, such as abstract, introduction, methods, results, and discussion. Maintain terminology decisions and a change list. Each batch should state the passages actually completed; unread sections must not be marked reviewed.

Editable text is preferable. Reading and preserving Word files, PDFs, equations, figures, tables, and reference-manager fields depend on host capabilities. If a figure or equation is inaccessible, ask for the specific gap and supply a clear image or text when needed. A successful Markdown check does not verify Word layout.

When pausing, say:

```text
Create a continuation card with the manuscript version, completed
sections, terminology decisions, unresolved questions, and next step.
Put it in the conversation for now; do not save a file.
```

Provide that card and the correct manuscript version in the next session. If you want it saved, specify a location. The assistant should not promise automatic memory of everything across sessions.

## 9. Optional offline term lookup

With Python 3.9 or newer installed, open a terminal inside the guide folder:

```sh
python scripts/search_terms.py "validity" --exact --format text
python scripts/search_terms.py "SOC" --exact --format text
python scripts/search_terms.py "yield" --domain agronomy-horticulture
python scripts/search_terms.py --list-domains --format text
python scripts/validate_bundle.py
python -B tests/test_bundle.py
```

The search script reads local resources; it does not call a model or upload text. Results include domain, definition, and location. A term may have several meanings. If nothing matches, check spelling or word forms, or inspect the resources manually. Zero results do not establish that the concept is absent from the field.

`--format text` is for direct reading. Omit it to retain the original JSON output for other programs.

## 10. Troubleshooting

| Symptom | Check first |
| :--- | :--- |
| Guide not found | ZIP extracted; correct `SKILL.md` depth; session opened in the relevant project; organization policy permits it |
| References unavailable | Complete folder copied; relative paths intact; assistant has read access |
| Responses in Chinese | Explicitly request English revisions and explanations; internal teaching materials are primarily Chinese |
| Too much rewriting | Restrict edits to language and list terms, sentences, or arguments that must remain |
| Journal rules seem outdated | Request current official guidance and an access date; supply the file if the page cannot be reached |
| Fictional exercise treated as a source | Remove that citation and verify a real source; examples are teaching materials only |
| Too many preliminary questions | Ask it to complete what it can and retain only questions that block correct editing |

## 11. What the author should check before using the result

- Numbers, units, direction, time windows, and equation conditions are preserved.
- Citations exist and support the corresponding claims.
- Technical definitions match the author's materials.
- Changes do not strengthen conclusions or introduce unsupported facts.
- Submission format, AI-use disclosure, and institutional requirements have been checked.
- Incomplete checks are clearly identified.

Review the host's data-processing rules and your authority to share the manuscript. Do not provide confidential information without permission or attach private drafts to public Issues. This bundle contains no third-party paper full texts. General writing guidance does not replace specialist judgment, clinical judgment, or review of high-risk operations.

Structure and search tests cover the glossaries, usage layer, and journal cards. Course tests check fictional counts, calculations, and bilingual tasks, with separate public-page locale checks. The [novice walkthrough record](../academic-manuscript-polish/tests/novice-session-audit.md) separately documents two Chinese agent dialogues, an English probe with maintainer-written learner messages, and a fresh retest after repairs: 12 tutor replies in total. These AI simulations do not validate human learning or emotional outcomes. See also the [course check record](../academic-manuscript-polish/tests/paper-course-audit.md) and [usage checks](../academic-manuscript-polish/tests/usage-journal-audit.md).

<a id="reviewer-response"></a>
## 12. After receiving reviewer comments

Supply the original comment, the relevant current manuscript passage, and the changes you actually made. Start with one comment if that is all you have organized.

```text
Use academic-manuscript-polish for this reviewer comment.
Original comment: [paste].
Current manuscript passage: [paste or locate in an accessible file].
Changes already made: [actual changes; say none if none].
My intended response: [optional; undecided is acceptable].
Draft a response with its manuscript location. Keep planned work
separate from text that is ready to submit.
```

The assistant distinguishes completed changes, planned work, requests for clarification, and changes the author has decided not to make. Without real line numbers, it uses section and paragraph openings. Technical disagreements require your judgment and evidence; it must not invent experiments, analyses, or completed work. See the [reviewer-response workflow](../academic-manuscript-polish/references/reviewer-response.md).

<a id="update"></a>
## 13. Update while preserving your own work

1. Download the new release to a separate temporary location and read the version in `bundle-manifest.json`.
2. Confirm the guide directory you actually use. Compare and save custom edits separately before replacing anything.
3. Back up the old version outside the host's automatic-loading folders, avoiding simultaneous loading of two same-name versions. Keep private manuscripts and temporary glossaries in your manuscript workspace.
4. Copy the complete new folder to the confirmed destination. Avoid mixing new files with leftovers or creating an extra nested folder.
5. Start a new session, ask which version and entry file were actually read, and use the fictional demo to check access.

Updating does not migrate your manuscript. If a problem occurs, stop using the new version and restore from your own previous copy. Do not let an assistant silently delete backups or merge conflicting files.

<p align="center"><img src="../assets/guild/next.svg" width="960" alt="Your next sentence starts here." /></p>
<p align="center"><a href="../README.en.md">Back to the homepage</a> · <a href="guide.zh-CN.md">中文指南</a> · <a href="../academic-manuscript-polish/references/beginner-guide.md">Continue to the beginner resources</a></p>
