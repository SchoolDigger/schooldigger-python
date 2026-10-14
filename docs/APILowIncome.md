# APILowIncome

The school's low-income measure (API 3.1; docs/lunch-measures-spec.md R1, R6). One of:  \"FRL\" = students eligible for free or reduced-price school meals;  \"DC\" = students directly certified for free meals (SNAP, TANF, FDPIR, Medicaid in most states, or homeless, migrant, runaway, foster or Head Start), used when the school does not report a usable free/reduced count;  \"CEP\" = the school's free/reduced count is 98% or more of enrollment and it reports no direct certification count, which usually means it serves free meals to all students under the Community Eligibility Provision (no percent).  FRL and DC are not comparable: do not rank or sort one against the other. Values older than 3 years are not used, and counts above enrollment are treated as missing. Absent when the school has no usable value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | \&quot;FRL\&quot; (free/reduced-price lunch eligible), \&quot;DC\&quot; (directly certified for free meals) or \&quot;CEP\&quot; (all students receive free meals under the Community Eligibility Provision; no percent) | [optional] 
**year** | **int** | School year of the value (2025 &#x3D; 2024-25), as in schoolYearlyDetails.year | [optional] 
**percent** | **float** | Percent of enrolled students (0-100, two decimals). Absent for \&quot;CEP\&quot;. | [optional] 
**count** | **int** | Number of students counted (free/reduced eligible for \&quot;FRL\&quot; and \&quot;CEP\&quot;, directly certified for \&quot;DC\&quot;) | [optional] 
**enrollment** | **int** | Enrollment the percent is based on (students excluding pre-kindergarten), same school year as count | [optional] 
**community_eligibility_likely** | **bool** | True when the school&#39;s newest usable free/reduced count is 98% or more of enrollment (a sign of the Community Eligibility Provision), whatever type is. A \&quot;DC\&quot; school can be true. | [optional] 
**statewide_free_meals** | **bool** | True when the state serves free school meals to all students in this school year (state law or state funding) | [optional] 

## Example

```python
from schooldigger.models.api_low_income import APILowIncome

# TODO update the JSON string below
json = "{}"
# create an instance of APILowIncome from a JSON string
api_low_income_instance = APILowIncome.from_json(json)
# print the JSON string representation of the object
print(APILowIncome.to_json())

# convert the object into a dict
api_low_income_dict = api_low_income_instance.to_dict()
# create an instance of APILowIncome from a dict
api_low_income_from_dict = APILowIncome.from_dict(api_low_income_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


