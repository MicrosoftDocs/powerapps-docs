---
title: Send a message to Copilot chat in model-driven apps 
description: Learn how to send a message from Agent to user in model-driven apps Copilot chat
author: Mattp123
ms.service: powerapps
ms.subservice: mda-maker
ms.author: hemantg
ms.reviewer: matp
ms.date: 03/16/2025
ms.topic: how-to
applies_to: 
  - "powerapps"
search.audienceType: 
  - maker
contributors:
  - makolomi
ms.collection: bap-ai-copilot
ai-usage: ai-assisted
---
# Send a message to Copilot chat (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Extend your app's Copilot chat engagement and affect by incorporating rich audio, video, and simple cards as a chat response type. The **Message** node, within the flow of a topic in Copilot Studio, can be used to send a message from the agent to the user in your model-driven app. Messages can be simple text messages, but can also include richer components, such as images, videos, quick replies, and cards.

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.
> - Copilot Studio license and agent editing permissions are required to customize Copilot chat.

## Add an image response to Copilot chat

When you add an image, Copilot can send a message as a response with the image from the agent to the user. To add an image, the image must be hosted through a URL.

1. [Add a Message node.](/microsoft-copilot-studio/authoring-send-message#send-a-text-message)
1. In the node's menu bar, select **Add** and choose **Image**.
1. Under **Image properties**, enter the **Image URL** for your image.
1. Optionally, enter a **Title** for the image.
:::image type="content" source="media/mda-copilot-chat-image-message.png" alt-text="Add an image response to Copilot chat" lightbox="media/mda-copilot-chat-image-message.png":::

## Add a video response to Copilot chat

When you add a video, Copilot can send a message with the video as a response from the agent to the user.

1. [Add a Message node.](/microsoft-copilot-studio/authoring-send-message#send-a-text-message)
1. In the node's menu bar, select **Add**, and then select **Video**.
1. Under **Media URL**, enter the URL of your video. The URL can either be a direct link to a publicly accessible MP4 file or a YouTube URL.
1. Optionally, enter a **Title**, **Subtitle**, **Image URL** (the URL of a publicly available image file), or **Text** to be shown alongside the video on the card. You can also add one or more buttons, which have the same properties as quick replies.
:::image type="content" source="media/mda-copilot-chat-video-message.png" alt-text="Add an video response to Copilot chat" lightbox="media/mda-copilot-chat-video-message.png":::

## Add a basic card response to Copilot chat

A basic card is a general-purpose card used for adding text, images, and interactive elements to an agent response message.

1. [Add a Message node.](/microsoft-copilot-studio/authoring-send-message#send-a-text-message)
1. In the node's menu bar, select **Add**, and then select **Basic card**.
1. In the **Basic Card properties** pane, fill in the properties for the content of your card. You can also add one or more buttons, which have the same effect as [quick replies](/microsoft-copilot-studio/authoring-send-message#use-quick-replies).
:::image type="content" source="media/mda-copilot-chat-basic-card-message.png" alt-text="Add a basic card response to Copilot chat" lightbox="media/mda-copilot-chat-basic-card-message.png":::

For more information about sending messages with Copilot, go to [send a message Copilot Studio documentation](/microsoft-copilot-studio/authoring-send-message)

## Related articles

- [Customize Copilot chat using Copilot Studio (preview)](customize-copilot-chat.md)
- [Add topics to Copilot chat in model-driven apps (preview)](copilot-chat-mda-topics.md)
- [FAQ for Copilot chat in model-driven apps](../common/faqs-copilot-model-driven-app.md)
- [Responsible AI FAQs for Power Apps](../common/responsible-ai-overview.md)
- [Enable copilots and generative AI features in Power Apps](/power-platform/admin/geographical-availability-copilot#enable-data-movement-across-regions)