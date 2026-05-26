---
title: "Best Practices and Guidance for Coding in Microsoft Dataverse"
description: "Explore best practices and guidance for developers writing code for Microsoft Dataverse. Learn how to avoid common issues and improve performance, security, and supportability."
suite: powerapps
author: MsSQLGirl
ms.author: jukoesma
ms.topic: best-practice
ms.date: 03/09/2026
ms.subservice: dataverse-developer
ms.reviewer: jdaly
search.audienceType: 
  - developer
---

# Best practices and guidance for using Microsoft Dataverse

This article describes best practices and guidance for developers writing code for Microsoft Dataverse. Dataverse provides an extensible framework that you can use to build highly customized and tailored experiences. When you customize, extend, or integrate with Dataverse, follow the established guidance and best practices to improve performance, security, and supportability.

This section describes the issues Microsoft has identified, their impact, and guidance to resolve those issues. It explains the background about why things should be done in a certain way and how to avoid potential problems. This understanding can benefit the usability, supportability, and performance of your environment. The guidance documentation supports the existing information within the Developer and Administration guides.

## Targeted customization types

This documentation targets the following customization types:

- [Custom workflow activities and plug-ins](business-logic/index.md)
- [Working with Dataverse data](work-with-data/index.md)
- [Working with Dataverse table definitions](work-with-metadata/index.md)

## Sections

Each guidance article includes most or all of the following sections:

|Section|Description|
|---------|-------------|
|Title|Description of the guidance|
|Category|One or more areas impacted by not following the guidance|
|Impact potential|The level of risk (high, medium, or low) of affecting the environment by not following the guidance|
|Symptoms|Possible indications that the guidance wasn't followed|
|Guidance|Recommendations that might also include examples|
|Problematic patterns|Description or examples of not following the guidance|
|Additional information|Supporting details for a more extensive view|
|See also|References to learn more about something mentioned in the article|

## Categories

Each guidance article is classified with one or more of the following categories:

|Category|Description|
|---------|-----------|
|Usage|Improper usage of a particular API, pattern, or configuration|
|Design|Design flaws in a customization|
|Performance|Customization or pattern that might produce a negative effect on performance in areas such as memory management, CPU utilization, network traffic, or user experience|
|Security|Potential vulnerabilities in a customization that malicious users could exploit in a runtime environment|
|Upgrade Readiness|Customization or pattern that might increase the risk of an unsuccessful version upgrade|
|Online Migration|Customization or pattern that might increase the risk of an unsuccessful online migration|
|Maintainability|Customization that unnecessarily increases the amount of developer effort required to make changes, the frequency of required changes, or the chance of introducing regressions|
|Supportability|Customization or pattern that falls outside the boundaries of published supportability statements, including usage of removed APIs or implementation of forbidden techniques|

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
