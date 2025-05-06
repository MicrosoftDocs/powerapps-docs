---
title: "Asynchronous service (Microsoft Dataverse) | Microsoft Docs"
description: "Learn about the asynchronous service that manages system jobs."
ms.date: 01/05/2024
ms.reviewer: pehecke
ms.topic: article
author: swylezol
ms.subservice: dataverse-developer
ms.author: swylezol 
search.audienceType: 
  - developer
contributors:
  - PHecke
  - JimDaly
---
# Asynchronous service

The asynchronous service executes long-running operations independent of the main Microsoft Dataverse core operation. Executing long-running operations this way results in improved overall system performance and improved scalability. The asynchronous service is a managed first-in, first-out (FIFO) queue for the execution of asynchronous registered plug-ins, workflows, and operations such as bulk mail, bulk import, and campaign activity propagation. These operations are registered with the asynchronous service and executed periodically when the service processes its queue.

After an event occurs and any synchronous extensions are processed, Dataverse serializes the context for any asynchronous extensions and saves it in the [System Job (AsyncOperation) table](reference/entities/asyncoperation.md). The system job defines and tracks the execution of the asynchronous operation. As resources become available, Dataverse processes system jobs and executes the operations they define. Dataverse processes any data operations defined in the extension again in the event execution pipeline, but this time as a synchronous operation.

## Execution order and dependencies

System jobs are evaluated as a queue using the [CreatedOn](reference/entities/asyncoperation.md#BKMK_CreatedOn) date. If there are no conditions to defer execution, they're executed as soon as resources are available. Execution isn't always performed in the order set by the `CreatedOn` date because different types of operations require different resources.

A system job can be dependent on another system job so that it will begin only after the other system job completes. The [DependencyToken](reference/entities/asyncoperation.md#BKMK_DependencyToken) column value establishes this dependency when a system job is created. If the `DependencyToken` value is null, the system job has no dependencies. Dependent system jobs have the same `DependencyToken` value and are executed in the order they were created. If a system job is postponed, all subsequent dependent system jobs continue to wait until the postponed system job executes.

> [!NOTE]
> This dependency system cannot be used by plug-ins registered to run asynchronously because the system jobs for them are created by the system.

## Managing system jobs

You can perform the following operations to manage system jobs using the [AsyncOperation Table](reference/entities/asyncoperation.md).

- Retrieve system jobs
- Delete system jobs
- Manage system job states
- Postpone system jobs

> [!NOTE]
> Creating system jobs with code is not supported. Although the `AsyncOperation` table supports several writeable columns and create operations, only the following columns are supported for update:
> - [StateCode](reference/entities/asyncoperation.md#BKMK_StateCode)
> - [StatusCode](reference/entities/asyncoperation.md#BKMK_StatusCode)
> - [PostPoneUntil](reference/entities/asyncoperation.md#BKMK_PostponeUntil)

## Retrieve system jobs

You can view system jobs in the application by navigating to **Settings** > **System** > **System Jobs** and you can also search them using [Advanced find in model-driven apps](../../user/advanced-find.md).

Using code, you can retrieve system jobs like any other table. The following table lists selected columns that are important in understanding system jobs:

|**Column**|**Description**|
|--|--|
|`AsyncOperationId`|Unique identifier of the system job.|
|`CompletedOn`|Date and time when the system job was completed.|
|`CreatedBy`|Unique identifier of the user who created the system job.|
|`CreatedOn`|Date and time when the system job was created.|
|`Data`|Unstructured data associated with the system job.|
|`DependencyToken`|Execution of all operations with the same dependency token is serialized. [Learn about execution order and dependencies](#execution-order-and-dependencies) |
|`Depth`|Number of SDK calls made since the first call.|
|`ErrorCode`|Error code returned from a canceled system job.|
|`ExecutionTimeSpan`|Time that the system job took to execute.|
|`FriendlyMessage`|Message provided by the system job.|
|`IsWaitingForEvent`|Indicates that the system job is waiting for an event.|
|`Message`|Message related to the system job.|
|`MessageName`|Name of the message that started this system job.|
|`ModifiedBy`|Unique identifier of the user who last modified the system job.|
|`ModifiedOn`|Date and time when the system job was last modified.|
|`Name`|Name of the system job.|
|`OperationType`|Type of the system job. [Learn about operation types](#operation-types)|
|`OwnerId`|Unique identifier of the user or team who owns the system job.|
|`OwningBusinessUnit`|Unique identifier of the business unit that owns the system job.|
|`OwningExtensionId`|Unique identifier of the owning extension with which the system job is associated.|
|`OwningTeam`|Unique identifier of the team who owns the record.|
|`OwningUser`|Unique identifier of the user who owns the record.|
|`PostponeUntil`|Indicates whether the system job should run only after the specified date and time. [Learn to postpone system jobs](#postpone-system-jobs)|
|`PrimaryEntityType`|Type of table with which the system job is primarily associated.|
|`RecurrencePattern`|Pattern of the system job's recurrence. [Learn about recurrence start times and patterns](#recurrence-start-times-and-patterns)|
|`RecurrenceStartTime`|Starting time in UTC for the recurrence pattern. [Learn about recurrence start times and patterns](#recurrence-start-times-and-patterns)|
|`RegardingObjectId`|Unique identifier of the object with which the system job is associated.|
|`RetryCount`|Number of times to retry the system job.|
|`Sequence` |Order in which operations were submitted.|
|`StartedOn`|Date and time when the system job was started.|
|`StateCode`|Status of the system job. [Learn to manage system job states](#manage-system-job-states)|
|`StatusCode`|Reason for the status of the system job. [Learn to manage system job states](#manage-system-job-states)|
|`UTCConversionTimeZoneCode` |Time zone code that was in use when the record was created.|
|`WorkflowStageName` |Name of a workflow stage. |

### Examples

You can use the following examples to retrieve System Job data.

#### [Web API](#tab/webapi)

Use the following Web API Query to retrieve the columns in the table above. [Learn how to query data using the Web API](webapi/query/overview.md

```http
GET <organization URL>/api/data/v9.2/asyncoperations?$top=1000
&$select=
asyncoperationid,
completedon,
createdon,
data,
dependencytoken,
depth,
errorcode,
executiontimespan,
friendlymessage,
iswaitingforevent,
message,
messagename,
modifiedon,
name,
operationtype,
_ownerid_value,
postponeuntil,
primaryentitytype,
recurrencepattern,
recurrencestarttime,
_regardingobjectid_value,
retrycount,
sequence,
startedon,
statecode,
utcconversiontimezonecode,
workflowstagename
&$expand=
createdby($select=fullname),
modifiedby($select=fullname),
owningbusinessunit($select=name),
owningextensionid($select=name),
owningteam($select=name),
owninguser($select=fullname)
```

> [!NOTE]
> With the Web API there is a single-valued navigation property for each table that supports system jobs. The name of this navigation property follows the pattern `regardingobjectid_<table logical name>`.

#### [FetchXml](#tab/fetchxml)

Use the following FetchXML to retrieve the columns in the table above. [Query data using FetchXml](fetchxml/overview.md)

```xml
<fetch top='1000'>
  <entity name='asyncoperation' >
    <attribute name='asyncoperationid' />
    <attribute name='completedon' />
    <attribute name='createdby' />
    <attribute name='createdon' />
    <attribute name='data' />
    <attribute name='dependencytoken' />
    <attribute name='depth' />
    <attribute name='errorcode' />
    <attribute name='executiontimespan' />
    <attribute name='friendlymessage' />
    <attribute name='iswaitingforevent' />
    <attribute name='message' />
    <attribute name='messagename' />
    <attribute name='modifiedby' />
    <attribute name='modifiedon' />
    <attribute name='name' />
    <attribute name='operationtype' />
    <attribute name='ownerid' />
    <attribute name='owningbusinessunit' />
    <attribute name='owningextensionid' />
    <attribute name='owningteam' />
    <attribute name='owninguser' />
    <attribute name='postponeuntil' />
    <attribute name='primaryentitytype' />
    <attribute name='recurrencepattern' />
    <attribute name='recurrencestarttime' />
    <attribute name='regardingobjectid' />
    <attribute name='retrycount' />
    <attribute name='sequence' />
    <attribute name='startedon' />
    <attribute name='statecode' />
    <attribute name='utcconversiontimezonecode' />
    <attribute name='workflowstagename' />
  </entity>
</fetch>
```

> [!NOTE]
> Every table that supports system jobs has a listed Many-to-One relationship with the `AsyncOperation` table via the [`RegardingObjectId` lookup column](reference/entities/asyncoperation.md#BKMK_RegardingObjectId). The name of this relationship follows the pattern `<table schema name>_AsyncOperations`.****

#### [SQL](#tab/sql)

You can use SQL to query the `AsyncOperation` table using the [Dataverse Tabular Data Stream (TDS) endpoint](dataverse-sql-query.md) when enabled.

```sql
SELECT TOP (1000) asyncoperationid
      ,completedon
      ,createdon
      ,data
      ,dependencytoken
      ,depth
      ,errorcode
      ,executiontimespan
      ,friendlymessage
      ,iswaitingforevent
      ,message
      ,messagename
      ,modifiedon
      ,name
      ,operationtype
      ,operationtypename
      ,ownerid
      ,postponeuntil
      ,recurrencepattern
      ,recurrencestarttime
      ,regardingobjectid
      ,regardingobjectidname
      ,retrycount
      ,sequence
      ,startedon
      ,statecode
      ,utcconversiontimezonecode
      ,workflowstagename
  FROM asyncoperation
```

---

### Operation types

The [OperationType](reference/entities/asyncoperation.md#BKMK_OperationType) column describes categories of system jobs. Dataverse initiates many of these types to perform maintenance tasks.

> [!NOTE]
> You cannot perform cancel, pause, or resume operations on system jobs generated by the platform.

Some of the types of these platform generated jobs are included in the following table:

|**OperationType Value**|**OperationType Label**|
|--|--|
|9|SQM Data Collection|
|16|Collect Organization Statistics|
|18|Calculate Organization Storage Size|
|19|Collect Organization Database Statistics|
|20|Collection Organization Size Statistics|
|22 |Calculate Organization Maximum Storage Size|
|24|Update Statistic Intervals|
|25 |Organization Full Text Catalog Index|
|27|Update Contract States|
|31|Storage Limit Notification|

For a complete list, see [OperationType Choices/Options](reference/entities/asyncoperation.md#operationtype-choicesoptions)

### Recurrence start times and patterns

Recurring system jobs require information about when they should start and how often to recur. These values are stored in the `AsyncOperation` table `RecurrenceStartTime` and `RecurrencePattern` columns.

Because you can't create `AsyncOperation` records directly with code, you need to interpret these values when you query the data. These property values are set indirectly by using messages that create new system jobs. The `BulkDelete` and `BulkDeleteDuplicates` messages both include parameters or properties in the corresponding Web API actions or SDK for .NET request classes. More information: <xref:Microsoft.Crm.Sdk.Messages.BulkDetectDuplicatesRequest> Class, [BulkDetectDuplicates Action](xref:Microsoft.Dynamics.CRM.BulkDetectDuplicates), <xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest> Class, and [BulkDelete Action](xref:Microsoft.Dynamics.CRM.BulkDelete)

The `RecurrenceStartTime` is simply a datetime value to indicate when the system job should start. If it isn't set, the system job was expected to start immediately.

The `RecurrencePattern` column stores information about how frequently recurring system jobs occur. The platform sometimes sets this value when a new asyncoperation record is created. You can set this value to change the pattern.

The values for this column use parts of the [RFC2445 Internet standard (Internet Calendaring and Scheduling Core Object Specification)](https://www.rfc-editor.org/info/rfc2445).

The following table provides from examples:

|Recurrence pattern|Frequency of job execution|
|--|--|
|`FREQ=MONTHLY;`|Once a month|
|`FREQ=WEEKLY;`|Once a week|
|`FREQ=DAILY;`|Once a day|
|`FREQ=DAILY;INTERVAL=3;`|Every three days|
|`FREQ=HOURLY;`|Once an hour|

If an `INTERVAL` value isn't set, it's interpreted as `1`.

## Diagnostic queries

Use the queries in this section to help diagnose problems.

### Jobs by state, status, and type


Use this query to understand the distribution and frequency of different types of jobs. The results might tell you which jobs are causing a problem.


#### [Web API](#tab/webapi)

This query doesn't order by `count` descending. You may want to use FetchXml with Web API instead. [Query data using FetchXml](fetchxml/overview.md)

```http
GET [Organization URI]/api/data/v9.2/asyncoperations?$apply=groupby((statecode,statuscode,operationtype),aggregate($count as count))
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

[Learn how to query data using the Web API](webapi/query/overview.md)

#### [FetchXml](#tab/fetchxml)

```xml
<fetch aggregate='true'>
  <entity name='asyncoperation'>
    <attribute name='statecode'
      alias='statecode'
      groupby='true' />
    <attribute name='statuscode'
      alias='statuscode'
      groupby='true' />
    <attribute name='operationtype'
      alias='operationtype'
      groupby='true' />
    <attribute name='asyncoperationid'
      alias='count'
      aggregate='count' />
    <order alias='count'
      descending='true' />
  </entity>
</fetch>
```

[Query data using FetchXml](fetchxml/overview.md)

#### [SQL](#tab/sql)

```sql
SELECT statecode,
      statuscode,
      operationtype,
      Count(*) AS count
FROM  asyncoperation
GROUP BY  statecode,
      statuscode,
      operationtype
ORDER BY Count DESC
```

[Use SQL to query data using the Dataverse Tabular Data Stream (TDS) endpoint](dataverse-sql-query.md)

---

### Top system jobs that are in suspended state by count

Use this query to extract a count of all jobs within the `AsyncOperation` table that are in a **Suspended** state. This query helps you to:

- Understand the volume and nature of waiting jobs.
- Identify where the hold-ups are occurring.
- Make informed decisions about how to address them to improve system performance and throughput.

#### [Web API](#tab/webapi)

This query doesn't order by `count` descending. You may want to use FetchXml with Web API instead. [Query data using FetchXml](fetchxml/overview.md)

```http
GET [Organization URI]/api/data/v9.2/asyncoperations?$apply=filter((statecode eq 1))/groupby((statecode,statuscode,operationtype),aggregate($count as count))
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

[Learn to query data using the Web API](webapi/query/overview.md)

#### [FetchXml](#tab/fetchxml)

```xml
<fetch aggregate='true'>
  <entity name='asyncoperation'>
    <attribute name='statecode'
      alias='statecode'
      groupby='true' />
    <attribute name='statuscode'
      alias='statuscode'
      groupby='true' />
    <attribute name='operationtype'
      alias='operationtype'
      groupby='true' />
    <attribute name='asyncoperationid'
      alias='count'
      aggregate='count' />
    <filter>
      <condition attribute='statecode'
        operator='eq'
        value='1' />
    </filter>
    <order alias='count'
      descending='true' />
  </entity>
</fetch>
```

[Query data using FetchXml](fetchxml/overview.md)

#### [SQL](#tab/sql)

```sql
SELECT statecode,
      statuscode,
      operationtype,
      Count(*) AS count
FROM  asyncoperation
WHERE statecode = 1
GROUP BY  statecode,
      statuscode,
      operationtype
ORDER BY Count DESC
```

[Use SQL to query data using the Dataverse Tabular Data Stream (TDS) endpoint](dataverse-sql-query.md)

---

Here's what to look for in the results:

- **Quantify Suspended Jobs**: The query specifically targets jobs that are **Suspended** (`statecode` = `1`). The results give you a count of all such jobs, categorized by their `statuscode` and `operationtype`.

- **Operation Type Breakdown**: The count of **Suspended** jobs grouped `operationtype`, showing you the types of operations are most commonly in a **Suspended** state.

- **Identifying Potential Bottlenecks**: A high count of **Suspended** jobs for extended periods of time might be due to resource limitations, dependencies on other processes, or system misconfigurations.

- **Capacity and Resource Management**: If certain jobs are consistently in the **Suspended** state, it could indicate that the system lacks the necessary resources to process these jobs efficiently.

- **System Health Check**: The jobs in a **Suspended** state serve as a health indicator. A healthy system should ideally have minimal jobs in a **Suspended** state or at least show a quick turnover from **Suspended** to active processing.

- **Workflow Efficiency**: The results can shed light on workflow efficiency. If a particular `operationtype` has a high count of **Suspended** jobs, it might indicate inefficiencies or the need for optimization within that workflow.


### Workflows by count

This query provides a detailed breakdown of workflow-related jobs, filtered by an `operationtype` value for workflows. Use the query results to gain a comprehensive view of workflow jobs, manage system resources more effectively, and ensure that workflows are running smoothly and efficiently.

#### [Web API](#tab/webapi)

```http
GET [Organization URI]/api/data/v9.2/asyncoperations?$apply=filter((operationtype eq 10))/groupby((statecode,statuscode,operationtype),aggregate($count as count))
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

[Learn to query Data using the Web API](webapi/query/overview.md)

#### [FetchXml](#tab/fetchxml)

```xml
<fetch aggregate='true'>
  <entity name='asyncoperation'>
    <attribute name='statecode'
      alias='statecode'
      groupby='true' />
    <attribute name='statuscode'
      alias='statuscode'
      groupby='true' />
    <attribute name='operationtype'
      alias='operationtype'
      groupby='true' />
    <attribute name='asyncoperationid'
      alias='count'
      aggregate='count' />
    <filter>
      <condition attribute='operationtype'
        operator='eq'
        value='10' />
    </filter>
    <order alias='count'
      descending='true' />
  </entity>
</fetch>
```

[Query data using FetchXml](fetchxml/overview.md)

#### [SQL](#tab/sql)

```sql
SELECT statecode,
      statuscode,
      operationtype,
      Count(*) AS count
FROM  asyncoperation
WHERE operationtype = 10
GROUP BY  statecode,
      statuscode,
      operationtype
ORDER BY Count DESC
```

[Use SQL to query data using the Dataverse Tabular Data Stream (TDS) endpoint](dataverse-sql-query.md)

---

Here's what to look for in the results:

- **Workflow-Specific Jobs**: The `operationtype` = `10` filter limits the results to workflow jobs. You can see how many jobs are related to workflows and their current statuses. You can also apply this example query with other types of operations. [Learn more about Operation Types](#operation-types)

- **Job State Distribution**: The `statecode` tells you the current state of these workflow jobs, such as whether they're **Ready**, **Suspended**, **Locked**, or **Completed**.

- **Status Code Analysis**: The `statuscode` can give specific insights into the reason behind a job's current state. For example, it could indicate if a job is **Waiting for Resources**, **Waiting**, **In Progress**, **Pausing**, **Cancelling**, **Succeeded**, **Failed**, or **Cancelled**.

- **Count of Each Category**: The  total number of jobs for each `statecode` and `statuscode` combination. This helps in identifying the most common outcomes of workflow operations.

- **Identifying Common Outcomes**: With the results ordered by count in descending order, you can identify the most frequent outcomes or bottlenecks in workflow processing.

- **Troubleshooting and Optimization**: High counts in **Failed** status or **Suspended** states can highlight areas where workflows might be failing or getting stuck, signaling a need for troubleshooting or process optimization.

- **Performance Metrics**: Understanding which workflows are most common and how they're distributed across different states can help in assessing the performance and reliability of the workflow management system.

- **Capacity Planning**: Consistently high number of **In Progress** or **Waiting** workflows could suggest that more resources are needed to handle the load, or that there's a need to optimize the workflow execution environment.

- **Workflow Management**: The query results can guide administrators on managing workflows more effectively, such as deciding which workflows to prioritize or identifying workflows that can be optimized or deactivated/disabled.

- **System Health Check**: The overall results can serve as a health check for your workflow system, indicating whether the system is performing optimally or if there are areas that require attention.


### Jobs waiting for system resources to become available

Use this query to retrieve a detailed analysis of jobs from the `AsyncOperation` table that are in a specific state of readiness but are pending execution due to unavailability of system resources. This query can identify factors contributing to slowness and making decisions for efficiency and better handling of backlog.

#### [Web API](#tab/webapi)

```http
GET [Organization URI]/api/data/v9.2/asyncoperations?$apply=filter((statecode eq 0 and statuscode eq 0))/groupby((statecode,statuscode,operationtype),aggregate($count as count))
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

[Learn to query Data using the Web API](webapi/query/overview.md)

#### [FetchXml](#tab/fetchxml)

```xml
<fetch aggregate='true'>
  <entity name='asyncoperation'>
    <attribute name='statecode'
      alias='statecode'
      groupby='true' />
    <attribute name='statuscode'
      alias='statuscode'
      groupby='true' />
    <attribute name='operationtype'
      alias='operationtype'
      groupby='true' />
    <attribute name='asyncoperationid'
      alias='count'
      aggregate='count' />
    <filter>
      <condition attribute='statecode'
        operator='eq'
        value='0' />
      <condition attribute='statuscode'
        operator='eq'
        value='0' />
    </filter>
    <order alias='count'
      descending='true' />
  </entity>
</fetch>
```

[Query data using FetchXml](fetchxml/overview.md)

#### [SQL](#tab/sql)

```sql
SELECT statecode,
      statuscode,
      operationtype,
      Count(*) AS count
FROM  asyncoperation
WHERE statecode = 0 AND statuscode = 0
GROUP BY  statecode,
      statuscode,
     operationtype
ORDER BY Count DESC
```

[Use SQL to query data using the Dataverse Tabular Data Stream (TDS) endpoint](dataverse-sql-query.md)

---

Here's what to look for in the results:

- **Filter for Ready Jobs Waiting for Resources**: Limiting results where `statecode` = `0` and `statuscode` = `0` filters for jobs that are in a **Ready**  and **Waiting For Resources**. This combination indicates jobs that are queued up and prepared to run but are on hold.

- **Optimizing Job Scheduling**: Identifying patterns in job readiness and wait times can inform improvements in job scheduling, possibly leading to a more balanced distribution of system load.

- **Identifying Underlying Issues**: In some cases, jobs waiting for resources might not be solely a resource issue but could be indicative of underlying problems such as deadlocks or inefficient resource locking mechanisms.


### Queries for file storage

Depending on the size of the [Data column](reference/entities/asyncoperation.md#BKMK_Data) of the `AsyncOperation` table, the data in that column may be saved in file storage. The [DataBlobId column](reference/entities/asyncoperation.md#BKMK_DataBlobId) has a value when the row uses file storage. To save space, you might want to identify and delete these records. Use the following queries to discover these records

#### AsyncOperation file storage datablobid count

Use this query to count the number of records in the `AsyncOperation` table where the `datablobid` column isn't null.

#### [Web API](#tab/webapi)

```http
GET [Organization URI]/api/data/v9.2/asyncoperations?$apply=filter((datablobid ne null))/aggregate($count as FileStorageCount)
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
```

[Learn to query Data using the Web API](webapi/query/overview.md)

#### [FetchXml](#tab/fetchxml)

```xml
<fetch aggregate='true'>
  <entity name='asyncoperation'>
    <attribute name='asyncoperationid'
      alias='FileStorageCount'
      aggregate='count' />
    <filter>
      <condition attribute='datablobid'
        operator='not-null' />
    </filter>
  </entity>
</fetch>
```

[Query data using FetchXml](fetchxml/overview.md)

#### [SQL](#tab/sql)

```sql
SELECT count(*) AS FileStorageCount 
FROM asyncoperation  
WHERE  datablobid IS NOT NULL
```

[Use SQL to query data using the Dataverse Tabular Data Stream (TDS) endpoint](dataverse-sql-query.md)

---

Here's what to look for in the results:

- **Data Storage Implications**:
You may want to delete the records in using file storage to save space so this is helpful to know.  Large numbers might suggest significant space used by these blobs, which can be important for database size managemement.

- **System Performance Considerations**:
If the `FileStorageCount` is unexpectedly high, you may want to take further action such as Bulk delete and clean up.

#### AsyncOperations not in blob storage

Use this query to count the number of records in the `AsyncOperation` table where the `datablobid` field is `NULL`.

#### [Web API](#tab/webapi)

```http
GET [Organization URI]/api/data/v9.2/asyncoperations?$apply=filter((datablobid eq null))/aggregate($count as DBCount)
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
```

[Learn to query Data using the Web API](webapi/query/overview.md)

#### [FetchXml](#tab/fetchxml)

```xml
<fetch aggregate='true'>
  <entity name='asyncoperation'>
    <attribute name='asyncoperationid'
      alias='DBCount'
      aggregate='count' />
    <filter>
      <condition attribute='datablobid'
        operator='null' />
    </filter>
  </entity>
</fetch>
```

[Query data using FetchXml](fetchxml/overview.md)

#### [SQL](#tab/sql)

```sql
SELECT count(*)  AS DBCount  
FROM asyncoperation 
WHERE datablobid IS NULL
```

[Use SQL to query data using the Dataverse Tabular Data Stream (TDS) endpoint](dataverse-sql-query.md)

---

Here's what to look for in the results:

- **Understanding Async Operations not in Blob Storage:** The `DBCount` result will indicate the volume of async operations that do not have associated data blobs. This shows us the storage status when not accounting for the blobs.

- **Identifying inefficiencies** Unless intended, high count here may suggest the need to schedule cleanup and run bulk delete. Low count in blob storage and high count here would attribute this as the primary volume contributor.

#### Find names of jobs using file storage

The results of this query shows the job types, the name of the jobs, and the number of times this job exists on the table consuming file storage. Use this to identify the specific job names that have the greatest impact on file consumption and create a bulk delete job for records having that name.

This will enable the identification of the specific job names that have the greatest impact on file consumption. As a result, the customer can initiate a bulk delete process for that particular job by targeting its name.

#### [Web API](#tab/webapi)

This query doesn't order by the `jobs` column decending. You may want to use FetchXml with Web API instead. [Query data using FetchXml](fetchxml/overview.md)

```http
GET [Organization URI]/api/data/v9.2/asyncoperations?$apply=filter((datablobid ne null))/groupby((operationtype,name,friendlymessage),aggregate($count as jobs))
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

[Learn to query Data using the Web API](webapi/query/overview.md)

#### [FetchXml](#tab/fetchxml)

```xml
<fetch aggregate='true'>
  <entity name='asyncoperation'>
    <attribute name='asyncoperationid'
      aggregate='count'
      alias='jobs' />
    <attribute name='operationtype'
      groupby='true'
      alias='operationtype' />
    <attribute name='name'
      groupby='true'
      alias='name' />
    <attribute name='friendlymessage'
      groupby='true'
      alias='friendlymessage' />
    <filter>
      <condition attribute='datablobid'
        operator='not-null' />
    </filter>
    <order alias='jobs'
      descending='true' />
  </entity>
</fetch>
```

[Query data using FetchXml](fetchxml/overview.md)

#### [SQL](#tab/sql)

```sql
SELECT operationtypename
      ,name
      ,friendlymessage
      ,count(*) AS Jobs  
FROM asyncoperation
WHERE datablobid IS NOT NULL 
GROUP BY operationtypename, name, friendlymessage
ORDER BY Jobs DESC
```

[Use SQL to query data using the Dataverse Tabular Data Stream (TDS) endpoint](dataverse-sql-query.md)

---

#### AsyncOperation file size and record count

Use this query to get total file size and record count for system jobs by state, status and owning extension.



#### [Web API](#tab/webapi)

This example uses the encoded FetchXml to send the query using Web API. [Query data using FetchXml](fetchxml/overview.md)

```http
GET [Organization URI]/api/data/v9.2/asyncoperations?fetchXml=%3Cfetch%20aggregate%3D%27true%27%3E%20%3Centity%20name%3D%27asyncoperation%27%3E%20%3Cattribute%20name%3D%27owningextensionid%27%20alias%3D%27owningextension%27%20groupby%3D%27true%27%20%2F%3E%20%3Cattribute%20name%3D%27statecode%27%20alias%3D%27statecode%27%20groupby%3D%27true%27%20%2F%3E%20%3Cattribute%20name%3D%27statuscode%27%20alias%3D%27statuscode%27%20groupby%3D%27true%27%20%2F%3E%20%3Cattribute%20name%3D%27operationtype%27%20alias%3D%27operationtype%27%20groupby%3D%27true%27%20%2F%3E%20%3Clink-entity%20name%3D%27fileattachment%27%20to%3D%27datablobid%27%20from%3D%27fileattachmentid%27%20alias%3D%27fileattachment%27%20link-type%3D%27inner%27%3E%20%3Cattribute%20name%3D%27filesizeinbytes%27%20alias%3D%27TotalSize%27%20aggregate%3D%27sum%27%20%2F%3E%20%3Cattribute%20name%3D%27filesizeinbytes%27%20alias%3D%27RecordCount%27%20aggregate%3D%27count%27%20%2F%3E%20%3Cfilter%3E%20%3Ccondition%20attribute%3D%27objectidtypecode%27%20operator%3D%27eq%27%20value%3D%274700%27%20%2F%3E%20%3C%2Ffilter%3E%20%3Corder%20alias%3D%27TotalSize%27%20descending%3D%27true%27%20%2F%3E%20%3C%2Flink-entity%3E%20%3C%2Fentity%3E%20%3C%2Ffetch%3E
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

[Learn to query Data using the Web API](webapi/query/overview.md)   


#### [FetchXml](#tab/fetchxml)

```xml
<fetch aggregate='true'>
  <entity name='asyncoperation'>
    <attribute name='owningextensionid'
      alias='owningextension'
      groupby='true' />
    <attribute name='statecode'
      alias='statecode'
      groupby='true' />
    <attribute name='statuscode'
      alias='statuscode'
      groupby='true' />
    <attribute name='operationtype'
      alias='operationtype'
      groupby='true' />
    <link-entity name='fileattachment'
      to='datablobid'
      from='fileattachmentid'
      alias='fileattachment'
      link-type='inner'>
      <attribute name='filesizeinbytes'
        alias='TotalSize'
        aggregate='sum' />
      <attribute name='filesizeinbytes'
        alias='RecordCount'
        aggregate='count' />
      <filter>
        <condition attribute='objectidtypecode'
          operator='eq'
          value='4700' />
      </filter>
      <order alias='TotalSize'
        descending='true' />
    </link-entity>
  </entity>
</fetch>
```

[Query data using FetchXml](fetchxml/overview.md)

#### [SQL](#tab/sql)

```sql
SELECT count(*) as RecordCount
   ,sum(filesizeinbytes) as TotalSize
   ,owningextensionid
   ,owningextensionidname
   ,statecode
   ,statuscode
   ,operationtype from fileattachment
 join asyncoperation on fileattachment.fileattachmentid =  asyncoperation.datablobid
 where fileattachment.objectidtypecode = 4700
 group by  owningextensionid, owningextensionidname, statecode, statuscode, operationtype
 order by TotalSize desc
```

[Use SQL to query data using the Dataverse Tabular Data Stream (TDS) endpoint](dataverse-sql-query.md)

---

Here's what to look for in the results:

- **Record Count:** `RecordCount` tells you how many records are being returned for each grouping of system job records. This will give you an idea of the volume of asynchronous operations being performed and which types are most common.
- **Total File Size:** `TotalSize` tells you the amount of data these operations are handling. This can help you identify if there are any unusually large files that could be affecting system performance.
- **Grouping by Owning Entities:** The query groups results by `owningextensionid`, `owningextensionidname`, `statecode`, `statuscode`, and `operationtype`. Look at these groupings to pinpoint which extensions are generating the most activity and if there are specific operation types that are predominant.
- **Operation States and Statuses:** The inclusion of `statecode` and `statuscode` in the grouping will help you determine the current state and status of these operations, such as which ones are pending, in progress, or completed.
- **Ordering by TotalSize:** Since the results are ordered by `TotalSize` in descending order, pay attention to the top results as they will highlight the operations that are consuming the most storage. This could be important for identifying potential areas for optimization or cleanup.


## Delete system jobs

You can delete system jobs in the application or in code just like any other table if you have the necessary privileges to do so.

> [!NOTE]
> When registering asynchronous plug-ins, there is an option to automatically delete successful operations. It is recommended that you use it. [Learn to write a plug-in](write-plug-in.md)

The common practice is to create a recurring bulk deletion job that deletes successful jobs. [Learn how to remove a large amount of specific, targeted data with bulk deletion](/power-platform/admin/delete-bulk-records)

## Manage system job states

The status of the system job changes multiple times until the operation is completed. The following are the `StateCode` and `StatusCode` options that represent the available state and status reason values:

|StateCode Value|StateCode Label|StatusCode Value|StatusCode Label|
|--|--|--|--|
|`0`|**Ready**|`0`|**Waiting For Resources**|
|`1`|**Suspended**|`10`|**Waiting**|
|`2`|**Locked**|`20`|**In Progress**|
|`2`|**Locked**|`21`|**Pausing**|
|`2`|**Locked**|`22`|**Canceling**|
|`3`|**Completed**|`30`|**Succeeded**|
|`3`|**Completed**|`31`|**Failed**|
|`3`|**Completed**|`32`|**Canceled**|

You can change the status of system jobs in the application by navigating to **Settings** > **System** > **System Jobs** and using commands available in the **More Actions** menu.

![Action commands available for system jobs in the application.](media/system-jobs-more-actions-commands.png)

> [!NOTE]
> Any action you can perform via this UI can also be performed using code. You cannot perform cancel, pause, or resume operations on system jobs generated by the platform. [Learn about Operation types](#operation-types)

Together with options to manage views, the following options to manage system jobs are available: 

|Option|Description|
|--|--|
|Delete|Using the ![delete command.](../../maker/data-platform/media/delete.gif) command.<br />Deletes a system job|
|Bulk Delete|Using the **More Actions** menu.<br />Opens a wizard to define conditions and create a new Bulk Deletion system job to delete the matching system jobs.|
|Cancel|Using the **More Actions** menu.<br />Cancels the system job.|
|Resume|Using the **More Actions** menu.<br />Resumes a paused system job.|
|Postpone|Using the **More Actions** menu.<br />Reschedules a system job|
|Pause|Using the **More Actions** menu.<br />Pauses a system job.|

Whether the requested operation occurs depends on the state of the system job. For example, you can't pause a job that is completed or hasn't started yet. The following table describes the conditions for each change and what happen when they're selected.

|Option|Valid StateCode values|Change|
|--|--|--|
|**Delete**|any|System Job is deleted|
|**Cancel**|`0` (**Ready**) <br /> `1` (**Suspended**) <br /> `2` (**Locked**)|`StateCode` changed to `3` (**Completed**) and `StatusCode` changed to `32` (**Cancelled**), or `StateCode` changed to `3` (**Completed**) and `StatusCode` changed to `31` (**Failed**) |
|**Resume**|`1` (**Suspended**)|StateCode changed to `0` (**Ready**)|
|**Postpone**|`0` (**Ready**) <br />`2` (**Locked**)|Postpone Job dialog prompts user for datetime value to postpone the system job. [Learn to Postpone system jobs](#postpone-system-jobs)|
|**Pause**|`2` (**Locked**)|StateCode changed to `1` (**Suspended**)|


## Postpone system jobs

The `PostPoneUntil` column contains a datetime value when the system job changes state from `1` (**Suspended**) to `0` (**Ready**). The `PostPoneUntil`, `StateCode`, and `StatusCode` columns  are the only `AsyncOperation` table columns supported for update.

### See also

[Write a plug-in](write-plug-in.md)   
[Write plug-ins to extend business processes](plug-ins.md)  



[!INCLUDE[footer-include](../../includes/footer-banner.md)]
