---
name: wincyfu-weekly-generator
description: Generate, review, and package a structured AI/design weekly issue while loading source lists, owner links, publishing adapters, and account details from private local configuration. Use for weekly issue generation, regeneration, item replacement, local review, or an explicitly authorized draft sync.
---

# WincyFu Weekly Generator

Create an evidence-backed AI/design weekly issue without embedding the owner's private source registry or publishing configuration in the Skill.

## Privacy boundary

Never write private runtime values into this Skill directory, generated documentation intended for publication, Git history, logs, or the final response.

Treat these as private inputs:

- source registries and source-priority notes;
- owner-submitted links and inbox/chat/document identifiers;
- credentials, application IDs, account allowlists, and API endpoints;
- publication history, candidate audits, drafts, analytics, and private templates.

Load them from `AI_WEEKLY_PRIVATE_CONFIG`. If the variable is missing, look for `.private/ai-weekly.json` at the active project root. Stop before source collection or external publishing when no valid private configuration is available.

Read [references/private-configuration.md](references/private-configuration.md) before configuring a new project. Use `config/ai-weekly.example.json` only as a schema example; never replace its placeholders with real values in the repository.

## Modes

- `local_generation`: collect candidates, prepare a local Markdown/HTML review package, and stop for review.
- `regeneration`: refresh the selected content or cover and rebuild all affected review artifacts.
- `item_replacement`: replace only named items, then invalidate and rebuild downstream evidence.
- `draft_sync`: run only after explicit user authorization and only through the private publishing adapter.

Local generation is the default. Do not notify chats, create cloud documents, create drafts, schedule, publish, or delete external content unless the user explicitly requests that exact action.

## Workflow

1. Resolve and validate the private configuration with `scripts/validate_private_config.py`.
2. Determine the issue window and output directory. Use the configured timezone and schedule; do not infer publication state from old folder names.
3. Collect current-window candidates from private sources. Keep discovery URLs separate from final article/tool/event URLs.
4. Apply the editorial and evidence gates in [references/editorial-gates.md](references/editorial-gates.md). Never fill a section with weak items merely to reach a target count.
5. Build the current Markdown and HTML preview, package metadata, candidate audit, and image audit.
6. Review every selected image at original size. Reject blocked pages, login screens, cookie overlays, blank captures, unrelated images, and misleading decorative images.
7. Run project-specific validators from `validation_commands` in the private configuration. A failed command blocks acceptance.
8. Report local artifact paths, validation results, and the remaining owner action. Keep automated validation, visual validation, and owner acceptance as separate states.

For schemas and minimum artifact expectations, read [references/output-contract.md](references/output-contract.md).

## External publishing

Before any draft sync:

1. Confirm the user explicitly requested draft creation.
2. Require an owner-accepted current package.
3. Re-run all configured validation commands.
4. Resolve the publishing adapter from private configuration.
5. Verify the detected account equals the private allowlisted account.
6. Create a draft only; do not publish or schedule.
7. Read the created draft back and verify title, body, image count, and account before reporting success.

A returned draft ID without successful read-back is incomplete. Never retry creation blindly when an earlier attempt may already have created an external draft.

## Private extensions

Project-specific rules may be loaded from `private_rule_files` in the private configuration. They may tighten this public workflow but must not silently weaken its privacy boundary, explicit-authorization rules, validation gates, or read-back requirement.
