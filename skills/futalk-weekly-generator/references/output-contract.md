# Output contract

Each run should produce a unique run directory containing at least:

- `preview.md`: readable local review copy.
- `preview.html`: styled browser review surface.
- `package.json`: structured issue metadata and selected items.
- `candidate_audit.tsv`: selected and rejected candidates with reasons.
- `image_audit.tsv`: selected image provenance, dimensions, and review state.
- `status.json`: separate automated, visual, and owner-acceptance states.

Recommended package fields:

```json
{
  "run_id": "opaque-current-run-id",
  "issue": "YYYY-MM-DD",
  "title": "Issue title",
  "digest": "Short digest",
  "cover_path": "/absolute/path/to/cover.png",
  "html_path": "/absolute/path/to/preview.html",
  "items": [
    {
      "section": "news",
      "title": "Displayed title",
      "original_title": "Original title",
      "summary": "Factual summary",
      "final_url": "https://example.invalid/item",
      "image_path": "/absolute/path/to/image.png"
    }
  ]
}
```

Bind review evidence to the current files with hashes when a private publishing adapter can create external drafts. Rebuilding any selected item, image, cover, HTML, or package invalidates downstream visual evidence.
