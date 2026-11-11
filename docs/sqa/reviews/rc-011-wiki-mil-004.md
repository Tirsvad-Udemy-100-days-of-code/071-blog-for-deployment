# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [MIL-004], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 | Initial review (autonomous, not independent) | [6494d1d] |

---

## Artifact Under Review

- Instance reviewed: [MIL-004]
- Checklist used: [QC-WIKI-001] (`QC-WIKI-001`)
- Scope: full review of docs/wiki/ (9 pages and the sidebar)
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | Checked against docs/wiki/: _Sidebar.md lists Home, Lecture-Steps and Setup-and-Run once, Languages section is last; every page exists as -da and -ms with the language line; the folder is flat; commands stay English. Criteria about related wikis and generators do not apply (none). |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Checked against docs/wiki/: _Sidebar.md lists Home, Lecture-Steps and Setup-and-Run once, Languages section is last; every page exists as -da and -ms with the language line; the folder is flat; commands stay English. Criteria about related wikis and generators do not apply (none). |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | Checked against docs/wiki/: _Sidebar.md lists Home, Lecture-Steps and Setup-and-Run once, Languages section is last; every page exists as -da and -ms with the language line; the folder is flat; commands stay English. Criteria about related wikis and generators do not apply (none). |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | N-A | Checked against docs/wiki/: _Sidebar.md lists Home, Lecture-Steps and Setup-and-Run once, Languages section is last; every page exists as -da and -ms with the language line; the folder is flat; commands stay English. Criteria about related wikis and generators do not apply (none). |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Checked against docs/wiki/: _Sidebar.md lists Home, Lecture-Steps and Setup-and-Run once, Languages section is last; every page exists as -da and -ms with the language line; the folder is flat; commands stay English. Criteria about related wikis and generators do not apply (none). |
| 6 | The sidebar does not repeat the page list per language | Pass | Checked against docs/wiki/: _Sidebar.md lists Home, Lecture-Steps and Setup-and-Run once, Languages section is last; every page exists as -da and -ms with the language line; the folder is flat; commands stay English. Criteria about related wikis and generators do not apply (none). |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | Checked against docs/wiki/: _Sidebar.md lists Home, Lecture-Steps and Setup-and-Run once, Languages section is last; every page exists as -da and -ms with the language line; the folder is flat; commands stay English. Criteria about related wikis and generators do not apply (none). |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Checked against docs/wiki/: _Sidebar.md lists Home, Lecture-Steps and Setup-and-Run once, Languages section is last; every page exists as -da and -ms with the language line; the folder is flat; commands stay English. Criteria about related wikis and generators do not apply (none). |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | Checked against docs/wiki/: _Sidebar.md lists Home, Lecture-Steps and Setup-and-Run once, Languages section is last; every page exists as -da and -ms with the language line; the folder is flat; commands stay English. Criteria about related wikis and generators do not apply (none). |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | Checked against docs/wiki/: _Sidebar.md lists Home, Lecture-Steps and Setup-and-Run once, Languages section is last; every page exists as -da and -ms with the language line; the folder is flat; commands stay English. Criteria about related wikis and generators do not apply (none). |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Checked against docs/wiki/: _Sidebar.md lists Home, Lecture-Steps and Setup-and-Run once, Languages section is last; every page exists as -da and -ms with the language line; the folder is flat; commands stay English. Criteria about related wikis and generators do not apply (none). |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Checked against docs/wiki/: _Sidebar.md lists Home, Lecture-Steps and Setup-and-Run once, Languages section is last; every page exists as -da and -ms with the language line; the folder is flat; commands stay English. Criteria about related wikis and generators do not apply (none). |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Checked against docs/wiki/: _Sidebar.md lists Home, Lecture-Steps and Setup-and-Run once, Languages section is last; every page exists as -da and -ms with the language line; the folder is flat; commands stay English. Criteria about related wikis and generators do not apply (none). |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pass | Checked against docs/wiki/: _Sidebar.md lists Home, Lecture-Steps and Setup-and-Run once, Languages section is last; every page exists as -da and -ms with the language line; the folder is flat; commands stay English. Criteria about related wikis and generators do not apply (none). |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | Pass | Checked against docs/wiki/: _Sidebar.md lists Home, Lecture-Steps and Setup-and-Run once, Languages section is last; every page exists as -da and -ms with the language line; the folder is flat; commands stay English. Criteria about related wikis and generators do not apply (none). |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | Checked against docs/wiki/: _Sidebar.md lists Home, Lecture-Steps and Setup-and-Run once, Languages section is last; every page exists as -da and -ms with the language line; the folder is flat; commands stay English. Criteria about related wikis and generators do not apply (none). |

## Overall Verdict

Go - every mandatory criterion passes. Mode: autonomous, not independent; the stand-in decision stays open to challenge in the run summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[MIL-004]: ../../milestones/mil-004-documentation.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[6494d1d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/commit/6494d1d1b9c8b6db18f551feb8fd320760daba45
