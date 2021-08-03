---
title: "RDL sandboxing  | MicrosoftDocs"
description: Learn about RDL sandboxing that may affect SSRS reports in Power Apps.
ms.custom: 
ms.date: 09/30/2017
ms.reviewer: 
ms.service: powerapps
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: conceptual
applies_to: 
  - Dynamics 365 for Customer Engagement (online)
ms.assetid: 8ec72014-9f0c-4964-ac67-24419b054e91
caps.latest.revision: 13
author: Mattp123
ms.subservice: mda-maker
ms.author: matp
manager: annbe
tags: 
  - MigrationHO
search.audienceType: 
  - customizer
search.app: 
  - D365CE
---
# RDL sandboxing 

In Microsoft Dataverse, reports run in the sandbox mode. This is done by enabling Report Definition Language (RDL) Sandboxing in SQL Server Reporting Services. The RDL Sandboxing lets you detect and restrict the usage of specific types of resources. As a result, certain features in Power Apps model-driven apps may not be available.  
  
The current RDL Sandboxing configuration settings in Dataverse are described in the following sections in this article.  
    
<a name="BKMK_Max"></a>   
## Limits of the array result length and string result length

The maximum number of items allowed in an array return value for an RDL expression is increased from 250 to 102400. The maximum number of items allowed in a string return value for an RDL expression is also increased from 250 to 102400. This enables you to include images and logos with sizes up to 75 KB, which will be stored in a database with Base64 encoding.  
  
 The MaxResourceSize is set to 2000. This lets you include external images in a report up to 1500 KB in size. More information: [TechNet: Add an External Image (Report Builder and SSRS)](/sql/reporting-services/report-design/add-an-external-image-report-builder-and-ssrs)  
  
<a name="BKMK_Allowed"></a>   
## Allowed types and denied members

 The RDL Sandboxing feature enables you to create a list of approved types and a list of denied members. The list of approved types is called an allowlist. The list of denied members that are not permitted in the RDL expressions is called a blocklist.  
  
 The following table contains a list of allowed types and denied members available in sandbox mode in Dataverse.  
  
|Allowed Types|Denied Members|  
|-------------------|--------------------|  
|`System.Array`|CreateInstance|  
||Finalize|  
||GetType|  
||MemberwiseClone|  
||Resize|  
|||  
|`System.DateTime`|FromBinary|  
||GetDateTimeFormats|  
||GreaterThan|  
||GreaterThanOrEqual|  
|||  
|||  
|`System.Object`|GetType|  
||MemberwiseClone|  
||ReferenceEquals|  
|||  
|`System.DbNull`|Finalize|  
||MemberwiseClone|  
||GetObjectData|  
||GetTypeCode|  
|||  
|`System.Math`|BigMul|  
||DivRem|  
||IEEERemainder|  
||E|  
||PI|  
||Pow|  
|`System.String`||  
|`System.TimeSpan`|Hours|  
||TicksPerDay|  
||TicksPerHour|  
||TicksPerMillisecond|  
||TicksPerMinute|  
||TicksPerSecond|  
||Zero|  
||TryParse|  
||TryParseExact|  
|`System.Convert`|ChangeType|  
||IConvertible.ToBoolean|  
||IConvertible.ToByte|  
||IConvertible.ToChar|  
||IConvertible.ToDateTime|  
||IConvertible.ToDecimal|  
||IConvertible.ToDouble|  
||IConvertible.ToInt16|  
||IConvertible.ToInt32|  
||IConvertible.ToInt64|  
||IConvertible.ToSByte|  
||IConvertible.ToSingle|  
||IConvertible.ToType|  
||IConvertible.ToUInt16|  
||IConvertible.ToUInt32|  
||IConvertible.ToUInt64|  
|`System.StringComparer`|Create|  
||Finalize|  
|||  
|`System.TimeZone`|Finalize|  
||GetType|  
||MemberwiseClone|  
|||  
|`System.Uri`|Unescape|  
||Parse|  
||Escape|  
||Finalize|  
|||  
|`System.UriBuilder`|Finalize|  
|||  
|`System.Globalization.CultureInfo`|ClearCachedData|  
|||  
|`System.Text.RegularExpressions.Match`|Empty|  
||NextMatch|  
||Result|  
||Synchronized|  
|||  
|||  
|`System.Text.RegularExpressions.Regex`|CacheSize|  
||CompileToAssembly|  
||GetGroupNames|  
||GetGroupNumbers|  
||GetHashCode|  
||Unescape|  
||UseOptionC|  
||UseOptionR|  
||capnames|  
||caps|  
||capsize|  
||capslist|  
||roptions|  
||pattern|  
||factory|  
||IsMatch|  
||Matches|  
||Iserializable.GetObjectData|  
||InitializeReferences|  
||RightToLeft|  
||Options|  
|||  
|||  
|`Microsoft.VisualBasic.Constants`|vbAbort|  
||vbAbortRetryIgnore|  
||vbApplicationModal|  
||vbArchive|  
||vbBinaryCompare|  
||vbCancel|  
||vbCritical|  
||vbDefaultButton1|  
||vbDefaultButton2|  
||vbDefaultButton3|  
||vbExclamation|  
||vbFormFeed|  
||vbGet|  
||vbHidden|  
||vbHide|  
||vbHiragana|  
||vbIgnore|  
||vbInformation|  
||vbKatakana|  
||vbLet|  
||vbLinguisticCasing|  
||vbMaximizedFocus|  
||vbMinimizedFocus|  
||vbMinimizedNoFocus|  
||vbMsgBoxHelp|  
||vbMsgBoxRight|  
||vbMsgBoxRtlReading|  
||vbMsgBoxSetForeground|  
||vbNo|  
||vbNormal|  
||vbNormalFocus|  
||vbNormalNoFocus|  
||vbObjectError|  
||vbOK|  
||vbOKCancel|  
||vbOKOnly|  
||vbQuestion|  
||vbReadOnly|  
||vbRetry|  
||vbRetryCancel|  
||vbSet|  
||vbSystem|  
||vbSystemModal|  
||VbTypeName|  
||vbVolume|  
||Zero|  
|`Microsoft.VisualBasic.ControlChars`|Finalize|  
||GetType|  
||MemberwiseClone|  
|||  
|`Microsoft.VisualBasic.Conversion`|Err|  
||ErrorToString|  
||Fix|  
|||  
|`Microsoft.VisualBasic.DateInterval`|Finalize|  
||GetType|  
||MemberwiseClone|  
|||  
|`Microsoft.VisualBasic.Financial`|Finalize|  
||GetType|  
||MemberwiseClone|  
||IRR|  
||NPV|  
||MIRR|  
|||  
|||  
|`Microsoft.VisualBasic.Interaction`|AppActivate|  
||Beep|  
||CallByName|  
||Command|  
||CreateObject|  
||Environ|  
||Finalize|  
||GetAllSettings|  
||GetObject|  
||GetSetting|  
||GetType|  
||InputBox|  
||MemberwiseClone|  
||MsgBox|  
||SaveSetting|  
||Shell|  
||Choose|  
||Switch|  
|||  
|||  
|`Microsoft.VisualBasic.Information`|Erl|  
||Err|  
||IsError|  
||IsDBNull|  
||Lbound|  
||Ubound|  
||SystemTypeName|  
|||  
|`Microsoft.VisualBasic.Strings`|Finalize|  
||GetType|  
||MemberwiseClone|  
||Lset|  
||Rset|  
|||  
|`Microsoft.Crm.Reporting.RdlHelper`||  
  
<a name="BKMK_Denied"></a>   
## Common denied members  
 The following table contains a list of denied members common in allowed types:  
  
|Denied member|  
|-|  
|DateString|  
|Duration|  
|Equality|  
|Equals|  
|Erl|  
|Filter|  
|GetChar|  
|GroupNameFromNumber|  
|GroupNumberFromName|  
|Int|  
|MaxValue|  
|MinValue|  
|Negate|  
|Timer|  
|TimeString|  
|ToBinary|  
|Finalize|  
|GetType|  
|MemberwiseClone|  
  

[!INCLUDE[footer-include](../../includes/footer-banner.md)]