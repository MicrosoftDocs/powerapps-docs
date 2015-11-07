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
   ms.date="11/07/2015"
   ms.author="gregli"/>

# Lower, Upper, and Proper functions in PowerApps #

Converts letters in a string of text to all lowercase, all uppercase, or proper case.

## Description ##

The **Lower**, **Upper**, and **Proper** functions convert the case of letters in strings.
- **Lower** converts any uppercase letters to lowercase.
- **Upper** converts any lowercase letters to uppercase.
- **Proper** converts the first letter in each word to uppercase if it's lowercase and any other uppercase letters to lowercase.

All three functions ignore characters that aren't letters.

If you [pass](file-name.md) a single string, the [return value](file-name.md) is the converted version of that string.  If you pass a single-column table that contains strings, the return value is a single-column table of converted strings. If you have a multi-column [data source](file-name.md), you can shape it into a single-column table, as [Working with Tables](file-name.md) describes.

## Syntax ##

**Lower**( *String* )<br>**Upper**( *String* )<br>**Proper**( *String* )

- *String* - Required. The string to convert.

**Lower**( *SingleColumnTable* )<br>**Upper**( *SingleColumnTable* )<br>**Proper**( *SingleColumnTable* )

- *SingleColumnTable* - Required. A single-column table of strings to convert.

## Examples ##

### Single string ###
The examples in this section use an input-text control, named **Author**, as their data source. The control contains the string **E. E. CummINGS**.

| Formula | Description | Result |
|---------|-------------|--------|
| **Lower(&nbsp;Author!Text&nbsp;)** | Converts any uppercase letters in the string to lowercase. | "e. e. cummings" |
| **Upper(&nbsp;Author!Text&nbsp;)** | Converts any lowercase letters in the string to uppercase. | "E. E. CUMMINGS" |
| **Proper(&nbsp;Author!Text&nbsp;)** | Converts the first letter of each word to uppercase if it's lowercase, and converts any other uppercase letters to lowercase. | "E. E. Cummings" |

### Single-column table
The examples in this section use this table, named **People**, as their data source:

| Name  | Address |
|-------|---------|
| Jean  | 123 Main St. NE |
| Frank | 789 SW 39th #3B |

| Formula | Description | Result |
|---------|-------------|--------|
| **Lower( ShowColumns(&nbsp;People,&nbsp;"Address"&nbsp;) )** |  In the **Address** column of the **People** table:<br><ul><li>Converts any letter that's lowercase to uppercase.</li><li>Returns a single-column table that contains the converted strings.</li> | <table><tr><th>Address</th></tr><td>123&nbsp;main st.&nbsp;ne</td></tr><tr><td>789&nbsp;sw&nbsp;39th&nbsp;#3b</td></tr></table> |
| **Upper( ShowColumns(&nbsp;People,&nbsp;"Address"&nbsp;) )** | In the **Address** column of the **People** table:<br><ul><li>Converts any letter that's lowercase to uppercase.</li><li>Returns a single-column table that contains the converted strings.</li> | <table><tr><th>Address</th></tr><td>123&nbsp;MAIN ST.&nbsp;NE</td></tr><tr><td>789&nbsp;SW&nbsp;39th&nbsp;#3B</td></tr></table> |
| **Proper( ShowColumns(&nbsp;People,&nbsp;"Address"&nbsp;) )** | In the **Address** column of the **People** table:<br><ul><li>Converts any first letter of a word that's lowercase to uppercase.</li><li>Converts any other letter that's uppercase to lowercase.</li><li>Returns a single-column table that contains the converted strings.</li> | <table><tr><th>Address</th></tr><td>123&nbsp;Main St.&nbsp;Ne</td></tr><tr><td>789&nbsp;Sw&nbsp;39th&nbsp;#3b</td></tr></table> |

### Step-by-step example ###

<ol><li>Add an input-text control, and name it **Source**.</li><br><li>Add a label, and set its **Text** property to this function:<br>**Proper(Source!Text)**</li><br><li>Press F5, and then type **WE ARE THE BEST!** into the **Source** box.<br>The label shows **We Are The Best!**</li></ol>
