---
title: Copilot chat in web player (preview)
description: Learn how users can use Copilot to get data insights in the web player for canvas apps using Dataverse.
ms.date: 01/02/2023
ms.custom: 
  - responsible-ai-faqs
ms.topic: article
ms.component: pa-user
ms.subservice: end-user
author: amchern
ms.author: amchern
ms.reviewer: 
search.audienceType: 
  - enduser

---

# Copilot chat in web player (preview)

[This article is prerelease documentation and is subject to change.]

End users can use Copilot chat to quickly get data insights for apps using Dataverse as their primary data source. This will allow users to analyze and summarize data easily through conversation with natural language. This functionality is available to all users using apps that qualify, with no maker intervention needed.

> [!IMPORTANT]
> - To use this capability your environment must be in a qualifying region. 
> - You need to allow data movement across regions for generative AI features as a prerequisite to use copilots in Power Apps. This step is important if your organization and your environment are in different regions. More information: [Enable copilots and generative AI features](/power-platform/admin/geographical-availability-copilot#enable-data-movement-across-regions).
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - This feature is in process of rolling out, and may not be available in your region yet. 
> - For more information, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
> - This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability  may be subject to usage limits or capacity throttling.
> - Copilot isn't supported and won't work for environments that have customer-managed key (CMK) or have lockbox.

## How to use this feature

1. In the Office header, you will see a Copilot button in the upper right corner.
2. Click on the Copilot button to open the chat sidepane. Type in a question.

     > [!Note]
     > You must enter the text in English. This feature only supports the English language at this time.
     > In some instances, the Copilot button will be disabled because we are still be preparing your data. Once we have finished preparing your data, you will need to refresh the browser to access Copilot.

## Turn off this feature

Makers can turn off this feature on a per app basis within app settings in the Maker Portal.

1. Go the app list page in Maker Portal
2. Click on the command bar
3. Select 'Settings'
4. Turn off the toggle for 'Copilot chat in web player (preview)'

[!INCLUDE[footer-include](../includes/footer-banner.md)]
