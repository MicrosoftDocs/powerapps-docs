<properties
	pageTitle="PowerApps: Validate function"
	description="Reference information for the Validate function in PowerApps, including syntax and examples"
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
   ms.date="11/01/2015"
   ms.author="gregli"/>

# Validate function in PowerApps #

The **Validate** function checks whether the value of a single [Column](file-name.md) or a complete [Record](file-name.md) is valid for a [Data Source](file-name.md).  

## Description ##

Before a user submits a data change, you can provide immediate feedback on the validity of that submission, resulting in a better user experience.

Data sources can provide information on what constitutes valid values within a record.  This information can include whether a column requires a value, the maximum length of a string, the minimum value of a date, and many other constraints.  The Validate function uses this information to determine whether a value is valid and to return an appropriate error message if not. You can also use the [DataSourceInfo](file-name.md) function to view much of the information that the Validate function uses.

Data sources vary in how much validation information they provide, including not providing any at all.  The Validate function can only verify values based on this information.  Even if the Validate function does not find a problem, applying the data change could still fail. You can use the Errors function to show information about the failure. 

If the Validate function finds a problem, the function returns an error message that you can show to the user of the app.  If all values are valid, Validate returns [Blank](file-name.md).  When working with a [Collection](file-name.md), values are always valid.

## Syntax ##

**Validate**( *DataSource*, *Column*, *Value* )

- *DataSource* – Required. The data source to validate with.

- *Column* – Required. The column to validate.

- *Value* – Required. The value for the selected column to be validated.

**Validate**( *DataSource*, *OriginalRecord*, *Updates* )

 - *DataSource* – Required. The data source to validate with.

- *OriginalRecord* - Required.  The record to which updates are to be validated.

- *Update* - Required.  The changes to apply to the original record.


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


