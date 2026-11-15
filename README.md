# nc-language — translations for Nimble Commander-Fork

Nimble Commander-Fork ships only **English** and **Simplified Chinese** and will not bundle other
languages. Translations for everything else are collected here: download the JSON file for your
language and import it, or contribute a new translation with a pull request.

## Using a translation

1. Download the file for your language from [`languages/`](languages/). More languages appear here
   as contributions arrive; [`languages/en.json`](languages/en.json) is the English reference.
2. In the app open **Preferences → Language → Import Language File…** and choose the file
   (中文界面：设置 → 语言 → 导入语言文件…).
3. Restart the app; the language appears in the language popup. Re-import after the file changes.

## Contributing a translation

1. Copy [`languages/en.json`](languages/en.json) to `languages/<code>.json` (for example
   `de.json`, `ja.json`, `pt-BR.json`).
2. In the copy:
   - set `"language"` to your language code and `"languageName"` to its display name;
   - translate the `"translation"` values; keep `source`, `bundle`, `table`, `key`, `comment`,
     `format` and `formatVersion` unchanged.
3. Test it: **Preferences → Language → Import Language File…**, choose your file, restart. Your
   language appears in the language popup; re-import after every edit.
4. Check the file and open a pull request:

   ```sh
   python3 tools/check-language.py languages/<code>.json
   ```

A partial translation is fine — empty or missing entries fall back to English.

## Files

| Path | Purpose |
| --- | --- |
| `languages/en.json` | The complete English export (Nimble Commander-Fork 1.9.3, 1473 entries) |
| `tools/check-language.py` | Small validator for a translated file |

## Format

The file is a JSON object:

```json
{
  "format": "nimble-commander-language-pack",
  "formatVersion": 1,
  "application": "1.9.3",
  "baseLanguage": "en",
  "language": "en",
  "languageName": "English",
  "entryCount": 1473,
  "entries": [
    {
      "bundle": "",
      "table": "FilePanelsContextMenu",
      "key": "Compress",
      "source": "Compress",
      "translation": "Compress",
      "comment": "optional hint for translators"
    }
  ]
}
```

- `bundle`, `table`, `key` identify the string — never change them.
- `source` is the English original — never change it.
- `translation` is the text to translate; an empty value falls back to `source`.
- `comment`, when present, explains the context.
- Entries whose `source` is empty are generated Interface Builder keys — leave their
  `translation` empty.

## Notes

- Translations are matched by `bundle` + `table` + `key`. `en.json` is re-exported from new app
  versions and keys may be added or removed; missing keys fall back to English.
- By submitting a pull request you agree to license the translation under the GPL-3.0, the license
  of Nimble Commander-Fork.
- See the app's [language-packs documentation](https://github.com/cfanmaoli/nimble-commander/blob/main/Tools/language-packs.md)
  for how the packs are exported, imported and applied.
