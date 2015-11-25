<properties
	pageTitle="PowerApps: Lower, Upper, and Proper functions"
	description="Reference information for the Lower, Upper, and Proper functions in PowerApps, including syntax and examples"
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
   ms.date="11/07/2015"
   ms.author="gregli"/>

# Lower, Upper, and Proper functions in PowerApps #

Converts letters in a string of text to all lowercase, all uppercase, or proper case.

## Description ##

The **Lower**, **Upper**, and **Proper** functions convert the case of letters in strings.

- **Lower** converts any uppercase letters to lowercase.
- **Upper** converts any lowercase letters to uppercase.
- **Proper** converts the first letter in each word to uppercase if it's lowercase and converts any other uppercase letters to lowercase.

All three functions ignore characters that aren't letters.

If you pass a single string, the return value is the converted version of that string.  If you pass a single-column [table](working-with-tables.md) that contains strings, the return value is a single-column table of converted strings. If you have a multi-column table, you can shape it into a single-column table, as [working with tables](working-with-tables.md) describes.

## Syntax ##

**Lower**( *String* )<br>**Upper**( *String* )<br>**Proper**( *String* )

- *String* - Required. The string to convert.

**Lower**( *SingleColumnTable* )<br>**Upper**( *SingleColumnTable* )<br>**Proper**( *SingleColumnTable* )

- *SingleColumnTable* - Required. A single-column table of strings to convert.

## Examples ##

### Single string ###
The examples in this section use an input-text control, named **Author**, as their [data source](working-with-data-sources.md). The control contains the string **E. E. CummINGS**.

| Formula | Description | Result |
|---------|-------------|--------|
| **Lower(&nbsp;Author!Text&nbsp;)** | Converts any uppercase letters in the string to lowercase. | "e. e. cummings" |
| **Upper(&nbsp;Author!Text&nbsp;)** | Converts any lowercase letters in the string to uppercase. | "E. E. CUMMINGS" |
| **Proper(&nbsp;Author!Text&nbsp;)** | Converts the first letter of each word to uppercase if it's lowercase, and converts any other uppercase letters to lowercase. | "E. E. Cummings" |

### Single-column table
The examples in this section use this data source, named **People**:

![](media/function-lower-upper-proper/people-table.png)

| Formula | Description | Result |
|---------|-------------|--------|
| **Lower( ShowColumns(&nbsp;People,&nbsp;"Address"&nbsp;) )** |  In the **Address** [column](working-with-tables.md#columns) of the **People** table:<br><ul><li>Converts any letter that's lowercase to uppercase.</li><li>Returns a single-column table that contains the converted strings.</li> | ![](media/function-lower-upper-proper/people-table-lower.png) |
| **Upper( ShowColumns(&nbsp;People,&nbsp;"Address"&nbsp;) )** | In the **Address** column of the **People** table:<br><ul><li>Converts any letter that's lowercase to uppercase.</li><li>Returns a single-column table that contains the converted strings.</li> | ![](media/function-lower-upper-proper/people-table-upper.png) |
| **Proper( ShowColumns(&nbsp;People,&nbsp;"Address"&nbsp;) )** | In the **Address** column of the **People** table:<br><ul><li>Converts any first letter of a word that's lowercase to uppercase.</li><li>Converts any other letter that's uppercase to lowercase.</li><li>Returns a single-column table that contains the converted strings.</li> | ![](media/function-lower-upper-proper/people-table-proper.png) |

### Step-by-step example ###

1. Add an input-text control, and name it **Source**.

1. Add a label, and set its **Text** property to this function:<br>**Proper(Source!Text)**

1. Press F5, and then type **WE ARE THE BEST!** into the **Source** box.<br>The label shows **We Are The Best!**
