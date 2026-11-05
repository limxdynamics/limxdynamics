# WeChat developer community badge

Every public LimX Dynamics repository (except the troncamp repos and anything
under the FluxVLA org) shows the same green "WeChat developer community" badge
as this profile, placed right under the README's language switcher.

## Updating the QR code (weekly)

The WeChat group QR code expires every 7 days. All badges link to one file:

    doc/wechat_qr.png   (in this repository)

Replace that file, keeping the same name, and commit. Every repository picks it
up immediately; no other repository needs to change.

## Changing the badge wording or style

1. Edit `BLOCK_EN` / `BLOCK_ZH` in `sync_community.py`.
2. Clone the repositories and run `python3 sync_community.py <clone dirs...>`.
   The badge sits between `<!-- limx-community:start -->` and
   `<!-- limx-community:end -->`, so the script replaces it in place.
3. Commit and push each repository.

Skipped repositories are listed in `EXCLUDE` in the script.
