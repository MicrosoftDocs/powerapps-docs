---
title: Dataflow refresh performance in Dataverse
description: Dataflow refresh performance depends on capacity, plug-ins, and data volume. Learn how to plan Microsoft Dataverse refreshes and speed up your data uploads.
#customer intent: As a Power Apps maker, I want to know what affects dataflow refresh performance in Dataverse, so that I can plan realistic refresh schedules.
ms.date: 11/18/2026
ms.topic: concept-article
ms.service: power-platform
ms.subservice: dataverse
author: Mattp123
ms.author: rahupandey
ms.reviewer: matp
---
# Considerations for dataflow refresh performance

When you refresh a dataflow that loads data into Microsoft Dataverse, the upload time depends on the resources available in your environment and how the environment is configured. For a typical dataflow, a refresh of about 2,000 records usually completes in two to five minutes, and a refresh of 10,000 or more records usually takes 15 to 30 minutes. These times are indicative, not a service-level agreement (SLA), and apply to the default case: no plug-ins on the destination tables, no concurrent refreshes, and normal degree of parallelism.

Consider the following factors when planning your dataflow refreshes:

-  Available processing capacity. Upload performance depends on the degree of parallelism ([DOP](/power-apps/developer/data-platform/send-parallel-requests?tabs=sdk)) available in your environment. Other applications and workloads can consume resources that would otherwise be available for data uploads. Where possible, schedule refreshes when there's less activity in the environment.

-  Plug-ins on destination tables. Plug-ins that run on the Dataverse tables receiving data can increase processing time and, in some cases, cause upload failures. Review these plug-ins and avoid unnecessary execution during uploads. Before disabling a plug-in, consider whether it's required for validation or other business processes.

-  Data volume. Large datasets, such as those containing millions of records, can take considerable time to upload. Allow extra time when planning refreshes for these datasets.

-  Concurrent dataflow refreshes. Refreshing multiple dataflows at the same time increases the number of requests to the environment. These requests share the available processing resources, which can increase overall refresh duration. Consider staggering refresh schedules to reduce competing requests.

- Number of tables. Refresh duration depends on the number of tables being loaded, not just the number of records. Dataflows that load data into more tables can take longer to complete, even when the tables contain a smaller record set.

## Impact of key resolution on data upload performance

Providing complete, non-null alternate key values in the source improves upload performance. Upload takes longer in the following scenarios because the dataflow runs extra queries to retrieve record GUIDs:

- Some, but not all, values in a composite alternate key are null.

- A child table's alternate key includes a lookup column, and the source identifies the parent by its alternate key instead of its GUID.

- The source supplies an incomplete parent alternate key.

To avoid these extra queries, supply complete alternate-key values, including the parent GUID for any lookup column in the key.

## See also

[Create and use dataflows](create-and-use-dataflows.md)
