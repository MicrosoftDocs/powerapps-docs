<properties
    pageTitle="Text input: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the text-input control"
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

# Text input in PowerApps #
[AZURE.INCLUDE [control-text-input](../../includes/control-text-input.md)]

## Description ##
The user can specify data by typing into a text-input control. Depending on how you configure the app, that data might be added to a data source, used to calculate a temporary value, or incorporated in some other way.

## Key properties ##

[AZURE.INCLUDE [long-text](../../includes/long-text.md)]

[AZURE.INCLUDE [long-default](../../includes/long-default.md)]

[AZURE.INCLUDE [long-reset](../../includes/long-reset.md)]

## All properties ##

[AZURE.INCLUDE [short-align](../../includes/short-align.md)]

[AZURE.INCLUDE [short-bordercolor](../../includes/short-bordercolor.md)]

[AZURE.INCLUDE [short-borderstyle](../../includes/short-borderstyle.md)]

[AZURE.INCLUDE [short-borderthickness](../../includes/short-borderthickness.md)]

[AZURE.INCLUDE [short-clear](../../includes/short-clear.md)]

[AZURE.INCLUDE [short-color](../../includes/short-color.md)]

[AZURE.INCLUDE [short-default](../../includes/short-default.md)]

[AZURE.INCLUDE [short-disabled](../../includes/short-disabled.md)]

[AZURE.INCLUDE [short-disabledbordercolor](../../includes/short-disabledbordercolor.md)]

[AZURE.INCLUDE [short-disabledcolor](../../includes/short-disabledcolor.md)]

[AZURE.INCLUDE [short-disabledfill](../../includes/short-disabledfill.md)]

[AZURE.INCLUDE [short-fill](../../includes/short-fill.md)]

[AZURE.INCLUDE [short-font](../../includes/short-font.md)]

[AZURE.INCLUDE [short-fontweight](../../includes/short-fontweight.md)]

[AZURE.INCLUDE [short-height](../../includes/short-height.md)]

[AZURE.INCLUDE [short-hinttext](../../includes/short-hinttext.md)]

[AZURE.INCLUDE [short-hoverbordercolor](../../includes/short-hoverbordercolor.md)]

[AZURE.INCLUDE [short-hovercolor](../../includes/short-hovercolor.md)]

[AZURE.INCLUDE [short-hoverfill](../../includes/short-hoverfill.md)]

[AZURE.INCLUDE [short-italic](../../includes/short-italic.md)]

[AZURE.INCLUDE [short-lineheight](../../includes/short-lineheight.md)]

[AZURE.INCLUDE [short-maxlength](../../includes/short-maxlength.md)]

[AZURE.INCLUDE [short-mode](../../includes/short-mode.md)]

[AZURE.INCLUDE [short-onchange](../../includes/short-onchange.md)]

[AZURE.INCLUDE [short-onselect](../../includes/short-onselect.md)]

[AZURE.INCLUDE [short-paddingbottom](../../includes/short-paddingbottom.md)]

[AZURE.INCLUDE [short-paddingleft](../../includes/short-paddingleft.md)]

[AZURE.INCLUDE [short-paddingright](../../includes/short-paddingright.md)]

[AZURE.INCLUDE [short-paddingtop](../../includes/short-paddingtop.md)]

[AZURE.INCLUDE [short-pressedbordercolor](../../includes/short-pressedbordercolor.md)]

[AZURE.INCLUDE [short-pressedcolor](../../includes/short-pressedcolor.md)]

[AZURE.INCLUDE [short-pressedfill](../../includes/short-pressedfill.md)]

[AZURE.INCLUDE [short-radiusbottomleft](../../includes/short-radiusbottomleft.md)]

[AZURE.INCLUDE [short-radiusbottomright](../../includes/short-radiusbottomright.md)]

[AZURE.INCLUDE [short-radiustopleft](../../includes/short-radiustopleft.md)]

[AZURE.INCLUDE [short-radiustopright](../../includes/short-radiustopright.md)]

[AZURE.INCLUDE [short-reset](../../includes/short-reset.md)]

[AZURE.INCLUDE [short-size](../../includes/short-size.md)]

[AZURE.INCLUDE [short-strikethrough](../../includes/short-strikethrough.md)]

[AZURE.INCLUDE [short-text](../../includes/short-text.md)]

[AZURE.INCLUDE [short-tooltip](../../includes/short-tooltip.md)]

[AZURE.INCLUDE [short-underline](../../includes/short-underline.md)]

[AZURE.INCLUDE [short-valid](../../includes/short-valid.md)]

[AZURE.INCLUDE [short-visible](../../includes/short-visible.md)]

[AZURE.INCLUDE [short-width](../../includes/short-width.md)]

[AZURE.INCLUDE [short-x](../../includes/short-x.md)]

[AZURE.INCLUDE [short-y](../../includes/short-y.md)]

## Related functions ##

[**DateTimeValue**( *String* )](function-datevalue-timevalue.md)

## Examples ##

### Collect data ###
1. Add two text-input controls, and name them **inputFirst** and **inputLast**.

1. Add a button, set its **Text** property to **Add**, and set its **OnSelect** property to this formula:<br>
**Collect(Names, {FirstName:inputFirst.Text, LastName:inputLast.Text})**

	Want more information about the [**Collect** function](function-clear-collect-clearcollect.md) or [other functions](formula-reference.md)?

1. Add a text gallery in portrait/vertical orientation, set its **Items** property to **Names**, and set the **Text** property of **Subtitle1** to **ThisItem.FirstName**.

1. (optional) In the template gallery, delete the bottom text box, named **Body1**, and set the **TemplateSize** property of the gallery to **80**.

1. Press F5, type a string of text into **inputFirst** and **inputLast**, and then click or tap the **Add** button.

1. (optional) Add more names to the collection, and then press Esc to return to the default workspace.

### Prompt for a password ###
1. Add a text-input control, name it **inputPassword**, and set its **Mode** property to **Password**.

1. Add a text box, and set its **Text** property to this formula:<br>
**If(inputPassword.Text = "P@ssw0rd", "Access granted", "Access denied")**

	Want more information about the [**If** function](function-if.md) or [other functions](formula-reference.md)?

1. Press F5, and then type **P@ssw0rd** in **inputPassword**.

	When you finish typing the password, the text box stops showing **Access denied** and starts to show **Access granted**.

1. To return to the default workspace, press Esc.

1. (optional) Add a control such as an arrow, configure it to navigate to another screen, and show it only after the user types the password.

1. (optional) Add a button, configure its **Text** property to show **Sign in**, add a timer, and disable the input-text control for a certain amount of time if the user types the wrong password and then clicks or taps the **Sign in** button.
