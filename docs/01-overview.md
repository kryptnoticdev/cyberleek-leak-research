# 1. Overview

This investigation tracks two separate but entangled threads:

1. **Is the leaked footage/map content real?** — forensic analysis of file metadata, codec fingerprints, and blockchain upload records to establish authenticity and provenance, independent of who's distributing it.
2. **How is Cyberleek exploiting it?** — tracking the `$CYBERLEEK` token, the wallet/contract that served the media, and the promotional mechanics.

## How this repo is organized

- Each known media item gets one file under [`media-metadata/`](../media-metadata/).
- Metadata entries record hashes and provenance so items can be cross-referenced and verified independently, without this repo functioning as a distribution point.