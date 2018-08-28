---
title: Customize a card | Microsoft Docs
description: Change the default control that appears in a card on a Details or Edit form in PowerApps
author: AFTOwen
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 03/18/2018
ms.author: anneta
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Customize a card in PowerApps
Perform basic customization (without unlocking a card) by, for example, changing its control. Perform advanced customization by unlocking the card and, for example, adding a control that isn't available for that card by default.

For an overview, see [Understand data cards](working-with-cards.md).

## Prerequisites

* Learn how to [add and configure controls](add-configure-controls.md).
* You can review this topic for general concepts only, or you can follow it step by step if you complete the procedures in these topics:

  1. [Generate an app](data-platform-create-app.md).
  2. [Customize its gallery](customize-layout-sharepoint.md).
  3. [Customize its forms](customize-forms-sharepoint.md).

## Customize a locked card
In this procedure, you'll replace a **[Text-input](controls/control-text-input.md)** control with a **[Slider](controls/control-slider.md)** control without unlocking the card.

1. Sign in to [PowerApps](http://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

    ![Home page for PowerApps](./media/customize-card/sign-in.png)

1. Open the app that you generated and customized, select **EditForm1**, and then open the **Data** pane by selecting **Accounts** in the right-hand pane.

1. In the list of fields, select the down arrow for **Number of Employees** to show a list of options, and then select **Edit Slider**.

    ![Drop-down list of options for a number card](./media/customize-card/card-selector.png)

    The screen reflects your change.

    ![EditForm1 with slider control](./media/customize-card/add-slider.png)

## Unlock and customize a card
In this procedure, you'll unlock a card and then replace a **[Toggle](controls/control-toggle.md)** control with a **[Checkbox](controls/control-check-box.md)** control.

1. In **EditForm1**, show the **Send Marketing Materials** field.

    ![Show field for Send Marketing Materials](./media/customize-card/show-field.png)

2. With that card selected, click or tap **Advanced** near the top of the right-hand pane, and then click or tap the lock icon to unlock the card.

    ![Show field for Send Marketing Materials](./media/customize-card/unlock-card.png)

1. In the card, delete the **Toggle** control, add a **Check box** control, and name the new control **chkMktg**.

    ![Replace toggle with checkbox](./media/customize-card/add-checkbox.png)

1. Select the card that you just updated.

    ![Select card](./media/customize-card/select-card.png)

1. In the right-hand pane, ensure that the **Advanced** tab is still showing, and then click or tap **More options**.

    ![More options button](./media/customize-card/more-options.png)

1. Change the value of the card's **Update** property to this expression:
<br>`chkMktg.Value`

1. Change value of the **Y** property of the error message for that card to this expression:<br>
`chkMktg.Y + chkMktg.Height`

    ![Select error message for new card](./media/customize-card/select-error.png)

1. Change the value of the **Text** property of **chkMktg** to **Yes**.

    The screen reflects your changes, and the errors are resolved.

    ![Final screen with errors resolved](./media/customize-card/final-screen.png)

## Next steps
Now that you have a basic understanding of how to generate an app and customize a gallery, a form, and a card, you can [build your own app from scratch](data-platform-create-app-scratch.md).
