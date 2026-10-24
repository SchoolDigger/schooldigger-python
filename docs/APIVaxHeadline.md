# APIVaxHeadline

The headline vaccination figure (API 3.1): one grade, vaccine and status per state, as the state leads with it (e.g. kindergartners with all required vaccines, or with MMR where the state publishes no all-vaccine figure).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** | School year of the value (2026 &#x3D; 2025-26) | [optional] 
**grade** | **str** | Grade code: \&quot;PK\&quot;, \&quot;KG\&quot;, \&quot;01\&quot;-\&quot;12\&quot;, or \&quot;14\&quot; &#x3D; all grades in the school | [optional] 
**grade_name** | **str** | Grade name, e.g. \&quot;Kindergarten\&quot;, \&quot;All grades\&quot; | [optional] 
**antigen** | [**APIVaxCode**](APIVaxCode.md) |  | [optional] 
**status** | [**APIVaxCode**](APIVaxCode.md) |  | [optional] 
**label** | **str** | The state&#39;s label for the headline, e.g. \&quot;Kindergartners complete for all required immunizations\&quot; | [optional] 
**level** | **str** | \&quot;school\&quot;; \&quot;district\&quot; when the state publishes the figure for the school&#39;s district only (see isDistrictFigure); \&quot;county\&quot; when the state publishes neither (e.g. NYC public schools: the borough figure); \&quot;district\&quot; on district records | [optional] 
**is_district_figure** | **bool** | True when the value is the district&#39;s published figure, not the school&#39;s (the state reports public schools as districts, e.g. TX). Absent otherwise | [optional] 
**sector** | **str** | \&quot;public\&quot; or \&quot;private\&quot; when the value is a county figure the state published for one sector only (e.g. NYC public schools: the borough&#39;s public-school figure); absent otherwise | [optional] 
**value** | [**APIVaxValue**](APIVaxValue.md) |  | [optional] 
**students** | **int** | Students with this status, when published | [optional] 
**students_total** | **int** | Students the state counted (enrolled, or with a record on file, as the state defines it), when published | [optional] 
**exemption_rate** | **float** | Exemption rate (0-100) at the headline grade and year, as published: any exemption, else medical + non-medical, else medical where the state allows only medical exemptions. Absent when not published | [optional] 
**exemption_antigen** | [**APIVaxCode**](APIVaxCode.md) |  | [optional] 
**notes** | **List[int]** | Ids of the notes (vaccination.notes) that apply to the value | [optional] 

## Example

```python
from schooldigger.models.api_vax_headline import APIVaxHeadline

# TODO update the JSON string below
json = "{}"
# create an instance of APIVaxHeadline from a JSON string
api_vax_headline_instance = APIVaxHeadline.from_json(json)
# print the JSON string representation of the object
print(APIVaxHeadline.to_json())

# convert the object into a dict
api_vax_headline_dict = api_vax_headline_instance.to_dict()
# create an instance of APIVaxHeadline from a dict
api_vax_headline_from_dict = APIVaxHeadline.from_dict(api_vax_headline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


