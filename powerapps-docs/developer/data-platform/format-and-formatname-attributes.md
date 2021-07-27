---
title: "Format and FormatName columns (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about Format and FormatName columns that store the format values and are used by the controls and UI to know how to display the contents." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 07/30/2021
ms.reviewer: "nabuthuk"
ms.service: powerapps
ms.topic: "article"
author: "nkrb" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "nabuthuk" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Format and FormatName columns

Format and FormatName are the columns used to store the format values and are used by the controls and UI to know how to display the contents.

**Format** is the older column that stored the values used by Microsoft Power Platform.To maintain backward compatibility, new formats were not able to be introduced. Because of this, some of the API responses won’t align with the new format. For `Text` and `Multiline Text` columns, it is recommended to use the `FormatName` column.

**FormatName** is the new column that is used to specify the format for `Text` and `Multiline Text` column data types. `FormatName` column provides a more accurate response for the format selected and supports newer format types.

## API behavior

- On **Retrieve** operation, a data type with a defined format may provide different values for the `Format` and `FormatName` API responses based on compatibility. For example, a text column set to `RichText` format returns the following:
   
   - Format: 'Text'
   - FormatName: 'RichText'.
   - Retrieve will correct any incompatible format or formatname values
        present on a data type by changing the values to the default of the data
        type.
        -   Example: if a Text field was changed to an incompatible format of
            “Date Only” via XML, it would be reverted to the values below upon
            retrieval.
            -   Format: 'Text'
            -   FormatName: 'Text'.
- On **Create**, if the incoming payload contains both Format and FormatName properties, the system will always honor the value from FormatName. If payload contains only one value, the system will honor whatever is present in the payload.
- On **Update**, system will only honor FormatName attributes. The value of Format property is **NOT** honored even if a FormatName attribute is not present.

The following table provides the Format and FormatName values and API responses for each type:

| **Column type** | **Platform format / Value in solution XML** | **Format**   | **FormatName** | **API response value**  | **Remarks**   |
|--------------------|---------------------------------------------------|--------------|----------------|----------------------------|---------------|
| Text               | Text   | StringFormat.Text  | StringFormatName.Text | **Format**: Text <br/> **FormatName**: Text   | Default format value for String column.  |
|                    | Email   | StringFormat.Email  | StringFormatName.Email | **Format**: Email <br/> **FormatName**: Email  | |
|                    | TextArea   | StringFormat.TextArea  | StringFormatName.TextArea | **Format**: TextArea <br/> **FormatName**: TextArea   ||
|                    | URL   | StringFormat.Url  | StringFormatName.Url | **Format**: Url <br/> **FormatName**: Url   |  |
|                    | TickerSymbol   | StringFormat.TickerSymbol  | StringFormatName.TickerSymbol | **Format**: TickerSymbol <br/> **FormatName**: TickerSymbol   |   |
|                    | VersionNumber   | StringFormat.VersionNumber  | StringFormatName.VersionNumber | **Format**: VersionNumber <br/> **FormatName**: VersionNumber   | |
|                    | Phone   | StringFormat.Phone  | StringFormatName.Phone | **Format**: Text <br/> **FormatName**: Phone   |  |
|                    | Json   | StringFormat.Json  | StringFormatName.Json | **Format**: Text <br/> **FormatName**: Json   |  |
|                    | RichText   | StringFormat.RichText  | MemoFormatName.RichText | **Format**: Text <br/> **FormatName**: RichText   | Only allowed for non-SQL data provider. |
| Memo/Multiline Text    | Text   | StringFormat.Text | MemoFormatName.Text | **Format**: Text <br/> **FormatName**: Text   | Default format value for Memo/Multiline column.  |
|                    | Email   | StringFormat.Email  | MemoFormatName.Email | **Format**: Email <br/> **FormatName**: Email   |   |
|                    | TextArea   | StringFormat.TextArea  | MemoFormatName.TextArea | **Format**: TextArea <br/> **FormatName**: TextArea   |  |
|                    | InternalExtentdata   | StringFormat.Te  | StringFormatName.Text | **Format**: Text <br/> **FormatName**: Text   |  |
|                    | Json   | StringFormat.Json  | MemoFormatName.Json | **Format**: Text <br/> **FormatName**: Json   |   |
|                    | RichText   | StringFormat.RichText  | MemoFormatName.RichText | **Format**: Text <br/> **FormatName**: RichText   | Only allowed for non-SQL data provider. |
| Integer            | None/String.Empty   | IntegerFormat.None | N/A| **Format**: None    | Default format value for Integer column.  |
|                    | Duration   |IntegerFormat.Duration  | N/A | **Format**: Duration   |   |
|                    | TimeZone   | IntegerFormat.TimeZone  | N/A | **Format**: TimeZone   |  |
|                    | Language   | IntegerFormat.Language  | N/A | **Format**: Language    |   |
|                    | Locale   | IntegerFormat.Locale  | N/A | **Format**: Locale |  |
| DateTime           | DateTime  | DateTimeFormat.DateAndTime | N/A| **Format**: DateAndTime    | Default format value for DateTime column.  |

### Related articles

[Data type format conversions](data-type-format-conversions.md)

[Format Validations](format-validations.md)