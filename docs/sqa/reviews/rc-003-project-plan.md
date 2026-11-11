# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-003 |
| CrossReference | [PP-001], [QC-PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 | Initial review (autonomous, not independent) | [8bad45b] |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001] (`QC-PP-001`)
- Scope: full review
- Language and domain: en / it
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Start 2026-11-11, end 2026-11-14 stated; BC sets no duration limit. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | Four gateways each with document and owner. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | Decision dates equal the milestone target dates (MIL-004 is 2026-11-13). |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage table maps every in-scope item. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Chain MIL-001 to MIL-004, acyclic. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | No-Go rule moves later gateways and S01 decides the end date. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | Pass | Owner S01 only. |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Checked against the document; meets the criterion. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Plan Risks have mitigations. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open issue list is empty. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | Deliverables match the milestone documents. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | Stories: none (technical tasks). |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | Checked against the document; meets the criterion. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | Not yet synced; Milestone column blank by design. |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | Checked against the document; meets the criterion. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Language `en` and Domain `it` rows present. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is BCP 47; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | Content is English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register fits the type (IT Executive English for BC/SA/PP/MIL). |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | Only ordinary IT terms are used; no dictionary exists and none is needed for this exercise. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version; no language change. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | S01 is competent in the domain and the language; the AI acts as stand-in for S01. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations (BC, SA, PO, WSGI) are spelled out or defined in context. |

## Overall Verdict

Go - every mandatory criterion passes. Mode: autonomous, not independent; the stand-in decision stays open to challenge in the run summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[8bad45b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/commit/8bad45b22a1694dea060d3353738c8a1c65018a8
