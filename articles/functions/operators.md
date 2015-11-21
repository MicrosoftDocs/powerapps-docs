<properties
	pageTitle="PowerApps: Operators"
	description="Reference information for the Operators in PowerApps, including syntax and examples"
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

|Symbol|Operator type|Syntax|Description|
|---|---|---|---|
|( )|Parentheses|Filter(T, A &lt; 10)<br><br>(1 + 2) * 3|Precedence-order enforcement, and grouping of sub-expressions in a larger expression|
|+|Arithmetic operators|1 + 2|Addition|
|-||2 - 1|Subtraction and sign|
|\*||2 * 3|Multiplication|
|/||2 / 3|Division|
|^||2 ^ 3|Exponentiation|
|%||20%|Percentage (equivalent to &quot;* 1/100&quot;)|
|=|Comparison operators|Price = 100|Equal to|
|&gt; ||Price &gt; 100|Greater than|
|&gt;=||Price &gt;= 100|Greater than or equal to|
|&lt; ||Price &lt; 100|Less than|
|&lt;=||Price &lt;= 100|Less than or equal to|
|&lt;&gt; ||Price &lt;&gt; 100|Not equal to|
|&amp;|String concatenation operator|&quot;hello&quot; &amp; &quot; &quot; &amp; &quot;world&quot;|Makes multiple strings appear continuous|
|&amp;&amp;|Logical operators|Price &lt; 100 &amp;&amp; slider!value = 20|Logical conjunction|
|&#124;&#124;||Price &lt; 100 &#124;&#124; slider!value = 20|Logical disjunction|
|!||!(Price &lt; 100)|Logical negation|
|exactin|Membership operators|gallery!Selected exactin SavedItems|Belonging to a collection or table|
|exactin||&quot;Windows&quot; exactin “To display windows in the Windows operating system...”|Substring test (case-sensitive)|
|in||gallery!Selected in SavedItems|Belonging to a collection or table<br><br>|
|in||&quot;The&quot; in &quot;The keyboard and the monitor...&quot;|Substring test (case-insensitive)|
|@|Disambiguation operator|MyTable[@fieldname]|Field disambiguation|
|||[@MyTable]|Global disambiguation|
|;|Formula chaining|Collect(T, A); Navigate(S1, &quot;&quot;)|Separate invocations of functions in behavior properties|

## in and exactin operators ##

You can use the **in** and **exactin** operators to find a string in a data source, such as a collection or an imported table. The **in** operator identifies matches regardless of case, and the **exactin** operator identifies matches only if they're capitalized the same way. Here's an example:

1. Create or import a collection named **Inventory**, and show it in a gallery, as Create your first app describes.

2. Set the **Items** property of the gallery to this function:

	**Filter(Inventory, "E" in ProductName)**

	The gallery shows all products except Callisto because the name of that product is the only one that doesn't contain the letter you specified.

3. Change the **Items** property of the gallery to this function:

	**Filter(Inventory, "E" exactin ProductName)**

	The gallery shows only Europa because only its name contains the letter you specified in the case that you specified.

## ThisItem operator for galleries ##

You show data in a gallery by binding it to a table or a collection and then adding one or more types of controls to show different kinds of data. You use the ThisItem operator to specify the column of data that each control shows. For example, that operator in the product gallery for Create your first app specified that the image control showed the product design, the upper label showed the product name, and the lower label showed the number of units in stock.

For nested galleries, ThisItem refers to the innermost gallery's items. Assuming the row fields in the inner and outer galleries don't conflict, you can also use the unqualified field (column) names directly—this approach enables rules in an inner gallery to refer to an outer gallery's items.

