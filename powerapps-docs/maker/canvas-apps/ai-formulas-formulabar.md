---
title: Using Formulas with Copilot
description: How to interact with formulas in the universal formula bar using AI.
author: warrenbryant-msft
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 04/09/2024
ms.subservice: canvas-maker
ms.author: warrenbryant-msft
search.audienceType: 
  - maker
ms.collection: 
    - bap-ai-copilot
    - get started
contributors:
  - warrenbryant-msft
---

# Using Formulas with Copilot in the Formula Bar

Leverage AI to improve the experience of creating and editing formulas in the Formula Bar.  By allowing Copilot to help explain Power Fx formulas in natural language, or create Power Fx formulas from natural language, makers can build new or existing apps faster.

> [!IMPORTANT]
> AI generated content may be inaccurate and should always be checked for accuracy.

### Prerequisities
- Power Fx Formula Bar experience enabled in Studio Settings
- Browser and Power Apps portal configured for English language
- Copilot enabled on the environment and tenant

## Explain This Formula
Select a control and property that you want to understand more about what the formula is doing.  Select the new Copilot button in the Formula Bar, and choose "Explain This Formula".  An explanation window will appear to let you know that the Copilot is working on the explanation, and then display the explanation once it is available.  Explanations can be copied and insertted as code comments or shared with other people that are collaborating on an application.

### Known Limitations
- 1,000 character formula limit for explanations
- AI is only aware of default properties
- Not available for User Defined Functions
- Not available in Canada

## Formula from Comments (Preview)

Begin typing a code comment using // or /* in the Formula Bar, pause, and Copilot will generate a recommended formula to use for that situation.  To select the recommendation, press "Tab", or begin typing through the recommendation.  The recommendation will remain until you click elsewhere or type a character that does not align with the recommendation.  Comments used to generate Power Fx formulas can remain in the Formula Bar to serve as ongoing documentation just like traditional code comments.

### Known Limitations
- AI is only aware of default properties in the app
- Only works with general Power Fx functions, not Power Apps specific functions like (e.g. Navigate())
- Retrieving Copilot formula recommendations may prevent other actions from occuring in the Canvas Studio until after the recommendation is generated
- Does not include existing formulas for that property in the recommendation
- Not available for User Defined Functions
- Not available in Canada

### Disabling Formula from Comments
This setting can be disabled from the Upcoming Features screen in Canvas Studio settings by toggling the flag for "Copilot comment-generated formulas".  This ability to disable will be removed when the feature becomes Generally Available
