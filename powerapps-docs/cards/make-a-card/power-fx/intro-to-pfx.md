---
title: "Adding business logic to your cards"
description: "Learn about Power FX and how it's used in cards to add business logic"
keywords: "Card Designer, Power Apps, cards, Power Fx"
ms.date: 09/20/2022
ms.topic: article
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Add business logic

Cards can calculate values, perform other tasks, and respond to user input using formulas expressed with Power Fx.

For example, a formula might determine what happens when a user selects a button or write text into a text input control. Formulas can also be used to update variables and data sources. 

## Known Limitations

- All device sensor formulas do not work (**Acceleration**, **App**, **Compass**, **Connection**, and **Location**)
- **SaveData**, **LoadData**, and **ClearData** do not work
- Form-related formulas do not work (**EditForm**, **NewForm**, **SubmitForm**, **ResetForm**, and **ViewForm**)
- **Collect**, **Patch**, and **Remove** only works for variables and Dataverse tables
- **Update** and **UpdateIf** do not work
- **Set** requires the type of the variable to match what you are trying to set it to and requires the variable to be already created using the variable creation
