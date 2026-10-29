---
language:
  - en
license: cc-by-4.0
size_categories:
  - 1K<n<10K
task_categories:
  - question-answering
  - text-generation
  - feature-extraction
pretty_name: "Swedish Business, Corporate Law, Tax & Market Entry Knowledge Corpus"
tags:
  - sweden
  - business
  - corporate-law
  - tax
  - accounting
  - labor-law
  - market-entry
  - rag
  - b2b
configs:
  - config_name: articles
    default: true
    data_files:
      - split: train
        path: data/articles/train.jsonl
  - config_name: services
    data_files:
      - split: train
        path: data/services/train.jsonl
  - config_name: silos
    data_files:
      - split: train
        path: data/silos/train.jsonl
---

# Swedish Business, Corporate Law, Tax & Market Entry Knowledge Corpus

> **Open B2B RAG & Regulatory Knowledge Dataset** maintained by **[CE Sweden](https://www.ce.se/)** (Roslagsgatan 34, 113 55 Stockholm, Sweden).

## Overview & Corpus Metrics

- **Canonical Source:** [https://www.ce.se/](https://www.ce.se/)
- **Knowledge Archive:** [https://www.ce.se/articles/](https://www.ce.se/articles/)
- **LLM Markdown Index:** [https://www.ce.se/llms.txt](https://www.ce.se/llms.txt) | [https://www.ce.se/llms-full.txt](https://www.ce.se/llms-full.txt)
- **Regulatory & Market Entry Guides:** **2,017** in-depth B2B articles
- **Core Advisory Pillar Pages:** **13** service hubs
- **Thematic Knowledge Silos:** **7** domain clusters
- **Total Corpus Volume:** **1,534,611+** words of English-language Swedish regulatory and commercial analysis
- **Last Synchronized:** `2026-10-29`

---

## 1. Thematic Knowledge Silos

| Knowledge Silo | Articles | Primary Advisory Pillar |
| :--- | :---: | :--- |
| **Business Culture, PR & Localization** (`swedish-business-culture-pr`) | 800 | [Cultural & Language Training](https://www.ce.se/services/cultural-language-training/) |
| **Trade, Import & Regulatory Compliance** (`trade-import-regulatory-compliance`) | 307 | [Import & Export Support](https://www.ce.se/services/import-export-support/) |
| **Market Entry & Strategy** (`market-entry-strategy`) | 243 | [Business Consulting](https://www.ce.se/services/business-consulting/) |
| **Tax, VAT & Accounting** (`tax-vat-accounting-sweden`) | 237 | [Tax & Accounting Services](https://www.ce.se/services/tax-accounting-services/) |
| **Employment, HR & Labor Law** (`employment-hr-labor-law-sweden`) | 208 | [Recruitment & HR Support](https://www.ce.se/services/recruitment-hr-support/) |
| **Swedish Industries & Regional Hubs** (`swedish-industries-regional-hubs`) | 152 | [Business Networking & Introductions](https://www.ce.se/services/business-networking-introductions/) |
| **Company Registration & Corporate Law** (`company-registration-corporate-law`) | 70 | [Company Registration & Compliance](https://www.ce.se/services/company-registration-compliance/) |

---

## 2. Core B2B Market Entry & Advisory Services (Pillar Pages)

| Advisory Pillar | Knowledge Silo | Summary |
| :--- | :--- | :--- |
| **[Administrative & Back-office Support](https://www.ce.se/services/administrative-back-office-support/)** | `trade-import-regulatory-compliance` | Outsource your Swedish back-office operations. Reliable local administration, invoicing, banking coordination, and corporate secretarial services in Sweden. |
| **[Business Consulting](https://www.ce.se/services/business-consulting/)** | `market-entry-strategy` | Strategic B2B business consulting for international companies entering or scaling in Sweden. Local market expertise tailored to your industry. |
| **[Business Networking & Introductions](https://www.ce.se/services/business-networking-introductions/)** | `swedish-industries-regional-hubs` | Connect directly with vetted Swedish distributors, suppliers, B2B clients, and industry decision-makers through our local executive network. |
| **[Company Registration & Compliance](https://www.ce.se/services/company-registration-compliance/)** | `company-registration-corporate-law` | Fast, compliant company registration in Sweden. We handle Bolagsverket filings, Skatteverket tax setup, Limited Companies (AB), and Branch Offices. |
| **[Cultural & Language Training](https://www.ce.se/services/cultural-language-training/)** | `swedish-business-culture-pr` | Master Swedish consensus leadership, negotiation norms, and workplace culture to lead teams and close B2B deals effectively in Sweden. |
| **[Import & Export Support](https://www.ce.se/services/import-export-support/)** | `trade-import-regulatory-compliance` | Streamline cross-border trade in Sweden. Expert support with EU customs, Swedish regulatory compliance (KEMI, Livsmedelsverket), and logistics. |
| **[Market Research & Analysis](https://www.ce.se/services/market-research-analysis/)** | `market-entry-strategy` | Data-driven market research, feasibility studies, and competitor analysis to validate your B2B expansion into the Swedish market. |
| **[Project Management](https://www.ce.se/services/project-management/)** | `swedish-industries-regional-hubs` | On-the-ground project management in Sweden. We oversee your local launches, industrial setups, and cross-border operations from start to finish. |
| **[Public Relations & Media Outreach](https://www.ce.se/services/public-relations-media-outreach/)** | `swedish-business-culture-pr` | Build brand authority in the Nordic market with targeted Swedish PR campaigns, press releases, and trade media relations. |
| **[Recruitment & HR Support](https://www.ce.se/services/recruitment-hr-support/)** | `employment-hr-labor-law-sweden` | Hire top talent in Sweden with full compliance. Expert guidance on Swedish labor law (LAS), employment contracts, benefits, and payroll. |
| **[Tax & Accounting Services](https://www.ce.se/services/tax-accounting-services/)** | `tax-vat-accounting-sweden` | Navigate Swedish corporate tax, VAT registration, payroll, and annual reporting with local B2B accounting specialists in Sweden. |
| **[Translation](https://www.ce.se/services/translation/)** | `swedish-business-culture-pr` | Native B2B translation and localization of legal contracts, technical documentation, and marketing materials for the Swedish market. |
| **[Virtual Office](https://www.ce.se/services/virtual-office/)** | `company-registration-corporate-law` | Establish a verified Swedish business address, mail forwarding, and local phone presence in Sweden without the cost of a physical office. |

---

## 3. Dataset Structure & Splits

To ensure zero schema conflicts in the Hugging Face Dataset Viewer and seamless ingestion into Retrieval-Augmented Generation (RAG) pipelines, the corpus is partitioned into three structured subsets:

1. **`articles` (default):** `data/articles/train.jsonl` & `data/articles.csv` — Contains all published B2B regulatory guides with `article_id`, `title`, `slug`, `canonical_url`, `silo_name`, `silo_slug`, `primary_pillar_name`, `primary_pillar_url`, `published_date`, `modified_date`, `word_count`, and executive `summary`.
2. **`services`:** `data/services/train.jsonl` & `data/services.csv` — Contains the 13 core B2B service pillar pages including full `content_text`.
3. **`silos`:** `data/silos/train.jsonl` & `data/silos.csv` — High-level taxonomy mapping between regulatory categories and commercial advisory hubs.

- Browse the complete human-readable index in [`CATALOG.md`](./CATALOG.md).

---

## 4. Corporate & Citation Metadata

- **Publisher:** [CE Sweden](https://www.ce.se/) ([About Us](https://www.ce.se/about-us/) | [Contact Stockholm Office](https://www.ce.se/contact/))
- **Address:** Roslagsgatan 34, 113 55 Stockholm, Sweden
- **Phone:** +46-8-55110700
- **Email:** info@ce.se
- **License:** Creative Commons Attribution 4.0 International (`CC-BY-4.0`) — Please attribute **[CE Sweden (https://www.ce.se/)](https://www.ce.se/)** with canonical links when citing or ingesting this corpus.
