<properties
	pageTitle="PowerApps: Working with State"
	description="Reference information for working with state, context variables, and collections"
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
   ms.date="11/10/2015"
   ms.author="gregli"/>

# Working with State in PowerApps #

You may be asking a question: **where are the variables?**

If you are asking this question, you have probably used another programming tool in the past, such as VBA (Visual Basic for Applications) or JavaScript.  PowerApps is a little different.

When reaching for a variable, instead ask yourself: **what would I do in Excel?**  PowerApps is modeled after Excel and what works there often works in PowerApps too.  Instead of performing a calculation and placing the result in a variable, create a formula that connects controls together (the equivalent of cells in Excel) and is automatically recalculated.  Your app will be easier to create, understand, and maintain. 

There is a place for variables in PowerApps.  PowerApps extends Excel's model with [behaviors]() that execute when, for example, a button is clicked.  It is often helpful to set a variable, an author defined piece of state, to be used in other formulas.

## Background ##

PowerApps is a [functional programming](https://en.wikipedia.org/wiki/Functional_programming) tool.  It borrows heavily from the design of Excel, which is also a functional programming tool, with these benefits:
- Many people already know how to work with Excel formulas.  They can leverage those skills to build and customize a PowerApp.
- The author is relieved from manually recalculating results as user inputs, device inputs, and data sources changes.  
- It is easy to understand and predict the behavior of a program.  A formula is only dependent on its inputs and outputs.

In Excel, the [state](https://en.wikipedia.org/wiki/State_%28computer_science%29) of the workbook is held entirely in the cells of the workbook.  This is all the information that is stored and can be changed by the user.  Formulas connect the cells together, calculating one cell's value based on the values of other cells.  

In PowerApps, the state of the app is primarily held in the controls, the equivalent of cells in Excel.  As a user types a letter into an Input Text control, any formulas that depend on the **Text** property of this control are automatically recalculated.  The results of all the recalculation can be displayed in other controls on the screen.

Where PowerApps departs from Excel is the introduction of [behavior formulas](working-with-formulas.md), a form of [imperative programming](https://en.wikipedia.org/wiki/Imperative_programming).  When a button is clicked, a series of formulas can be evaluated that alter the state of the app.  Excel has no equivalent to this.






