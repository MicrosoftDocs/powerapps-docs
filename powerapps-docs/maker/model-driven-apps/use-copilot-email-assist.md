---
title: Use Copilot in the email rich text editor
description: Learn how to use Copilot in the rich text editor to make your customer emails clearer, shorter, and more compelling.
author: udaykirang
ms.author: udag
ms.reviewer: udag
ms.topic: how-to
ms.date: 04/30/2025
ms.update-cycle: 180-days
ms.subservice: mda-maker
ms.collection: bap-ai-copilot
tags:
search.audienceType:
  - maker
ms.custom:
  - bap-template
  - ai-gen-docs-bap
  - ai-gen-desc
  - ai-seo-date:10/02/2023
---

# Use Copilot in the email rich text editor 

When you draft customer emails in the rich text editor in a model-driven app, Copilot can offer suggestions to make them clearer, more concise, and more compelling.

> [!IMPORTANT]
> By using Copilot features powered by Azure OpenAI, you agree that data may be stored and/or processed outside of your geographic region, compliance boundary, or national cloud instance. Learn more: [Data, privacy, and security for Azure OpenAI Service](/legal/cognitive-services/openai/data-privacy#preventing-abuse-and-harmful-content-generation)

## Prerequisites

The [generative AI feature in emails](/power-platform/admin/settings-features#ai-suggestions-for-email-content) must be turned on in the [model-driven app feature settings](/power-platform/admin/settings-features).

## Draft and refine an email in the rich text editor

1. Select the **Copilot** icon in the rich text editor toolbar and then select **Draft with Copilot**.  
1. In the **Draft with Copilot** dialog box, select a prompt as required.  
1. To refine or update the generated content, select the following options as required:  

    | Option | Description |
    |--------|-------------|
    | Keep it | Retains the current text and adds it to the email. |
    | Start over| Removes the current suggestion and takes you back to the email prompt. |
    | Discard | Removes the content suggestion and takes you back to email editor. |
    | Adjust | Refines the text and tone of suggested content. <br>- To adjust the length of the content, select **Short**, **Medium**, or **Long**.<br>- To adjust the tone of the content, select **Friendly**, **Professional**, or **Formal**.<br> Select **Update** and the content is updated according to your refinements. |
    | Translate | Translates the content into the selected language. The languages listed here are those supported by your environment. To go back to the language that the content was originally generated, select **Show original**.  |

## Adjust existing email content with Copilot

1. Select the text that you want to refine.
1. Select the **Copilot** icon in the rich text editor toolbar and then select **Adjust with Copilot**.  
1. Refine the length and tone of the selected text:

    - Length: Select **Short**, **Medium**, or **Long** to condense or expand on your text.
    - Tone: Select **Friendly**, **Professional**, or **Formal** to adjust the tone of your text.

1. Select **Update** to apply Copilot's suggested refinements.

For example, Marina wants to send an email to a customer about a new product. Marina types a draft, selects **Adjust with Copilot**, and asks Copilot to rewrite the draft to be shorter and in a more formal tone.

- Before Copilot's assistance:

  ```text
  Hi Samir,
  
  My name is Marina; I'm a Sales executive at Contoso Inc. I was 
  recommended by Kevin to get in touch with you.
  
  I noticed on your website that you don't have CRM application. I'd 
  love to connect with you to discuss the potential of partnering up. 
  When would you have time to chat about this?
  
  If you want to learn more about the product first, here's a quick 
  link: www.contoso.com.
  
  Kind regards,
  Marina
  ```

- After Copilot's assistance:

    ```text
    Dear Mr. Samir,

    I am Marina, a Sales Executive at Contoso Inc. Kevin recommended that I 
    contact you. I noticed that your website does not have a CRM application. 
    I would like to discuss the possibility of a partnership. When would you 
    have time to talk about this? If you would like to learn more about our 
    product, please refer to this link: www.contoso.com.

    Sincerely,
    Marina
    ```

### See also

- [Add the rich text editor control](../model-driven-apps/rich-text-editor-control.md)
- [Add the Copilot control to the rich text editor](../model-driven-apps/copilot-control.md)
- [FAQ about using Copilot in the rich text editor](../common/faqs-email-assist-rte.md)
