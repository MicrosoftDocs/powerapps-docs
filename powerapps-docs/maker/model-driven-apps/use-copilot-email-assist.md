---
title: Use Copilot in rich text editor for email (preview)
description: Refine content for emails with Copilot in rich text editor.
author: udaykirang
ms.author: udag
ms.reviewer: shujoshi
ms.topic: how-to 
ms.date: 08/25/2023
ms.custom: bap-template 
ms.subservice: mda-maker
tags: 
search.audienceType: 
  - maker
---

# Use Copilot in rich text editor for email (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

The Copilot for email assist feature helps in refining content for emails specific to customer’s needs with clarity, conciseness, and compelling content.

> [!IMPORTANT]
> This is a preview feature
>
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]
>
> By using Copilot features powered by Azure OpenAI, you agree that data may be stored and/or processed outside of your geographic region, compliance boundary, or national cloud instance. More information: [Data, privacy, and security for Azure OpenAI Service](/legal/cognitive-services/openai/data-privacy#preventing-abuse-and-harmful-content-generation)

## Prerequisites

The Copilot for email assist feature must be enabled in app settings for the model-driven app. More information: [Controlling which features are enabled](../canvas-apps/working-with-experimental-preview.md#controlling-which-features-are-enabled) 

## Refine content for emails

When you open an email with the rich text editor, the **Adjust with Copilot** option is displayed on the toolbar. This feature allows you to enhance and polish the content of your email with the assistance of Copilot.

1. After you enter the content in the email, select the text that you want to refine.
1. Select **Adjust with Copilot** and refine the content as per your requirements. The following refinement options are available:

    | Refinement option | Description | 
    |------------------|-------------|
    | Length | Use an option from Short, Medium, or Long to determine the length of the text. |
    | Tone | Use an option from Friendly, Professional, or Formal to determine the tone of the content with which you want to communicate with customer. |

1. Select **Update** and the content is refined according to your selected options in the email.

For example, Marina wants to send an email with short length and in a formal tone to Kenny (a customer) to inform about their CRM product.

|Unrefined content| Refined content using Copilot email assist |
|-----------------|--------------------------------------------|
| Hi Kenny,<br>My name is Marina; I’m Sales executive at Contoso Inc.<br>I was recommended by Kevin to get in touch with you.<br>I noticed on your website that you don’t have CRM application.<br>I’d love to connect with you to discuss the potential of partnering up. When would you have time to chat about this?<br>If you want to learn more about the product first, here’s a quick link: www.contoso.com.<br>Kind regards,<br>Marina | Dear Mr. Kenny,<br>I am Marina, a Sales Executive at Contoso Inc. Kevin recommended that I contact you. I noticed that your website does not have a CRM application. I would like to discuss the possibility of a partnership. When would you have time to talk about this? If you would like to learn more about our product, please refer to this link: www.contoso.com.<br>Sincerely,<br>Marina |

### See also

- [Add the rich text editor control](../model-driven-apps/rich-text-editor-control.md)  
- [Add the Copilot control to a form](../model-driven-apps/copilot-control.md)  
- [FAQ for Copilot in rich text editor](../common/faqs-email-assist-rte.md)
