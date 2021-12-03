---
title: Get the session or app ID
description: Learn about how to get a session ID or a canvas-app ID for troubleshooting.
author: tapanm-msft
ms.service: powerapps
ms.subservice: troubleshoot
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 09/02/2021
ms.author: tapanm
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
---
# Get session and app ID details

If you find a problem with an app in Power Apps, you can help Microsoft troubleshoot the problem much more effectively with a session ID, an app ID, or both.

## Get the session ID for a canvas app

### When editing a canvas app

1. In the upper-left corner, select **File**.

1. Select **Account**.

1. Select **Support** > **Session details**.

    ![Get a session ID from Power Apps Studio.](media/get-sessionid/studio.png "Get a session ID from Power Apps Studio")

1. Select **Copy details** to copy all session to clipboard.

### When running a canvas app in a browser

1. In the upper-right corner, select ![Gear icon.](media/get-sessionid/gear-icon.png "Gear icon").

1. Select **Session details**.

    ![Get a session ID from a browser.](media/get-sessionid/browser.png "Get a session ID from a browser")

### When running a canvas app on a phone or a tablet

1. In the upper-left corner, select ![App settings from top-left.](media/get-sessionid/mobile-icon.png "App settings from top-left").

    ![App settings from top-left - on mobile screen.](media/get-sessionid/mobile-2.png "App settings from top-left - on mobile screen")

1. Tap **Session details**.

    ![Get a session ID from a phone or a tablet.](media/get-sessionid/mobile.png "Get a session ID from a phone or a tablet")

### When running an embedded canvas app or form

1. Do one of these steps:

    - While holding down the Alt key, right-click the app or form.
    - Tap the app or form with two fingers for 1-2 seconds, and then release.

1. Select **Session details**.

    ![Get a session ID from an embedded app.](media/get-sessionid/embedded.png "Get a session ID from an embedded app")

## Get the session ID for a model-driven app

### When editing a model-driven app

1. From the preview pane in app designer, on the command bar in the model-driven app displayed, select **Settings** (gear).
1. Select **About**.

### When running a model-driven app in a browser

1. On the command bar in a model-driven app, select **Settings** (gear).
1. Select **About**.
   :::image type="content" source="media/get-sessionid/session-details-mda.png" alt-text="Session ID displayed with session details":::

## Get the session ID for Power Apps (make.powerapps.com)

1. Sign into Power Apps (make.powerapps.com), and then, on the command bar, select **Settings** (gear).
1. Select the **Session details**.
   :::image type="content" source="media/get-sessionid/session-details-powerapps.png" alt-text="Session details from Power Apps site":::

## Get an app ID

Get the app ID for either a canvas or model-driven app: 
1. [Sign in to Power Apps](https://powerapps.microsoft.com).

1. Near the left edge, select **Apps**.

1. Select ![Ellipsis - More Commands option.](media/get-sessionid/ellipsis.png "Ellipsis - More Commands option") (More Commands).

1. Select **Details**.

    ![Go to app details.](./media/get-sessionid/details.png "Go to app details")

    The app ID appears at the bottom of the **Details** pane for that app.

    ![Copy app ID from details.](./media/get-sessionid/app-id.png "Copy app ID from details")



[!INCLUDE[footer-include](../../includes/footer-banner.md)]