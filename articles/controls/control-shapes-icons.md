<properties
    pageTitle="Shape and icon controls: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about shape and icon controls"
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

# Shape and icon controls in PowerApps #
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
1. Name the default screen **Target**, add a text box, and set its **Text** property to show **Target**.

	Don't know how to [add and configure a control](add-configure-controls.md)?

1. Add a screen, and name it **Source**.

1. In **Source**, add a left-pointing arrow, and set its **OnSelect** property to this formula:
<br>**Navigate(Target, ScreenTransition.Fade)**

1. Press F5, and then select the arrow.

	The **Target** screen appears.

1. (optional) Press Esc to return to the default workspace, add a right-pointing arrow to **Target**, and set the arrow's **OnSelect** property to this formula:
<br>**Navigate(Source, ScreenTransition.Fade)**
