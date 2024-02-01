---
title: Draft well-written, input text with Copilot (preview)
description: Learn how to use Copilot to quickly generate well-written text that can be used in text boxes in apps made with Power Apps.
ms.date: 01/11/2024
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

# Draft well-written, input text with Copilot (preview)

[This article is prerelease documentation and is subject to change.]

You can use Copilot to quickly generate well-written text to use as input text in text boxes in canvas apps. Using Copilot saves time because you won’t have to worry about creating text that meets grammar rules. Copilot is especially helpful for users who are using apps that aren’t in their native language. 

When trying to quickly input text into multiline text boxes or rich text editors in a canvas app, you might worry about forming complete sentences and having grammatically correct text. With the assistance of Copilot, you can quickly jot down ideas in a text box without worrying about format and grammar. Copilot corrects errors in grammar and eloquently refines your ideas. You can also change the tone and length of the output to fit the scenario.


## Use this feature

1. Insert your cursor into a multiline text box or rich text editor in a canvas app.
1. Select the **Draft with Copilot** icon, and then select the **Draft with Copilot** option.
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

Makers can turn off this feature on a per-app basis within app settings using the [Power Apps](https://make.powerapps.com) maker portal.

1. Sign in to [Power Apps](https://make.powerapps.com).
1. On the left navigation pane, select **Apps**.
1. Select a canvas app and then select **Settings** on the command bar.
1. On the **App settings** pane, set the toggle for **Text assistance in web player (preview)** to  **Off**.
1. Select **Save**.

Power Platform admins can turn off this feature on a per-environment basis using Windows PowerShell **Set-EnvironmentCopilotSettings** cmdlet.

   ```powershell
   $Set-EnvironmentCopilotSettings -EnvironmentName 'EnvironmentName' -AppDraftingCopilotEnabled false
   ```
   

> [!IMPORTANT]
> - To use this feature, your admin must allow data movement across regions. Your environment must also be in a supported region. For information about supported regions and how to allow data movement across regions, see [Enable copilots and generative AI features](/power-platform/admin/geographical-availability-copilot).
> - This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability may be subject to usage limits or capacity throttling.
> - Copilot isn't supported and won't work for environments that have customer-managed key (CMK) or have lockbox.
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - This feature is in the process of rolling out, and may not be available in your region yet. 
> - For more information about the preview, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).

## Known issue

**Error**: There was a problem using this description. Try again.

**Resolution**: This error may be due to capacity limits. We recommend that you give the system some time before trying again. It may also be that you haven't given the system enough information to properly generate output. Add more details to try again.

