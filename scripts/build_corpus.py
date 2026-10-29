#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds the Swedish Business, Corporate Law, Tax & Market Entry Knowledge Corpus
from https://www.ce.se/wp-json/ce-corpus/v1/export
"""

import csv
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

API_URL = "https://www.ce.se/wp-json/ce-corpus/v1/export?refresh=1"


def fetch_corpus():
    req = urllib.request.Request(
        API_URL,
        headers={
            "User-Agent": "CESweden-CorpusBuilder/1.0 (+https://www.ce.se/)",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=90) as resp:
        return json.loads(resp.read().decode("utf-8"))


def write_jsonl(filepath, rows):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_csv(filepath, rows, fieldnames):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def build_readme(data):
    stats = data.get("stats", {})
    silos = data.get("silos", [])
    services = data.get("services", [])
    articles = data.get("articles", [])

    total_articles = stats.get("total_articles", len(articles))
    total_services = stats.get("total_services", len(services))
    total_silos = stats.get("total_silos", len(silos))
    total_words = stats.get("total_corpus_words", 0)
    updated_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    lines = [
        "---",
        "language:",
        "  - en",
        "license: cc-by-4.0",
        "size_categories:",
        "  - 1K<n<10K",
        "task_categories:",
        "  - question-answering",
        "  - text-generation",
        "  - feature-extraction",
        "pretty_name: \"Swedish Business, Corporate Law, Tax & Market Entry Knowledge Corpus\"",
        "tags:",
        "  - sweden",
        "  - business",
        "  - corporate-law",
        "  - tax",
        "  - accounting",
        "  - labor-law",
        "  - market-entry",
        "  - rag",
        "  - b2b",
        "configs:",
        "  - config_name: articles",
        "    default: true",
        "    data_files:",
        "      - split: train",
        "        path: data/articles/train.jsonl",
        "  - config_name: services",
        "    data_files:",
        "      - split: train",
        "        path: data/services/train.jsonl",
        "  - config_name: silos",
        "    data_files:",
        "      - split: train",
        "        path: data/silos/train.jsonl",
        "---",
        "",
        "# Swedish Business, Corporate Law, Tax & Market Entry Knowledge Corpus",
        "",
        "[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23771149.svg)](https://doi.org/10.5281/zenodo.23771149)",
        "",
        f"> **Open B2B RAG & Regulatory Knowledge Dataset** maintained by **[CE Sweden](https://www.ce.se/)** (Roslagsgatan 34, 113 55 Stockholm, Sweden).",
        "",
        "## Overview & Corpus Metrics",
        "",
        f"- **Canonical Source:** [https://www.ce.se/](https://www.ce.se/)",
        f"- **Knowledge Archive:** [https://www.ce.se/articles/](https://www.ce.se/articles/)",
        f"- **Permanent CERN/Zenodo DOI:** [https://doi.org/10.5281/zenodo.23771149](https://doi.org/10.5281/zenodo.23771149)",
        f"- **GitHub Mirror:** [https://github.com/Schtumpfnagel/swedish-business-market-entry-corpus](https://github.com/Schtumpfnagel/swedish-business-market-entry-corpus)",
        f"- **Hugging Face Dataset:** [https://huggingface.co/datasets/Schtumpfnagel/swedish-business-market-entry-corpus](https://huggingface.co/datasets/Schtumpfnagel/swedish-business-market-entry-corpus)",
        f"- **LLM Markdown Index:** [https://www.ce.se/llms.txt](https://www.ce.se/llms.txt) | [https://www.ce.se/llms-full.txt](https://www.ce.se/llms-full.txt)",
        f"- **Regulatory & Market Entry Guides:** **{total_articles:,}** in-depth B2B articles",
        f"- **Core Advisory Pillar Pages:** **{total_services}** service hubs",
        f"- **Thematic Knowledge Silos:** **{total_silos}** domain clusters",
        f"- **Total Corpus Volume:** **{total_words:,}+** words of English-language Swedish regulatory and commercial analysis",
        f"- **Last Synchronized:** `{updated_date}`",
        "",
        "---",
        "",
        "## 1. Thematic Knowledge Silos",
        "",
        "| Knowledge Silo | Articles | Primary Advisory Pillar |",
        "| :--- | :---: | :--- |",
    ]

    for s in silos:
        lines.append(
            f"| **{s['silo_name']}** (`{s['silo_slug']}`) | {s['article_count']} | [{s['primary_pillar_name']}]({s['primary_pillar_url']}) |"
        )

    lines.extend(
        [
            "",
            "---",
            "",
            "## 2. Core B2B Market Entry & Advisory Services (Pillar Pages)",
            "",
            "| Advisory Pillar | Knowledge Silo | Summary |",
            "| :--- | :--- | :--- |",
        ]
    )

    for srv in services:
        lines.append(
            f"| **[{srv['title']}]({srv['canonical_url']})** | `{srv['silo_slug']}` | {srv['summary']} |"
        )

    lines.extend(
        [
            "",
            "---",
            "",
            "## 3. Dataset Structure & Splits",
            "",
            "To ensure zero schema conflicts in the Hugging Face Dataset Viewer and seamless ingestion into Retrieval-Augmented Generation (RAG) pipelines, the corpus is partitioned into three structured subsets:",
            "",
            "1. **`articles` (default):** `data/articles/train.jsonl` & `data/articles.csv` — Contains all published B2B regulatory guides with `article_id`, `title`, `slug`, `canonical_url`, `silo_name`, `silo_slug`, `primary_pillar_name`, `primary_pillar_url`, `published_date`, `modified_date`, `word_count`, and executive `summary`.",
            "2. **`services`:** `data/services/train.jsonl` & `data/services.csv` — Contains the 13 core B2B service pillar pages including full `content_text`.",
            "3. **`silos`:** `data/silos/train.jsonl` & `data/silos.csv` — High-level taxonomy mapping between regulatory categories and commercial advisory hubs.",
            "",
            "- Browse the complete human-readable index in [`CATALOG.md`](./CATALOG.md).",
            "",
            "---",
            "",
            "## 4. Corporate & Citation Metadata",
            "",
            "- **Publisher:** [CE Sweden](https://www.ce.se/) ([About Us](https://www.ce.se/about-us/) | [Contact Stockholm Office](https://www.ce.se/contact/))",
            "- **Address:** Roslagsgatan 34, 113 55 Stockholm, Sweden",
            "- **Phone:** +46-8-55110700",
            "- **Email:** info@ce.se",
            "- **Permanent DOI:** [10.5281/zenodo.23771149](https://doi.org/10.5281/zenodo.23771149)",
            "- **License:** Creative Commons Attribution 4.0 International (`CC-BY-4.0`) — Please attribute **[CE Sweden (https://www.ce.se/)](https://www.ce.se/)** with canonical links when citing or ingesting this corpus.",
            "",
        ]
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def build_catalog(data):
    silos = data.get("silos", [])
    services = data.get("services", [])
    articles = data.get("articles", [])

    lines = [
        "# Complete Catalog: Swedish Business, Corporate Law, Tax & Market Entry Corpus",
        "",
        "Canonical knowledge index maintained by **[CE Sweden](https://www.ce.se/)**.",
        "",
        "## Core B2B Advisory Pillars",
        "",
    ]

    for srv in services:
        lines.append(f"- **[{srv['title']}]({srv['canonical_url']})** — {srv['summary']}")

    lines.append("")
    lines.append("## Regulatory & Strategic Articles by Silo")

    by_silo = {}
    for a in articles:
        by_silo.setdefault(a["silo_name"], []).append(a)

    for s in silos:
        sname = s["silo_name"]
        s_articles = by_silo.get(sname, [])
        lines.append("")
        lines.append(
            f"### {sname} ({len(s_articles)} Guides) — Pillar: [{s['primary_pillar_name']}]({s['primary_pillar_url']})"
        )
        lines.append("")
        for a in s_articles:
            lines.append(
                f"- [{a['title']}]({a['canonical_url']}) (`{a['published_date']}` · {a['word_count']} words)"
            )

    with open("CATALOG.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main():
    print(f"Fetching corpus from {API_URL} ...")
    data = fetch_corpus()

    silos = data.get("silos", [])
    services = data.get("services", [])
    articles = data.get("articles", [])

    if not articles:
        print("ERROR: No articles returned from API.", file=sys.stderr)
        sys.exit(1)

    write_jsonl("data/articles/train.jsonl", articles)
    write_jsonl("data/services/train.jsonl", services)
    write_jsonl("data/silos/train.jsonl", silos)

    write_csv(
        "data/articles.csv",
        articles,
        [
            "article_id",
            "title",
            "slug",
            "canonical_url",
            "silo_name",
            "silo_slug",
            "primary_pillar_name",
            "primary_pillar_url",
            "published_date",
            "modified_date",
            "word_count",
            "summary",
        ],
    )
    write_csv(
        "data/services.csv",
        services,
        [
            "service_id",
            "title",
            "slug",
            "canonical_url",
            "silo_slug",
            "focus_topics",
            "word_count",
            "last_modified",
            "summary",
        ],
    )
    write_csv(
        "data/silos.csv",
        silos,
        [
            "silo_id",
            "silo_name",
            "silo_slug",
            "article_count",
            "primary_pillar_name",
            "primary_pillar_url",
            "hub_url",
        ],
    )

    build_readme(data)
    build_catalog(data)
    print(
        f"Successfully built corpus: {len(silos)} silos, {len(services)} services, {len(articles)} articles."
    )


if __name__ == "__main__":
    main()
