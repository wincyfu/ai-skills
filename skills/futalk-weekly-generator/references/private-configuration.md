# Private configuration

Keep the real configuration outside the public repository. Set:

```bash
export AI_WEEKLY_PRIVATE_CONFIG=/absolute/path/to/ai-weekly.private.json
```

Alternatively, place it at `<project-root>/.private/ai-weekly.json`; `.private/` is ignored by the repository.

Required fields:

- `publication.name`: expected publication/account name.
- `publication.timezone`: IANA timezone used for issue windows.
- `source_registry_files`: absolute paths to private source registries.
- `owner_intake_files`: absolute paths to private owner-link inputs; may be empty.
- `private_rule_files`: absolute paths to private editorial or brand rules; may be empty.
- `validation_commands`: local commands that must pass before acceptance.

Optional publishing fields belong under `publishing` and remain private:

- `adapter_command`: local draft-creation adapter.
- `expected_account`: exact account allowlist value.
- `credential_files`: paths to locally protected credential files.

Do not store credentials themselves in JSON. Store only paths to protected local files or use the adapter's secure credential mechanism.

The validator checks structure and rejects obvious placeholder values, but it does not print private values.
