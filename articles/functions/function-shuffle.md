<properties
	pageTitle="PowerApps: Shuffle function"
	description="Reference information for the Shuffle function in PowerApps, including syntax and examples"
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

# Shuffle function in PowerApps #

Randomly reorders the [records](working-with-tables.md#records) of a [table](working-with-tables.md).

## Description ##

The **Shuffle** function reorders the records of a table. 

**Shuffle** returns a table that has the same [columns](working-with-tables.md#columns) and number of rows as the argument. 

## Syntax ##

**Shuffle**( *Table* )

- *Table* - Required.  Table to shuffle.

## Examples ##

If you stored details about playing cards in a [collection](working-with-data-sources.md#collections) named Deck, this function would return a copy of that collection that has been randomly shuffled.

**Shuffle(Deck)**


