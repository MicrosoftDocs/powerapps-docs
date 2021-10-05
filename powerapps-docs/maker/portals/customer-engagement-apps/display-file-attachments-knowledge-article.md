---
title: Display file attachments with knowledge articles
description: Learn how to display file attachments with knowledge articles on a portal.
author: sbmjais
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/01/2021
ms.subservice: portals
ms.author: shjais
ms.reviewer: shjais
contributors:
    - tapanm-msft
    - shjais
---

# Display file attachments with knowledge articles

Knowledge articles help you achieve self-service. As a Knowledge Manager, you might want to share some downloadable files along with your articles to provide detailed information or a case study. You can author knowledge articles and add them as notes attachments that can be used by users. These attachments aren't displayed automatically on portals, thereby limiting the effectiveness of self-service.

To display knowledge articles with downloadable file attachments, you must [create the site setting](../configure/configure-site-settings.md) KnowledgeManagement/DisplayNotes, and set the value to true. When you set the site setting to true, knowledge articles are displayed along with their attachments, so portal users can search for these attachments.

To search for knowledge article attachments in the portal, for knowledge authors, you'll want to use the attachments function in the knowledge article editor instead of adding attachments in the notes section. If you've enabled **Sync knowledge article attachments to portal**, knowledge article attachments will automatically be synced to the notes attachment. To learn how to create knowledge article attachments, see [Add a file attachment to a knowledge article](/dynamics365/customer-service/customer-service-hub-user-guide-knowledge-article.md#add-a-file-attachment-to-a-knowledge-article).
