# Start with one paragraph

[中文](START-HERE.zh-CN.md) · [Bundle contents](README.md) · [Full online user guide](https://github.com/NoNightWatch/EZ-to-write-a-paper/blob/main/docs/guide.en.md)

This folder contains writing instructions and resources for an AI assistant. You do not need to learn the terminology or choose a writing category first. Resources and lookup tools work locally; AI processing depends on your host's settings. Most teaching resources are in Chinese, with bilingual terms. Ask for English output and explanations.

## Try it before installing

Extract the ZIP into a workspace your assistant can read, then send:

```text
Read academic-manuscript-polish/SKILL.md and follow its workflow.
Confirm that the entry file and the resources needed are accessible.
Do not install anything or change settings.
Use the fictional paragraph in assets/first-session-demo.md for
a demonstration. Revise and explain in English. Do not save files.
```

Supply the actual location if the folder is elsewhere. Reading a local file does not configure automatic loading. A chat interface without file access requires you to provide the relevant content separately. You can try the workflow without sharing a private draft.

## Bring your own text

```text
Use academic-manuscript-polish to edit this paragraph.
Change only the language and preserve the meaning.
Keep the draft's language; explain the edits in English.
[Paste text.]
```

A target journal is optional. When available, supply its name, article type, and current author guidelines. Specify another explanation language if you prefer.

## Change the editing controls at any time

To learn a whole paper from the beginning, open the [complete-paper course](references/first-paper-course.en.md) and say: “Use the fictional case for E01. Let me try before giving specific feedback. Teach in English.” It includes a full model paper, an [English workbook](references/paper-workbook.en.md), and a new-material exercise. You may request an answer at any time.

- “Diagnose only. Do not revise yet.”
- “Give a clean version and the important before/after changes.”
- “Keep this term and restore the original second sentence.”
- “Give me the answer without an exercise.”
- “Demonstrate one sentence, then let me try.”

The assistant should preserve the original and state the work actually completed. Missing technical definitions, data, or explanations require the author's materials.

## Install when you want to use it regularly

Copy the whole folder into `.agents/skills/` in a Codex project or `.claude/skills/` in a Claude Code project, and start a session there. Follow your host's current instructions. Do not copy only `SKILL.md`. Ask the assistant to report the entry file it actually read, then use the demo to check resource access.

If a version with the same name exists, compare versions and custom edits first. Keep an old copy outside the host's automatic-loading folders before replacing the confirmed target. Do not merge versions or leave backups in a folder that automatically loads guides. Downloading this bundle does not install or update an existing guide.

## Choose the resource for your current task

| Your task | Open |
|---|---|
| See a first output | [Fictional demo](assets/first-session-demo.md) |
| Control edits and explanations | [Session controls](references/session-controls.md) |
| Learn with notes or sentences | [Beginner entry](references/beginner-guide.md) |
| Turn sources into a paragraph | [Review mentor](references/literature-review-mentor.md) |
| Respond to reviewers | [Revision-response workflow](references/reviewer-response.md) |
| Work in an unlisted field | [Author-supplied references](references/author-literature.md) |

Optional offline lookup: from this folder, run `python scripts/search_terms.py "SOC" --exact --format text`. Python 3.9+ is required for scripts only.
