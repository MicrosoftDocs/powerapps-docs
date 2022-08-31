---
title: "Cards overview"
description: "Get a quick overview of cards as a Power Apps capability and what issues this capability can help you solve"
keywords: "Cards, Power Apps, overview"
ms.date: 09/20/2022
ms.topic: article
author: eberhardts
ms.author: v-eberhardts
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Cards Overview

Cards are a low-code capability of Power Apps enabling business users and developers to design, send, and use cards - micro-apps using enterprise data that can be sent as content in Teams.

Business users and subject matter experts can create cards with a guided, low-code graphical interface to optimize and automate business tasks and to create actionable scenarios with interactive, data-driven, lightweight UI and make these cards available for other people to use.

As a part of the Power Apps ecosystem, cards add business logic through Power Fx and integration with business data through connectors.

Using cards, you can quickly build, manage, and share rich, actionable UI cards without needing coding or IT expertise.

## Get started in minutes

Cards are available to makers as a part of Power Apps. You can easily sign up and create your card with a few clicks; there is no complex systems or services to deploy and maintain.

To create a card, you can go to make.powerapps.com and navigate to the Cards section:  

:::image type="content" source="media/overview/cards-get-started.png" alt-text="Screenshot of the card create page." border="false":::

There are two key parts to this solution:

- **Card Designer**: a low-code designer for creating new cards using drag-and-drop controls, Power Fx logic, and data from connectors

- **Lightweight runtime**: manages sending and receiving cards, replacing the need for a secondary bot

## Card Designer

Use the intuitive drag-and-drop Designer to easily create a card consisting of buttons, tables, text, images, checkboxes, input fields, containers, and many other types of elements without writing any code.

:::image type="content" source="media/overview/placeholder-cards-designer-get-started.png" alt-text="Screenshot of the card designer." border="false":::

### Add data and connect to services with connectors

Leverage connectors to work with enterprise data and invoke cloud-based functions safely and securely in your cards.

The lightweight runtime of cards securely handles tokens for each participant in the card transaction, enabling data-rich and powerful scenarios that respect security boundaries within an organization.

:::image type="content" source="media/overview/placeholder-cards-add-data.png" alt-text="Screenshot of the card designer." border="false":::

### Build business logic with actions and calculations

Use Power Fx to add inline calculations and dynamic actions to cards. Create powerful actions, including data operations, and assign them to interactive UI elements in the card.

Adaptive Cards provides a simple, efficient UI to present buttons, text, and images in a card, but building logic into those elements requires a developer. Not only does this limit the type of developer who can create cards, but it also limits the sophistication of cards in the market, as using advanced features of adaptive cards is overly complex and requires expertise in multiple frameworks. Adaptive Cards also has minimal support for card distribution and management, needing a separate bot to send cards, and limitations on what kind of data can be used in cards.

:::image type="content" source="media/overview/placeholder-cards-power-fx.png" alt-text="Screenshot of the card designer." border="false":::

## Lightweight Runtime

The card runtime is the core of what allows users to play their interactive cards, using an easy declarative format to embed data and workflows. This engine abstracts over the interactive transaction capabilities of card canvases (where Adaptive Cards render) in Teams, enabling users to send and receive cards without needing to deploy a secondary bot service or build a Teams app.

Share cards on Teams with other people by using the Send button in the Designer and copying the link into a Teams chat or channel.

:::image type="content" source="media/overview/placeholder-cards-play-page.png" alt-text="Screenshot of the card designer." border="false":::
