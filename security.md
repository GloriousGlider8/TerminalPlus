# Security Policy

## Reporting a Vulnerability

If you notice a security flaw, **STOP RUNNING THE HOSTED CONTENT IMMEDIATELY using the Security Flaw Keybind: [CTRL] + [SHIFT] + [C]** and report the flaw [here](https://github.com/GloriousGlider8/webTest/issues "PyHost GitHub Issues Page").

#### Abusing a flaw will result in an IP and system ban

## Manual Security Actions

Use **[CTRL] + [A]** when hosting to access the actions menu.

## host.yml

`host.yml` is located in the main folder and deafults to:

```yaml
denylist:
  - null
allowlist:
  - null
use: denylist
type: text/html
code: 200
```

In JSON that is:

```json
{
  "denylist": [
    null
  ],
  "allowlist": [
    null
  ],
  "use": "denylist",
  "type": "text/html",
  "code": 200
}
```

It contains security settings like who can view documents.
You can edit it safely.

> **If you do not know YAML, the settings menu changes this safely.**