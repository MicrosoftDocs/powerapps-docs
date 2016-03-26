<properties
    pageTitle="Screen control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about a Screen control"
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

# Screen control in PowerApps #
[AZURE.INCLUDE [control-summary-screen](../../includes/control-summary-screen.md)]

## Description ##
Most apps have multiple **Screen** controls that contain **Text Box** controls, **Button** controls, and other controls that show data and support navigation.

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
1. Add a **Radio** control, name it **ScreenFills**, and set its **Items** property to this value:<br>
**["Red", "Green"]**

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

1. Name the default **Screen** control **Source**, add another **Screen** control, and name it **Target**.

1. On **Source**, add a **Shape** control (such as an arrow), and set its **OnSelect** property to this formula:<br>
**Navigate(Target, ScreenTransition.Fade)**

	Want more information about the [**Navigate** function](function-navigate.md) or [other functions](formula-reference.md)?

1. In **Target**, add a **Shape** control (such as an arrow), and set its **OnSelect** property to this formula:<br>
**Navigate(Source, ScreenTransition.Fade)**

1. Set the **Fill** property of **Target** to this formula:<br>
**If("Red" in ScreenFills.Selected.Value, RGBA(255, 0, 0, 1), RGBA(54, 176, 75, 1))**

1. From **Source**, press F5, click or tap either option in the **Radio** control, and then click or tap the **Shape** control.

	**Target** appears in the color that you chose.

1. On **Target**, click or tap the **Shape** control to return to **Source**.

1. (optional) Click or tap the other option in the **Radio** control, and then click or tap the **Shape** control to confirm that **Target** appears in the other color.

1. To return to the default workspace, press Esc.
