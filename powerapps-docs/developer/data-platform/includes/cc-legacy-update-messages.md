|Deprecated message request|Attribute(s) to update|  
|--------------------------------|-------------------------|  
|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|*&lt;entity&gt;*.`OwnerId`|  
|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|*&lt;entity&gt;*.`StateCode`<br />*&lt;entity&gt;*.`StatusCode`|
|<xref:Microsoft.Crm.Sdk.Messages.SetParentSystemUserRequest>|[SystemUser](../reference/entities/systemuser.md).[ParentSystemUserId](../reference/entities/systemuser.md#BKMK_ParentSystemUserId)|  
|<xref:Microsoft.Crm.Sdk.Messages.SetParentTeamRequest>|[Team](../reference/entities/team.md).[BusinessUnitId](../reference/entities/team.md#BKMK_BusinessUnitId)|  
|<xref:Microsoft.Crm.Sdk.Messages.SetParentBusinessUnitRequest>|[BusinessUnit](../reference/entities/businessunit.md).[ParentBusinessUnitId](../reference/entities/businessunit.md#BKMK_ParentBusinessUnitId)|  
|<xref:Microsoft.Crm.Sdk.Messages.SetBusinessEquipmentRequest>|[Equipment](/dynamics365/customer-engagement/developer/entities/equipment).[BusinessUnitId](/dynamics365/customer-engagement/developer/entities/equipment#BKMK_BusinessUnitId)|  
|<xref:Microsoft.Crm.Sdk.Messages.SetBusinessSystemUserRequest>|[SystemUser](../reference/entities/systemuser.md).[BusinessUnitId](../reference/entities/systemuser.md#BKMK_BusinessUnitId)|  
  
 *&lt;entity>* refers to any entity that provides this attribute.  

> [!IMPORTANT]
> When you update the `StateCode` column, it is important to always set the desired `StatusCode`.
> 
>`StateCode` and `StatusCode` have dependent values. There can be multiple valid `StatusCode` values for a given `StateCode` value, but each `StateCode` column has a single [DefaultStatus](xref:Microsoft.Xrm.Sdk.Metadata.StateOptionMetadata.DefaultStatus) value configured.   When you update `StateCode` without specifying a `StatusCode`, the default status value will be set by the system.
>
> Also, when auditing is enabled on the table and the `StatusCode` column, the changed value for the `StatusCode` column will not be captured in the audit data unless it is specified in the update operation.