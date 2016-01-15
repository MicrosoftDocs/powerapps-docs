<properties
	pageTitle="Operators | Microsoft PowerApps"
	description="Reference information, including syntax and examples, for the operators in PowerApps"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="dwrede"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/20/2015"
   ms.author="gregli"/>

# Operators in PowerApps #

|Symbol|Type|Syntax|Description|
|---|---|---|---|
|**.**|Property Selector|Slider1.Value<br>Color.Red<br>Acceleration.X|Extracts a property from a [table](working-with-tables.md), control, [signal](signals.md), or enumeration.  For backwards compatibility, **!** may also be used.
|**( )**|Parentheses|Filter(T, A &lt; 10)<br><br>(1 + 2) * 3|Enforces precedence order, and groups sub-expressions in a larger expression|
|**+**|Arithmetic operators|1 + 2|Addition|
|**-**|&nbsp;|2 - 1|Subtraction and sign|
|**\***|&nbsp;|2 * 3|Multiplication|
|**/**|&nbsp;|2 / 3|Division (also see the **[Mod](function-mod.md)** function) |
|**^**|&nbsp;|2 ^ 3|Exponentiation|
|**%**|&nbsp;|20%|Percentage (equivalent to &quot;* 1/100&quot;)|
|**=**|Comparison operators|Price = 100|Equal to|
|**&gt;** |&nbsp;|Price &gt; 100|Greater than|
|**&gt;=**|&nbsp;|Price &gt;= 100|Greater than or equal to|
|**&lt;** |&nbsp;|Price &lt; 100|Less than|
|**&lt;=**|&nbsp;|Price &lt;= 100|Less than or equal to|
|**&lt;&gt;** |&nbsp;|Price &lt;&gt; 100|Not equal to|
|**&amp;**|String concatenation operator|&quot;hello&quot; &amp; &quot; &quot; &amp; &quot;world&quot;|Makes multiple strings appear continuous|
|**&amp;&amp;**|Logical operators|Price &lt; 100 &amp;&amp; Slider1.Value = 20|Logical conjunction or **[And](function-logicals.md)**|
|**&#124;&#124;**|&nbsp;|Price &lt; 100 &#124;&#124; Slider1.Value = 20|Logical disjunction or **[Or](function-logicals.md)**|
|**!**|&nbsp;|!(Price &lt; 100)|Logical negation or **[Not](function-logicals.md)**|
|**exactin**|Membership operators|Gallery1.Selected exactin SavedItems|Belonging to a [collection](working-with-data-sources.md#collections) or a table|
|**exactin**|&nbsp;|&quot;Windows&quot; exactin “To display windows in the Windows operating system...”|Substring test (case-sensitive)|
|**in**|&nbsp;|Gallery1.Selected in SavedItems|Belonging to a collection or a table|
|**in**|&nbsp;|&quot;The&quot; in &quot;The keyboard and the monitor...&quot;|Substring test (case-insensitive)|
|**@**|Disambiguation operator|MyTable[@fieldname]|Field disambiguation|
|&nbsp;|&nbsp;|[@MyTable]|Global disambiguation|
|**;**|Formula chaining|Collect(T, A); Navigate(S1, &quot;&quot;)|Separate invocations of functions in behavior properties|

## in and exactin operators ##

You can use the **in** and **exactin** operators to find a string in a [data source](working-with-data-sources.md), such as a collection or an imported table. The **in** operator identifies matches regardless of case, and the **exactin** operator identifies matches only if they're capitalized the same way. Here's an example:

1. Create or import a collection named **Inventory**, and show it in a gallery, as the first procedure in [Show images and text in a gallery](../show-images-text-gallery-sort-filter.md) describes.

2. Set the **Items** property of the gallery to this formula:
<br>**Filter(Inventory, "E" in ProductName)**

	The gallery shows all products except Callisto because the name of that product is the only one that doesn't contain the letter you specified.

3. Change the **Items** property of the gallery to this formula:
<br>**Filter(Inventory, "E" exactin ProductName)**

	The gallery shows only Europa because only its name contains the letter that you specified in the case that you specified.

## ThisItem operator for galleries ##
You show data in a gallery by binding it to a table or a collection and then adding one or more types of controls to show different kinds of data. You use the **ThisItem** operator to specify the [column](working-with-tables.md#columns) of data that each control shows. For example, that operator in the product gallery for [Show images and text in a gallery](../show-images-text-gallery-sort-filter.md) specified that the image control showed the product design, the upper label showed the product name, and the lower label showed the number of units in stock.

For nested galleries, **ThisItem** refers to the innermost gallery's items. Assuming the row fields in the inner and outer galleries don't conflict, you can also use the unqualified field (column) names directly. This approach enables rules in an inner gallery to refer to an outer gallery's items.
