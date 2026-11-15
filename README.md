# nc-language — translations for Nimble Commander-Fork

This repository holds the language packs of
[Nimble Commander-Fork](https://github.com/cfanmaoli/nimble-commander). `languages/en.json` is the
English reference export; translate it into your language and open a pull request.

The app ships English and Simplified Chinese. Everything else comes from language packs like the
ones in this repository.

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

## How to translate

1. Copy `languages/en.json` to `languages/<code>.json` (for example `de.json`, `ja.json`,
   `pt-BR.json`).
2. In the copy:
   - set `"language"` to your language code and `"languageName"` to its display name;
   - translate the `"translation"` values; keep `source`, `bundle`, `table`, `key`, `comment`,
     `format` and `formatVersion` unchanged.
3. Test it in the app: **Preferences → Language → Import Language File…**, choose your file, then
   restart the app. Your language appears in the language popup; re-import after every edit.
   (中文界面：设置 → 语言 → 导入语言文件…)
4. Check the file and open a pull request:

   ```sh
   python3 tools/check-language.py languages/<code>.json
   ```

A partial translation is fine — empty or missing entries fall back to English.

## Notes

- Translations are matched by `bundle` + `table` + `key`. `en.json` is re-exported from new app
  versions and keys may be added or removed; missing keys fall back to English.
- By submitting a pull request you agree to license the translation under the GPL-3.0, the license
  of Nimble Commander-Fork.
- See the app's [language-packs documentation](https://github.com/cfanmaoli/nimble-commander/blob/main/Tools/language-packs.md)
  for how the packs are exported, imported and applied.
