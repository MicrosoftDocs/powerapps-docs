<properties
	pageTitle="Understand delegation | Microsoft PowerApps"
	description="Use delegation to process large data sets efficiently."
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="anneta"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/25/2016"
   ms.author="gregli"/>

# Understand delegation #

PowerApps offers a powerful set of functions for filtering, sorting, and shaping data.  Filter, Lookup, Sort, Search, AddColumns, and RemoveColumns to name a few.  With these functions, you can provide your users with focused access to the information they need.  For those with a database background, this is how you create the equivalent of SQL queries.  

The key to building efficient apps is to minimize the amount of data that needs to come down to your device.  This could be only a handful of records from a sea of millions, or a single aggregate value based on thousands of records.  This results in fast response times for the app's users, even on phones connected via a wireless network.

*Delegation* is where the expressiveness of PowerApps formulas meets the need to minimize the amount of data the app needs to process.  It is short for saying "PowerApps will delegate processing to the data source."  Instead of pulling data to the app to process, we push the processing to the data source.  This dramatically reduces the processing power, memory, and network bandwidth needed by your app.

Where this becomes complicated, and the reason this article exists, is because not everything that can be expressed in PowerApps can be delegated to every data source.  Data sources vary wildly in what they support.  Also, the PowerApps language mimics Excel's formula language, designed with complete and instant access to an entire workbook in memory.  As a result, the PowerApps language is far richer than any data source can completely support, including powerful database engines such as SQL Server.  

As an author, you must take care to ensure your formulas are delegatable.  PowerApps helps you        

It is possible to create a very powerful formula that returns exactly the data that you seek.   

With PowerApps, you can build apps that work with large volumes of data efficiently.  

*Delegation* is how this is accomplished.  


What is desired is the best of both worlds.  All the power of PowerApps formulas with the ability to push the work off the local device.  

For those of you with a database background: delegation is the equivalent of running a SQL query on a SQL server.  PowerApps 

