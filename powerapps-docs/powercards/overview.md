---
title: "Power Cards overview"
description: "Get a quick overview of Power Cards as a product and what issues this product can help you solve"
keywords: "Power Cards, Power Apps, Cards, overview"
ms.date: 03/18/2022
ms.topic: article
author: v-eberhardts
ms.author: v-eberhardts
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Power Cards Overview

## What are Power Apps Cards?

Power Apps Cards are a low-code solution enabling citizens and pros to design, send and use Cards – micro-apps using enterprise data that can be sent as content in Teams, Outlook, Search results, and chat.

:::image type="content" source="media/overview/power-card-in-teams.png" alt-text="Screenshot of a card in Teams." border="false":::

There are three key parts of this solution:

- **Card Gallery**: a consumer-facing gallery for finding, customizing, and sending interactive cards from within Teams, Outlook, and other environments

- **Power Apps Card Designer**: a low-code card designer for creating new cards using data from both Microsoft data sources (SharePoint & Dataverse) and third-party data sources (Salesforce, etc.)

- **Lightweight runtime**: manages sending and receiving cards, replacing the need for a secondary bot

## Why Power Apps Cards?

Power Apps Cards are intended to be a steppingstone between Adaptive Cards and future products.

Adaptive Cards were the first step in creating small "app snippets" within Microsoft products (Teams, Outlook, etc.), consisting of bits of data such as a status update or a button allowing a follow-on action. This product was intended to help meet users where they're at in a post-COVID workplace, allowing for more efficient communication in the same real-time collaborative environments they spend their days in.

Adaptive Cards are currently available in the following Microsoft products, with an installed user base of a billion endpoints via:

- Teams
- Outlook
- SharePoint on Windows, Mac, iOS, and Android

In the future, Loop Components intends to expand upon the capabilities of Adaptive Cards, allowing Cards to handle increasingly complex scenarios. This feature is slated for release in 2022.

## The Problem

Adaptive Cards provides a simple, efficient UI to present buttons, text, and images in a card, but building logic into those elements requires a developer. Not only does this limit the type of developer who can create cards, but it also limits the sophistication of cards in the market, as using advanced features of adaptive cards is overly complex and requires expertise in multiple frameworks. Adaptive Cards also has minimal support for card distribution and management, needing a separate bot to send cards, and limitations on what kind of data can be used in cards.

## The Solution

Power Apps Cards expands upon the idea of Adaptive Cards, making cards accessible to a wider range of people, removing the requirement for a developer. The Card Gallery allows non-technical users to become comfortable with finding and using cards, while Power Card Studio allows for Excel-level users to learn and grow with Microsoft products and languages. And the lightweight runtime allows users to access Power Apps Cards quickly and efficiently from wherever they may need, all while keeping enterprise data securely within an organization.

### Power Card Gallery

The Power Apps Cards Gallery provides users with a no-code, consumer-facing user interface via Microsoft products that allows them to browse, customize, and send cards. Via the Gallery, a user only needs a few clicks to customize and send a card of their choice, utilizing their enterprise's data quickly and efficiently. For example, a Dynamics 365 Sales "Order Estimate" Power Card enables a salesperson to:

1. embed a D365 Opportunity record into a card
1. share that card with their team members in a chat
1. quickly gather feedback
1. write information back to the Dataverse

### Power Card Studio

For the Excel-level user, Power Card Studio allows them to create cards from scratch using a combination of:

- drag-and-drop design
- simple data import via connectors
- a small amount of PowerFX to format data and invoke cloud-based functions and workflows

### Lightweight Runtime

The cloud-based card runtime behind Power Apps Cards is the core of what allows users to create their interactive cards, using an easy declarative format to embed data and workflows. This engine abstracts over the interactive transaction capabilities of card canvases (where Adaptive Cards render) in Teams, Outlook, and Web chat. PowerFX is integrated into the Power Card engine, allowing for initial maker scenarios to be driven by simple PowerFX expressions and drag-and-drop card building. Power Apps Cards also provides the security delegations to handle access tokens for each participant in the card transaction, enabling data-rich and powerful scenarios that respect security boundaries within an organization.
