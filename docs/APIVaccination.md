# APIVaccination

Vaccination rates as the state published them (API 3.1; docs/vaccination-spec.md R7). Present when the school's (or district's) state publishes vaccination data. By default figures holds one grade (the headline grade, else the first grade published for the school) for its most recent school year; add includeVaccinationDetail=true for every grade and every year (within the plan's yearly history window).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**APIVaxSource**](APIVaxSource.md) |  | [optional] 
**other_sources** | [**List[APIVaxSource]**](APIVaxSource.md) | Other sources some figures come from (older SchoolDigger sources for early years); absent when none | [optional] 
**headline** | [**APIVaxHeadline**](APIVaxHeadline.md) |  | [optional] 
**is_district_figure** | **bool** | True when the state publishes figures for the school&#39;s district, not for the school (e.g. TX public schools): figures carry district (and state) values only, which are the district&#39;s, never the school&#39;s. Absent otherwise | [optional] 
**district_name** | **str** | Name of the district the district figures are for (absent when there are none) | [optional] 
**county_name** | **str** | Name of the county the county figures are for (absent when there are none) | [optional] 
**state_name** | **str** | Name of the state the state figures are for (absent when there are none) | [optional] 
**years_available** | **List[int]** | School years with published figures for the school (or, without school figures, for its district or county), most recent first | [optional] 
**grades_available** | [**List[APIVaxGrade]**](APIVaxGrade.md) | Grades with published figures for the school (or, without school figures, for its district or county), in grade order | [optional] 
**detail_included** | **bool** | True when figures holds every grade and year (includeVaccinationDetail&#x3D;true); false when it holds one grade for its most recent year | [optional] 
**figures** | [**List[APIVaxFigure]**](APIVaxFigure.md) | Every published measure for the years returned, most recent year first: the school&#39;s own value and the state&#39;s published district, county and state values for the same year, grade, vaccine and status. Empty when the state publishes nothing for this school | [optional] 
**grades** | [**List[APIVaxGrade]**](APIVaxGrade.md) | Names of the grade codes used in figures | [optional] 
**antigens** | [**List[APIVaxCode]**](APIVaxCode.md) | Names of the vaccine codes used in figures | [optional] 
**statuses** | [**List[APIVaxCode]**](APIVaxCode.md) | Names and groups (coverage, exemption, other) of the status codes used in figures | [optional] 
**notes** | [**List[APIVaxNote]**](APIVaxNote.md) | Footnotes referenced by figures and the headline; absent when none apply | [optional] 

## Example

```python
from schooldigger.models.api_vaccination import APIVaccination

# TODO update the JSON string below
json = "{}"
# create an instance of APIVaccination from a JSON string
api_vaccination_instance = APIVaccination.from_json(json)
# print the JSON string representation of the object
print(APIVaccination.to_json())

# convert the object into a dict
api_vaccination_dict = api_vaccination_instance.to_dict()
# create an instance of APIVaccination from a dict
api_vaccination_from_dict = APIVaccination.from_dict(api_vaccination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


