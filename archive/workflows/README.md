# Retired write workflows

The repository is closed. Write-capable correction workflows have been removed from `.github/workflows/` so the frozen corpus has no routine automation that can rewrite corrected JSON or audit ledgers.

The retired `backwards_pdf_corrections.yml` remains recoverable in Git history (last active blob `b23aa516f7a8ab7f25c25a54e40df8e1266f076a`). Its function was to reapply the already-recorded PDF correction ledgers for chunks 067–071, validate the resulting corrected derivatives and verification logs, and commit those generated outputs back to `main`.

Any future use of that workflow should be treated as an explicit reopening of the bounded correction/editorial layer, not ordinary maintenance of the frozen research corpus.
