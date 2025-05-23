---
title: Troubleshoot common errors when creating app from Figma
description: Learn about common errors and resolutions when creating apps from a Figma design.
author: mduelae
ms.topic: troubleshooting-general
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 05/24/2022
ms.subservice: canvas-maker
ms.author: kaagar
search.audienceType: 
  - maker
contributors:
  - mduelae
---

# Troubleshoot common errors when creating app from Figma

[This article is pre-release documentation and is subject to change.]

In this article, learn about common errors that you may see when creating apps from a Figma design.

## Error: Invalid link. Copy a specific page link or frame link, and not a link to just the file

:::image type="content" source="media/error-invalid-link.png" alt-text="Invalid link. Copy a specific page link or frame link, and not a link to just the file.":::

This error appears when you enter the link to a Figma file instead of the link to a specific page or a frame within the Figma file. Sometimes, the link may also have a missing "node-id".

To get the Figma page or frame URL with "node-id", ensure you select any frame inside Figma before copying the URL from the address bar. You can also find a link to the page with "node-id" by selecting the page you want to convert > right-click on the page name > select **Copy link to page**.

:::image type="content" source="media/copy-link-page.png" alt-text="Copy link to page option inside Figma.":::

Ensure the URL contains `?node-id=<node ID>` when you paste the copied link in the app from Figma screen inside Power Apps.

For more information about creating links to a page or a frame, see [Copy links to Files, Pages, and Frames](https://help.figma.com/hc/articles/360045942953-Add-links-to-text) and [Copy link to page](https://help.figma.com/hc/articles/360055904133-Maker-and-Figma#In_Figma).

## Error: Access denied. Check the information you entered and try again

:::image type="content" source="media/error-invalid-token.png" alt-text="Access denied. Check the information you entered and try again.":::

This error appears when you provide an invalid token while creating app from Figma. To learn about how to generate a personal access token in Figma, see [Access tokens](https://www.figma.com/developers/api#access-tokens).

## App creation fails because of invalid structure

The app creation will fail if the Figma page or frame you provided doesn't have a valid structure with a list of components all within a frame. When this happens, ensure that you follow the **Detach instance** step before using the frame to generate the app.

:::image type="content" source="media/error-detach-screen.png" alt-text="App creation fails - detach the screen from its main component by selecting Detach instance.":::

Also ensure the components added to the page inside Figma are contained within a frame, and they're from the list of supported components that the UI kit provided.

### See also

- [Create a canvas app from Figma](create-app-from-figma.md)
- [Components supported by the UI Kit](supported-components.md)
- [Troubleshoot common errors](common-errors.md)
