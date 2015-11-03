<properties
	pageTitle="PowerApps: Validate function"
	description="Reference information for the Validate function in PowerApps, including syntax and examples"
	services="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="bills"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/01/2015"
   ms.author="gregli"/>

# Validate function in PowerApps #

The **Validate** function checks if the value of a single [Column](file-name.md) or complete [Record](file-name.md) are valid for a [Data Source](file-name.md).  

## Description ##

Before submitting a data change, you can provide your users with immediate feedback on the validity of their submission, resulting in a better user experience.  

Data sources can provide information on what constitutes valid values within a record.  This can include whether a column requires a value, the maximum length of a string, the minimum value of a date, and many other constraints.  The Validate function uses this information to determine if a value is valid and to return an appropriate error message if not. You can also use the [DataSourceInfo](file-name.md) function to view much of the information used by the Validate function.

Data sources vary in how much validation information they provide, including not providing any at all.  The Validate function can only check values based on this information.  Even after checking the result of Validate, when the call is made to change a record's value, the data source may still return a validation error.  

If there is a validation problem, Validate returns an error message that is suitable for display to the user of the app.  If all values are valid, Validate returns [Blank](file-name.md).  When working with a [Collection](file-name.md), values are always valid.

## Syntax ##

**Validate**(*DataSource*, *Column*, *Value* )

- DataSource – Required. The data source to validate with.

- Column – Required. The column to validate.

- Value – Required. The value for the selected column to be validated.

**Validate**(*DataSource*, *OriginalRecord*, *Updates* )

 - DataSource – Required. The data source to validate with.

- OriginalRecord - Required.  The record to which updates are to be validated.

- Update - Required.  The changes to apply to the original record.


## Examples ##

#### Validate with a Single Column ###
| Formula                                 | Description                                                                                                                                           | Result              |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| Validate( Scores, Percentage, 10 ) | Checks if 10 is a valid value for Percentage in the Scores data source.  In this case, the value is valid and Blank is returned. | Blank |
| Validate( Scores, Percentage, 120 ) | Checks if 120 is a valid value for Percentage in the Scores data source.  In this case, it is not valid and an error message is returned.| "Values must be between 0 and 100."  |

### Validate with a Complete Record ###
| Formula                                 | Description                                                                                                                                           | Result              |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| Validate( Scores, EditRecord, Gallery!Updates ) | Checks if 10 is a valid value for Percentage in the Scores data source.  In this case, the value is valid and Blank is returned. | Blank |
| Validate( Scores, EditRecord, Gallery!Updates ) | Checks if 120 is a valid value for Percentage in the Scores data source.  In this case, it is not valid and an error message is returned.| "Values must be between 0 and 100."  |


