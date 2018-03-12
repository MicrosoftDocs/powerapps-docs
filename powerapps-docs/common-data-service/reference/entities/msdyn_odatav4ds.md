---
title: "msdyn_odatav4ds Entity Reference (Common Data Service for Apps)| MicrosoftDocs"
description: "Includes schema information and supported messages for the msdyn_odatav4ds entity."

services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/07/2018
ms.author: jdaly
---
# msdyn_odatav4ds Entity Reference

Data sources used by the OData v4 data provider to access data from an external web service.

**Added by**: OData v4 Data Provider Solution<br />
## Entity Properties

**DisplayName**: OData v4 Data Source<br />
**DisplayCollectionName**: OData v4 Data Sources<br />
**SchemaName**: msdyn_odatav4ds<br />
**CollectionSchemaName**: msdyn_odatav4dses<br />
**LogicalName**: msdyn_odatav4ds<br />
**LogicalCollectionName**: msdyn_odatav4dses<br />
**EntitySetName**: msdyn_odatav4ds<br />
**PrimaryIdAttribute**: msdyn_odatav4dsid<br />
**PrimaryNameAttribute**: msdyn_name<br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [msdyn_description](#BKMK_msdyn_description)
- [msdyn_isparameter10header](#BKMK_msdyn_isparameter10header)
- [msdyn_isparameter1header](#BKMK_msdyn_isparameter1header)
- [msdyn_isparameter2header](#BKMK_msdyn_isparameter2header)
- [msdyn_isparameter3header](#BKMK_msdyn_isparameter3header)
- [msdyn_isparameter4header](#BKMK_msdyn_isparameter4header)
- [msdyn_isparameter5header](#BKMK_msdyn_isparameter5header)
- [msdyn_isparameter6header](#BKMK_msdyn_isparameter6header)
- [msdyn_isparameter7header](#BKMK_msdyn_isparameter7header)
- [msdyn_isparameter8header](#BKMK_msdyn_isparameter8header)
- [msdyn_isparameter9header](#BKMK_msdyn_isparameter9header)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_odatav4dsId](#BKMK_msdyn_odatav4dsId)
- [msdyn_paginationmode](#BKMK_msdyn_paginationmode)
- [msdyn_paginationtype](#BKMK_msdyn_paginationtype)
- [msdyn_parameter10name](#BKMK_msdyn_parameter10name)
- [msdyn_parameter10value](#BKMK_msdyn_parameter10value)
- [msdyn_parameter1name](#BKMK_msdyn_parameter1name)
- [msdyn_parameter1value](#BKMK_msdyn_parameter1value)
- [msdyn_parameter2name](#BKMK_msdyn_parameter2name)
- [msdyn_parameter2value](#BKMK_msdyn_parameter2value)
- [msdyn_parameter3name](#BKMK_msdyn_parameter3name)
- [msdyn_parameter3value](#BKMK_msdyn_parameter3value)
- [msdyn_parameter4name](#BKMK_msdyn_parameter4name)
- [msdyn_parameter4value](#BKMK_msdyn_parameter4value)
- [msdyn_parameter5name](#BKMK_msdyn_parameter5name)
- [msdyn_parameter5value](#BKMK_msdyn_parameter5value)
- [msdyn_parameter6name](#BKMK_msdyn_parameter6name)
- [msdyn_parameter6value](#BKMK_msdyn_parameter6value)
- [msdyn_parameter7name](#BKMK_msdyn_parameter7name)
- [msdyn_parameter7value](#BKMK_msdyn_parameter7value)
- [msdyn_parameter8name](#BKMK_msdyn_parameter8name)
- [msdyn_parameter8value](#BKMK_msdyn_parameter8value)
- [msdyn_parameter9name](#BKMK_msdyn_parameter9name)
- [msdyn_parameter9value](#BKMK_msdyn_parameter9value)
- [msdyn_returninlinecount](#BKMK_msdyn_returninlinecount)
- [msdyn_timeout](#BKMK_msdyn_timeout)
- [msdyn_uri](#BKMK_msdyn_uri)


### <a name="BKMK_msdyn_description"></a> msdyn_description

**Description**: Type additional information to describe this OData v4 data source. What environment does this data source target and what is the purpose of this system ?<br />
**DisplayName**: Description<br />
**LogicalName**: msdyn_description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_msdyn_isparameter10header"></a> msdyn_isparameter10header

**Description**: Parameter10 Type<br />
**DisplayName**: Parameter10 Type<br />
**LogicalName**: msdyn_isparameter10header<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Header
- **FalseOption Value**: 0 **Label**: Query String

**DefaultValue**: False


### <a name="BKMK_msdyn_isparameter1header"></a> msdyn_isparameter1header

**Description**: Parameter1 Type<br />
**DisplayName**: Parameter1 Type<br />
**LogicalName**: msdyn_isparameter1header<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Header
- **FalseOption Value**: 0 **Label**: Query String

**DefaultValue**: False


### <a name="BKMK_msdyn_isparameter2header"></a> msdyn_isparameter2header

**Description**: Parameter2 Type<br />
**DisplayName**: Parameter2 Type<br />
**LogicalName**: msdyn_isparameter2header<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Header
- **FalseOption Value**: 0 **Label**: Query String

**DefaultValue**: False


### <a name="BKMK_msdyn_isparameter3header"></a> msdyn_isparameter3header

**Description**: Parameter3 Type<br />
**DisplayName**: Parameter3 Type<br />
**LogicalName**: msdyn_isparameter3header<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Header
- **FalseOption Value**: 0 **Label**: Query String

**DefaultValue**: False


### <a name="BKMK_msdyn_isparameter4header"></a> msdyn_isparameter4header

**Description**: Parameter4 Type<br />
**DisplayName**: Parameter4 Type<br />
**LogicalName**: msdyn_isparameter4header<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Header
- **FalseOption Value**: 0 **Label**: Query String

**DefaultValue**: False


### <a name="BKMK_msdyn_isparameter5header"></a> msdyn_isparameter5header

**Description**: Parameter5 Type<br />
**DisplayName**: Parameter5 Type<br />
**LogicalName**: msdyn_isparameter5header<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Header
- **FalseOption Value**: 0 **Label**: Query String

**DefaultValue**: False


### <a name="BKMK_msdyn_isparameter6header"></a> msdyn_isparameter6header

**Description**: Parameter6 Type<br />
**DisplayName**: Parameter6 Type<br />
**LogicalName**: msdyn_isparameter6header<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Header
- **FalseOption Value**: 0 **Label**: Query String

**DefaultValue**: False


### <a name="BKMK_msdyn_isparameter7header"></a> msdyn_isparameter7header

**Description**: Parameter7 Type<br />
**DisplayName**: Parameter7 Type<br />
**LogicalName**: msdyn_isparameter7header<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Header
- **FalseOption Value**: 0 **Label**: Query String

**DefaultValue**: False


### <a name="BKMK_msdyn_isparameter8header"></a> msdyn_isparameter8header

**Description**: Parameter8 Type<br />
**DisplayName**: Parameter8 Type<br />
**LogicalName**: msdyn_isparameter8header<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Header
- **FalseOption Value**: 0 **Label**: Query String

**DefaultValue**: False


### <a name="BKMK_msdyn_isparameter9header"></a> msdyn_isparameter9header

**Description**: Parameter9 Type<br />
**DisplayName**: Parameter9 Type<br />
**LogicalName**: msdyn_isparameter9header<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Header
- **FalseOption Value**: 0 **Label**: Query String

**DefaultValue**: False


### <a name="BKMK_msdyn_name"></a> msdyn_name

**Description**: Name of the OData v4 data source. This name appears in the data source drop-down list when creating a new entity.<br />
**DisplayName**: Name<br />
**LogicalName**: msdyn_name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_msdyn_odatav4dsId"></a> msdyn_odatav4dsId

**Description**: Unique identifier for entity instances<br />
**DisplayName**: OData v4 Data Source<br />
**LogicalName**: msdyn_odatav4dsid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_msdyn_paginationmode"></a> msdyn_paginationmode

**Description**: <br />
**DisplayName**: Pagination Mode<br />
**LogicalName**: msdyn_paginationmode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Server-side Paging
- **FalseOption Value**: 0 **Label**: Client-side Paging

**DefaultValue**: False


### <a name="BKMK_msdyn_paginationtype"></a> msdyn_paginationtype

**Description**: <br />
**DisplayName**: Pagination Mode<br />
**LogicalName**: msdyn_paginationtype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Client-side Paging
- **Value**: 1 **Label**: Server-side Paging



### <a name="BKMK_msdyn_parameter10name"></a> msdyn_parameter10name

**Description**: <br />
**DisplayName**: parameter10name<br />
**LogicalName**: msdyn_parameter10name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_msdyn_parameter10value"></a> msdyn_parameter10value

**Description**: <br />
**DisplayName**: parameter10value<br />
**LogicalName**: msdyn_parameter10value<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_msdyn_parameter1name"></a> msdyn_parameter1name

**Description**: <br />
**DisplayName**: parameter1name<br />
**LogicalName**: msdyn_parameter1name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_msdyn_parameter1value"></a> msdyn_parameter1value

**Description**: <br />
**DisplayName**: parameter1value<br />
**LogicalName**: msdyn_parameter1value<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_msdyn_parameter2name"></a> msdyn_parameter2name

**Description**: <br />
**DisplayName**: parameter2name<br />
**LogicalName**: msdyn_parameter2name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_msdyn_parameter2value"></a> msdyn_parameter2value

**Description**: <br />
**DisplayName**: parameter2value<br />
**LogicalName**: msdyn_parameter2value<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_msdyn_parameter3name"></a> msdyn_parameter3name

**Description**: <br />
**DisplayName**: parameter3name<br />
**LogicalName**: msdyn_parameter3name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_msdyn_parameter3value"></a> msdyn_parameter3value

**Description**: <br />
**DisplayName**: parameter3value<br />
**LogicalName**: msdyn_parameter3value<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_msdyn_parameter4name"></a> msdyn_parameter4name

**Description**: <br />
**DisplayName**: parameter4name<br />
**LogicalName**: msdyn_parameter4name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_msdyn_parameter4value"></a> msdyn_parameter4value

**Description**: <br />
**DisplayName**: parameter4value<br />
**LogicalName**: msdyn_parameter4value<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_msdyn_parameter5name"></a> msdyn_parameter5name

**Description**: <br />
**DisplayName**: parameter5name<br />
**LogicalName**: msdyn_parameter5name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_msdyn_parameter5value"></a> msdyn_parameter5value

**Description**: <br />
**DisplayName**: parameter5value<br />
**LogicalName**: msdyn_parameter5value<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_msdyn_parameter6name"></a> msdyn_parameter6name

**Description**: <br />
**DisplayName**: parameter6name<br />
**LogicalName**: msdyn_parameter6name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_msdyn_parameter6value"></a> msdyn_parameter6value

**Description**: <br />
**DisplayName**: parameter6value<br />
**LogicalName**: msdyn_parameter6value<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_msdyn_parameter7name"></a> msdyn_parameter7name

**Description**: <br />
**DisplayName**: parameter7name<br />
**LogicalName**: msdyn_parameter7name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_msdyn_parameter7value"></a> msdyn_parameter7value

**Description**: <br />
**DisplayName**: parameter7value<br />
**LogicalName**: msdyn_parameter7value<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_msdyn_parameter8name"></a> msdyn_parameter8name

**Description**: <br />
**DisplayName**: parameter8name<br />
**LogicalName**: msdyn_parameter8name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_msdyn_parameter8value"></a> msdyn_parameter8value

**Description**: <br />
**DisplayName**: parameter8value<br />
**LogicalName**: msdyn_parameter8value<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_msdyn_parameter9name"></a> msdyn_parameter9name

**Description**: <br />
**DisplayName**: parameter9name<br />
**LogicalName**: msdyn_parameter9name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_msdyn_parameter9value"></a> msdyn_parameter9value

**Description**: <br />
**DisplayName**: parameter9value<br />
**LogicalName**: msdyn_parameter9value<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_msdyn_returninlinecount"></a> msdyn_returninlinecount

**Description**: <br />
**DisplayName**: Return Inline Count<br />
**LogicalName**: msdyn_returninlinecount<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: True
- **FalseOption Value**: 0 **Label**: False

**DefaultValue**: True


### <a name="BKMK_msdyn_timeout"></a> msdyn_timeout

**Description**: Amount of time to wait, in seconds, before timing out an OData v4 request.<br />
**DisplayName**: Timeout<br />
**LogicalName**: msdyn_timeout<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 120<br />
**MinValue**: 0


### <a name="BKMK_msdyn_uri"></a> msdyn_uri

**Description**: URL of the OData v4 web service endpoint this data source will target.<br />
**DisplayName**: URL<br />
**LogicalName**: msdyn_uri<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


msdyn_odatav4ds

