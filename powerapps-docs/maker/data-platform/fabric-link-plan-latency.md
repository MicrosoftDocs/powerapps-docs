---
title: Plan your latency for Link to Fabric
description: Understand the data freshness you can expect when Link to Fabric replicates Microsoft Dataverse data to Microsoft Fabric, grouped by real-world load patterns.
author: anibakore-msft
ms.author: banirud
ms.reviewer: matp
ms.service: powerapps
ms.subservice: dataverse-maker
ms.topic: concept-article
ms.date: 08/17/2026
ms.custom: template-concept
---
# Plan your latency for link to Fabric

This article describes the data freshness you can expect when link to Fabric replicates Microsoft Dataverse data to Microsoft Fabric. It groups real workloads by industry and, more importantly, by load pattern (how much data changes and how it arrives), so you can find the profile closest to your environment and use its measured latency as a planning reference. All figures are point-in-time measurements from production telemetry. They're indicative and shift as the platform and workloads evolve.

> [!IMPORTANT]
> These figures are indicative, not a service-level agreement (SLA). The numbers come from observed telemetry in real customer environments and vary with volume, churn, table mix, and configuration. Use these examples to plan for scenarios similar to your own, not as guaranteed performance.

## How to read these numbers

Observed sync speed isn't a single fixed value. It varies with the workload. The numbers in this article are indicative, drawn from real customer environments and validation runs. They aren't a service-level guarantee.

The main factors that affect the speed you observe:

| Factor | Effect on observed speed |
|--------|--------------------------|
| Initial load size | Larger historical loads take longer to complete the first full sync. |
| Data churn | Higher change volume per interval increases the rows processed per delta cycle. |
| Table size and row width | Wide tables (many columns) and very large tables process more slowly per row. |
| Number of tables | More tables in a single link share throughput across the environment. |
| Long-running source transactions | Uncommitted or long-running transactions in the source hold back the visible watermark, producing occasional lag spikes unrelated to load. |
| Change Data Feed (CDF) | Enabling CDF on the Delta tables adds change-tracking work to every write and increases sync latency. The environments measured here don't have CDF enabled. |

## How to use this article

The scenarios in this article are grouped by industry and, more importantly, by *load pattern*: how much data changes and how it arrives. Throughout this article, *CRM apps* refers to the Dynamics 365 customer engagement applications (such as Sales, Customer Service, and Contact Center), and *ERP apps* refers to the Dynamics 365 finance and operations applications (such as Finance, Supply Chain Management, and Commerce). Freshness depends far more on load pattern than on industry or app family, so find the pattern closest to your own environment and use its numbers as an indicative reference.

We report *P95 freshness latency* (95 percent of changes land within this time) as the primary measure. Each scenario also describes how freshness behaves during bursts, so you can judge whether the pattern fits your tolerance. To keep the figure meaningful, we measure a specific, named high-volume table in each environment rather than averaging across all tables. Latency is the time between a source row's modified timestamp and its availability in the lake, so it's only accurate when that timestamp reflects the actual change. In some cases it doesn't. For example, when a child row is updated, the change can update an association on the parent row (so the parent is resynced), but the parent's modified timestamp isn't always bumped. Measuring against that stale timestamp produces extremely high, false latencies. We therefore choose tables that update their modified timestamp reliably and have load-appropriate latency expectations, and we cross-check that the modified timestamp is the latest one before trusting a number. All figures are point-in-time measurements from production telemetry (a typical recent window for steady workloads, and a representative invoice run for the burst scenario). They're indicative, not guarantees.

For typical CRM app and mainstream ERP app workloads, the majority of changes land within a few minutes, and most within about 10 minutes. P95 and the spike notes describe the slower tail, not the bulk of the workload. Only at very high volume (hundreds of millions of changes per day) does the typical figure itself move into tens of minutes.

| Industry and scenario | Load pattern (typical change volume) | Measured table (top-volume) | Freshness on top high-volume tables (P50 / P95) |
|---------------------|--------------------------------------|-----------------------------|--------------------------------------------------|
| [Financial services (CRM apps)](#financial-services-crm-apps) | Continuous, moderate: ~0.5 to 0.8M changes/day | `msdynci_customerprofile` | ~2 min / ~19 min |
| [Retail and consumer goods (ERP apps)](#retail-and-consumer-goods-erp-apps) | Steady operational posting: ~1 to 3M changes/day | `inventtrans` | ~1.5 min / ~13 min |
| [Distribution and commerce, very high volume (ERP apps)](#distribution-and-commerce-very-high-volume-erp-apps) | Extreme continuous: ~80 to 400M+ changes/day | `inventsum` | ~7 min / ~47 min |
| [Utility billing, invoice burst (ERP apps)](#utility-billing-erp-apps) | Invoice-processing burst: ~250M changes in a few hours | `custinvoicetrans` | ~10 min / ~92 min |

Read the matching section for the load pattern, the spike profile, and what drives it.

The P50 and P95 figures are measured on the *top five high-volume tables* in each environment (the named table above is representative of that set), not the low-volume tables. The high-volume tables carry the most load and the longest latency, so these numbers represent the worst case rather than the best case. Low-volume tables typically sync much faster. We exclude them deliberately so you can plan against the worst case, not the best.

## Why freshness varies and spikes occur

Freshness isn't constant. The median change is fast. The P95 tail and occasional spikes come from a few identifiable causes:

- **Environment-level operations.** Solution installs and platform or environment upgrade operations temporarily consume capacity, slowing sync while they run.
- **Database-level locking.** When an app holds heavy or long-running transaction locks on specific tables, the sync engine can't read those changes until the locks release, so those rows land later.
- **Load bursts.** Large batch operations (for example, invoice runs or mass postings) briefly produce more change than the sync path clears in real time. The backlog drains and freshness returns to normal.

These effects are transient and clear on their own. They move the tail (P95, P99, and maximum), not the median.

**Change Data Feed (CDF).** The environments measured here don't have Change Data Feed enabled on their Delta tables. Enabling CDF adds change-tracking work to every write, which increases sync latency. If you enable CDF, expect freshness somewhat higher than the numbers shown here.

## Financial services (CRM apps)

Continuous CRM app streaming: half a million to a million changes a day, no batch bursts. The key thing to understand is that freshness here is table-specific, not uniform. The busiest tables (event membership, segments) land in two to four minutes, while a few (customer profiles, accounts) trail to 20 to 40 minutes. We report `msdynci_customerprofile` (P95 ~19 min) as a representative high-volume table. A cross-table average will hide that spread. Plan around a P95 in the tens of minutes, and treat the far-tail rows as exceptions rather than the norm.

## Retail and consumer goods (ERP apps)

Steady ERP app operational posting, one to three million changes a day. The distribution is bimodal: reference and ledger tables sync almost instantly (P95 under a minute), while heavy transactional tables carry the tail. `inventtrans` (P95 about 13 minutes) is the reference. Posting-heavy days push it to roughly 20 to 25 minutes, then it settles. A solid baseline for a mainstream ERP app reporting workload.

## Distribution and commerce, very high volume (ERP apps)

ERP apps at the extreme end: tens to hundreds of millions of changes a day, sustained. What's distinctive here is uniformity. The top tables all sit at a similar P95 (`inventsum` about 47 minutes, others 47 to 67 minutes), so latency is set by overall throughput, not by any single slow table. On the heaviest days (250M+ changes), the sync falls behind and P95 stretches to several hours before catching up. Watch this profile if near-real-time freshness is a hard requirement at very high volume.

## Utility billing (ERP apps)

A billing environment defined by periodic invoice bursts. One run posts a batch of invoices that fans out across roughly 30 tables (invoice header and lines, subledger and settlement, ledger and tax, and billing-calculation and batch tables), producing on the order of 250 million changes in a few hours. The load is uneven across those tables: line-detail tables stay under a minute, while the heavy transaction and tax tables carry the lag. `custinvoicetrans` runs P50  about 10 / P95 about 90 / P99 about 120 minutes, capped near two hours, then drains back to normal once the run completes. Plan for tens of minutes to a couple of hours of freshness during runs. Between runs, the environment is quiet.

## Measure latency in your own environment

Use this guidance if you want to measure sync freshness yourself. Freshness latency is normally calculated as sink write time minus the source `ModifiedOn` value. Keep the following in mind so your numbers reflect real sync performance.

- *Some tables don't update `ModifiedOn` on change.* A number of system tables (for example, `mailbox`, `systemuser`, and `asyncoperation`) don't refresh the `ModifiedOn` column even when the row is updated. Because `ModifiedOn` stays in the past, sink time minus `ModifiedOn` produces very large, misleading latency values for these tables. Exclude or special-case them when measuring latency.
- *Related-record (parent-child) updates might not bump `ModifiedOn`.* When a child row changes, it can update an association on its parent row, so the parent is resynced even though the parent's own `ModifiedOn` wasn't updated. Sink time minus that stale `ModifiedOn` then shows an extremely high, false latency for the parent table. This is the main reason we report specific tables with load-appropriate latency expectations rather than a cross-table average. Always cross-check that `ModifiedOn` reflects the latest change before trusting a latency number.
- *Exclude initial-load backfill.* During and shortly after the first full sync, historical rows with old `ModifiedOn` values are written for the first time, which inflates the tail (P95/P99). Measure a steady-state window after the initial load completes, and only count rows modified within that window.
- *Test in a UAT or test environment first, and simulate your production load pattern.* Before you rely on any latency figure, measure it in a preproduction (UAT or test) environment that reproduces your real production load pattern (change volume, table mix, and burst timing). Run the simulation long enough to reach steady state and capture the P95 tail, so the numbers reflect what production actually does.
- *Enable in production only after validating in preproduction.* Turn on Link to Fabric in production only after the simulated UAT or test runs confirm that the measured latency meets your freshness requirements. This sequence avoids surprises when real production load arrives.

## Keep this guidance current

We update this article as we invest further in improving sync latency and as we simulate progressively larger loads, so that the guidance here stays as close to real-world, real-time behavior as possible. Treat the figures as a point-in-time reference that moves as the platform and workloads evolve.

## About latency planning

- These figures are indicative and based on observed telemetry from production and validation environments. They aren't a contractual service-level agreement.
- Actual speed depends on initial load, data churn, table sizes, number of columns, number of tables, and source transaction patterns, as described in this article.
- Reliability telemetry is sampled. Individual environment results vary.
- Scenarios are anonymized by industry and load pattern, not by customer.

## Related information

- [Link to Microsoft Fabric](fabric-link-to-data-platform.md)
- [Link Dataverse to Microsoft Fabric overview](azure-synapse-link-view-in-fabric.md)
- [Work with Fabric data and Power BI](fabric-work-data-and-power-bi.md)
