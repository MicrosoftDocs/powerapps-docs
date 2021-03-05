---
title: Build a multi-language app. | Microsoft Docs
description: Use Power Apps to build apps that that can support multiple languages.
author: tapanm-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 03/05/2021
ms.author: lunune
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

# Build a multi-language app
> [!IMPORTANT] This approach uses a feature of canvas apps that is still in public preview. For more information, see [Create a component for canvas apps](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/create-component)

In this article we'll describe an approach to creating multi-language apps that makers can use to provide their users with a localized experience. The approach uses canvas app components to make translations available across the entire app using a uniform formula syntax. 

## Create the Translation Component

1. In your app create a new **component** using the canvas editor. Give the component a name such as “**Translation Component**”

   ![Microsoft Power Apps Canvas App Editor: Create a new Power Apps component](media/multi-language-apps/image-20210305114316890.png)

1. Create the Input and Output parameters for your component, as follows: 

   - **Language**: An input property that will receive the current LCID (Locale ID) of the logged-in user. 
   
      - Select the Data type "Text"

      - Select the option “Raise OnReset when value changes”, since this will call the formula on the OnReset event of the component that we will write later.

      ![Microsoft Power Apps Canvas App Editor: Custom Language Property](media/multi-language-apps/image-20210304105245593.png)
   
   - **Labels**: An output property of type Table that will expose the translated labels based on the input LCID property.

      ![Microsoft Power Apps Canvas App Editor: Custom Labels Property](media/multi-language-apps/image-20210304105449314.png)

1. Next, create a table that will be the dictionary of all translations. To do this, declare a table variable on the **OnReset** event of the component as follows:

   ![Microsoft Power Apps Canvas App Editor: Create Table OnReset](media/multi-language-apps/image-20210304131142608.png)

   ```
   Set(
    varTranslations,
    Table(
        {
            Language: "en-us",
            Labels: {
                Title: "UI Tips for Building Canvas Apps",
                JobTitle: "Power Platform Specialist",
                Close: "Close",
                Open: "Open",
                Cancel: "Cancel"
            }
        },
        {
            Language: "pt-br",
            Labels: {
                Title: "Dicas de UI para construir Canvas Apps",
                JobTitle: "Especialista de Power Platform",
                Close: "Fechar",
                Open: "Abrir",
                Cancel: "Cancelar"
            }
        }
    )
   )
   ```

   The table should have an entry for each language that your app supports. Each entry will have a **Labels** property that will contain the translated content of all possible buttons, inputs and labels in your app.

1. Now change the formula of the output property **Labels** as follows:

   ![Microsoft Power Apps Canvas App Editor: Set Custom Output Labels Formula](media/multi-language-apps/image-20210304132515675.png)

   > [!NOTE] The formula will find the right translation entry based on the input **Language**. In the case where the language was not set, the formula will use the current user's language as the filter, hence the usage of the [Coalesce](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/functions/function-isblank-isempty) function.

   ```
   LookUp(
    varTranslations,
    Language = Lower(
        Coalesce(
            Self.Language,
            Language()
        )
    )).Labels
    ```

## Use the Translation Component in a Canvas App

To use the translation component in your app

1. Add the component to the app and set the Name to "**Translation**".

   ![Microsoft Power Apps Canvas App Editor: Add the Translation Component](media/multi-language-apps/image-20210305114727047.png)

1. Set the component **Visible** to **false**
   
   ![Microsoft Power Apps Canvas App Editor: Set Translation Component Visible to False](media/multi-language-apps/image-20210304135035793.png)
1. Pass the value of the **Language** to the input property of the **translation component**. In this case we have a toggle control that sets a variable called `varLanguage` to the language selected by the user.

   ![Microsoft Power Apps Canvas App Editor: Set Translation Component Language input parameter to the language of your app](media/multi-language-apps/image-20210304135729817.png)

1. On every control in your app that needs to be translated, instead of using static text as the label, use the formula `Translation.Labels.[ControlName]` where [ControlName] is the name of the control defined in the dictionary.

   ![image-20210304170138224](media/multi-language-apps/image-20210304170138224.png)

With this approach, whenever the user changes their language, the app will automatically change the text of all buttons, inputs, labels etc. as shown below

![Power Apps: Multi-Language Support](media/multi-language-apps/multi-langugage.gif)