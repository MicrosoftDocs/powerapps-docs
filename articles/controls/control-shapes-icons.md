<properties
    pageTitle="Shape controls and icon controls: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about shape controls and icon controls"
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
   ms.date="03/11/2016"
   ms.author="anneta"/>

# Shape controls and icon controls in PowerApps #
[AZURE.INCLUDE [control-summary-shapes-icons](../../includes/control-summary-shapes-icons.md)]

## Description ##
These controls include arrows, geometric shapes, action icons, and symbols for which you can configure properties such as fill, size, and location. You can also configure their **OnSelect** property so that the app responds if the user clicks or taps the control.

## Key properties ##

[AZURE.INCLUDE [short-onselect](../../includes/short-onselect.md)]

[AZURE.INCLUDE [short-fill](../../includes/short-fill.md)]

## All properties ##

[AZURE.INCLUDE [short-disabled](../../includes/short-disabled.md)]

[AZURE.INCLUDE [short-disabled](../../includes/short-disabledfill.md)]

[AZURE.INCLUDE [short-fill](../../includes/short-fill.md)]

[AZURE.INCLUDE [short-height](../../includes/short-height.md)]

[AZURE.INCLUDE [short-hoverfill](../../includes/short-hoverfill.md)]

[AZURE.INCLUDE [short-onselect](../../includes/short-onselect.md)]

[AZURE.INCLUDE [short-pressedbordercolor](../../includes/short-pressedfill.md)]

[AZURE.INCLUDE [short-visible](../../includes/short-visible.md)]

[AZURE.INCLUDE [short-width](../../includes/short-width.md)]

[AZURE.INCLUDE [short-x](../../includes/short-x.md)]

[AZURE.INCLUDE [short-y](../../includes/short-y.md)]

## Related functions ##

[**Navigate**( *ScreenName*, *ScreenTransition* )](function-navigate.md)

## Example ##
1. Name the default **Screen** control **Target**, add a **Text box** control, and set its **Text** property to show **Target**.

	Don't know how to [add and configure a control](add-configure-controls.md)?

1. Add a **Screen** control, and name it **Source**.

1. In **Source**, add a **Shape** control, and set its **OnSelect** property to this formula:
<br>**Navigate(Target, ScreenTransition.Fade)**

1. Press F5, and then click or tap the **Shape** control.

	The **Target** screen appears.

1. (optional) Press Esc to return to the default workspace, add a **Shape** control to **Target**, and set the **OnSelect** property of the **Shape** control to this formula:
<br>**Navigate(Source, ScreenTransition.Fade)**
