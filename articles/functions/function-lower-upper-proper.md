<properties
	pageTitle="PowerApps: Lower, Upper, and Proper functions"
	description="Reference information for the Lower, Upper, and Proper functions in PowerApps, including syntax and examples"
	services="powerapps"
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
   ms.date="10/21/2015"
   ms.author="gregli"/>

# Lower, Upper, and Proper functions in PowerApps #

Converts a string to all lower case, all upper case, or to proper case.

## Description ##

The **Lower**, **Upper**, and **Proper** functions convert the case of strings.
- The **Lower** function converts all characters to lower case.
- The **Upper** function converts all characters to upper case.
- The **Proper** function converts the first character of all words to upper case and all other characters to lower case.

For all three functions, characters that are not letters are not altered.

Pass a single string to return the converted version of that string.  You can also pass a single column table that contains strings, resulting in a single column table of converted strings.  See [Working with Tables](file-name.md) for information on shaping a multi-column data source into a single column table. 

## Syntax ##

**Lower**( *String* )
**Upper**( *String* )
**Proper**( *String* )

- *String* - Required. String to convert.

**Lower**( *OneColumnTable* )
**Upper**( *OneColumnTable* )
**Proper**( *OneColumnTable* )

- *OneColumnTable* - Required. A single column table of strings to convert. 

## Examples ##

### Single String ###

| Formula | Description | Result |
|---------|-------------|--------|
| **Lower(&nbsp;"E.&nbsp;E.&nbsp;CummINGS"&nbsp;)** | Converts all characters of the string to lower case. | "e. e. cummings" |
| **Upper(&nbsp;"E.&nbsp;E.&nbsp;CummINGS"&nbsp;)** | Converts all characters of the string to upper case. | "E. E. CUMMINGS" |
| **Proper(&nbsp;"E.&nbsp;E.&nbsp;CummINGS"&nbsp;)** | Converts characters of the string to proper case.  The first letter of each word is upper case, the rest are lower case. | "E. E. Cummings" |

### Single Column Table

#### People Data Source ####

| Name | Address | 
|-------|---------|
| Jean |  123 Main St. NE |
| Frank | 789 SW 39th #3B |

| Formula | Description | Result |
|---------|-------------|--------|
| **Lower( ShowColumns(&nbsp;People,&nbsp;"Address"&nbsp;) )** | Converts all characters of each string in the single column table to lower case. | <table><tr><th>Address</th></tr><td>123&nbsp;main st.&nbsp;ne</td></tr><tr><td>789&nbsp;sw&nbsp;39th&nbsp;#3b</td></tr></table> |
| **Upper( ShowColumns(&nbsp;People,&nbsp;"Address"&nbsp;) )** | Converts all characters of each string in the single column table to to upper case. | <table><tr><th>Address</th></tr><td>123&nbsp;MAIN ST.&nbsp;NE</td></tr><tr><td>789&nbsp;SW&nbsp;39th&nbsp;#3B</td></tr></table> |
| **Proper( ShowColumns(&nbsp;People,&nbsp;"Address"&nbsp;) )** | Converts characters of each string in the single column table to to proper case.  The first letter of each word is upper case, the rest are lower case. | <table><tr><th>Address</th></tr><td>123&nbsp;Main St.&nbsp;Ne</td></tr><tr><td>789&nbsp;Sw&nbsp;39th&nbsp;#3b</td></tr></table> |

## Step-by-step Example ##

<ol><li>Add an input-text control, and name it **Source**.</li><br><li>Add a label, and set its **Text** property to this function:<br>**Proper(Source!Text)**</li><br><li>Press F5, and then type **WE ARE THE BEST!** into the **Source** box.<br>The label shows **We Are The Best!**</li></ol>



