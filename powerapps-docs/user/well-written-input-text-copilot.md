---
title: Draft well-written, input text with Copilot (preview)
description: Learn how to use Copilot to quickly generate well-written text that can be used in text boxes in apps made with Power Apps.
ms.date: 02/20/2024
ms.custom: 
  - responsible-ai-faqs
ms.topic: article
ms.component: pa-user
ms.subservice: end-user
author: jordanchodak
ms.author: jordanchodak
ms.reviewer: sericks
ms.collection: 
    - bap-ai-copilot 
search.audienceType: 
  - enduser
---

# Draft well-written input text with Copilot (preview)

[This article is prerelease documentation and is subject to change.]

You can use Copilot to quickly generate well-written text to use as input text in text boxes in canvas apps. Using Copilot saves time because you won’t have to worry about creating text that meets grammar rules. Copilot is especially helpful for users who are using apps that aren’t in their native language. 

When trying to quickly input text into multiline text boxes or rich text editors in a canvas app, you might worry about forming complete sentences and having grammatically correct text. With the assistance of Copilot, you can quickly jot down ideas in a text box without worrying about format and grammar. Copilot corrects errors in grammar and eloquently refines your ideas. You can also change the tone and length of the output to fit the scenario.

> [!IMPORTANT]
> - To use this feature, your environment must be in a US region.
> - To use this feature, the browser language must be US English.
> - This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability may be subject to usage limits or capacity throttling.
> - Copilot isn't supported and won't work for environments that have customer-managed key (CMK) or have lockbox.
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - This feature is in the process of rolling out, and may not be available in your region yet. 
> - For more information about the preview, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).

## Use this feature

1. Insert your cursor into a multiline text box or rich text editor in a canvas app.
1. The option to **Draft with Copilot** should appear. Select that option.
2. Insert text into the text box. For example, you can quickly jot down an idea.

     > [!Note]
     > You must enter the text in English. This feature only supports the English language at this time.
     
4. Select the **Send** icon.
5. Copilot generates well-written text for you. Review the text. The following options are available:
    - If you want Copilot to suggest text that is shorter or longer, select **Length** and then select the appropriate length.
    - If you want Copilot to suggest text that has a different tone, select **Tone** and then select the appropriate tone for the text.
    - If you want Copilot to suggest different text, select **Rewrite**.
    - If you are satisfied with the text that Copilot suggested, select **Add** to enter the text in the text box.
  
## Turn off text assistance in web player

You can turn off text assistance on for an app using app setting or PowerShell cmdlet, or an environment using PowerShell cmdlet. 

> [!NOTE]
> When using PowerShell cmdlets, you must use Power Apps admin PowerShell module version 2.0.179 or later. More information: [Get started using the Power Apps admin module](/powershell/powerapps/get-started-powerapps-admin).

### Turn off text assistance for an app

You can use either the app setting, or PowerShell cmdlet to turn this setting off for an app.

To turn off for an app using the app settings:

1. Sign in to [Power Apps](https://make.powerapps.com).
1. On the left navigation pane, select **Apps**.
1. Select a canvas app and then select **Settings** on the command bar.
1. On the **App settings** pane, set the toggle for **Text assistance in web player (preview)** to  **Off**.
1. Select **Save**.

To turn off for an app using PowerShell:

```powershell
Set-PowerAppSettings -AppName 'AppName' -DraftingCopilotEnabled $false
```

### Turn off text assistance for an environment

To turn off text assistance for a specific environment, use the following cmdlet.

```powershell
Set-AdminPowerAppEnvironmentCopilotSettings -EnvironmentName 'EnvironmentName' -AppDraftingCopilotEnabled $false
```
   
## Known issue

- You might see "There was a problem using this description. Try again." error. This error occurs due to the following possibilities:
  - You've reached capacity limits. In this case, try again after some time.
  - You've not provided enough information to properly generate output. In this case, add more details to try again.
- There is not a way to disable this feature on a per-tenant basis.  It can only be disabled by the methods listed in this document.
