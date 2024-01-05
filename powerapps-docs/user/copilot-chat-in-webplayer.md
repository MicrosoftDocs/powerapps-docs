---
title: Use Copilot chat in canvas apps (preview)
description: Learn how users can use Copilot chat to get data insights for canvas apps using Dataverse data.
ms.date: 01/05/2023
ms.topic: article
ms.component: pa-user
ms.subservice: end-user
author: amchern
ms.author: amchern
ms.reviewer: sericks
search.audienceType: 
  - enduser

---

# Use Copilot chat in canvas apps (preview)

[This article is prerelease documentation and is subject to change.]

End users can use Copilot chat to quickly get data insights for canvas apps that use Dataverse as their primary data source. Copilot chat allow users to analyze and summarize data easily through conversation with natural language. 

No maker invovlement is needed for users to take advantage of this feature.

Copilot chat is available when using Power Apps in a browser. It is not available in the Power Apps mobile app.  

> [!IMPORTANT]
> - To use this feature, your admin must allow data movement across regions. Your environment must also be in a supported region. For information about supported regions and how to allow data movement across regions, see [Enable copilots and generative AI features](/power-platform/admin/geographical-availability-copilot).
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - This feature is in process of rolling out, and may not be available in your region yet. 
> - For more information about the preview, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
> - This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability may be subject to usage limits or capacity throttling.
> - Copilot isn't supported and won't work for environments that have customer-managed key (CMK) or have lockbox.

## How to use this feature

1. In the Power Apps header, notice the **Copilot** button in the upper-right corner.
2. Select the Copilot button to open the **Copilot** chat pane.
3. Type in a question.

     > [!Note]
     > You must enter the text in English. This feature only supports the English language at this time.
     > In some instances, the **Copilot** button is disabled because we are preparing your data. Once we have finished preparing your data, you must refresh the browser to access Copilot.

## Turn off this feature

Makers can turn off this feature on a per app-basis within app settings using the [Power Apps](https://make.powerapps.com) maker portal.

1. Go to the [Power Apps](https://make.powerapps.com) maker portal.
2. Select **Apps** in the navigation pane.
3. Select the check mark next to a canvas app.
4. Select **Settings** in the command bar. The **App settings** pane appears.
5. Select **Off** for the **Copilot chat in web player (preview)** feature.
6. Select **Save**.

[!INCLUDE[footer-include](../includes/footer-banner.md)]
