---
title: Data Loss Prevention (DLP)
description: This article helps you configure data loss prevention (DLP) policies for cards.
ms.date: 11/17/2022
ms.topic: overview
author: mduelae
ms.author: mkaur
ms.reviewer: 
ms.custom: 
ms.collection: 

---

# Manage cards with DLP policies

[!INCLUDE[cards-deprecation-banner](~/includes/cards-deprecation-notice.md)]

The **Cards for Power Apps** connector is used to automatically send cards through Power Automate. However, there are specific rules enforced by [DLP policies](/power-platform/admin/wp-data-loss-prevention) that dictate which connectors can be used with one another.

Administrators can use DLP policies to determine which connectors can be used in flows that send cards. For example, if both the MSN Weather connector and Cards for Power Apps connector are classified as **Business**, then makers can send daily status cards with the weather.
