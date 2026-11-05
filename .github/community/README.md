# WeChat developer community badge

Every public LimX Dynamics repository (except the troncamp repos and anything
under the FluxVLA org) carries a small green "WeChat developer community" badge
in the badge row at the top of its README. Repositories derived from an
upstream project also carry a "fork of <upstream>" badge in the same row.

## Updating the QR code (weekly)

The WeChat group QR code expires every 7 days. All badges link to one file:

    doc/wechat_qr.png   (in this repository)

Replace that file, keeping the same name, and commit. Every repository picks it
up immediately; no other repository needs to change.

## Changing the badge wording or style

1. Edit `WECHAT_EN` / `WECHAT_ZH` (or `FORKS`, `BASE_ROWS`) in `sync_community.py`.
2. Clone the repositories and run `python3 sync_community.py <clone dirs...>`.
   Managed badges are found by their link, so re-running replaces them in place.
3. Commit and push each repository.

Skipped repositories are listed in `EXCLUDE` in the script.
