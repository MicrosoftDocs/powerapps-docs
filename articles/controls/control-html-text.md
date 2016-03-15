<properties
    pageTitle="HTML text control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the HTML text control"
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

# HTML text control in PowerApps #
[AZURE.INCLUDE [control-summary-html-text](../../includes/control-summary-html-text.md)]

## Description ##
An HTML text control not only shows plain text and numbers but also converts HTML tags, such as non-breaking spaces.

## Key properties ##

[AZURE.INCLUDE [short-html-text](../../includes/short-html-text.md)]

[AZURE.INCLUDE [short-font](../../includes/short-font.md)]

[AZURE.INCLUDE [short-color](../../includes/short-color.md)]

## All properties ##
[AZURE.INCLUDE [short-bordercolor](../../includes/short-bordercolor.md)]

[AZURE.INCLUDE [short-borderstyle](../../includes/short-borderstyle.md)]

[AZURE.INCLUDE [short-borderthickness](../../includes/short-borderthickness.md)]

[AZURE.INCLUDE [short-color](../../includes/short-color.md)]

[AZURE.INCLUDE [short-disabled](../../includes/short-disabled.md)]

[AZURE.INCLUDE [short-disabledbordercolor](../../includes/short-disabledbordercolor.md)]

[AZURE.INCLUDE [short-disabledfill](../../includes/short-disabledfill.md)]

[AZURE.INCLUDE [short-fill](../../includes/short-fill.md)]

[AZURE.INCLUDE [short-font](../../includes/short-font.md)]

[AZURE.INCLUDE [short-height](../../includes/short-height.md)]

[AZURE.INCLUDE [short-hoverbordercolor](../../includes/short-hoverbordercolor.md)]

[AZURE.INCLUDE [short-html-text](../../includes/short-html-text.md)]

[AZURE.INCLUDE [short-onselect](../../includes/short-onselect.md)]

[AZURE.INCLUDE [short-paddingbottom](../../includes/short-paddingbottom.md)]

[AZURE.INCLUDE [short-paddingleft](../../includes/short-paddingleft.md)]

[AZURE.INCLUDE [short-paddingright](../../includes/short-paddingright.md)]

[AZURE.INCLUDE [short-paddingtop](../../includes/short-paddingtop.md)]

[AZURE.INCLUDE [short-size](../../includes/short-size.md)]

[AZURE.INCLUDE [short-tooltip](../../includes/short-tooltip.md)]

[AZURE.INCLUDE [short-visible](../../includes/short-visible.md)]

[AZURE.INCLUDE [short-width](../../includes/short-width.md)]

[AZURE.INCLUDE [short-x](../../includes/short-x.md)]

[AZURE.INCLUDE [short-y](../../includes/short-y.md)]

## Related functions ##

[**Find**( *FindString*, *WithinString* )](function-find.md)

## Example ##

1. Add a text box, name it **Source**, and set its **Text** property to this string:

\<p> We have done an unusually \&nbsp; \&quot; deep \&quot; globalization and localization. \<p> 

Don't know how to [add, name, and configure a control](add-configure-controls.md)?

1. Add an HTML text control, and set its **HTMLText** property to this value:<br>
**Source.Text**

 	The HTML text control converts the tags to the appropriate characters.
