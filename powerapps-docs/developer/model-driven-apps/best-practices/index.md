---
title: "Developers: Best practices and guidance for model-driven apps"
description: Best practices and guidance for developers of model-driven apps in Power Apps.
suite: powerapps
author: JimDaly
ms.author: jdaly
ms.reviewer: jdaly
ms.topic: best-practice
ms.date: 04/14/2021
ms.subservice: mda-developer
search.audienceType: 
  - developer
---

# Best practices and guidance for model-driven apps

Model-driven apps are a component-focused approach to app development which developers can extend to achieve a much more
tailored experience. A developer customizing model-driven apps should be aware of the established guidance and best practices.

[!INCLUDE[cc-terminology](../../data-platform/includes/cc-terminology.md)]

Within this section you learn about identified issues, their impact, and understand the guidance to resolve them. We'll explain the background about why things should be done in a certain way and avoid potential problems in the future. This understanding can benefit the usability, supportability, and performance of your environment. The guidance documentation supports the existing information within the Developer and Administration guides.

> [!NOTE]
> Right now, only client scripting best practices are documented in the TOC and rest of them will be added eventually.
> This document covers the overall structure of how the best practice page should look with the sections and guidelines.

## Targeted customization types

The documentation targets the following customization types:

- Model-driven app design
- Form design
- Client scripting
- Web resources

## Sections

Each guidance article includes most or all of the following sections:

- Title - description of the guidance
- Category - one or more areas impacted by not following the guidance
- Impact potential - the level of risk (high, medium, or low) of affecting the environment by not following the guidance
- Symptoms - possible indications that the guidance hasn't been followed
- Guidance - recommendations that might also include examples
- Problematic patterns - description or examples of not following the guidance
- Additional information - supporting details for a more extensive view
- See also - references to learn more about something mentioned in the article

## Categories

Each guidance article is classified with one or more of the following categories:

- Usage – improper usage of a particular API, pattern, or configuration
- Design – design flaws in a customization
- Performance – customization or pattern that might produce a negative effect on performance in areas such as memory management, CPU utilization, network traffic, or user experience
- Security – potential vulnerabilities in a customization that could be exploited in a runtime environment
- Upgrade Readiness - customization or pattern that might increase risk of having an unsuccessful version upgrade
- Online Migration - customization or pattern that might increase risk of having an unsuccessful online migration
- Maintainability – customization that unnecessarily increases the amount of developer effort required to make changes, the frequency of required changes, or the chance of introducing regressions
- Supportability – customization or pattern that falls outside the boundaries of published supportability statements, including usage of removed APIs or implementation of forbidden techniques

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
