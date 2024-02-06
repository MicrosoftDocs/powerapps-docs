---
title: Use Copilot chat in canvas apps (preview)
description: Learn how to use Copilot chat to get data insights for canvas apps using Dataverse data.
ms.date: 01/08/2023
ms.topic: article
ms.component: pa-user
ms.subservice: end-user
author: amchern
ms.author: amchern
ms.reviewer: sericks
ms.collection: 
    - bap-ai-copilot 
search.audienceType: 
  - enduser

---

# Use Copilot chat in canvas apps (preview)

[This article is prerelease documentation and is subject to change.]

End users can use Copilot chat to quickly get data insights for canvas apps that use Dataverse as their primary data source. Copilot chat allows users to analyze and summarize data easily through conversations with natural language.

No maker action is needed for users to take advantage of this feature.

Copilot chat is available when using Power Apps in a browser. It isn't available in the Power Apps mobile app.  

> [!IMPORTANT]
>
> - To use this feature, your admin must allow data movement across regions. Your environment must also be in a supported region. For information about supported regions and how to allow data movement across regions, see [Enable copilots and generative AI features](/power-platform/admin/geographical-availability-copilot).
> - This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability may be subject to usage limits or capacity throttling.
> - Copilot isn't supported and won't work for environments that have customer-managed key (CMK) or have lockbox.
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - This feature is in process of rolling out, and may not be available in your region yet.
> - For more information about the preview, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).

## How to use this feature

1. In your web browser, go to [Power Apps](https://make.powerapps.com).
1. Open a canvas app.
1. In the Power Apps header, select the **Copilot** button in the upper-right corner.
1. In the **Copilot** chat pane, type in a question.

     You must enter the text in English. This feature only supports the English language at this time.
     In some instances, the **Copilot** button is disabled because we're preparing your data. Once we finish preparing your data, you need to refresh the browser to access Copilot.

## Turn off this feature

Makers can turn off this feature on a per app-basis in app settings using the [Power Apps](https://make.powerapps.com) maker portal.

1. Go to the [Power Apps](https://make.powerapps.com) maker portal.
1. Select **Apps** in the navigation pane.
1. Select the check mark next to a canvas app.
1. Select **Settings** in the command bar. The **App settings** pane appears.
1. Select **Off** for the **Copilot chat in web player (preview)** feature.
1. Select **Save**.

[!INCLUDE[footer-include](../includes/footer-banner.md)]
