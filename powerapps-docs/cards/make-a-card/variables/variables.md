---
title: "Using variables"
description: "Learn about storing data in variables"
keywords: "Card Designer, Power Apps, cards, variables"
ms.date: 09/20/2022
ms.topic: article
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Variables

Variables are used to store data within the context of a card. That data can be of different types like table, text, or a number. The value can also be temporary, where it resets for every card session, or permanent, where it is shared across all sessions for a specific card instance. Variables have unique names, which is how they are referenced in [formulas](../../make-a-card/power-fx/intro-to-pfx.md).

For example, if you wanted a card that counted how many times a user pressed a button during a session, you would create a temporary number variable. If you wanted to capture the name of the last user to press a button for a card instance, you would use a permanent text variable. If you wanted to save data between card instances, you would use a [data connection](../connectors/connector-intro.md).
