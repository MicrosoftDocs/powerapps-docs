<properties
    pageTitle="Screen: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about screens"
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="aftowen"
    manager="erikre"
    editor=""
    tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="02/29/2016"
   ms.author="anneta"/>

# Screens in PowerApps #
[AZURE.INCLUDE [control-summary-screen](../../includes/control-summary-screen.md)]

## Description ##
A screen contains controls such as text boxes and buttons so that the user can review and update data in an app. Most apps have multiple screens with buttons or other controls that support navigation and determine the data that appears on each screen.

## Key properties ##

[AZURE.INCLUDE [short-onvisible](../../includes/short-onvisible.md)]

[AZURE.INCLUDE [short-fill](../../includes/short-fill.md)]

## All properties ##

[AZURE.INCLUDE [short-backgroundimage](../../includes/short-backgroundimage.md)]

[AZURE.INCLUDE [short-fill](../../includes/short-fill.md)]

[AZURE.INCLUDE [short-imageposition](../../includes/short-imageposition.md)]

[AZURE.INCLUDE [short-onhidden](../../includes/short-onhidden.md)]

[AZURE.INCLUDE [short-onvisible](../../includes/short-onvisible.md)]

## Related functions ##

[**Distinct**( *DataSource*, *ColumnName* )](function-distinct.md)

## Example ##
1. Add a radio-button control, name it **ScreenFills**, and set its **Items** property to this value:<br>
**["Red", "Green"]**

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

1. Name the default screen **Source**, add another screen, and name it **Target**.

1. On **Source**, add a shape (such as an arrow), and set its **OnSelect** property to this formula:<br>
**Navigate(Target, ScreenTransition.Fade)**

	Want more information about the [**Navigate** function](function-navigate.md) or [other functions](formula-reference.md)?

1. In **Target**, add a shape (such as an arrow), and set its **OnSelect** property to this formula:<br>
**Navigate(Source, ScreenTransition.Fade)**

1. Set the **Fill** property of **Target** to this formula:<br>
**If("Red" in ScreenFills.Selected.Value, RGBA(255, 0, 0, 1), RGBA(54, 176, 75, 1))**

1. From **Source**, press F5, click or tap either radio button, and then click or tap the arrow.

	**Target** appears in the color that you chose.

1. On **Target**, click or tap the arrow to return to **Source**.

1. (optional) Click or tap the other radio button, and then click or tap the arrow to confirm that **Target** appears in the other color.

1. To return to the default workspace, press Esc.
