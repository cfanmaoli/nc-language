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

## Target languages

[languages.json](languages.json) lists the languages we would like to have, based on Mozilla
Firefox's *browser/locales/all-locales* list. English variants and the built-in Simplified Chinese
are omitted; a file for any of these can be added in one command (see below).

<details>
<summary>110 target languages</summary>

| Code | Language | Code | Language |
| --- | --- | --- | --- |
| `ach` | Acoli | `af` | Afrikaans |
| `an` | Aragonese | `ar` | Arabic |
| `ast` | Asturian | `az` | Azerbaijani |
| `be` | Belarusian | `bg` | Bulgarian |
| `bn` | Bangla | `bo` | Tibetan |
| `bqi` | Bakhtiari | `br` | Breton |
| `brx` | Bodo | `bs` | Bosnian |
| `ca` | Catalan | `ca-valencia` | Catalan (Valencian) |
| `cak` | cak | `ckb` | Central Kurdish |
| `cs` | Czech | `cy` | Welsh |
| `da` | Danish | `de` | German |
| `dsb` | Lower Sorbian | `el` | Greek |
| `eo` | Esperanto | `es-AR` | Spanish (Argentina) |
| `es-CL` | Spanish (Chile) | `es-ES` | European Spanish |
| `es-MX` | Mexican Spanish | `et` | Estonian |
| `eu` | Basque | `fa` | Persian |
| `ff` | Fula | `fi` | Finnish |
| `fr` | French | `fur` | Friulian |
| `fy-NL` | Western Frisian (Netherlands) | `ga-IE` | Irish (Ireland) |
| `gd` | Scottish Gaelic | `gl` | Galician |
| `gn` | Guarani | `gu-IN` | Gujarati (India) |
| `he` | Hebrew | `hi-IN` | Hindi (India) |
| `hr` | Croatian | `hsb` | Upper Sorbian |
| `hu` | Hungarian | `hy-AM` | Armenian (Armenia) |
| `hye` | Armenian | `ia` | Interlingua |
| `id` | Indonesian | `is` | Icelandic |
| `it` | Italian | `ja` | Japanese |
| `ka` | Georgian | `kab` | Kabyle |
| `kk` | Kazakh | `km` | Khmer |
| `kn` | Kannada | `ko` | Korean |
| `lij` | Ligurian | `lo` | Lao |
| `lt` | Lithuanian | `ltg` | Latgalian |
| `lv` | Latvian | `meh` | meh |
| `mk` | Macedonian | `ml` | Malayalam |
| `mr` | Marathi | `ms` | Malay |
| `my` | Burmese | `nb-NO` | Norwegian Bokmål (Norway) |
| `ne-NP` | Nepali (Nepal) | `nl` | Dutch |
| `nn-NO` | Norwegian Nynorsk (Norway) | `oc` | Occitan |
| `pa-IN` | Punjabi (India) | `pl` | Polish |
| `pt-BR` | Brazilian Portuguese | `pt-PT` | European Portuguese |
| `rm` | Romansh | `ro` | Romanian |
| `ru` | Russian | `sat` | Santali |
| `sc` | Sardinian | `scn` | Sicilian |
| `sco` | Scots | `si` | Sinhala |
| `sk` | Slovak | `skr` | skr |
| `sl` | Slovenian | `son` | son |
| `sq` | Albanian | `sr` | Serbian |
| `sv-SE` | Swedish (Sweden) | `szl` | Silesian |
| `ta` | Tamil | `te` | Telugu |
| `tg` | Tajik | `th` | Thai |
| `tl` | Filipino | `tr` | Turkish |
| `trs` | trs | `uk` | Ukrainian |
| `ur` | Urdu | `uz` | Uzbek |
| `vi` | Vietnamese | `wo` | Wolof |
| `xh` | Xhosa | `zh-TW` | Chinese (Taiwan) |

</details>

To start a translation, generate the skeleton from the English reference - every entry is present,
with an empty translation, so the app falls back to English for the parts that are not translated
yet:

```sh
python3 tools/new-language.py de
```

This writes `languages/de.json`. Fill in the `translation` values, then check the file and open a
pull request - exactly as described below.

## Machine-translated drafts

`languages/` contains machine-translated drafts for 92 of the target languages, bootstrapped from
the English reference with Google Translate. They are a starting point, not reviewed translations:
every entry that could not be translated safely (for example one whose format placeholders would
have been damaged) was left empty and falls back to English. Native speakers are very welcome to
correct these files.

The remaining target languages are not supported by the machine translation engine and still need a
manual translation - run `python3 tools/new-language.py <code>` to get the skeleton.

## Contributing a translation

1. Create `languages/<code>.json` - either copy [`languages/en.json`](languages/en.json) or run
   `python3 tools/new-language.py <code>` (for example `de.json`, `ja.json`, `pt-BR.json`).
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
| `languages.json` | The target languages, based on Firefox's locale list |
| `tools/new-language.py` | Creates a translation skeleton for one language |
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
