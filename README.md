# WincyFu AI Skills

Reusable AI workflow skills maintained by WincyFu.

## Skills

- [`futalk-weekly-generator`](skills/futalk-weekly-generator/) — generate and review a structured AI/design weekly issue while keeping private sources and publishing configuration outside the repository.

## Privacy model

This repository contains workflow logic only. Real source lists, owner-submitted links, chat/document identifiers, credentials, publication history, drafts, analytics, and account-specific templates are private runtime inputs and are intentionally excluded from Git.

Each skill documents its private configuration contract. Copy the provided example locally, keep the real file outside the repository or under `.private/`, and point the skill to it through an environment variable.
