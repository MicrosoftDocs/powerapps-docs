---
title: "Cards glossary"
description: "Learn the terminology of cards"
keywords: "Cards, Power Apps, glossary"
ms.date: 09/20/2022
ms.topic: article
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Glossary

| Term | Description |
| - | - |
| Card | Lightweight, data-driven, interactive UI that can be sent in Teams |
| Card definition | JSON representation of a **card** that is stored in Dataverse, including all the controls, their properties, the screens, formulas, data connections, and so on |
| Control | a UI element for a card, like a text label, a container, a date input or a button, see [controls](/make-a-card/ui-elements/controls.md) |
| Screen | a set of **controls** put together for a user to interact with. A **card** can have multiple screens. See [screens](/make-a-card/screens/understand-screens.md) |
| Formula | an expression used to define business logic within a card like calculating values, updating variables, or changing data sources from connections, see [formulas](/make-a-card/power-fx/intro-to-pfx.md) |
| Data connection | a way to bring in data and run actions through services in a secure way, see [connectors](/make-a-card/connectors/connector-intro.md) |
| Variable | a way to store data within the context of card, see [variables](/make-a-card/variables/variables.md) |
| Card instance | When a **card definition** is played, we turn that definition into a card instance by populating the data from connections, taking any variable customizations. Card instances are what you send to other users and can be shared across users and across clients (like Teams or the Play Page) |
| Card session | When a user views a card instance within a specific client (like Teams or the Play Page), they are in a card session. Each time the user reloads the card, that is another session. A session is for a single user, in a single client, for a single card instance. |
| Card Designer | Where you author cards, see [Designer overview](/make-a-card/designer-overview.md) |
| JSON view | a pane on the right-hand side of the **Card Designer** where you can see the **card defintion** in its JSON representation |
| Formula bar | a bar along the top of the **Card Designer** used to change properties or write **formulas** |
| Tree view | a pane on the left-hand side of the **Card Designer** where you can see the hierarchical structure of the card, including **screens** and **controls** |
| Insert pane | a pane on the left-hand side of the **Card Designer** where you can see the **controls** available to add into a card |
| Data pane | a pane on the left-hand side of the **Card Designer** where you can add and manage the **data connections** for a card |
| Variable pane | a pane on the left-hand side of the **Card Designer** where you can add and manage the **variables** for a card |
| Play Page | A place to play cards, used to either validate cards during the authoring process or to share cards in the web |
| Debug pane | a pane on the right-hand side of the **Play Page** that lets the user see information about the card like what the variables are set to, what connections are available, what the current card JSON looks like, etc |
