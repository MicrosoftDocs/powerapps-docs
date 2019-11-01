---
title: "Customize content by using content snippets on a portal | MicrosoftDocs"
description: "Learn how to customize content by using content snippets."
author: sbmjais
manager: shujoshi
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 11/04/2019
ms.author: shjais
ms.reviewer:
---

# Customize content by using content snippets

Content snippets are small chunks of editable content that can be placed by a developer on a page template, allowing for customizable content to populate any portion of a page's layout easily. Snippet controls, which are responsible for rendering the content of snippets on the web-facing portal, are placed on a page template by developers.

## Edit snippets

Snippets can be edited either through the Portal Management app. The main power of the snippet is the fact that you can abstract a bit of content (other than the main copy of the page) and edit it separately, allowing essentially any static content on your site to be fully content-managed and editable.

1. Open the [Portal Management app](configure-portal.md).

2.  Go to **Portals** > **Content Snippets**.

3.  To create a new snippet, select **New**.

4.  To edit an existing snippet, select an existing **Content Snippet** in the grid.

Enter values for the following fields:

| Name    | Description                                                                                                   |
|---------|---------------------------------------------------------------------------------------------------------------|
| Name    | The name can be used by a developer to place the snippet value into a page template within the portal's code. |
| Website | The website that is associated with the snippet.                                                              |
| Value   | The content of the snippet to be displayed in the portal. This can contain plain text or HTML markup.         |



